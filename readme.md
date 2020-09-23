# Amazon S3 Bucket Terminator
특정 substring이 이름에 포함된 복수의 S3 버킷을 **버전 관리 활성화 여부에 관계 없이** 한번에 삭제할 수 있는 스크립트입니다.

사용자 AWS 계정이 소유한 모든 버킷 이름을 받아온 뒤, 이름에 사용자가 입력한 substring이 들어가는 버킷에 대해 일괄적으로 객체 버전 및 버킷 삭제 작업을 수행합니다.


> ### 🚧 **주의사항**
>
>스크립트 실행의 결과로 **다수의 버킷이 삭제될 수 있으며** 한 번 삭제된 버킷은 **복구가 불가능합니다.**
실행하실 때 주의해 주세요.

## 사용법
```
python bucketterminator.py
```

## 참고사항
- `boto3` 모듈이 설치되어 있어야 합니다.
- 직접 credential을 입력하거나 프로필을 지정하는 방식을 제공하지 않으며, default 프로필을 사용합니다.
- python 3.7에서 테스트했습니다.
