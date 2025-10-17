# 자동 사업계획서 작성기 (Auto Business Plan Generator)

AI 기반 자동 사업계획서 생성 웹 애플리케이션

## 🎯 주요 기능

### 1. DOCX 양식 분석
- 사업계획서 양식 업로드 (DOCX)
- 문단 및 표 자동 분석
- 구조화된 데이터 추출

### 2. 참고자료 관리
- 참고 문서 업로드 (PDF, DOCX, TXT)
- 텍스트 입력 (사업계획서 제목, 주의사항, 필수 사항)
- 멀티미디어 자료 첨부

### 3. AI 자동 작성
- GPT-4 기반 시장 분석
- 자동 경쟁사 분석 및 차별화 전략
- 재무 계획 자동 생성
- SWOT 분석

### 4. 문서 출력
- 완성된 사업계획서 DOCX 다운로드
- 한글 양식 유지
- 표 형식 보존

## 🛠 기술 스택

### Frontend
- React 18
- TypeScript
- Vite
- TailwindCSS
- React Query

### Backend
- Python 3.11+
- FastAPI
- python-docx
- OpenAI GPT-4 API

### 배포
- Cloudflare Pages (Frontend)
- Cloudflare Workers (Backend)
- GitHub Actions (CI/CD)

## 📦 프로젝트 구조

```
auto-business-plan/
├── frontend/              # React TypeScript 앱
│   ├── src/
│   │   ├── components/   # UI 컴포넌트
│   │   ├── pages/        # 페이지
│   │   ├── services/     # API 서비스
│   │   └── utils/        # 유틸리티
│   └── package.json
│
├── backend/              # FastAPI 백엔드
│   ├── app/
│   │   ├── api/         # API 엔드포인트
│   │   ├── services/    # 비즈니스 로직
│   │   ├── models/      # 데이터 모델
│   │   └── utils/       # 유틸리티
│   └── requirements.txt
│
└── README.md
```

## 🚀 시작하기

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🔐 환경 변수

```env
OPENAI_API_KEY=your_openai_api_key
```

## 📝 사용 방법

1. **양식 업로드**: 사업계획서 DOCX 양식 업로드
2. **참고자료 추가**: 관련 문서 및 정보 입력
3. **AI 생성**: 각 섹션별 자동 생성 시작
4. **검토 및 수정**: 생성된 내용 확인 및 편집
5. **다운로드**: 완성된 사업계획서 DOCX 다운로드

## 🤝 기여

GitHub Pull Request를 통해 기여해주세요.

## 📄 라이선스

MIT License

---

**Made with MoAI-ADK** 🚀
