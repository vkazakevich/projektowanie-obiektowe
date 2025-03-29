#!/bin/bash

readonly DOCKER_IMAGE="vkthedev/pascal"

docker_build_and_run() {
    fpc_command=$1
    filename=$2

    docker build --quiet -t $DOCKER_IMAGE .
    docker run --rm -it -v "$(pwd)":/home/student/projobj/ vkthedev/pascal:latest $fpc_command $filename.pas >/dev/null
    docker run --rm -it -v "$(pwd)":/home/student/projobj/ vkthedev/pascal:latest ./bin/$filename
}

compile_and_run() {
    docker_build_and_run "fpc -FE./bin" "Randomizer"
}

compile_and_run_tests() {
    docker_build_and_run "fpc -FE./bin -Fu./fptest/src -Fu./fptest/3rdparty/epiktimer -Mobjfpc" "TestRunner"
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
