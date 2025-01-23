#!/usr/bin/bash
nasm mysys.s -o /tmp/mysys.o
bcc -c -Md libdos.c -o libdos.a
bcc -c -Md libdos.c -o /tmp/libdos.a