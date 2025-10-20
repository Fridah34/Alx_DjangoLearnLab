# Django REST API Deployment - Render

## Hosting
- Platform: Render.com
- Live URL: https://social-media-api.onrender.com

## Deployment Steps
1. Install dependencies
2. Set up `settings.py` for production
3. Push to GitHub
4. Connect repo to Render
5. Configure environment variables
6. Deploy and test endpoints

## Environment Variables
- DEBUG=False
- SECRET_KEY=<secret_key>
- ALLOWED_HOSTS=your-app-name.onrender.com
- DATABASE_URL=<render_db_url>

## Maintenance
- Regularly update dependencies
- Monitor logs in Render Dashboard
- Collect static files after updates
