#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p backups
stamp=$(date -u +%Y%m%dT%H%M%SZ)
docker compose --env-file .env -f infra/docker-compose.yml exec -T postgres pg_dump -U "${POSTGRES_USER:-jarvis}" "${POSTGRES_DB:-jarvis}" | gzip > "backups/postgres-${stamp}.sql.gz"
tar -czf "backups/files-${stamp}.tar.gz" artifacts workspaces
printf 'Backup created: %s\n' "$stamp"
