import { useState } from 'react'
import { FileText, Upload, Sparkles, Download } from 'lucide-react'

function App() {
  const [step, setStep] = useState(1)
  const [templateFile, setTemplateFile] = useState<File | null>(null)
  const [templateAnalysis, setTemplateAnalysis] = useState<any>(null)
  const [businessInfo, setBusinessInfo] = useState({
    title: '',
    description: '',
    requirements: '',
    notes: ''
  })

  const handleTemplateUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file && file.name.endsWith('.docx')) {
      setTemplateFile(file)
      
      // API 호출하여 문서 분석
      const formData = new FormData()
      formData.append('file', file)
      
      try {
        const response = await fetch('/api/documents/upload-template', {
          method: 'POST',
          body: formData
        })
        const data = await response.json()
        setTemplateAnalysis(data.structure)
        setStep(2)
      } catch (error) {
        console.error('템플릿 분석 오류:', error)
        alert('템플릿 분석 중 오류가 발생했습니다.')
      }
    } else {
      alert('DOCX 파일만 업로드 가능합니다.')
    }
  }

  const handleGenerate = async (section: string) => {
    try {
      const response = await fetch(`/api/generation/${section}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(businessInfo)
      })
      const data = await response.json()
      console.log(`${section} 생성 완료:`, data)
      alert(`${section} 생성 완료!`)
    } catch (error) {
      console.error(`${section} 생성 오류:`, error)
      alert(`${section} 생성 중 오류가 발생했습니다.`)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <header className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            🚀 자동 사업계획서 작성기
          </h1>
          <p className="text-gray-600">AI가 당신의 사업계획서를 완성합니다</p>
        </header>

        {/* Progress Steps */}
        <div className="flex justify-center mb-8">
          <div className="flex items-center space-x-4">
            {[1, 2, 3, 4].map((s) => (
              <div key={s} className="flex items-center">
                <div className={`w-10 h-10 rounded-full flex items-center justify-center font-bold ${
                  step >= s ? 'bg-indigo-600 text-white' : 'bg-gray-300 text-gray-600'
                }`}>
                  {s}
                </div>
                {s < 4 && <div className="w-12 h-1 bg-gray-300 mx-2" />}
              </div>
            ))}
          </div>
        </div>

        {/* Step 1: Template Upload */}
        {step === 1 && (
          <div className="max-w-2xl mx-auto bg-white rounded-lg shadow-lg p-8">
            <div className="text-center">
              <FileText className="mx-auto mb-4 text-indigo-600" size={64} />
              <h2 className="text-2xl font-bold mb-4">1단계: 사업계획서 양식 업로드</h2>
              <p className="text-gray-600 mb-6">
                작성할 사업계획서 양식(DOCX)을 업로드해주세요.
                <br />
                AI가 문단과 표를 자동으로 분석합니다.
              </p>
              
              <label className="inline-block">
                <input
                  type="file"
                  accept=".docx"
                  onChange={handleTemplateUpload}
                  className="hidden"
                />
                <div className="cursor-pointer bg-indigo-600 text-white px-8 py-3 rounded-lg hover:bg-indigo-700 transition inline-flex items-center space-x-2">
                  <Upload size={20} />
                  <span>양식 업로드</span>
                </div>
              </label>

              {templateFile && (
                <div className="mt-4 text-sm text-gray-600">
                  업로드된 파일: {templateFile.name}
                </div>
              )}
            </div>
          </div>
        )}

        {/* Step 2: Business Information */}
        {step === 2 && (
          <div className="max-w-2xl mx-auto bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-2xl font-bold mb-4">2단계: 사업 정보 입력</h2>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  사업계획서 제목 *
                </label>
                <input
                  type="text"
                  value={businessInfo.title}
                  onChange={(e) => setBusinessInfo({...businessInfo, title: e.target.value})}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-600 focus:border-transparent"
                  placeholder="예: AI 기반 스마트 물류 플랫폼"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  사업 설명
                </label>
                <textarea
                  value={businessInfo.description}
                  onChange={(e) => setBusinessInfo({...businessInfo, description: e.target.value})}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-600 focus:border-transparent"
                  rows={4}
                  placeholder="사업에 대한 간단한 설명을 입력하세요"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  필수 요구사항
                </label>
                <textarea
                  value={businessInfo.requirements}
                  onChange={(e) => setBusinessInfo({...businessInfo, requirements: e.target.value})}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-600 focus:border-transparent"
                  rows={3}
                  placeholder="사업계획서에 반드시 포함되어야 할 내용"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  주의사항
                </label>
                <textarea
                  value={businessInfo.notes}
                  onChange={(e) => setBusinessInfo({...businessInfo, notes: e.target.value})}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-600 focus:border-transparent"
                  rows={2}
                  placeholder="특별히 주의할 사항이나 추가 메모"
                />
              </div>

              <div className="pt-4">
                <button
                  onClick={() => setStep(3)}
                  disabled={!businessInfo.title}
                  className="w-full bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700 transition disabled:bg-gray-400 disabled:cursor-not-allowed"
                >
                  다음 단계
                </button>
              </div>
            </div>

            {templateAnalysis && (
              <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h3 className="font-semibold mb-2">📄 문서 분석 결과</h3>
                <p className="text-sm text-gray-600">
                  문단 수: {templateAnalysis.metadata?.paragraph_count || 0} | 
                  표 수: {templateAnalysis.metadata?.table_count || 0}
                </p>
              </div>
            )}
          </div>
        )}

        {/* Step 3: AI Generation */}
        {step === 3 && (
          <div className="max-w-2xl mx-auto bg-white rounded-lg shadow-lg p-8">
            <h2 className="text-2xl font-bold mb-4">3단계: AI 자동 생성</h2>
            <p className="text-gray-600 mb-6">
              각 섹션별로 AI가 내용을 자동 생성합니다.
            </p>

            <div className="space-y-4">
              <button
                onClick={() => handleGenerate('market-analysis')}
                className="w-full bg-white border-2 border-indigo-600 text-indigo-600 px-6 py-4 rounded-lg hover:bg-indigo-50 transition flex items-center justify-between"
              >
                <span className="font-semibold">시장 분석 생성</span>
                <Sparkles size={24} />
              </button>

              <button
                onClick={() => handleGenerate('competitive-analysis')}
                className="w-full bg-white border-2 border-indigo-600 text-indigo-600 px-6 py-4 rounded-lg hover:bg-indigo-50 transition flex items-center justify-between"
              >
                <span className="font-semibold">경쟁사 분석 생성</span>
                <Sparkles size={24} />
              </button>

              <button
                onClick={() => handleGenerate('financial-plan')}
                className="w-full bg-white border-2 border-indigo-600 text-indigo-600 px-6 py-4 rounded-lg hover:bg-indigo-50 transition flex items-center justify-between"
              >
                <span className="font-semibold">재무 계획 생성</span>
                <Sparkles size={24} />
              </button>
            </div>

            <div className="mt-6">
              <button
                onClick={() => setStep(4)}
                className="w-full bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700 transition"
              >
                다음: 문서 다운로드
              </button>
            </div>
          </div>
        )}

        {/* Step 4: Download */}
        {step === 4 && (
          <div className="max-w-2xl mx-auto bg-white rounded-lg shadow-lg p-8">
            <div className="text-center">
              <Download className="mx-auto mb-4 text-green-600" size={64} />
              <h2 className="text-2xl font-bold mb-4">4단계: 사업계획서 다운로드</h2>
              <p className="text-gray-600 mb-6">
                AI가 생성한 사업계획서를 확인하고 다운로드하세요.
              </p>

              <button className="bg-green-600 text-white px-8 py-3 rounded-lg hover:bg-green-700 transition inline-flex items-center space-x-2">
                <Download size={20} />
                <span>DOCX 다운로드</span>
              </button>

              <div className="mt-8 p-4 bg-blue-50 rounded-lg">
                <p className="text-sm text-blue-800">
                  💡 생성된 내용을 검토하고 필요시 수정하세요.
                </p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
