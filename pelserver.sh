#!/bin/bash
pushd output
python -m pelican.server
popd
