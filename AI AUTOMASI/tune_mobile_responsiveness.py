import os

# 1. NAVBAR: tune mobile header height and logo/button
with open('src/components/layout/Navbar.jsx', 'r', encoding='utf-8') as f:
    nav = f.read()

nav = nav.replace('h-11 sm:h-13 lg:h-14', 'h-9 sm:h-12 lg:h-14')
nav = nav.replace('className="h-9 px-4 bg-[#0F58A8]', 'className="h-8 sm:h-9 px-2.5 sm:px-4 bg-[#0F58A8]')
nav = nav.replace('text-[11px] font-heading font-semibold uppercase tracking-wider inline-flex items-center gap-1.5', 'text-[10px] sm:text-[11px] font-heading font-semibold uppercase tracking-wider inline-flex items-center gap-1')
nav = nav.replace('isScrolled\n          ? "bg-white/95 backdrop-blur-xl border-b border-slate-200/90 shadow-xs h-18 sm:h-20"\n          : "bg-white/90 backdrop-blur-lg border-b border-slate-200/60 h-20"',
                  'isScrolled\n          ? "bg-white/95 backdrop-blur-xl border-b border-slate-200/90 shadow-xs h-16 sm:h-20"\n          : "bg-white/90 backdrop-blur-lg border-b border-slate-200/60 h-16 sm:h-20"')

with open('src/components/layout/Navbar.jsx', 'w', encoding='utf-8') as f:
    f.write(nav)

# 2. CTA SECTION: tune mobile padding, headings & buttons
with open('src/components/sections/CTASection.jsx', 'r', encoding='utf-8') as f:
    cta = f.read()

cta = cta.replace('pt-20 sm:pt-24 pb-28 sm:pb-36', 'pt-12 sm:pt-20 pb-20 sm:pb-32')
cta = cta.replace('text-xl sm:text-2xl lg:text-3xl font-black', 'text-lg sm:text-2xl lg:text-3xl font-black')
cta = cta.replace('h-10 px-6 text-xs', 'h-9 sm:h-10 px-4 sm:px-6 text-[11px] sm:text-xs')

with open('src/components/sections/CTASection.jsx', 'w', encoding='utf-8') as f:
    f.write(cta)

# 3. SERVICES PAGE: tune mobile workflow cards & spacing
with open('src/pages/ServicesPage.jsx', 'r', encoding='utf-8') as f:
    srv = f.read()

srv = srv.replace('py-16 sm:py-24 bg-white text-slate-900 border-b border-sky-100', 'py-10 sm:py-20 bg-white text-slate-900 border-b border-sky-100')
srv = srv.replace('grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6 lg:gap-4', 'grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3.5 sm:gap-4')
srv = srv.replace('bg-white p-6 rounded-3xl border border-sky-100 shadow-lg shadow-blue-900/5 hover:shadow-xl transition-all flex flex-col justify-between space-y-5 relative group',
                  'bg-white p-4 sm:p-6 rounded-2xl sm:rounded-3xl border border-sky-100 shadow-xs hover:shadow-md transition-all flex flex-col justify-between space-y-3.5 sm:space-y-5 relative group')
srv = srv.replace('w-10 h-10', 'w-7 h-7 sm:w-10 sm:h-10')
srv = srv.replace('p-3.5 rounded-2xl', 'p-2.5 sm:p-3.5 rounded-xl sm:rounded-2xl')

with open('src/pages/ServicesPage.jsx', 'w', encoding='utf-8') as f:
    f.write(srv)

# 4. CONTACT PAGE: tune mobile banner and cards
with open('src/pages/ContactPage.jsx', 'r', encoding='utf-8') as f:
    cnt = f.read()

cnt = cnt.replace('py-14 sm:py-20', 'py-10 sm:py-18')
cnt = cnt.replace('py-16 sm:py-24', 'py-10 sm:py-20')
cnt = cnt.replace('text-2xl sm:text-3xl lg:text-4xl font-extrabold', 'text-xl sm:text-3xl lg:text-4xl font-extrabold')
cnt = cnt.replace('p-6 sm:p-8 space-y-7', 'p-4 sm:p-8 space-y-5 sm:space-y-7')
cnt = cnt.replace('rounded-3xl shadow-lg', 'rounded-2xl sm:rounded-3xl shadow-xs sm:shadow-lg')

with open('src/pages/ContactPage.jsx', 'w', encoding='utf-8') as f:
    f.write(cnt)

# 5. RFQ MODAL: compact mobile padding & sizing
with open('src/components/ui/RFQModal.jsx', 'r', encoding='utf-8') as f:
    rfq = f.read()

rfq = rfq.replace('p-4 sm:p-6 overflow-y-auto', 'p-2.5 sm:p-6 overflow-y-auto')
rfq = rfq.replace('rounded-3xl shadow-2xl', 'rounded-2xl sm:rounded-3xl shadow-2xl')
rfq = rfq.replace('p-6 sm:p-7 relative border-b', 'p-4 sm:p-7 relative border-b')
rfq = rfq.replace('p-6 sm:p-8 space-y-5', 'p-4 sm:p-8 space-y-3.5 sm:space-y-5')
rfq = rfq.replace('text-xl sm:text-2xl font-extrabold', 'text-lg sm:text-2xl font-extrabold')

with open('src/components/ui/RFQModal.jsx', 'w', encoding='utf-8') as f:
    f.write(rfq)

# 6. FOOTER: compact mobile spacing
with open('src/components/layout/Footer.jsx', 'r', encoding='utf-8') as f:
    ftr = f.read()

ftr = ftr.replace('pt-16 sm:pt-20 pb-12 sm:pb-16', 'pt-10 sm:pt-20 pb-8 sm:pb-16')
ftr = ftr.replace('pb-14 sm:pb-16 border-b border-slate-800/80', 'pb-8 sm:pb-16 border-b border-slate-800/80')

with open('src/components/layout/Footer.jsx', 'w', encoding='utf-8') as f:
    f.write(ftr)

print('All major pages and components tuned for compact mobile responsiveness!')
