#!/bin/bash
killall tint2 
tint2 -c .config/tint2/tint2rc &
tint2 -c .config/tint2/dashboard.tint2rc &
killall trayer ; trayer --widthtype request --align right --distance 2 --transparent true --alpha 255 &
killall polybar ; polybar mybar; polybar expb &
killall jgmenu
