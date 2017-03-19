#!/bin/bash
set -e

# cd to where build script is located
# allows easy predictable paths everywhere in build chain
cd "$( dirname "${BASH_SOURCE[0]}" )"

docker build -t trading/app:latest .
