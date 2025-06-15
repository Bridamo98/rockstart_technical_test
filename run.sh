#!/bin/bash

ALLOWED_ACTIONS=("build" "up" "stop" "down" "restart" "restart_rmd" "rem_data")
ALLOWED_ENVS=("prod" "dev")

usage() {
cat <<- EOF

    * To Docker Services execution: $0 <ENVIRONMENT> <ACTION> [SERVICES]
    
    Parameters:
        1) <ENVIRONMENT>: ${ALLOWED_ENVS[*]}
        2) <ACTION>: ${ALLOWED_ACTIONS[*]}
        3) [SERVICES]: Name(s) of the service(s) to process
                       * If not specified, all services are lifted

EOF
exit 1
}

build() {
    docker compose -f "$compose_file" build
}

build_services() {
    docker compose -f "$compose_file" build --parallel "$@"
}

up() {
    docker compose -f "$compose_file" up -d --build
    docker compose -f "$compose_file" logs -f
}

up_services() {
    docker compose -f "$compose_file" up -d --build "$@"
    docker compose -f "$compose_file" logs -f
}

stop() {
    docker compose -f "$compose_file" stop
}

down() {
    docker compose -f "$compose_file" down --volumes --remove-orphans
}

down_services() {
    services=("$@")
    docker compose -f "$compose_file" stop "${services[@]}" \
    && docker compose -f "$compose_file" rm -v -f "${services[@]}"
}

rem_data() {
    echo "Deleting data (database/$valid_environment/persistence/data/)"
    sudo rm -rf "database/$valid_environment/persistence/data/"
}


(( $# < 2 )) && usage

environment=$1
shift

action=$1
shift

services=("$@")

is_valid=false
for value in "${ALLOWED_ENVS[@]}"; do
    if [ "$value" == "$environment" ]; then
        is_valid=true
        break
    fi
done

if ! $is_valid; then
    echo "Error: The argument '$environment' is not in the set of allowed environments."
    usage
    exit 1
fi

is_valid=false
for value in "${ALLOWED_ACTIONS[@]}"; do
    if [ "$value" == "$action" ]; then
        is_valid=true
        break
    fi
done

if ! $is_valid; then
    echo "Error: The argument '$action' is not in the set of allowed actions."
    usage
    exit 1
fi

valid_environment=$environment
compose_file="docker-compose.$environment.yml"

case $action in
    build)
        if [ -z "$services" ]; then
            build
        else
            build_services "${services[@]}"
        fi
        ;;
    up)
        if [ -z "$services" ]; then
            up
        else
            up_services "${services[@]}"
        fi
        ;;
    stop) stop;;
    down) down;;
    restart)
        if [ -z "$services" ]; then
            down
            build
            up
        else
            down
            build_services "${services[@]}"
            up_services "${services[@]}"
        fi
        ;;
    restart_rmd)
        if [ -z "$services" ]; then
            down
            rem_data
            build
            up
        else
            down
            rem_data
            build_services "${services[@]}"
            up_services "${services[@]}"
        fi
        ;;
    rem_data) rem_data ;;
    *)
        echo "Error: Unknown command '$action'."
        exit 1
        ;;
esac
