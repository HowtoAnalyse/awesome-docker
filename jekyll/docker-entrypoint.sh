#!/bin/bash
set -e

if [ ! -f Gemfile ]; then
  echo "Gemfile not found"
  exit 1
fi

bundle install

exec "$@"