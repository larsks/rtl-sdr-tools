#!/bin/sh

nc -u -l ${NC_LISTEN_PORT:-7355} |
	padsp dsd -i- -o /dev/dsp "$@"
