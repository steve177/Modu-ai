from openai import AsyncOpenAI
from typing import Dict, Any, List
import os
import logging

logger = logging.getLogger(__name__)

class AIGenerator:
    """GPT-4 기반 사업계획서 자동 생성 서비스"""
    
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            logger.warning("OPENAI_API_KEY not found. AI generation will be disabled.")
        self.client = AsyncOpenAI(api_key=api_key) if api_key else None
    
    async def generate_market_analysis(
        self, 
        business_info: Dict[str, Any],
        reference_docs: List[str]
    ) -> str:
        """
        시장 분석 자동 생성
        
        Args:
            business_info: 사업 정보
            reference_docs: 참고 문서 내용
            
        Returns:
            생성된 시장 분석 텍스트
        """
        if not self.client:
            return "AI 생성 기능이 비활성화되어 있습니다. OPENAI_API_KEY를 설정해주세요."
        
        prompt = self._create_market_analysis_prompt(business_info, reference_docs)
        
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": "당신은 전문 사업계획서 작성자입니다. 시장 분석을 상세하고 체계적으로 작성합니다."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"시장 분석 생성 오류: {str(e)}")
            raise
    
    async def generate_competitive_analysis(
        self,
        business_info: Dict[str, Any],
        reference_docs: List[str]
    ) -> str:
        """
        경쟁사 분석 및 차별화 전략 생성
        
        Args:
            business_info: 사업 정보
            reference_docs: 참고 문서 내용
            
        Returns:
            생성된 경쟁사 분석 텍스트
        """
        if not self.client:
            return "AI 생성 기능이 비활성화되어 있습니다."
        
        prompt = self._create_competitive_analysis_prompt(business_info, reference_docs)
        
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": "당신은 시장 전문가입니다. 경쟁사 분석과 차별화 전략을 명확하게 제시합니다."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"경쟁사 분석 생성 오류: {str(e)}")
            raise
    
    async def generate_financial_plan(
        self,
        business_info: Dict[str, Any],
        table_structure: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        재무 계획 생성 (표 포함)
        
        Args:
            business_info: 사업 정보
            table_structure: 표 구조
            
        Returns:
            생성된 재무 계획 (텍스트 + 표 데이터)
        """
        if not self.client:
            return {
                "text": "AI 생성 기능이 비활성화되어 있습니다.",
                "tables": []
            }
        
        prompt = self._create_financial_plan_prompt(business_info, table_structure)
        
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": "당신은 재무 전문가입니다. 현실적이고 구체적인 재무 계획을 수립합니다."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2500
            )
            
            content = response.choices[0].message.content
            
            # 표 데이터 파싱 (간단한 예시)
            tables = self._parse_financial_tables(content)
            
            return {
                "text": content,
                "tables": tables
            }
            
        except Exception as e:
            logger.error(f"재무 계획 생성 오류: {str(e)}")
            raise
    
    def _create_market_analysis_prompt(
        self,
        business_info: Dict[str, Any],
        reference_docs: List[str]
    ) -> str:
        """시장 분석 프롬프트 생성"""
        ref_context = "\n\n".join(reference_docs) if reference_docs else "참고 문서 없음"
        
        return f"""
다음 사업에 대한 상세한 시장 분석을 작성해주세요:

**사업 정보:**
- 제목: {business_info.get('title', 'N/A')}
- 설명: {business_info.get('description', 'N/A')}
- 요구사항: {business_info.get('requirements', 'N/A')}

**참고 자료:**
{ref_context}

**작성 내용:**
1. 시장 규모 및 성장률
2. 주요 트렌드
3. 타겟 고객 분석
4. 시장 진입 기회

한글로 상세하게 작성하되, 구조화되고 전문적으로 작성해주세요.
"""
    
    def _create_competitive_analysis_prompt(
        self,
        business_info: Dict[str, Any],
        reference_docs: List[str]
    ) -> str:
        """경쟁사 분석 프롬프트 생성"""
        ref_context = "\n\n".join(reference_docs) if reference_docs else "참고 문서 없음"
        
        return f"""
다음 사업에 대한 경쟁사 분석 및 차별화 전략을 작성해주세요:

**사업 정보:**
- 제목: {business_info.get('title', 'N/A')}
- 설명: {business_info.get('description', 'N/A')}

**참고 자료:**
{ref_context}

**작성 내용:**
1. 주요 경쟁사 분석 (최소 3개)
2. 경쟁사 대비 강점/약점
3. 차별화 전략
4. 경쟁 우위 요소

한글로 상세하게 작성해주세요.
"""
    
    def _create_financial_plan_prompt(
        self,
        business_info: Dict[str, Any],
        table_structure: Dict[str, Any]
    ) -> str:
        """재무 계획 프롬프트 생성"""
        return f"""
다음 사업에 대한 3개년 재무 계획을 작성해주세요:

**사업 정보:**
- 제목: {business_info.get('title', 'N/A')}
- 설명: {business_info.get('description', 'N/A')}

**작성 내용:**
1. 매출 계획 (연도별)
2. 비용 구조
3. 손익 예측
4. 자금 조달 계획

표 형식으로 구체적인 숫자를 포함하여 작성해주세요.
"""
    
    def _parse_financial_tables(self, content: str) -> List[Dict[str, Any]]:
        """재무 계획에서 표 데이터 추출 (간단한 구현)"""
        # TODO: 더 정교한 파싱 로직 구현
        return []
