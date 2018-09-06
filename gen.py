#!/usr/bin/env python3
import os

CHALLENGES = {
    # 'tag name': (path, port)
    'callme': ('callme', 5566),
    'ret2sc': ('ret2sc', 5567),
    'guess': ('guess', 5568),
    'r3t2lib': ('r3t2lib', 5569),
    'simplerop_revenge': ('simplerop_revenge', 5570),
    'calc': ('ais3/2018/preexam/calc', 5571),
    'mail': ('ais3/2018/preexam/mail', 5572),
    'darling': ('ais3/2018/preexam/darling', 5573),
    'justfmt': ('ais3/2018/preexam/justfmt', 5574),
    'magicworld': ('ais3/2018/preexam/Magic_World', 5575),
    'cr4ck': ('cr4ck', 5576),
    'craxme': ('craxme', 5577),
}


def gen_build(fname='build.sh'):
    with open(fname, 'w+') as f:
        print("#!/bin/bash", file=f)
        for tag, conf in CHALLENGES.items():
            print("docker build -t %s %s" % (tag, conf[0]), file=f)
    os.chmod(fname, 0o755)


def gen_run(fname='run.sh'):
    with open(fname, 'w+') as f:
        print("#!/bin/bash", file=f)
        for tag, conf in CHALLENGES.items():
            print("docker run -d -p %d:8000 -t %s" % (conf[1], tag), file=f)
    os.chmod(fname, 0o755)


def gen_stop(fname='stop.sh'):
    with open(fname, 'w+') as f:
        print("#!/bin/bash", file=f)
        for tag, conf in CHALLENGES.items():
            print('docker stop $(docker ps -q -f "ancestor=%s")' % (tag), file=f)
    os.chmod(fname, 0o755)

gen_build()
gen_run()
gen_stop()
