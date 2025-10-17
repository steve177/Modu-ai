from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.services.docx_parser import DocxParser
import aiofiles
import os
import tempfile

router = APIRouter()

@router.post("/upload-template")
async def upload_template(file: UploadFile = File(...)):
    """
    사업계획서 양식 업로드 및 분석
    """
    if not file.filename.endswith('.docx'):
        raise HTTPException(status_code=400, detail="DOCX 파일만 업로드 가능합니다.")
    
    try:
        # 임시 파일 저장
        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_path = temp_file.name
        
        # 문서 파싱
        parser = DocxParser()
        document_structure = parser.parse_document(temp_path)
        
        # 임시 파일 삭제
        os.unlink(temp_path)
        
        return {
            "message": "문서 분석 완료",
            "filename": file.filename,
            "structure": document_structure
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"문서 분석 오류: {str(e)}")

@router.post("/upload-reference")
async def upload_reference(file: UploadFile = File(...)):
    """
    참고 문서 업로드
    """
    try:
        content = await file.read()
        
        # 파일 형식에 따라 처리
        if file.filename.endswith('.txt'):
            text_content = content.decode('utf-8')
        elif file.filename.endswith('.docx'):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as temp_file:
                temp_file.write(content)
                temp_path = temp_file.name
            
            parser = DocxParser()
            doc_data = parser.parse_document(temp_path)
            text_content = "\n".join([p['text'] for p in doc_data['paragraphs']])
            
            os.unlink(temp_path)
        else:
            text_content = "지원되지 않는 파일 형식"
        
        return {
            "message": "참고 문서 업로드 완료",
            "filename": file.filename,
            "content": text_content[:500]  # 처음 500자만 미리보기
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"참고 문서 처리 오류: {str(e)}")
