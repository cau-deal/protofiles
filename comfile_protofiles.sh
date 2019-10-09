#!/bin/bash
protoc -I=./deal --python_out=.. ./deal/AccountService.proto
protoc -I=./deal --python_out=.. ./deal/AuthService.proto
protoc -I=./deal --python_out=.. ./deal/CommonResult.proto
protoc -I=./deal --python_out=.. ./deal/Data.proto
protoc -I=./deal --python_out=.. ./deal/Date.proto
protoc -I=./deal --python_out=.. ./deal/Datetime.proto
protoc -I=./deal --python_out=.. ./deal/DealService.proto
protoc -I=./deal --python_out=.. ./deal/Empty.proto
protoc -I=./deal --python_out=.. ./deal/MissionService.proto
protoc -I=./deal --python_out=.. ./deal/NotificationService.proto
protoc -I=./deal --python_out=.. ./deal/PhoneService.proto
protoc -I=./deal --python_out=.. ./deal/PlatformType.proto
protoc -I=./deal --python_out=.. ./deal/PointService.proto
protoc -I=./deal --python_out=.. ./deal/UserService.proto
echo "Compile Done!!"
echo "Please check debug message of command"
