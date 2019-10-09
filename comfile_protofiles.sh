#!/bin/bash
protoc -I=./deal --python_out=.. ./deal/AuthService.proto
protoc -I=./deal --python_out=.. ./deal/Empty.proto
protoc -I=./deal --python_out=.. ./deal/CommonResult.proto
protoc -I=./deal --python_out=.. ./deal/PlatformType.proto
echo "Compile Done!!"
