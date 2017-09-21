#/bin/sh

#### Include the library
. `dirname $0`/sh2ju.sh


# Test cases
proEmptymesh() {
   # process the model
   cd /mnt/dev/mp_vision-build/deploy/ && ./vision_mesh_code.work /mnt/dev/mp_vision-build/deploy/ /mnt/dev/testResults/emptymesh/
   return 0
}

juLog  -name=proEmptymesh             proEmptymesh

