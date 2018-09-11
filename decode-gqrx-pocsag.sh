#!/bin/sh

nc -l -u 7355  |
	sox \
		-r 48000 -t raw -b 16 -c 1 -e signed-integer /dev/stdin \
		-r 22050 -t raw -b 16 -c 1 -e signed-integer - |
	multimon-ng -t raw -c -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -f alpha -
