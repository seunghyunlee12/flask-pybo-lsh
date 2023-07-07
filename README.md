# flask-pybo

## 프로젝트 소개

### 시작 동기

플라스크(Flask)를 활용하여 간단한 게시판을 만들었습니다. HTML5, CSS3, JavaScript, BootStrap, SQLite 등을 활용하였고, 웹의 기본적인 구조와 웹 프레임워크를 조금 더 습득하는 것을 목적으로 진행하였습니다. 또한 서버와 데이터베이스(DB) 연동에 대한 내용도 공부하였습니다.

### 폴더와 파일 구조

flask-pybo
```├─ .idea
```│ └─ inspectionProfiles
```├─ migrations
```│ ├─ versions
```│ │ └─ pycache
```│ └─ pycache
```├─ pybo
```│ ├─ static
```│ ├─ templates
```│ │ ├─ answer
```│ │ ├─ auth
```│ │ └─ question
```│ ├─ views
```│ │ └─ pycache
```│ └─ pycache
└─ pycache  

- **models.py**: 데이터베이스를 처리하는 파일로 ORM을 지원하는 SQLAlchemy를 사용하여 모델 기반으로 데이터베이스를 처리합니다.
- **forms.py**: 서버로 전송된 폼을 처리하는 파일로 WTForms 라이브러리를 사용하여 모델 기반으로 폼을 처리합니다.
- **views**: 화면을 구성하는 함수들로 구성된 뷰 파일들을 저장하는 디렉터리입니다.
- **static**: CSS, JavaScript, 이미지 파일(.css, .js, .jpg, .png 등)을 저장하는 디렉터리입니다.
- **templates**: HTML 파일을 저장하는 디렉터리로, 질문 목록, 질문 상세 등의 HTML 파일을 저장합니다.
- **config.py**: 프로젝트 환경을 설정하는 파일로, 환경 변수, 데이터베이스 등의 설정을 저장합니다.

## 사용 가능한 기능

- 계정 생성, 로그인, 로그아웃
- 글 생성/수정 및 댓글 생성/수정
- 글/댓글 추천
- 글 작성 시 마크다운 사용
- 검색 기능
