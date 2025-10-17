# 자동 사업계획서 작성기 - 프로젝트 요약

## 📊 프로젝트 개요

**프로젝트명**: Auto Business Plan Generator (자동 사업계획서 작성기)
**저장소**: https://github.com/steve177/Modu-ai
**개발 기간**: 2025-10-17
**기술 스택**: React + TypeScript + FastAPI + GPT-4

## ✅ 완성된 기능

### 1. 프론트엔드 (React + TypeScript)
- ✅ 4단계 사용자 워크플로우 UI
- ✅ 사업계획서 양식 업로드 인터페이스
- ✅ 사업 정보 입력 폼
- ✅ AI 생성 버튼 (시장분석, 경쟁사분석, 재무계획)
- ✅ DOCX 다운로드 기능
- ✅ TailwindCSS 반응형 디자인
- ✅ Vite 빌드 시스템

### 2. 백엔드 (FastAPI + Python)
- ✅ DOCX 파일 파싱 서비스 (표 분석 포함)
- ✅ GPT-4 API 통합
- ✅ AI 자동 생성 서비스
  - 시장 분석 생성
  - 경쟁사 분석 생성
  - 재무 계획 생성
- ✅ DOCX 문서 생성 및 출력
- ✅ 참고 문서 업로드 처리
- ✅ RESTful API 엔드포인트
- ✅ CORS 설정

### 3. 핵심 기능

#### DOCX 파싱 (표 분석)
```python
- 문단 추출 및 분석
- 표 구조 파싱 (헤더, 행, 열)
- 섹션 타입 자동 식별
- 메타데이터 추출
```

#### AI 자동 생성
```python
- GPT-4 Turbo 사용
- 컨텍스트 기반 프롬프트 생성
- 시장/경쟁사/재무 분석 자동화
- 한글 출력 최적화
```

#### DOCX 출력
```python
- 템플릿 기반 문서 생성
- 표 형식 유지
- 스타일링 (제목, 본문, 표)
- BytesIO 스트리밍
```

## 📁 프로젝트 구조

```
auto-business-plan/
├── frontend/
│   ├── src/
│   │   ├── App.tsx           # 메인 애플리케이션
│   │   ├── main.tsx          # React 엔트리
│   │   └── index.css         # 스타일
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   └── tsconfig.json
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── documents.py  # 문서 업로드 API
│   │   │   ├── analysis.py   # 분석 API
│   │   │   ├── generation.py # AI 생성 API
│   │   │   └── export.py     # 내보내기 API
│   │   ├── services/
│   │   │   ├── docx_parser.py      # DOCX 파싱
│   │   │   ├── ai_generator.py     # AI 생성
│   │   │   └── docx_generator.py   # DOCX 출력
│   │   ├── models/
│   │   │   └── __init__.py   # Pydantic 모델
│   │   └── main.py           # FastAPI 앱
│   └── requirements.txt
│
├── README.md
├── .gitignore
└── PROJECT_SUMMARY.md
```

## 🔑 주요 API 엔드포인트

| 메서드 | 경로 | 설명 |
|--------|------|------|
| POST | `/api/documents/upload-template` | 사업계획서 양식 업로드 |
| POST | `/api/documents/upload-reference` | 참고 문서 업로드 |
| POST | `/api/analysis/identify-sections` | 섹션 식별 |
| POST | `/api/generation/market-analysis` | 시장 분석 생성 |
| POST | `/api/generation/competitive-analysis` | 경쟁사 분석 생성 |
| POST | `/api/generation/financial-plan` | 재무 계획 생성 |
| POST | `/api/export/export-docx` | DOCX 다운로드 |
| GET | `/docs` | API 문서 (Swagger) |

## 🚀 실행 방법

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# .env에 OPENAI_API_KEY 설정
uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 🎯 사용 플로우

1. **양식 업로드**: 사업계획서 DOCX 양식 업로드
2. **정보 입력**: 사업 제목, 설명, 요구사항 입력
3. **AI 생성**: 시장분석/경쟁사분석/재무계획 자동 생성
4. **다운로드**: 완성된 DOCX 파일 다운로드

## 🔧 환경 변수

```env
OPENAI_API_KEY=your_openai_api_key_here
APP_ENV=development
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000
```

## 📦 의존성

### Frontend
- React 18
- TypeScript 5
- Vite 5
- TailwindCSS 3
- Lucide React (아이콘)

### Backend
- FastAPI 0.108
- Python-docx 1.1
- OpenAI 1.6
- Uvicorn 0.25
- Pydantic 2.5

## 🌐 배포 (Todo)

### Cloudflare Pages
- Frontend 빌드 결과물 배포
- 환경 변수 설정 필요
- GitHub Actions 연동 (수동 설정 필요)

## 🔮 향후 개발 계획

- [ ] Cloudflare Pages 배포 완료
- [ ] GitHub Actions 자동 배포 설정
- [ ] 사용자 인증 시스템
- [ ] 프로젝트 저장/불러오기
- [ ] 실시간 편집 기능
- [ ] PDF 출력 지원
- [ ] 다국어 지원 (영문)
- [ ] 템플릿 마켓플레이스

## 💰 비용 예상

- **OpenAI API**: 사업계획서 1개당 약 $0.5-2
- **Cloudflare Pages**: 무료 (프리 티어)
- **GitHub**: 무료

## 🎨 특징

1. **표 분석 특화**: python-docx를 활용한 정교한 표 파싱
2. **GPT-4 통합**: 최신 AI 모델로 고품질 콘텐츠 생성
3. **한글 최적화**: 한국 사업계획서에 특화된 프롬프트
4. **4단계 워크플로우**: 직관적인 사용자 경험
5. **반응형 디자인**: 모든 기기에서 사용 가능

## 📝 Git 커밋 히스토리

```
1f9b5d5 - feat: Add DOCX export functionality and enhance documentation
b16af3b - chore: Remove GitHub Actions workflow temporarily due to permissions
b27fb8c - feat: Initialize auto business plan generator project
```

## 🔗 링크

- **GitHub 저장소**: https://github.com/steve177/Modu-ai
- **API 문서**: http://localhost:8000/docs (로컬)
- **프론트엔드**: http://localhost:3000 (로컬)

## 👨‍💻 개발자 노트

- GitHub Actions 워크플로우는 권한 문제로 수동 추가 필요
- OpenAI API 키는 반드시 환경 변수로 관리
- CORS 설정은 프로덕션에서 특정 도메인으로 제한 권장
- 파일 업로드 크기 제한 설정 필요

---

**개발 완료**: 2025-10-17
**상태**: MVP 완성 ✅
**다음 단계**: 배포 및 테스트
