## Security Measures Implemented

- **DEBUG = False** in production
- Configured `SECURE_BROWSER_XSS_FILTER`, `SECURE_CONTENT_TYPE_NOSNIFF`, `X_FRAME_OPTIONS`
- Enforced HTTPS-only cookies (`CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`)
- All forms include `{% csrf_token %}` for CSRF protection
- ORM queries used exclusively to prevent SQL injection
- Implemented Content Security Policy (CSP) to mitigate XSS risks
- User inputs validated through Django forms
