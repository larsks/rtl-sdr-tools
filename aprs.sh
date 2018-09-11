#!/bin/sh

rtl_fm -f 144.39M -r 24000 ${RTL_INDEX:+-d $RTL_INDEX} | direwolf -n 1 -r 24000 -b 16 -t 0 "$@" -
