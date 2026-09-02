import { Suspense, lazy } from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { HelmetProvider } from 'react-helmet-async'

import Navbar from '@/components/layout/Navbar'
import Footer from '@/components/layout/Footer'
import WhatsAppFloat from '@/components/ui/WhatsAppFloat'

// Lazy-loaded 9-Page Corporate Suite
const HomePage = lazy(() => import('@/pages/HomePage'))
const AboutPage = lazy(() => import('@/pages/AboutPage'))
const ProductsPage = lazy(() => import('@/pages/ProductsPage'))
const ServicesPage = lazy(() => import('@/pages/ServicesPage'))
const IndustriesPage = lazy(() => import('@/pages/IndustriesPage'))
const CompliancePage = lazy(() => import('@/pages/CompliancePage'))
const ContactPage = lazy(() => import('@/pages/ContactPage'))
const PrivacyPolicyPage = lazy(() => import('@/pages/PrivacyPolicyPage'))
const TermsPage = lazy(() => import('@/pages/TermsPage'))
const NotFoundPage = lazy(() => import('@/pages/NotFoundPage'))

function LoadingFallback() {
  return (
    <div className="min-h-screen bg-white flex items-center justify-center">
      <div className="w-8 h-8 rounded-full border-2 border-[#0F58A8] border-t-transparent animate-spin" />
    </div>
  )
}

export default function App() {
  return (
    <HelmetProvider>
      <BrowserRouter>
        <div className="min-h-screen bg-white text-slate-900 flex flex-col">
          <Navbar />
          <div className="flex-1">
            <Suspense fallback={<LoadingFallback />}>
              <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/about" element={<AboutPage />} />
                <Route path="/products" element={<ProductsPage />} />
                <Route path="/services" element={<ServicesPage />} />
                <Route path="/industries" element={<IndustriesPage />} />
                <Route path="/compliance" element={<CompliancePage />} />
                <Route path="/contact" element={<ContactPage />} />
                <Route path="/privacy-policy" element={<PrivacyPolicyPage />} />
                <Route path="/terms" element={<TermsPage />} />
                <Route path="*" element={<NotFoundPage />} />
              </Routes>
            </Suspense>
          </div>
          <Footer />
          <WhatsAppFloat />
        </div>
      </BrowserRouter>
    </HelmetProvider>
  )
}
