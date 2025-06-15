#!/usr/bin/env sh
set -e

echo "🔁 Migrating DB up to revision: $COMMIT_ID"

pipenv run alembic downgrade base || true

exec pipenv run alembic upgrade "$COMMIT_ID"
