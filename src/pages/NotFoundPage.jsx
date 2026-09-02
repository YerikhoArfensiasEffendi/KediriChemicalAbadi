import { Link } from 'react-router-dom'
import { ArrowLeft, Factory } from 'lucide-react'

export default function NotFoundPage() {
  return (
    <main className="min-h-[70vh] flex items-center justify-center bg-[#07111E] text-white px-6">
      <div className="max-w-md text-center space-y-6">
        <div className="w-16 h-16 rounded-2xl bg-blue-600/20 border border-blue-500/40 text-blue-400 flex items-center justify-center mx-auto">
          <Factory className="w-8 h-8" />
        </div>
        <h1 className="text-4xl sm:text-5xl font-extrabold font-heading text-white">
          404
        </h1>
        <p className="text-sm text-slate-300">
          Halaman yang Anda cari tidak ditemukan atau telah dipindahkan ke direktori lain.
        </p>
        <Link
          to="/"
          className="inline-flex items-center gap-2 h-11 px-6 bg-blue-600 hover:bg-blue-700 text-white rounded-xl text-xs font-bold font-heading uppercase tracking-wider shadow-md transition-all cursor-pointer"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Kembali ke Beranda</span>
        </Link>
      </div>
    </main>
  )
}
