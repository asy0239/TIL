# 190527 기초 설치 및 사용법 학습

## markdown 작성하기

### 제목 작성

제목은 , Semantic 하게 작성한다.

### 나열(리스트) 작성하기

#### 순서가 있는 리스트

1. WeMakeO 앱을 받는다.
2. 회원가입한다.
   - 카카오
   - 네이버
   - 페북
3. W카페를 찾는다.
4. 커피를 주문한다.
5. 알림이 오면 픽업하러 간다.

#### 순서가 없는 리스트

- 파이썬 설치하기
- 타이포라 설치하기
- Git 설치하기

### 일반 문단 작성하기

그냥 작성하면 된다.

### 코드 블럭 작성하기

터미널에서 `python -e` 라고 입력하면 , **코드가 실행**됩니다. <- ctrl + b로 강조 사용    

```python
def index():
    return 'hi'

def create():
    return 'typora'
```

$$
latex 작성하기를 읽고 사용법 익히기
$$



### 표 그리기

| title | content | desc | a    | b    | c    | d    |
| ----- | ------- | ---- | ---- | ---- | ---- | ---- |
|       |         |      |      |      |      |      |
|       |         |      |      |      |      |      |
|       |         |      |      |      |      |      |

ctrl + enter 는 표 행 생성

### 단축키

ctrl + t 는 표 그리기( 파이프 )

ctrl + , 는 환경설정 불러옴

ctrl + shift + m 으로 수식 박스 생성

ctrl + b 로 강조 사용

## git , git_hub 사용법

```sh
$ git init # pwd 에서 관리를 시작, 드라이버를 지정
$ git remote add origin "url"   # 저장할 git_hub의 저장소 지정 , origin = 저장소이름
$ git add dir_name # 저장할 목표물 지정 , 스냅샷
$ git commit -m "message" # 메세지와 함께 git_hub 저장소에 지정
$ git push origin master  # git_hub에 저장한다 
$ git status # 지금 스냅샷의 상태를 보여줌
$ git clone 상대 url teacher_TIL # 상대의 자료를 가져온다
$ git pull # 저장된 상대 자료위치에서 pull 을 하면 변경사항만 가져온다
```

