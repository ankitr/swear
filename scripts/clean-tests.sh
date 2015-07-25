#!/bin/bash
set -eo pipefail

BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/../.." && pwd )"

rm -rf "$BASEDIR/../tests/"
rm "$BASEDIR/../data/test-answers.json"
