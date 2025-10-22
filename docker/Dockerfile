# Base Postgres 16 image
FROM postgres:16

# Install pgvector extension
RUN apt-get update && \
    apt-get install -y postgresql-16-pgvector && \
    rm -rf /var/lib/apt/lists/*

# Preload pgvector library on Postgres startup
CMD ["postgres", "-c", "shared_preload_libraries=pgvector"]