#!/bin/bash

readonly DOCKER_IMAGE_NAME="pascal"
readonly DOCKER_DIR="/home/student/projobj/"

docker_build_if_not_exists() {
    if [[ "$(docker images -q $DOCKER_IMAGE_NAME:latest 2>/dev/null)" == "" ]]; then
        docker build -t $DOCKER_IMAGE_NAME .
    fi
}

docker_build_and_run() {
    docker_build_if_not_exists
    docker run --rm -it -v "$(pwd)":$DOCKER_DIR $DOCKER_IMAGE_NAME:latest $@
}

compile_and_run() {
    docker_build_and_run fpc -FE./build Randomizer.pas >/dev/null
    docker_build_and_run ./build/Randomizer
}

compile_and_run_tests() {
    docker_build_and_run fpc -FE./build -Fu./fptest/src -Fu./fptest/3rdparty/epiktimer -Mobjfpc TestRunner.pas >/dev/null
    docker_build_and_run ./build/TestRunner
}

shift $((OPTIND - 1))

case "$1" in
--tests)
    compile_and_run_tests
    ;;
*)
    compile_and_run
    ;;
esac
