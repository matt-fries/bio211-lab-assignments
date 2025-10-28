import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

# read csv file
df = pd.read_csv('lab4.csv')

print(df['treatment'].unique())
print(len(df['treatment'].unique()))
# Create the figure
fig, ax = plt.subplots(figsize=(10, 6))

# define colors for each treatment (6 colors for all treatments)
colors = ['gray', 'blue', 'green', 'red', 'purple']
treatments = df['treatment'].unique()

# plot each treatment
for i, treatment in enumerate(treatments):
    treatment_data = df[df['treatment'] == treatment]
    x = treatment_data['time'].values
    y = treatment_data['value'].values
    sem = treatment_data['sem'].values

    # scatter plot with error bars
    ax.errorbar(x, y, yerr=sem, fmt='o', color=colors[i], label=treatment,
        capsize=5, capthick=2, alpha=0.7, markersize=6)

    # calculate and plot trendline
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    x_smooth = np.linspace(x.min(), x.max(), 100)
    trendline = slope * x_smooth + intercept
    linestyle = "--" if treatment == 'neg control' else '-'
    ax.plot(x_smooth, trendline, linestyle=linestyle, color=colors[i], linewidth=2, alpha=0.5)

    print(f"{treatment}: R^2 = {r_value**2:.3f}, "
          f"p-value = {p_value:.3f}, slope = {slope:.3f}")

ax.set_xlabel("Time (min)", fontsize=12, fontweight='bold')
ax.set_ylabel("Concentration (μM)", fontsize=12, fontweight='bold')
ax.legend(fontsize=10, loc='best', framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle=':', linewidth=0.5)
ax.set_xlim(-0.5, 14.5)

# Add figure caption at the bottom
fig.text(0.5, 0.01, 'Figure 1: DCPIP reduction over time across different treatment conditions',
         fontsize=11, ha='center', style='italic', wrap=True)

plt.style.use('dark_background')
plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.savefig('lab4_plot.png', dpi=300, bbox_inches='tight')
plt.show()
