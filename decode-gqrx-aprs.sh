#!/bin/sh

nc -l -u 7355  |
	direwolf -n 1 -r 48000 -b 16 -t 0 "$@" -
