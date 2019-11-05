#!/bin/bash

[ -e ff_config ] || mkdir ff_config

sudo docker run \
--rm \
-it   --name=firefox     -p 5900:5900     -v $PWD/ff_config:/config:rw     --shm-size 2g jlesage/firefox

