#!/bin/bash
protoc -I=./deal --dart_out=./gen ./deal/AccountService.proto
protoc -I=./deal --dart_out=./gen ./deal/AuthService.proto
protoc -I=./deal --dart_out=./gen ./deal/CommonResult.proto
protoc -I=./deal --dart_out=./gen ./deal/Data.proto
protoc -I=./deal --dart_out=./gen ./deal/Date.proto
protoc -I=./deal --dart_out=./gen ./deal/Datetime.proto
protoc -I=./deal --dart_out=./gen ./deal/DealService.proto
protoc -I=./deal --dart_out=./gen ./deal/Empty.proto
protoc -I=./deal --dart_out=./gen ./deal/MissionService.proto
protoc -I=./deal --dart_out=./gen ./deal/NotificationService.proto
protoc -I=./deal --dart_out=./gen ./deal/PhoneService.proto
protoc -I=./deal --dart_out=./gen ./deal/PlatformType.proto
protoc -I=./deal --dart_out=./gen ./deal/PointService.proto
protoc -I=./deal --dart_out=./gen ./deal/UserService.proto

echo "Done."
echo "Please check debug message of command"
