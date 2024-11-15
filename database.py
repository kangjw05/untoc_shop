from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
import os
load_dotenv()


# .env의 정보를 불러온다.
DB_HOST = os.environ.get("DB_HOST")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
ITEM_DB_NAME = os.environ.get("ITEM_DB_NAME")
DB_PORT = os.environ.get("DB_PORT", 3306)

# 어떤 DB와 연결할지 정의한다.
SQLALCHEMY_DATABASE_URL_ITEM = f"mysql+mysqlconnector://root:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{ITEM_DB_NAME}"

# create_engine 함수는 데이터베이스와 연결을 설정할 수 있는 엔진을 생성한다.
# 이 엔진을 통해 데이터베이스와 상호작용할 수 있다.
item_engine = create_engine(SQLALCHEMY_DATABASE_URL_ITEM)

# sessionmaker는 SQLAlchemy에서 세션을 관리하기 위한 함수이다.
# 세션은 데이터베이스에 대한 트랜잭션을 관리하는 객체로, 데이터베이스와의 통신을 효율적으로 처리한다.
item_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=item_engine)

# declarative_base는 SQLAlchemy에서 데이터베이스의 테이블과 매핑될 클래스를 정의할 때 사용하는 기본 클래스이다. 
item_Base = declarative_base()

def get_itemdb():
    db = item_SessionLocal()
    try:
        yield db
    finally:
        db.close()