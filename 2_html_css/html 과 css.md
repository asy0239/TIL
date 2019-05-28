# html 과 css

## html 구성

- head  : 웹 상에서 보여지지 않는 정보들을 담는 공간 
- body : 웹 상에서 보여지는 정보들을 담는 공간
- title : 웹 문서의 제목, 주제를 지정하는 공간
- h1 : 가장 중요한 제목을 적는 공간,   h1,h2,h3,h4,h5,h6 순으로 생성가능
- p : 문단의 구성, 다음 줄의 의미
- img src = ' ' : img 를 불러오는 태그 , src에 url 이나 image 파일이 저장된 경로를 넣어준다.
  1. alt = ' ' : alt 는 대체라는 뜻으로 image를 못 불러올때 대체로 표시해준다.
  2. width = '100' : 가로 크기
  3. height = '100' : 세로 크기

- div : body 안에서 구분자 역할을 하는 태그
- section : div를 더욱 명확하게 표시해주는 태그 section 안에 또 다른 div 를 <명명> 할 수 있다.

꿀 Tip : emmet 이라는 사이트에 유용한 단축키들 정보가 있다. 자동완성 등 

- a href="url 또는 파일의 저장된 위치 경로" : 이동태그를 표시해주는 태그

## css 구성

### style 태그를 사용해 정의하는 방법

html 에서 style 태그를 작성하여 적용한다.

```html
<style>
    article {           # article 은 태그 이름을 말한다.
        color: white;
    	background-color: black;
    	font-size: 40px;
    }
</style>
```



### css 파일을 따로 링크하는 방법

html 이 아닌 css 파일을 따로 지정해 링크를 단다.

```html
<link rel="stylesheet" href="./main.css">  # main.css 는 css파일의 저장 경로를 적는다.
```

css 작성법

```css
tag-name {
	color: red;
	font-size: 10px;
	등등등
}

.class-name {
	color: red; 
}
```

.class-name 해서 class 를 정해 태그에 class 이름으로 사용 가능

