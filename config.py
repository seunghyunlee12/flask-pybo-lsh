import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLALCHEMY_DATABASE_URI : 데이터베이스 접속 주소
# SQLite 데이터베이스가 사용되고, 데이터베이스 파일은 프로젝트 홈 디렉터리 바로 밑에 저장
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_TRACK_MODIFICATIONS : SQLAlchemy의 이벤트 처리 옵션. 파이보에 필요하지 않아서 False
SECRET_KEY = "dev"
