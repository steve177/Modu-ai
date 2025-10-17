# Alfred Commands - MoAI-ADK

**Project**: Auto Business Plan Generator
**Version**: 1.0.0

## Available Commands

### /alfred:1-spec
**Description**: 명세서 생성 워크플로우
**Usage**: `/alfred:1-spec [feature-name]`
**Output**: `.spec/features/` 디렉토리에 SPEC 문서 생성

**Example**:
```
/alfred:1-spec pdf-export
```

**Result**:
- 새 SPEC 문서 생성 with @SPEC tags
- Requirements 정의
- Acceptance criteria 명시
- 관련 아키텍처 문서 링크

---

### /alfred:2-build
**Description**: TDD 기반 빌드 워크플로우 (Red → Green → Refactor)
**Usage**: `/alfred:2-build [spec-id]`
**Output**: 테스트 파일 + 구현 코드 생성

**Workflow**:
1. **Red**: 실패하는 테스트 먼저 작성 (@TEST tags)
2. **Green**: 테스트 통과하는 최소 코드 작성 (@CODE tags)
3. **Refactor**: 코드 품질 개선 (TRUST-5 적용)

**Example**:
```
/alfred:2-build FEAT-001
```

**Result**:
- `.test/` 디렉토리에 테스트 생성
- 해당 서비스/API 코드 구현
- @TAG 자동 삽입

---

### /alfred:3-sync
**Description**: 문서 동기화 및 PR 준비
**Usage**: `/alfred:3-sync`
**Output**: 문서 업데이트 + 추적성 매트릭스

**Actions**:
1. SPEC ↔ CODE ↔ TEST ↔ DOC 추적성 검증
2. README 업데이트
3. API 문서 생성 (Swagger)
4. 추적성 매트릭스 생성
5. Git commit with conventional commit message
6. PR 생성 준비

**Result**:
- `.docs/` 디렉토리 업데이트
- `TRACEABILITY.md` 생성
- Git branch + commit 생성

---

## Tag System

### @SPEC Tags
```
@SPEC:FEAT-001          # Feature specification
@SPEC:FEAT-001-REQ-001  # Specific requirement
```

### @TEST Tags
```
@TEST:docx-parser-unit          # Test suite
@TEST:docx-parser-unit-001      # Specific test
@TEST:ai-generator-integration  # Integration test
```

### @CODE Tags
```
@CODE:docx-parser-service        # Service implementation
@CODE:docx-parser-service-parse  # Specific method
@CODE:api-documents-upload       # API endpoint
```

### @DOC Tags
```
@DOC:api-docx-parser    # API documentation
@DOC:user-guide-upload  # User guide
```

---

## Quality Gates (TRUST-5)

Every feature must pass:

- **T**est-first: TDD approach mandatory
- **R**eadable: Clear naming, comments, docstrings
- **U**nified: Consistent architecture patterns
- **S**ecured: Security best practices
- **T**rackable: Full @TAG system implementation

---

## Traceability Matrix

| SPEC | CODE | TEST | DOC | Status |
|------|------|------|-----|--------|
| @SPEC:FEAT-001 | @CODE:docx-parser-service | @TEST:docx-parser-unit | @DOC:api-docx-parser | ✅ |
| @SPEC:FEAT-002 | @CODE:ai-generator-service | @TEST:ai-generator-unit | @DOC:api-generation | ✅ |
| @SPEC:FEAT-003 | @CODE:api-endpoints | @TEST:api-integration | @DOC:api-reference | ⏳ |

---

## Usage Example

### Complete Feature Development Cycle

```bash
# 1. Create Specification
/alfred:1-spec table-export-excel

# Output: .spec/features/FEATURE-005-table-export-excel.md

# 2. Build with TDD
/alfred:2-build FEAT-005

# Output: 
# - .test/unit/test_excel_exporter.py (Red)
# - backend/app/services/excel_exporter.py (Green)
# - Refactored code (TRUST-5)

# 3. Sync Documentation
/alfred:3-sync

# Output:
# - Updated README.md
# - Generated API docs
# - Created TRACEABILITY.md
# - Git commit with tags
```

---

## Configuration

Configuration file: `.claude/config.json`

```json
{
  "workflows": {
    "spec": "/alfred:1-spec",
    "build": "/alfred:2-build",
    "sync": "/alfred:3-sync"
  },
  "quality_gates": {
    "test_first": true,
    "readable": true,
    "unified": true,
    "secured": true,
    "trackable": true
  }
}
```

---

## Notes

- All commands are idempotent
- Tags are automatically validated
- TRUST-5 gates are enforced
- Traceability is automatically maintained
- Git workflow is integrated

---

**Powered by MoAI-ADK** 🚀
