#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A data_branch.taskapp worker -l INFO
