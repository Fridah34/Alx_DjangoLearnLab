# Security Review – HTTPS & Secure Redirects

## Configured Measures:
- **SECURE_SSL_REDIRECT**: Forces HTTPS for all requests.
- **HSTS (Strict Transport Security)**: Ensures browsers always use HTTPS.
- **Secure Cookies**: Session and CSRF cookies marked `secure` → only sent over HTTPS.
- **Security Headers**:
  - `X_FRAME_OPTIONS = DENY` → prevents clickjacking.
  - `SECURE_CONTENT_TYPE_NOSNIFF = True` → prevents MIME type sniffing.
  - `SECURE_BROWSER_XSS_FILTER = True` → enables browser-level XSS protection.

## Deployment:
- Requires SSL/TLS certificates.
- Web server (Nginx/Apache) must redirect HTTP → HTTPS.

## Areas for Improvement:
- Implement a strict Content Security Policy (CSP).
- Regularly rotate SSL/TLS certificates.
- Use automated vulnerability scans before deployment.
