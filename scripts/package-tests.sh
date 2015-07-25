#!/bin/bash
set -eo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/../.." && pwd )"

zip -r "$BASEDIR/../testpackage.zip" "$BASEDIR/../tests"
