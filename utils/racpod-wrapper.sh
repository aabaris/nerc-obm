#!/bin/sh
#
set -e

for n in `seq 143 143`;
do
#  podman run --security-opt label=disable -v /tmp/a:/tmp/a stackdot/racadm -u root -p $IPMIPW -r 10.255.1.$n hwinventory export -f /tmp/a/$n.xml
echo   podman run stackdot/racadm -u root -p $IPMIPW -r 10.255.1.$n storage get vdisk
echo   podman run stackdot/racadm -u root -p $IPMIPW -r 10.255.1.$n storage deletevd:Disk.Virtual.3:RAID.Slot.5-1 
#   podman run stackdot/racadm -u root -p $IPMIPW -r 10.255.1.$n storage help deletevd
done

