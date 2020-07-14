#!/bin/bash
words="Hello World"

i=$(cat ~/.config/polybar/mods/var)
echo ${words:: $i}

expr $(cat ~/.config/polybar/mods/var) + 1 > ~/.config/polybar/mods/var
