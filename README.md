# protofiles
proto files for gRPC 

style guide는 google developer site를 따릅니다.(단, rpc method만 시작을 소문자로 함)
https://developers.google.com/protocol-buffers/docs/style

proto naming convention 정리

Standard file formatting
- 1줄의 길이는 80글자 이하로 작성
- indent는 2space 사용

File structure
- file name은 lower_snake_case.proto를 사용
모든 파일에는 다음과 같은 내용들을 포함
1. License header
2. FIle overview
3. Syntax
4. Package
5. Imports(sorted)
6. File options
7. Everything else

Packages
package 이름은 lowercase로 사용하고, directory 계층과 관련있게 ex> my/package에 있으면 my.package

Message and field name
CamelCase를 사용(시작은 대문자)
field 이름으로는 underscope_separated_name들을 사용
field 이름에 숫자가 들어가면 _의 뒤에 쓰는 것 보다 문자 뒤에 붙여서 씀 song_name_1 대신에 song_name1

Repeated fields
복수형을 사용

Enums
enum type의 이름은 CamelCase를 사용(시작은 대문자)
value들은 CAPITALS_WITH_UNDERSCORES를 사용
각 enum 값의 끝에는 ; (semicolon)이 있어야 함 (, comma 가 아님)
enum에서 0을 UNSPECIFIED를 위해 두는 것을 추천

Service
service의 이름은 CamelCase를 사용(시작은 대문자)
service의 RPC method의 이름도 CamelCase(시작은 소문자)를 사용

피해야 할 것(지양해야 할 것)
field return
