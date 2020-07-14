#!/bin/bash

pidof glava
if [[ $? -eq 1 ]]; then
	glava -i
else
	killall glava

fi
