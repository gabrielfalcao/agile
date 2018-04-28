#!/bin/bash

# shellcheck disable=SC2013

pkgfile="$(pwd)/packages.txt"
target="$(pwd)/dependencies.txt"

rm -f "${target}"

set -e
for name in $(cat "${pkgfile}"); do
    pip install -U "${name}";
    pip freeze | grep -Ei "${name}" >> "${target}";
done
