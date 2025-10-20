# posts/views.py
from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.response import Response
from accounts.models import CustomUser
from notifications.utils import create_notification

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'author__username']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    following_users = user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    # prevent liking own post? usually allowed; we'll allow but still create notification only if different user
    like, created = Like.objects.get_or_create(user=user, post=post)
    if not created:
        return Response({'detail': 'Post already liked.'}, status=status.HTTP_400_BAD_REQUEST)

    # create notification for post author if not self
    if post.author != user:
         create_notification(recipient=post.author, actor=user, verb='liked your post', target=post)
        
    serializer = LikeSerializer(like)
    return Response(serializer.data, status=201)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    
    like = Like.objects.filter(user=user, post=post).first()
    if not like:
       return Response({"detail": "You have not liked this post."}, status=400)

    like.delete()
    return Response({"detail": "Unliked successfully."}, status=200)