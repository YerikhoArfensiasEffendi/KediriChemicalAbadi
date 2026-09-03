import os

with open('src/components/sections/ProductShowcaseSection.jsx', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Grid: 2 COLUMNS ON MOBILE!
c = c.replace(
    'grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-5',
    'grid grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-2.5 sm:gap-4 lg:gap-5'
)

# 2. Card rounded & shadow
c = c.replace(
    'className={`bg-white border rounded-3xl transition-all duration-300 flex flex-col justify-between group relative overflow-hidden ${theme.border} shadow-lg shadow-blue-900/5 hover:shadow-xl hover:-translate-y-1`}',
    'className={`bg-white border rounded-2xl sm:rounded-3xl transition-all duration-300 flex flex-col justify-between group relative overflow-hidden ${theme.border} shadow-xs hover:shadow-md`}'
)

# 3. Card padding
c = c.replace(
    'className="p-4 sm:p-5 space-y-3.5 bg-gradient-to-b from-sky-50/40 via-white to-white"',
    'className="p-2.5 sm:p-4 space-y-2 sm:space-y-3 bg-gradient-to-b from-sky-50/40 via-white to-white"'
)

# 4. Product image: h-24 on mobile, remove drop-shadow
c = c.replace(
    'className="w-full h-36 sm:h-40 flex items-center justify-center overflow-hidden py-1 group-hover:scale-105 transition-transform duration-500"',
    'className="w-full h-24 sm:h-36 lg:h-40 flex items-center justify-center overflow-hidden py-0.5 group-hover:scale-105 transition-transform duration-500"'
)

c = c.replace(
    'className="w-full h-full object-contain filter drop-shadow-md select-none mix-blend-multiply"',
    'className="w-full h-full object-contain select-none mix-blend-multiply"'
)

# 5. Title & Description
c = c.replace(
    'className="text-sm sm:text-[14.5px] font-extrabold font-heading text-slate-900 group-hover:text-[#0F58A8] transition-colors leading-snug"',
    'className="text-xs sm:text-[14.5px] font-extrabold font-heading text-slate-900 group-hover:text-[#0F58A8] transition-colors leading-snug line-clamp-2"'
)

c = c.replace(
    'className="text-[11px] sm:text-xs text-slate-600 leading-relaxed line-clamp-2 font-normal"',
    'className="hidden sm:block text-[11px] sm:text-xs text-slate-600 leading-relaxed line-clamp-2 font-normal"'
)

# 6. Spec matrix: compact text
c = c.replace(
    'className="grid grid-cols-2 gap-1.5 p-2 rounded-xl bg-sky-50/50 border border-sky-100 text-[11px]"',
    'className="grid grid-cols-2 gap-1 p-1.5 sm:p-2 rounded-lg bg-sky-50/50 border border-sky-100 text-[9.5px] sm:text-[11px]"'
)

# 7. Bottom action bar: compact button
c = c.replace(
    'className="p-3 bg-white border-t border-sky-100 flex items-center justify-between text-xs"',
    'className="p-2 sm:p-3 bg-white border-t border-sky-100 flex items-center justify-between text-xs"'
)

c = c.replace(
    'className={`px-3 py-1.5 rounded-full text-xs font-bold font-heading uppercase tracking-wider transition-all flex items-center gap-1 cursor-pointer shadow-xs ${theme.btnBg}`}',
    'className={`px-2 py-1 sm:px-3 sm:py-1.5 rounded-lg sm:rounded-full text-[10px] sm:text-xs font-bold font-heading uppercase tracking-wider transition-all flex items-center gap-1 cursor-pointer shadow-xs ${theme.btnBg}`}'
)

with open('src/components/sections/ProductShowcaseSection.jsx', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated ProductShowcaseSection.jsx with compact 2-column mobile cards!')
