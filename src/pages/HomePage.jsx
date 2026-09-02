import { Helmet } from 'react-helmet-async'
import HeroSection from '@/components/sections/HeroSection'
import BannerSliderSection from '@/components/sections/BannerSliderSection'
import ProductShowcaseSection from '@/components/sections/ProductShowcaseSection'
import WhyChooseUsSection from '@/components/sections/WhyChooseUsSection'
import MakloonSchemeSection from '@/components/sections/MakloonSchemeSection'
import IndustriesSection from '@/components/sections/IndustriesSection'
import CTASection from '@/components/sections/CTASection'

export default function HomePage() {
  return (
    <main className="bg-white text-slate-900 w-full">
      <Helmet>
        <title>PT Kediri Chemical Abadi — Pusat Manufaktur & Formulasi Kimia Pembersih Industri</title>
        <meta
          name="description"
          content="Pusat riset dan manufaktur kimia pembersih konsentrat 100% non-fosfat berkapasitas 500+ Ton/bulan di Mojoroto, Kediri. Penyaluran massal B2B dan maklon private label."
        />
        <link rel="canonical" href="https://kedirichemical.id/" />
        <meta property="og:title" content="PT Kediri Chemical Abadi — Pusat Manufaktur & Formulasi Kimia Pembersih Industri" />
        <meta property="og:description" content="Pusat riset dan manufaktur kimia pembersih konsentrat 100% non-fosfat berkapasitas 500+ Ton/bulan di Mojoroto, Kediri." />
        <meta property="og:url" content="https://kedirichemical.id/" />
      </Helmet>

      <HeroSection />
      <BannerSliderSection />
      <ProductShowcaseSection />
      <WhyChooseUsSection />
      <MakloonSchemeSection />
      <IndustriesSection />
      <CTASection />
    </main>
  )
}
