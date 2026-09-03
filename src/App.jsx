import { Suspense, lazy, useEffect } from 'react'
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom'
import { HelmetProvider } from 'react-helmet-async'
import { motion, AnimatePresence } from 'framer-motion'
import Lenis from 'lenis'
import 'lenis/dist/lenis.css'

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
    <div className="min-h-[60vh] bg-white flex items-center justify-center">
      <div className="w-8 h-8 rounded-full border-2 border-[#0F58A8] border-t-transparent animate-spin" />
    </div>
  )
}

function ScrollToTop() {
  const { pathname } = useLocation()
  useEffect(() => {
    if (window.__lenis) {
      window.__lenis.scrollTo(0, { immediate: true })
    } else {
      window.scrollTo({ top: 0, left: 0, behavior: 'instant' })
    }
  }, [pathname])
  return null
}

function useLenisScroll() {
  useEffect(() => {
    const lenis = new Lenis({
      duration: 1.15,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      orientation: 'vertical',
      gestureOrientation: 'vertical',
      smoothWheel: true,
      wheelMultiplier: 0.95,
      touchMultiplier: 1.6,
      infinite: false,
    })

    window.__lenis = lenis

    function raf(time) {
      lenis.raf(time)
      requestAnimationFrame(raf)
    }

    const rafId = requestAnimationFrame(raf)

    return () => {
      cancelAnimationFrame(rafId)
      lenis.destroy()
      delete window.__lenis
    }
  }, [])
}

function AnimatedRoutes() {
  const location = useLocation()

  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={location.pathname}
        initial={{ opacity: 0, y: 6 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -6 }}
        transition={{ duration: 0.26, ease: [0.22, 1, 0.36, 1] }}
        className="w-full"
      >
        <Suspense fallback={<LoadingFallback />}>
          <Routes location={location}>
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
      </motion.div>
    </AnimatePresence>
  )
}

export default function App() {
  useLenisScroll()

  return (
    <HelmetProvider>
      <BrowserRouter>
        <ScrollToTop />
        <div className="min-h-screen bg-white text-slate-900 flex flex-col">
          <Navbar />
          <div className="flex-1">
            <AnimatedRoutes />
          </div>
          <Footer />
          <WhatsAppFloat />
        </div>
      </BrowserRouter>
    </HelmetProvider>
  )
}
