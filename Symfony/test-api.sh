#!/bin/bash

readonly BASE_URL="http://localhost:8000/api"

# Colors for messages
readonly RED_TEXT="\033[31m"
readonly GREEN_TEXT="\033[32m"
readonly ENDCOLOR="\033[0m"

display_error() {
    echo -e "${RED_TEXT}$1${ENDCOLOR}"
}

display_success() {
    echo -e "${GREEN_TEXT}$1${ENDCOLOR}"
}

check_status_code() {
    local entity=$1
    local method=$2
    local result=$3
    local expected=$4

    if [[ "$status_code" -eq $expected ]]; then
        display_success "Test: ${entity}: $method — OK"
    else
        display_error "Test: ${entity}: $method — FAILED"
    fi
}

get_data_by_entity() {
    case $1 in
    "products")
        echo '{"name": "Test Product", "price": 1000.25, "quantity": 10000}'
        ;;
    "categories")
        echo '{"name": "Test Category"}'
        ;;
    "customers")
        random_email="$(openssl rand -hex 6)@example.com"
        echo '{"firstName": "John", "lastName": "Doe", "email": "'$random_email'"}'
        ;;
    *) echo '{}' ;;
    esac
}

check_create_endpoint() {
    local url="${BASE_URL}/$1"

    status_code=$(curl --silent $url \
        --header 'Content-Type: application/json' \
        --header 'Accept: application/json' \
        --data "$(get_data_by_entity $1)" \
        --write-out %{http_code} \
        --output /dev/null)

    check_status_code $1 "create" $status_code 201
}

check_index_endpoint() {
    local url="${BASE_URL}/$1"

    status_code=$(curl --silent --request GET $url \
        --header 'Content-Type: application/json' \
        --header 'Accept: application/json' \
        --write-out %{http_code} \
        --output /dev/null)

    check_status_code $1 "index" $status_code 200
}

check_show_endpoint() {
    local url="${BASE_URL}/$1/${2}"

    status_code=$(curl --silent --request GET $url \
        --header 'Content-Type: application/json' \
        --header 'Accept: application/json' \
        --write-out %{http_code} \
        --output /dev/null)

    check_status_code $1 "show" $status_code 200
}

check_update_endpoint() {
    local url="${BASE_URL}/$1/${2}"

    status_code=$(curl --silent --request PUT $url \
        --header 'Content-Type: application/json' \
        --header 'Accept: application/json' \
        --data "$(get_data_by_entity $1)" \
        --write-out %{http_code} \
        --output /dev/null)

    check_status_code $1 "update" $status_code 200
}

check_delete_endpoint() {
    local url="${BASE_URL}/$1/${2}"

    status_code=$(curl --silent --request DELETE $url \
        --header 'Accept: application/json' \
        --write-out %{http_code} \
        --output /dev/null)

    check_status_code $1 "delete" $status_code 204
}

get_last_entity_id() {
    local entity=$1
    local url="${BASE_URL}/${entity}"

    curl --silent --request GET $url \
        --header 'Content-Type: application/json' \
        --header 'Accept: application/json' |
        jq -r '[.[].id] | max'
}

run_tests_for_entity() {
    local entity=$1
    check_create_endpoint $entity
    check_index_endpoint $entity

    local entity_last_id=$(get_last_entity_id $entity)
    check_show_endpoint $entity $entity_last_id
    check_update_endpoint $entity $entity_last_id
    check_delete_endpoint $entity $entity_last_id
}

run_tests_for_entity "products"
run_tests_for_entity "categories"
run_tests_for_entity "customers"
