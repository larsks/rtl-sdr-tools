#!/bin/sh

nc -u -l 7355 | padsp dsd -i- -o /dev/dsp "$@"
