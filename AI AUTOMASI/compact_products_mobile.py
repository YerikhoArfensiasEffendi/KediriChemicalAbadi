import os

with open('src/pages/ProductsPage.jsx', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Grid: 2 COLUMNS ON MOBILE!
c = c.replace(
    'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6',
    'grid grid-cols-2 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-2.5 sm:gap-6'
)

# 2. Card container
c = c.replace(
    'bg-white border border-slate-200/90 hover:border-[#0F58A8]/40 rounded-3xl p-5 sm:p-6 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between group relative space-y-5',
    'bg-white border border-slate-200/90 hover:border-[#0F58A8]/40 rounded-2xl sm:rounded-3xl p-3 sm:p-5 shadow-xs hover:shadow-lg transition-all duration-300 flex flex-col justify-between group relative space-y-3 sm:space-y-4'
)

# 3. Product image height
c = c.replace(
    'w-full h-44 sm:h-52 flex items-center justify-center overflow-hidden py-1 group-hover:scale-105 transition-transform duration-500',
    'w-full h-28 sm:h-48 flex items-center justify-center overflow-hidden py-0.5 group-hover:scale-105 transition-transform duration-500'
)

# 4. Title & Description
c = c.replace(
    'font-heading font-extrabold text-base sm:text-lg text-slate-900 group-hover:text-[#0F58A8] transition-colors leading-snug',
    'font-heading font-extrabold text-xs sm:text-base text-slate-900 group-hover:text-[#0F58A8] transition-colors leading-snug line-clamp-2'
)

c = c.replace(
    'text-xs text-slate-600 leading-relaxed font-normal line-clamp-2',
    'text-[10px] sm:text-xs text-slate-600 leading-relaxed font-normal line-clamp-2'
)

# 5. Spec matrix
c = c.replace(
    'grid grid-cols-2 gap-2 p-3 rounded-xl bg-slate-50/80 border border-slate-200/70 text-xs',
    'grid grid-cols-2 gap-1 sm:gap-2 p-2 sm:p-3 rounded-lg sm:rounded-xl bg-slate-50/80 border border-slate-200/70 text-[9.5px] sm:text-xs'
)

# 6. Hide features checkmarks on mobile so card remains super compact and fits 2 per row
c = c.replace(
    'space-y-1.5 text-xs text-slate-700',
    'hidden sm:block space-y-1.5 text-xs text-slate-700'
)

# 7. Action buttons
c = c.replace(
    'pt-2 flex items-center gap-2',
    'pt-1 sm:pt-2 flex items-center gap-1.5 sm:gap-2'
)
c = c.replace(
    'flex-1 h-10 px-3 rounded-xl text-xs font-bold font-heading uppercase tracking-wider transition-all flex items-center justify-center gap-1.5 cursor-pointer shadow-xs',
    'flex-1 h-8 sm:h-10 px-2 sm:px-3 rounded-lg sm:rounded-xl text-[10px] sm:text-xs font-bold font-heading uppercase tracking-wider transition-all flex items-center justify-center gap-1 cursor-pointer shadow-xs'
)
c = c.replace(
    'h-10 px-3.5 bg-emerald-50 hover:bg-emerald-100 text-emerald-700 border border-emerald-200 rounded-xl text-xs font-bold transition-colors flex items-center justify-center cursor-pointer shadow-2xs',
    'h-8 sm:h-10 px-2.5 sm:px-3.5 bg-emerald-50 hover:bg-emerald-100 text-emerald-700 border border-emerald-200 rounded-lg sm:rounded-xl text-[10px] sm:text-xs font-bold transition-colors flex items-center justify-center cursor-pointer shadow-2xs'
)

with open('src/pages/ProductsPage.jsx', 'w', encoding='utf-8') as f:
    f.write(c)

print('Optimized ProductsPage.jsx for compact 2-column mobile view!')
