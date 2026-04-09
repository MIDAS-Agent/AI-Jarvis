# AI-Jarvis

AI를 통한 업무 효율성 강화 및 자동화

## 프로젝트 소개

대학 행정 업무를 자동화하고 효율성을 높이기 위한 AI 기반 도구 모음입니다.

## 프로젝트 구조

AI-Jarvis/
├── .github/workflows/   # GitHub Actions 워크플로우
│   └── autofix.yml      # Claude AutoFix (PR 자동 수정)
├── src/                 # 소스 코드
│   └── automation.py    # 업무 자동화 핵심 모듈
├── tests/               # 테스트 코드
│   └── test_automation.py
├── pytest.ini           # pytest 설정
├── requirements.txt     # Python 패키지 의존성
└── README.md

## 설치 및 실행

pip install -r requirements.txt

## 테스트 실행

pytest

## CI/CD

- Claude AutoFix: PR에서 테스트 실패 시 Claude AI가 자동으로 원인 분석 및 수정 PR 생성
