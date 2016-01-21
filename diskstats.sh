#!/bin/bash



case $1 in
discovery)
    let first=1

    echo "{"
    echo '"data": [ '

    drives=`ls /dev/ | egrep "^(sd.|md.)$"`

    for drive in $drives; do 
        if [ $first -eq 0 ]; then
            echo ','
        fi
        let first=0
        echo '{'
        echo '"{#DRIVENAME}": "'$drive'"'
        echo '}'

    done
    echo ']'
    echo '}'
;;


*)
    reads=`cat /proc/diskstats | egrep "$1{1}\s" | awk '{print $4}'`
    writes=`cat /proc/diskstats | egrep "$1{1}\s" | awk '{print $8}'`
    let iops=$reads+$writes
    echo $iops
;;
esac

