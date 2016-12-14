#!/usr/bin/env bash

if [ -x $(command -v docker) ]; then
    echo "Building...";
    docker build $(dirname "$0")
    echo "Complete.";
fi