from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import documents, analysis, generation

app = FastAPI(
    title="Auto Business Plan Generator API",
    description="AI-powered business plan generation service",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서는 특정 도메인으로 제한
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(documents.router, prefix="/api/documents", tags=["documents"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["analysis"])
app.include_router(generation.router, prefix="/api/generation", tags=["generation"])

@app.get("/")
async def root():
    return {
        "message": "Auto Business Plan Generator API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
