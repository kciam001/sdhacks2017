echo starting...
title EToT2
cd ../english_to_code
mvn clean compile exec:java -Dexec.args="example/code/train city"
::cmd \k