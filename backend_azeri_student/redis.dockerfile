FROM redis:4.0.11


ENV REDIS_PASSWORD Z1aLnnZmGTDWzIqc


CMD ["sh", "-c", "exec redis-server --requirepass \"$REDIS_PASSWORD\""]