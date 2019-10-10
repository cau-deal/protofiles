#!/bin/bash
protoc -I=./deal --dart_out=grpc:./gen ./deal/AccountService.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/AuthService.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/CommonResult.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/Data.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/Date.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/Datetime.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/DealService.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/Empty.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/MissionService.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/NotificationService.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/PhoneService.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/PlatformType.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/PointService.proto
protoc -I=./deal --dart_out=grpc:./gen ./deal/UserService.proto

echo "Done."
echo "Please check debug message of command"
