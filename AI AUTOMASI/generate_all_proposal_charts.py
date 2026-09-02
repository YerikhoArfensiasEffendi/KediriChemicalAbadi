import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

charts_dir = "/Users/arthur/Documents/WebsiteKCA/kediri-chemical/Keuangan/Proposal/charts"
os.makedirs(charts_dir, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# -------------------------------------------------------------
# CHART 1: DIAGRAM ALUR PERPUTARAN KAS & ROI (PROCESS FLOW)
# -------------------------------------------------------------
def make_flowchart():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.axis('off')
    
    # 4 Steps Boxes
    steps = [
        ("1. INJEKSI MODAL MESIN", "Mitra setor Rp 200 Juta\nKCA pasang mesin mixing\n& filling khusus SUS316", "#0E2A47"),
        ("2. REPEAT ORDER 90/10", "Mitra pesan produk berkala\nBayar 90% kas tunai\n10% potong modal mesin", "#1E3A8A"),
        ("3. PENJUALAN PASAR", "Jual ke laundry/hotel/spa\nTotal omzet Rp 3.000.000.000\n(200.000 unit x Rp 15.000)", "#2563EB"),
        ("4. PANEN PROFIT 500%", "• Modal Rp 200 Jt Balik 100%\n• Laba Bersih: Rp 1 Miliar\nTotal Kas: Rp 3.000.000.000", "#10B981")
    ]
    
    for i, (title, desc, color) in enumerate(steps):
        x = i * 2.5 + 0.2
        # Box
        rect = patches.FancyBboxPatch((x, 0.6), 2.1, 3.6, boxstyle="round,pad=0.15", 
                                      edgecolor=color, facecolor="#F8FAFC", linewidth=2)
        ax.add_patch(rect)
        
        # Header banner inside box
        header_rect = patches.FancyBboxPatch((x, 3.2), 2.1, 1.0, boxstyle="round,pad=0.1", 
                                             edgecolor=color, facecolor=color, linewidth=1)
        ax.add_patch(header_rect)
        
        ax.text(x + 1.05, 3.7, title, color="white", fontsize=9, fontweight="bold", ha="center", va="center")
        ax.text(x + 1.05, 1.9, desc, color="#0F172A", fontsize=8.5, ha="center", va="center", linespacing=1.4)
        
        # Arrow to next box
        if i < 3:
            arrow = patches.FancyArrowPatch((x + 2.15, 2.4), (x + 2.45, 2.4), 
                                           arrowstyle="->", mutation_scale=20, 
                                           color="#0E2A47", linewidth=2.5)
            ax.add_patch(arrow)

    ax.set_xlim(-0.2, 10.0)
    ax.set_ylim(0.2, 4.8)
    fig.suptitle("DIAGRAM ALUR PERPUTARAN KAS & AKUMULASI ROI 500% (KCA PARTNERSHIP)", 
                 fontsize=12, fontweight="bold", color="#0E2A47", y=0.98)
    
    out_p = os.path.join(charts_dir, "chart1_flowchart_cashflow.png")
    plt.tight_layout()
    plt.savefig(out_p, bbox_inches='tight', dpi=300)
    plt.close()
    print("Saved:", out_p)

# -------------------------------------------------------------
# CHART 2: PERBANDINGAN STRUKTUR MARGIN & PROFIT PER UNIT
# -------------------------------------------------------------
def make_margin_comparison():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=300)
    
    categories = ['Distributor Biasa\n(Tanpa Skema)', 'Mitra KCA\n(Skema Dedikasi 10%)']
    
    # 1. Harga Beli vs Laba per Unit
    beli = [10000, 9000]
    laba = [5000, 6000]
    
    x = np.arange(len(categories))
    width = 0.35
    
    rects1 = ax1.bar(x - width/2, beli, width, label='Harga Beli Pabrik', color='#64748B')
    rects2 = ax1.bar(x + width/2, laba, width, label='Laba Kotor / Unit', color='#2563EB')
    
    ax1.set_ylabel('Rupiah (Rp)', fontsize=10, fontweight='bold', color='#0E2A47')
    ax1.set_title('Harga Beli vs Laba Bersih / Unit (Harga Jual Rp 15.000)', fontsize=10, fontweight='bold', color='#0E2A47')
    ax1.set_xticks(x)
    ax1.set_xticklabels(categories, fontsize=9)
    ax1.legend(loc='upper right', fontsize=8.5)
    ax1.set_ylim(0, 13000)
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    
    for r in rects1:
        ax1.text(r.get_x() + r.get_width()/2., r.get_height() + 200, f"Rp {int(r.get_height()):,}", ha='center', va='bottom', fontsize=8.5, fontweight='bold')
    for r in rects2:
        ax1.text(r.get_x() + r.get_width()/2., r.get_height() + 200, f"Rp {int(r.get_height()):,}", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#2563EB')
        
    # 2. Persentase Margin Keuntungan
    margins = [50.0, 66.67]
    bars = ax2.bar(categories, margins, color=['#64748B', '#10B981'], width=0.45)
    ax2.set_ylabel('Persentase Margin (%)', fontsize=10, fontweight='bold', color='#0E2A47')
    ax2.set_title('Persentase Margin Keuntungan Riil', fontsize=10, fontweight='bold', color='#0E2A47')
    ax2.set_ylim(0, 85)
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    
    for bar in bars:
        ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 2, f"{bar.get_height():.1f}%", ha='center', va='bottom', fontsize=10, fontweight='bold')
        
    # Annotate Difference
    ax2.annotate('Lonjakan Margin\n+16.7% Murni!', xy=(1, 67), xytext=(0.5, 76),
                arrowprops=dict(arrowstyle="->", color="#10B981", lw=2),
                fontsize=9, fontweight='bold', color="#065F46", ha='center')

    fig.suptitle("PERBANDINGAN ANATOMI MARGIN & PROFIT PER UNIT", fontsize=12, fontweight="bold", color="#0E2A47", y=0.98)
    
    out_p = os.path.join(charts_dir, "chart2_margin_comparison.png")
    plt.tight_layout()
    plt.savefig(out_p, bbox_inches='tight', dpi=300)
    plt.close()
    print("Saved:", out_p)

