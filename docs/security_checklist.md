# CWP Crypto Mind Security Checklist

## Secrets

- [ ] Never commit `.env`
- [ ] Never commit API keys
- [ ] Never commit Telegram bot token
- [ ] Never commit database URL with password
- [ ] Use Railway environment variables in production

## Database

- [ ] Use SQLAlchemy ORM/query builder
- [ ] Avoid raw SQL with user input
- [ ] Use least-privilege DB users later
- [ ] Do not expose database publicly without password

## Trading

- [ ] Start with read-only API keys
- [ ] Never enable withdrawal permission
- [ ] Use demo trading before live trading
- [ ] Separate demo keys from live keys

## Logging

- [ ] Do not log secrets
- [ ] Do not log full DATABASE_URL
- [ ] Do not log private API keys
- [ ] Do not log user passwords

## Deployment

- [ ] Use HTTPS
- [ ] Use environment variables
- [ ] Rotate leaked credentials immediately