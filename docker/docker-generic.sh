#!/bin/bash


case $1 in
    collect)
        sudo -g docker docker ps -a --no-trunc > /tmp/.zbx_containers
    break;;
    all)
        cat /tmp/.zbx_containers | grep -v "CONTAINER ID" | wc -l
    break;;
    running)
        cat /tmp/.zbx_containers | grep "\sUp\s" | wc -l
    break;;
    crashed)
        cat /tmp/.zbx_containers | grep -v -F 'Exited (0)' | grep -c -F 'Exited ('
    break;;


esac

