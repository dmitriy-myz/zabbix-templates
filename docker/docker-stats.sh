#!/bin/bash

#ls /sys/fs/cgroup/cpu/docker/ -l | grep "^d" | rev | awk '{print $1}' | rev

function memory_stat() {
    container=$1
    if [ -d "/sys/fs/cgroup/cpu/docker" ]; then
        pids=`cat "/sys/fs/cgroup/cpu/docker/${container}/cgroup.procs"`
    else
        pids=`cat "/sys/fs/cgroup/cpu/system.slice/docker-${container}.scope/cgroup.procs"`
    fi
    mem=0
#    pids=`echo $pids | tr " " "|"`
#    ps aux | awk "\$2 ~ \"^($pids)\$\" {SUM += \$6} END {print SUM}"
    for pid in $pids; do
        let mem=$mem+`sudo cat /proc/$pid/smaps  | grep Pss | awk '{SUM += $2} END {print SUM}'`
    done
    echo ${mem}
}

function process_count() {
    container=$1
    if [ -d "/sys/fs/cgroup/cpu/docker" ]; then
        cat /sys/fs/cgroup/cpu/docker/${container}/cgroup.procs | wc -l
    else
        cat /sys/fs/cgroup/cpu/system.slice/docker-${container}.scope/cgroup.procs | wc -l
    fi
}

function cpu_usage() {
    type=$1
    container=$2
    if [ -d "/sys/fs/cgroup/cpuacct/docker" ]; then
        cat /sys/fs/cgroup/cpuacct/docker/${container}/cpuacct.stat |  grep ${type} | awk '{print $2}'
    else
        cat /sys/fs/cgroup/cpuacct/system.slice/docker-${container}.scope/cpuacct.stat |  grep ${type} | awk '{print $2}'
    fi
}

case $1 in
    memory)
        memory_stat $2
        ;;
    process_count)
        process_count $2
        ;;
    cpu_user)
        cpu_usage user $2
        ;;
    cpu_system)
        cpu_usage system $2
        ;;

esac

