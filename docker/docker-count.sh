#!/bin/bash


case $1 in
    collect)
        sudo -g docker docker ps -a --no-trunc > /tmp/.zbx_containers
        cat /tmp/.zbx_containers | awk '{print $1 " " $NF}' | /opt/scripts/docker-discover.py
    ;;
    all)
        cat /tmp/.zbx_containers | grep -v "CONTAINER ID" | wc -l
    ;;
    running)
        cat /tmp/.zbx_containers | grep "\sUp\s" | wc -l
    ;;
    crashed)
        cat /tmp/.zbx_containers | grep -v -F 'Exited (0)' | grep -c -F 'Exited ('
    ;;


esac

