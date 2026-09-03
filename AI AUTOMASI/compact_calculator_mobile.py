import os

with open('src/pages/CalculatorPage.jsx', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Hero title: compact on mobile
c = c.replace(
    'text-2xl sm:text-4xl lg:text-5xl font-black font-heading text-slate-900 tracking-tight leading-[1.15] uppercase',
    'text-xl sm:text-3xl lg:text-5xl font-black font-heading text-slate-900 tracking-tight leading-[1.2] uppercase'
)

# 2. Hero padding
c = c.replace(
    'pt-28 sm:pt-36 pb-12 sm:pb-16',
    'pt-24 sm:pt-36 pb-8 sm:pb-14'
)

# 3. Main section py
c = c.replace(
    'py-10 sm:py-16 bg-white text-slate-900 relative',
    'py-8 sm:py-14 bg-white text-slate-900 relative'
)

# 4. Heading in workspace
c = c.replace(
    'text-xl sm:text-2xl lg:text-3xl font-black font-heading text-slate-900 tracking-tight uppercase',
    'text-lg sm:text-2xl lg:text-3xl font-black font-heading text-slate-900 tracking-tight uppercase'
)

# 5. Parameter input box
c = c.replace(
    'p-6 sm:p-7 rounded-3xl bg-slate-50/80 border border-slate-200/90 grid grid-cols-1 md:grid-cols-3 gap-6 items-center',
    'p-4 sm:p-7 rounded-2xl sm:rounded-3xl bg-slate-50/80 border border-slate-200/90 grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-6 items-center'
)

# 6. Product grid: 2 COLUMNS ON MOBILE!
c = c.replace(
    'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6',
    'grid grid-cols-2 sm:grid-cols-2 lg:grid-cols-4 gap-2.5 sm:gap-6'
)

# 7. Product card container & image
c = c.replace(
    'bg-white border border-slate-200/90 rounded-3xl p-5 shadow-sm hover:shadow-lg transition-all duration-300 flex flex-col justify-between group space-y-4',
    'bg-white border border-slate-200/90 rounded-2xl sm:rounded-3xl p-3 sm:p-5 shadow-xs hover:shadow-md transition-all duration-300 flex flex-col justify-between group space-y-2.5 sm:space-y-4'
)

c = c.replace(
    'w-full h-40 sm:h-44 flex items-center justify-center overflow-hidden py-1 group-hover:scale-105 transition-transform duration-500',
    'w-full h-28 sm:h-44 flex items-center justify-center overflow-hidden py-0.5 group-hover:scale-105 transition-transform duration-500'
)

c = c.replace(
    'font-heading font-extrabold text-sm sm:text-[15px] text-slate-900 group-hover:text-[#0F58A8] transition-colors leading-snug',
    'font-heading font-extrabold text-xs sm:text-[15px] text-slate-900 group-hover:text-[#0F58A8] transition-colors leading-snug line-clamp-2'
)

# 8. Bottom Knowledge Base py & grid
c = c.replace(
    'py-16 sm:py-24 bg-slate-50/60 text-slate-900 border-t border-slate-200/90',
    'py-10 sm:py-20 bg-slate-50/60 text-slate-900 border-t border-slate-200/90'
)

c = c.replace(
    'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6',
    'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5 sm:gap-6'
)

c = c.replace(
    'bg-white border border-slate-200/90 rounded-3xl p-6 shadow-sm hover:shadow-lg transition-all duration-300 flex flex-col justify-between group space-y-5',
    'bg-white border border-slate-200/90 rounded-2xl sm:rounded-3xl p-4 sm:p-6 shadow-xs hover:shadow-md transition-all duration-300 flex flex-col justify-between group space-y-3.5 sm:space-y-5'
)

with open('src/pages/CalculatorPage.jsx', 'w', encoding='utf-8') as f:
    f.write(c)

print('Optimized CalculatorPage.jsx for compact mobile view!')
