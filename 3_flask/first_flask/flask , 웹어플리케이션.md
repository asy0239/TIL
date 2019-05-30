# flask , 웹어플리케이션



```python
from flask import Flask, render_template
import random

print(__name__)
app = Flask(__name__)


@app.route('/')   ## app은 app.py, 즉 작업공안의 py파일 이름을 뜻 함.
def index():
    return render_template('index.html')  ## html파일을 불러온다, app.py와 같은위치에 templates 디렉토리를 생성하고 그 안에 index.html 파일이 있어야 함.


@app.route('/lotto/1')
def pick_lotto():
    lucky_numbers = random.sample(range(1, 46), 6)
    return f'{lucky_numbers}'


@app.route('/lotto/<num>')
def find_lotto(num):
    return num


@app.route('/square/<int:num>')  ## int로 변경해 입력 받을 수 있다.
def square(num):
    result = num ** 2
    return f'{result}'


if __name__ == '__main__':
    app.run(debug=True)
```

## flask , 웹 어플리케이션 순서

1. client 에서 url로 요청이 들어옴   # request, url
2. server 에서 url 분석을 통해 그게 맞는 함수가 실행됨  # action
3. 함수 return 값으로 그 함수에 지정된 html 로 보내어줌 # html
4. html 받아 화면에 보여줌 # response