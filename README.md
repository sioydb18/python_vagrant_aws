# vagrant_alpine_docker_simpleLogic

## 1. vagrant download
<br/>

<img src="images/port1.png">
<br/><br/>
Vagrant 공식홈페이지에서 Window용 msi 파일을 다운 받는다.
<br/><br/>
<img src="images/port2.png">
<br/><br/>
next 누르고 바로 설치하고나서
<br/><br/>
<img src="images/port3.png">
<br/>
시스템을 다시시작해준다.
<br/>

## 2. Vagrantfile 있는 폴더에서 git bash 열기
<br/>
리눅스 명령어 사용을 위해 Vagrantfile이 있는 폴더에서 우클릭하여 git bash를 실행한다.
<br/>

## 3. vagrant global-status로 전역상태 확인
<br/>
<img src="images/port8.png">
<br/>
vagrant global-status 명령어로 box를 검색하니 아직 실행한 적이 없어 나오지 않는 걸 알 수 있다.
<br/>


## 4. vagrant up
<br/>
vagrant를 실행한다.


## 5. virtual box에서 alpine linux 실행 확인
<br/>
<img src="images/port6.png">
<br/>
<img src="images/port7.png">
<br/>
이렇게 virtual box에 alpine linux가 생성 된 것을 확인 할 수 있다. 기본 아이디 패스워드는 vagrant로 로그인 할 수 있다.


## 6. vagrant global-status
<br/>
<img src="images/port8.png">
<br/>
이렇게 동작하는 걸 확인 할 수 있다.

## 7. vagrant halt(stop)
<br/>
사용하지 않는다면 이렇게 stop 명령어를 주고

## 8. vagrant detroy
<br/>
<img src="images/port9.png">
<br/>
destroy 명령어로 둘 다 삭제 할 수 있다.