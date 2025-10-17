from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class DocumentStructure(BaseModel):
    """문서 구조 모델"""
    paragraphs: List[Dict[str, Any]]
    tables: List[Dict[str, Any]]
    metadata: Dict[str, Any]

class ReferenceDocument(BaseModel):
    """참고 문서 모델"""
    filename: str
    content: str
    document_type: str

class BusinessPlanInput(BaseModel):
    """사업계획서 입력 모델"""
    title: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    notes: Optional[str] = None
    reference_documents: Optional[List[str]] = []

class GeneratedSection(BaseModel):
    """생성된 섹션 모델"""
    section_name: str
    content: str
    tables: Optional[List[Dict[str, Any]]] = []

class BusinessPlanOutput(BaseModel):
    """사업계획서 출력 모델"""
    sections: List[GeneratedSection]
    metadata: Dict[str, Any]