# -------------------------------------------------------------
# CHART 3: GRAFIK PENGEMBALIAN MODAL & AKUMULASI LABA
# -------------------------------------------------------------
def make_capital_recovery_growth():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=300)
    
    order_units = np.array([0, 40000, 80000, 120000, 160000, 200000])
    sisa_modal = np.array([200, 160, 120, 80, 40, 0]) # in Juta Rupiah
    profit_akum = np.array([0, 200, 400, 600, 800, 1000]) # in Juta Rupiah
    
    ax.plot(order_units, sisa_modal, marker='o', color='#EF4444', linewidth=2.5, label='Sisa Saldo Modal Mesin (Menuju Lunas)')
    ax.plot(order_units, profit_akum, marker='s', color='#10B981', linewidth=2.5, label='Akumulasi Laba Bersih Tunai Distributor')
    
    ax.fill_between(order_units, 0, profit_akum, color='#10B981', alpha=0.1)
    
    ax.set_title("GRAFIK PENGURANGAN SALDO MODAL MESIN VS AKUMULASI LABA BERSIH (TOTAL 200.000 UNIT)", fontsize=11, fontweight='bold', color='#0E2A47')
    ax.set_xlabel("Volume Akumulasi Pesanan (Unit Botol/Jerigen)", fontsize=10, fontweight='bold', color='#0E2A47')
    ax.set_ylabel("Nominal Finansial (Juta Rupiah)", fontsize=10, fontweight='bold', color='#0E2A47')
    ax.set_ylim(-20, 1150)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc='center left', fontsize=9)
    
    for x_val, y_mod, y_prof in zip(order_units, sisa_modal, profit_akum):
        if x_val == 0:
            ax.text(x_val, y_mod + 35, f"Rp {y_mod} Jt", ha='center', fontsize=8.5, fontweight='bold', color='#EF4444')
        elif x_val == 200000:
            ax.text(x_val, y_mod - 50, "Rp 0\n(LUNAS)", ha='center', fontsize=8.5, fontweight='bold', color='#EF4444')
            ax.text(x_val, y_prof + 35, f"Rp {y_prof:,} Jt\n(1 MILIAR)", ha='center', fontsize=9, fontweight='bold', color='#10B981')
        else:
            ax.text(x_val, y_mod + 25, f"Rp {y_mod} Jt", ha='center', fontsize=8, color='#EF4444')
            ax.text(x_val, y_prof + 25, f"Rp {y_prof} Jt", ha='center', fontsize=8, color='#10B981')

    out_p = os.path.join(charts_dir, "chart3_capital_recovery_growth.png")
    plt.tight_layout()
    plt.savefig(out_p, bbox_inches='tight', dpi=300)
    plt.close()
    print("Saved:", out_p)

# -------------------------------------------------------------
# CHART 4: 3 SKENARIO TIMELINE & LABA BULANAN
# -------------------------------------------------------------
def make_scenario_timeline():
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)
    
    scenarios = ['Konservatif (12 Bulan)', 'Moderat (8 Bulan)', 'Agresif (5 Bulan)']
    omzet_bln = [250, 375, 600] # Juta / Bulan
    laba_bln = [83.3, 125, 200] # Juta / Bulan
    
    y = np.arange(len(scenarios))
    height = 0.35
    
    r1 = ax.barh(y - height/2, omzet_bln, height, label='Omzet Kas Masuk Pasar / Bulan (Juta Rp)', color='#1E3A8A')
    r2 = ax.barh(y + height/2, laba_bln, height, label='Laba Bersih Tunai / Bulan (Juta Rp)', color='#10B981')
    
    ax.set_xlabel('Nominal per Bulan (Juta Rupiah)', fontsize=10, fontweight='bold', color='#0E2A47')
    ax.set_title('PROYEKSI ARUS KAS & LABA BERSIH BULANAN PADA 3 SKENARIO DISTRIBUSI', fontsize=11, fontweight='bold', color='#0E2A47')
    ax.set_yticks(y)
    ax.set_yticklabels(scenarios, fontsize=9.5, fontweight='bold')
    ax.legend(loc='lower right', fontsize=9)
    ax.set_xlim(0, 720)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    
    for rect in r1:
        w = rect.get_width()
        ax.text(w + 10, rect.get_y() + rect.get_height()/2., f"Rp {w:,.0f} Jt/bln", va='center', fontsize=8.5, fontweight='bold', color='#1E3A8A')
    for rect in r2:
        w = rect.get_width()
        ax.text(w + 10, rect.get_y() + rect.get_height()/2., f"Rp {w:,.1f} Jt/bln", va='center', fontsize=8.5, fontweight='bold', color='#10B981')

    out_p = os.path.join(charts_dir, "chart4_scenario_timeline.png")
    plt.tight_layout()
    plt.savefig(out_p, bbox_inches='tight', dpi=300)
    plt.close()
    print("Saved:", out_p)

if __name__ == "__main__":
    make_flowchart()
    make_margin_comparison()
    make_capital_recovery_growth()
    make_scenario_timeline()
    print("ALL CHARTS GENERATED SUCCESSFULLY!")
