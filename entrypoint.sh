#!/bin/bash
set -e

echo "Running entrypoint with args: $@"
exec "$@"
