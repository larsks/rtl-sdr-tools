#!/bin/sh

nc -l -u ${NC_LISTEN_PORT}  |
	direwolf -n 1 -r 48000 -b 16 -t 0 "$@" -
