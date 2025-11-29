# Financial Advisor Agent

**Financial Advisor Agent**는 사용자가 지정한 주식 티커(Ticker)에 대해 포괄적인 투자 조언 보고서를 생성하는 AI 기반 에이전트입니다. Google의 Gemini 모델을 활용하여 데이터 분석, 재무 분석, 뉴스 분석을 수행하고 이를 종합하여 인사이트를 제공합니다.

## 주요 기능

이 프로젝트는 3개의 전문 서브 에이전트와 협력하여 작동합니다:

1.  **Data Analyst (`data_analyst`)**: 주가 데이터 및 기술적 지표를 분석합니다.
2.  **Financial Analyst (`financial_analyst`)**: 회사의 재무 제표 및 건전성을 분석합니다.
3.  **News Analyst (`news_analyst`)**: 최신 뉴스 및 시장 동향을 분석하여 정성적인 정보를 제공합니다.

최종적으로 **Financial Advisor**는 이들의 분석 결과를 종합하여 마크다운 형식의 투자 조언 보고서(`{ticker}_investment_advice.md`)를 생성합니다.

## 설치 및 설정

이 프로젝트는 Python 환경에서 실행됩니다. 의존성 관리를 위해 `uv`를 사용하는 것을 권장합니다.

### 필수 요구 사항

- Python 3.10 이상
- Google Gemini API Key
- Firecrawl API Key (웹 검색용)

### 환경 변수 설정

프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 다음 변수들을 설정해주세요:

```bash
GOOGLE_API_KEY=your_google_api_key
FIRECRAWL_API_KEY=your_firecrawl_api_key
```

### 패키지 설치

`uv`를 사용하여 의존성을 설치합니다:

```bash
uv sync
```

또는 `pip`를 사용할 수 있습니다:

```bash
pip install -r requirements.txt
```

## 사용 방법

에이전트는 `financial_advisor` 패키지 내에 정의되어 있습니다. `main.py`를 통해 실행하거나 다른 스크립트에서 임포트하여 사용할 수 있습니다.

```python
from financial_advisor.agent import financial_advisor

# 에이전트 실행 예시 (구체적인 실행 코드는 구현 필요)
# ...
```

### ADK CLI 사용

`adk` CLI 도구를 사용하여 에이전트를 실행할 수 있습니다. 프로젝트 루트에서 실행하면 에이전트를 자동으로 감지합니다.

**1. 웹 인터페이스로 실행 (테스트 및 시연용):**

```bash
adk web
```

**2. API 서버로 실행 (외부 연동용):**

```bash
adk api_server
```

## 프로젝트 구조

```
.
├── financial_advisor/          # Financial Advisor 에이전트 패키지
│   ├── agent.py                # 메인 에이전트 정의 (FinancialAdvisor)
│   ├── prompt.py               # 에이전트 프롬프트
│   └── sub_agents/             # 서브 에이전트 (Data, Financial, News)
├── tools.py                    # 유틸리티 도구 (웹 검색 등)
├── main.py                     # 진입점 파일
├── .env                        # 환경 변수 파일
└── README.md                   # 프로젝트 문서
```