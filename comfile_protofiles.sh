#!/bin/bash
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/AccountService.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/AuthService.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/CommonResult.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/Data.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/Date.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/Datetime.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/DealService.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/Empty.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/MissionService.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/NotificationService.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/PhoneService.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/PlatformType.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/PointService.proto
python3 -m grpc_tools.protoc -I=./deal --python_out=.. --grpc_python_out=.. ./deal/UserService.proto
echo "Compile Done!!"
echo "Please check debug message of command"

# python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/route_guide.proto