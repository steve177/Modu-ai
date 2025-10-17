# @SPEC:FEAT-002 - AI-Powered Content Generation

**Status**: Implemented ✅
**Priority**: High
**Version**: 1.0.0
**Last Updated**: 2025-10-17

## Overview

GPT-4 기반 사업계획서 콘텐츠 자동 생성 서비스

## Requirements

### @SPEC:FEAT-002-REQ-001 - Market Analysis Generation
- **Description**: AI가 시장 분석 자동 생성
- **Input**: 사업 정보 (제목, 설명, 요구사항), 참고 문서
- **Output**: 시장 분석 텍스트 (한글)
- **Acceptance Criteria**:
  - 시장 규모 및 성장률 포함
  - 주요 트렌드 분석
  - 타겟 고객 분석
  - 시장 진입 기회 제시
  - 2000 토큰 이내

### @SPEC:FEAT-002-REQ-002 - Competitive Analysis Generation
- **Description**: 경쟁사 분석 및 차별화 전략 생성
- **Input**: 사업 정보, 참고 문서
- **Output**: 경쟁사 분석 텍스트 (한글)
- **Acceptance Criteria**:
  - 최소 3개 경쟁사 분석
  - 강점/약점 비교
  - 차별화 전략 제시
  - 경쟁 우위 요소 명시

### @SPEC:FEAT-002-REQ-003 - Financial Plan Generation
- **Description**: 재무 계획 자동 생성 (표 포함)
- **Input**: 사업 정보, 표 구조
- **Output**: 재무 계획 텍스트 + 표 데이터
- **Acceptance Criteria**:
  - 3개년 매출 계획
  - 비용 구조 분석
  - 손익 예측
  - 자금 조달 계획
  - 표 형식 데이터 포함

### @SPEC:FEAT-002-REQ-004 - Context-Aware Prompting
- **Description**: 컨텍스트 기반 프롬프트 생성
- **Input**: 사업 정보, 섹션 타입
- **Output**: 최적화된 GPT-4 프롬프트
- **Acceptance Criteria**:
  - 섹션별 맞춤 시스템 프롬프트
  - 참고 문서 컨텍스트 포함
  - 한글 출력 명시
  - 구조화된 출력 요청

## Implementation Reference

**@CODE:ai-generator-service**
- File: `backend/app/services/ai_generator.py`
- Class: `AIGenerator`
- Methods:
  - `generate_market_analysis(business_info, reference_docs) -> str`
  - `generate_competitive_analysis(business_info, reference_docs) -> str`
  - `generate_financial_plan(business_info, table_structure) -> Dict`
  - `_create_market_analysis_prompt(...) -> str`
  - `_create_competitive_analysis_prompt(...) -> str`
  - `_create_financial_plan_prompt(...) -> str`

## Test Reference

**@TEST:ai-generator-unit**
- File: `.test/unit/test_ai_generator.py`
- **@TEST:ai-generator-integration**
- File: `.test/integration/test_ai_generator_integration.py`

## API Configuration

- Model: `gpt-4-turbo-preview`
- Temperature: 0.7
- Max Tokens: 2000-2500
- System Role: 전문 사업계획서 작성자/시장 전문가/재무 전문가

## Dependencies

- `openai==1.6.1`
- Environment: `OPENAI_API_KEY`

## Related Specifications

- @SPEC:FEAT-001 (DOCX Parser)
- @SPEC:FEAT-003 (API Endpoints)

## Traceability

| SPEC | CODE | TEST | DOC |
|------|------|------|-----|
| @SPEC:FEAT-002-REQ-001 | @CODE:ai-generator-service | @TEST:ai-generator-unit-001 | @DOC:api-generation |
| @SPEC:FEAT-002-REQ-002 | @CODE:ai-generator-service | @TEST:ai-generator-unit-002 | @DOC:api-generation |
| @SPEC:FEAT-002-REQ-003 | @CODE:ai-generator-service | @TEST:ai-generator-unit-003 | @DOC:api-generation |
| @SPEC:FEAT-002-REQ-004 | @CODE:ai-generator-service | @TEST:ai-generator-unit-004 | @DOC:api-generation |

## Quality Gates (TRUST-5)

- ✅ **T**est-first: Mock OpenAI API for testing
- ✅ **R**eadable: Clear prompt templates
- ✅ **U**nified: Consistent async patterns
- ✅ **S**ecured: API key from environment only
- ✅ **T**rackable: Full @TAG system

## Security Considerations

- API key는 환경 변수에서만 로드
- 민감한 정보 로깅 금지
- Rate limiting 고려
- 에러 핸들링 필수

## Cost Estimation

- Market Analysis: ~$0.10-0.30
- Competitive Analysis: ~$0.10-0.30
- Financial Plan: ~$0.15-0.40
- **Total per business plan**: ~$0.35-1.00

## Notes

- GPT-4 API 응답 시간: 평균 5-15초
- 네트워크 오류 시 재시도 로직 필요
- 향후 Claude, Gemini 등 다른 모델 지원 계획
