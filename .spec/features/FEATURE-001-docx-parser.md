# @SPEC:FEAT-001 - DOCX Parser with Table Analysis

**Status**: Implemented ✅
**Priority**: High
**Version**: 1.0.0
**Last Updated**: 2025-10-17

## Overview

DOCX 파일을 파싱하여 문단, 표, 메타데이터를 추출하는 서비스

## Requirements

### @SPEC:FEAT-001-REQ-001 - Document Parsing
- **Description**: DOCX 파일을 읽어 구조화된 데이터로 변환
- **Input**: DOCX 파일 경로
- **Output**: JSON 형식의 문서 구조
- **Acceptance Criteria**:
  - 모든 문단이 순서대로 추출됨
  - 문단 스타일 정보 포함
  - 빈 문단은 제외

### @SPEC:FEAT-001-REQ-002 - Table Analysis (핵심 기능)
- **Description**: 표를 파싱하여 헤더, 행, 열 정보 추출
- **Input**: DOCX 내 표 객체
- **Output**: 구조화된 표 데이터
- **Acceptance Criteria**:
  - 첫 번째 행을 헤더로 인식
  - 모든 셀의 텍스트 추출
  - 행/열 인덱스 정보 포함
  - 병합된 셀 처리

### @SPEC:FEAT-001-REQ-003 - Section Type Identification
- **Description**: 문단의 섹션 타입 자동 식별
- **Input**: 문단 텍스트
- **Output**: 섹션 타입 (market_analysis, competitive_analysis, financial_plan 등)
- **Acceptance Criteria**:
  - 키워드 기반 분류
  - 한글/영문 키워드 지원
  - 매칭 없을 시 "general" 반환

### @SPEC:FEAT-001-REQ-004 - Metadata Extraction
- **Description**: 문서의 메타데이터 추출
- **Input**: DOCX 파일
- **Output**: 제목, 저자, 주제 등
- **Acceptance Criteria**:
  - Core properties 접근
  - 누락된 필드는 빈 문자열 반환

## Implementation Reference

**@CODE:docx-parser-service**
- File: `backend/app/services/docx_parser.py`
- Class: `DocxParser`
- Methods:
  - `parse_document(file_path: str) -> Dict[str, Any]`
  - `_parse_table(table, table_idx: int) -> Dict[str, Any]`
  - `identify_section_type(text: str) -> str`

## Test Reference

**@TEST:docx-parser-unit**
- File: `.test/unit/test_docx_parser.py`
- Coverage: 80%+

## Dependencies

- `python-docx==1.1.0`

## Related Specifications

- @SPEC:FEAT-002 (AI Generator)
- @SPEC:FEAT-004 (DOCX Export)

## Traceability

| SPEC | CODE | TEST | DOC |
|------|------|------|-----|
| @SPEC:FEAT-001-REQ-001 | @CODE:docx-parser-service | @TEST:docx-parser-unit-001 | @DOC:api-docx-parser |
| @SPEC:FEAT-001-REQ-002 | @CODE:docx-parser-service | @TEST:docx-parser-unit-002 | @DOC:api-docx-parser |
| @SPEC:FEAT-001-REQ-003 | @CODE:docx-parser-service | @TEST:docx-parser-unit-003 | @DOC:api-docx-parser |
| @SPEC:FEAT-001-REQ-004 | @CODE:docx-parser-service | @TEST:docx-parser-unit-004 | @DOC:api-docx-parser |

## Quality Gates (TRUST-5)

- ✅ **T**est-first: TDD approach with unit tests
- ✅ **R**eadable: Clear method names and docstrings
- ✅ **U**nified: Consistent with project architecture
- ✅ **S**ecured: Safe file handling with try-except
- ✅ **T**rackable: Full @TAG system implementation

## Notes

- 표 분석이 가장 중요한 핵심 기능
- 병합된 셀 처리는 향후 개선 예정
- 이미지/차트 추출은 현재 버전에서 미지원
