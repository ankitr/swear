#!/bin/bash
set -eo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}")" && pwd )"

python "$BASEDIR/../src/app.py"
