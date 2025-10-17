from fastapi import APIRouter
from app.services.docx_parser import DocxParser

router = APIRouter()

@router.post("/identify-sections")
async def identify_sections(document_data: dict):
    """
    문서의 각 섹션 식별
    """
    parser = DocxParser()
    
    sections = []
    for paragraph in document_data.get('paragraphs', []):
        section_type = parser.identify_section_type(paragraph['text'])
        sections.append({
            "index": paragraph['index'],
            "text": paragraph['text'],
            "section_type": section_type
        })
    
    return {
        "sections": sections,
        "total_sections": len(sections)
    }
