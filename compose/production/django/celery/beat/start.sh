#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A data_branch.taskapp beat -l INFO
