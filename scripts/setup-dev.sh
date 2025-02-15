#!/bin/bash
set -e

# Install dependencies
poetry install

# Install pre-commit hooks
poetry run pre-commit install

echo "✅ Development environment setup complete!"
