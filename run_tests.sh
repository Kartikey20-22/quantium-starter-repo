#!/bin/bash

# Exit immediately if any command fails
set -e

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Running test suite..."
pytest

echo "All tests passed!"
exit 0