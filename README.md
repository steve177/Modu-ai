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

## 📸 스크린샷

### 1단계: 양식 업로드
사업계획서 DOCX 양식을 업로드하면 AI가 자동으로 문단과 표를 분석합니다.

### 2단계: 사업 정보 입력
사업 제목, 설명, 요구사항, 주의사항을 입력합니다.

### 3단계: AI 자동 생성
- 시장 분석 자동 생성
- 경쟁사 분석 및 차별화 전략 생성
- 재무 계획 생성 (표 포함)

### 4단계: 다운로드
완성된 사업계획서를 DOCX 형식으로 다운로드합니다.

## 🔧 개발 환경 설정

### 필수 요구사항
- Node.js 18+
- Python 3.11+
- OpenAI API Key

### Backend 설정

```bash
cd backend

# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 환경 변수 설정
cp .env.example .env
# .env 파일에 OPENAI_API_KEY 입력

# 서버 실행
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend 설정

```bash
cd frontend

# 의존성 설치
npm install

# 개발 서버 실행
npm run dev
```

## 🌐 API 문서

서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 주요 엔드포인트

#### 문서 관리
- `POST /api/documents/upload-template` - 사업계획서 양식 업로드
- `POST /api/documents/upload-reference` - 참고 문서 업로드

#### 분석
- `POST /api/analysis/identify-sections` - 섹션 식별

#### AI 생성
- `POST /api/generation/market-analysis` - 시장 분석 생성
- `POST /api/generation/competitive-analysis` - 경쟁사 분석 생성
- `POST /api/generation/financial-plan` - 재무 계획 생성

#### 내보내기
- `POST /api/export/export-docx` - DOCX 파일 다운로드

## 🚀 배포

### Cloudflare Pages 배포

1. Cloudflare 계정 생성
2. GitHub 저장소 연결
3. 빌드 설정:
   - Build command: `cd frontend && npm install && npm run build`
   - Build output directory: `frontend/dist`
4. 환경 변수 설정 (OPENAI_API_KEY)

### 수동 배포

```bash
# Frontend 빌드
cd frontend
npm run build

# Cloudflare Pages CLI 사용
npx wrangler pages publish frontend/dist --project-name=auto-business-plan
```

## 🔐 보안 고려사항

- OpenAI API Key는 절대 노출하지 마세요
- 프로덕션 환경에서는 CORS 설정을 특정 도메인으로 제한하세요
- 파일 업로드 크기 제한을 설정하세요
- 사용자 인증 시스템을 추가하는 것을 권장합니다

## 🤝 기여 방법

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 로드맵

- [ ] DOCX 템플릿 더 정교한 파싱
- [ ] 사용자 인증 및 프로젝트 저장 기능
- [ ] 다국어 지원 (영문 사업계획서)
- [ ] 실시간 협업 편집 기능
- [ ] 템플릿 마켓플레이스
- [ ] PDF 출력 지원
- [ ] 사업계획서 버전 관리
- [ ] AI 모델 선택 옵션 (GPT-4, Claude 등)

## 💡 사용 팁

1. **상세한 정보 입력**: AI가 더 나은 결과를 생성하려면 사업 정보를 구체적으로 입력하세요
2. **참고 자료 활용**: 관련 문서를 참고 자료로 업로드하면 더 정확한 분석이 가능합니다
3. **검토 필수**: AI가 생성한 내용은 반드시 검토하고 수정하세요
4. **표 형식**: 재무 계획 등 표가 필요한 부분은 템플릿에 표 형식을 포함하세요

## ❓ FAQ

**Q: OpenAI API 비용은 얼마나 드나요?**
A: GPT-4 API 사용량에 따라 다릅니다. 일반적인 사업계획서 생성에는 $0.5-2 정도 소요됩니다.

**Q: 오프라인에서 사용할 수 있나요?**
A: 현재 버전은 OpenAI API를 사용하므로 인터넷 연결이 필요합니다.

**Q: 한글 외 다른 언어도 지원하나요?**
A: 현재는 한글을 주로 지원하지만, 입력 내용에 따라 다국어도 가능합니다.

## 📞 문의

- 이슈: [GitHub Issues](https://github.com/steve177/Modu-ai/issues)
- 이메일: your-email@example.com

## 📄 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

**Made with ❤️ using MoAI-ADK**

AI가 만드는 미래, 사업계획서 작성의 혁신을 경험하세요! 🚀
