import os

# 1. Update CompliancePage.jsx
with open('src/pages/CompliancePage.jsx', 'r', encoding='utf-8') as f:
    comp = f.read()

comp = comp.replace(
    'className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6 lg:gap-4 relative items-stretch"',
    'className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3.5 sm:gap-4 relative items-stretch"'
)

comp = comp.replace(
    'className="bg-white rounded-xl p-5 sm:p-6 border border-slate-200/90 shadow-sm hover:shadow-md transition-all flex flex-col justify-between space-y-5 relative group"',
    'className="bg-white rounded-xl p-4 sm:p-6 border border-slate-200/90 shadow-xs hover:shadow-md transition-all flex flex-col justify-between space-y-3.5 sm:space-y-5 relative group"'
)

comp = comp.replace(
    'className={`w-14 h-14 rounded-lg ${step.iconContainerBg} border flex items-center justify-center group-hover:scale-105 transition-transform shadow-2xs`}',
    'className={`w-11 h-11 sm:w-14 sm:h-14 rounded-lg ${step.iconContainerBg} border flex items-center justify-center group-hover:scale-105 transition-transform shadow-2xs`}'
)

comp = comp.replace(
    'className={`w-8 h-8 ${step.textColor}`}',
    'className={`w-6 h-6 sm:w-8 sm:h-8 ${step.textColor}`}'
)

comp = comp.replace(
    'text-sm sm:text-base font-extrabold font-heading text-slate-900 leading-tight',
    'text-xs sm:text-base font-extrabold font-heading text-slate-900 leading-tight'
)

comp = comp.replace(
    'text-xs text-slate-600 leading-relaxed font-normal',
    'text-[11px] sm:text-xs text-slate-600 leading-relaxed font-normal'
)

with open('src/pages/CompliancePage.jsx', 'w', encoding='utf-8') as f:
    f.write(comp)

# 2. Update IndustriesPage.jsx
with open('src/pages/IndustriesPage.jsx', 'r', encoding='utf-8') as f:
    ind = f.read()

ind = ind.replace(
    'py-16 sm:py-20 bg-slate-100/70 text-slate-900 border-b border-slate-200',
    'py-10 sm:py-20 bg-slate-100/70 text-slate-900 border-b border-slate-200'
)

ind = ind.replace(
    'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6',
    'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6'
)

ind = ind.replace(
    'relative h-40 w-full overflow-hidden bg-slate-950',
    'relative h-32 sm:h-40 w-full overflow-hidden bg-slate-950'
)

ind = ind.replace(
    'p-5 sm:p-6 space-y-3.5 flex-1 flex flex-col justify-between',
    'p-4 sm:p-6 space-y-2.5 sm:space-y-3.5 flex-1 flex flex-col justify-between'
)

with open('src/pages/IndustriesPage.jsx', 'w', encoding='utf-8') as f:
    f.write(ind)

print('Successfully optimized CompliancePage and IndustriesPage for compact mobile view!')
