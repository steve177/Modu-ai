from fastapi import APIRouter, HTTPException
from app.services.ai_generator import AIGenerator
from app.models import BusinessPlanInput
from typing import List

router = APIRouter()
ai_generator = AIGenerator()

@router.post("/market-analysis")
async def generate_market_analysis(input_data: BusinessPlanInput):
    """
    AI 기반 시장 분석 생성
    """
    try:
        business_info = {
            "title": input_data.title,
            "description": input_data.description,
            "requirements": input_data.requirements
        }
        
        # 참고 문서는 실제 구현에서는 저장소에서 가져옴
        reference_docs = []
        
        analysis = await ai_generator.generate_market_analysis(
            business_info,
            reference_docs
        )
        
        return {
            "section": "market_analysis",
            "content": analysis
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"시장 분석 생성 오류: {str(e)}")

@router.post("/competitive-analysis")
async def generate_competitive_analysis(input_data: BusinessPlanInput):
    """
    AI 기반 경쟁사 분석 생성
    """
    try:
        business_info = {
            "title": input_data.title,
            "description": input_data.description
        }
        
        reference_docs = []
        
        analysis = await ai_generator.generate_competitive_analysis(
            business_info,
            reference_docs
        )
        
        return {
            "section": "competitive_analysis",
            "content": analysis
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"경쟁사 분석 생성 오류: {str(e)}")

@router.post("/financial-plan")
async def generate_financial_plan(input_data: BusinessPlanInput):
    """
    AI 기반 재무 계획 생성
    """
    try:
        business_info = {
            "title": input_data.title,
            "description": input_data.description
        }
        
        # 표 구조는 실제로는 업로드된 양식에서 추출
        table_structure = {}
        
        financial_plan = await ai_generator.generate_financial_plan(
            business_info,
            table_structure
        )
        
        return {
            "section": "financial_plan",
            "content": financial_plan["text"],
            "tables": financial_plan["tables"]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"재무 계획 생성 오류: {str(e)}")
