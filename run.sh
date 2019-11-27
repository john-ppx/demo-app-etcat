#!/bin/bash

#trap 'echo start;halcmd -R;halcmd stop;halcmd unload all;echo end' 2
#trap 'halrun -U;exit' INT

halcmd loadusr `pwd`/exp1.py
halcmd -f app.hal
halcmd start

halshow my.halshow

halrun -U

#case "${1}" in
#start)
#    halcmd loadusr `pwd`/exp1.py
#    halcmd -f app.hal
#    halcmd start
#    exit 0
#    ;;
#
##------------------------------------------------------------------------------
#stop)
#    halrun -U
#    exit 0
#    ;;
#
##------------------------------------------------------------------------------
#restart)
#    $0 stop || exit 1
#    sleep 1
#    $0 start
#    ;;
#
##------------------------------------------------------------------------------
#status)
#    halcmd show
#    exit 0
#    ;;
#
##------------------------------------------------------------------------------
#*)
#    echo "USAGE: $0 {start|stop|restart|status}"
#    exit 1
#    ;;
#esac

#
