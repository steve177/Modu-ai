from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.services.docx_generator import DocxGenerator
from app.models import BusinessPlanInput
from typing import Dict, Any

router = APIRouter()

@router.post("/export-docx")
async def export_docx(data: Dict[str, Any]):
    """
    생성된 사업계획서를 DOCX로 내보내기
    """
    try:
        template_structure = data.get('template_structure', {})
        generated_content = data.get('generated_content', {})
        business_info = data.get('business_info', {})
        
        # DOCX 생성
        generator = DocxGenerator()
        docx_stream = generator.create_business_plan(
            template_structure,
            generated_content,
            business_info
        )
        
        # 파일명 생성
        filename = f"{business_info.get('title', 'business_plan')}.docx"
        filename = filename.replace(' ', '_')
        
        return StreamingResponse(
            docx_stream,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DOCX 생성 오류: {str(e)}")
