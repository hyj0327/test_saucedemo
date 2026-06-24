# SauceDemo Test

## 프로젝트 소개

- SauceDemo(https://www.saucedemo.com/) E2E 자동화 테스트 입니다.

## 🛠 기술 스택

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Playwright](https://img.shields.io/badge/-playwright-%232EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3)

## 설치 방법
1. 레포지토리 클론
```commandline
git clone https://github.com/hyj0327/test_saucedemo.git
```
2. 패키지 설치
```commandline
pip install -r requirements.txt
```
3. Playwright 브라우저 설치
```commandline
playwright install chromium
playwright install --with-deps chromium
```

## 실행
- 전체 테스트 실행
```commandline
pytest
```

- 특정 파일 / 테스트만 실행
```commandline
pytest tests/test_login.py
```

- Headed 모드
```commandline
pytest --headed

# 실행 속도 조절
pytest --headed --slowmo=1000 
```

## Test Case
https://docs.google.com/spreadsheets/d/1YH8JFLgbjMw6LqD9XAyePEy2DqwDlM59IS2Y_gXBKso/edit?usp=sharing