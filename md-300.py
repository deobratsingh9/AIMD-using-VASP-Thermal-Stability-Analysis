import numpy as np
import matplotlib.pyplot as plt
import re

# -------- USER SETTINGS ----------
filename = "OSZICAR"
dt_fs = 1.0
dpi_value = 600
xmax = 2854   # ✅ force x-axis range 0 → 2854 fs
end_step = None   # optional: limit data (e.g., 3000). Keep None for full
# --------------------------------

steps, energies, temperatures = [], [], []

# -------- DATA EXTRACTION ----------
with open(filename, "r") as f:
    for line in f:
        if "T=" in line and "E0=" in line:
            try:
                step = int(line.strip().split()[0])
                temp = float(re.search(r"T=\s*([0-9.]+)", line).group(1))
                energy = float(re.search(r"E0=\s*([-0-9.E+]+)", line).group(1))

                steps.append(step)
                temperatures.append(temp)
                energies.append(energy)

            except:
                continue

steps = np.array(steps)
energies = np.array(energies)
temperatures = np.array(temperatures)

# -------- OPTIONAL: LIMIT DATA ----------
if end_step is not None:
    mask = steps <= end_step
    steps = steps[mask]
    energies = energies[mask]
    temperatures = temperatures[mask]

# -------- TIME SHIFT (START FROM ZERO) ----------
steps = steps - steps[0]
time_fs = steps * dt_fs

# -------- SMOOTHING ----------
def moving_average(data, window=50):
    return np.convolve(data, np.ones(window)/window, mode='valid')

temp_smooth = moving_average(temperatures)
time_smooth = time_fs[:len(temp_smooth)]

# -------- STYLE SETTINGS ----------
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 18,
    "axes.labelsize": 20,
    "axes.titlesize": 20,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16,
    "legend.fontsize": 16,
    "lines.linewidth": 2.8
})

# -------- CREATE FIGURE ----------
fig, ax = plt.subplots(2, 1, figsize=(8, 9), sharex=True)

# -------- ENERGY PLOT ----------
ax[0].plot(time_fs, energies, color='black', label="Total Energy")
ax[0].set_ylabel("Total Energy (eV)")
ax[0].set_title("Molecular Dynamics Energy Evolution")
ax[0].legend(frameon=False)

# Panel label (a)
ax[0].text(0.02, 0.95, '(a)', transform=ax[0].transAxes,
           fontsize=16, fontweight='bold', va='top')

# -------- TEMPERATURE PLOT ----------
ax[1].plot(time_fs, temperatures, color='lightcoral', alpha=0.5, label="Raw")
ax[1].plot(time_smooth, temp_smooth, color='red', label="Smoothed")
ax[1].set_ylabel("Temperature (K)")
ax[1].set_xlabel("Time (fs)")
ax[1].set_title("Temperature Fluctuation (NVT)")
ax[1].legend(frameon=False)

# Panel label (b)
ax[1].text(0.02, 0.95, '(b)', transform=ax[1].transAxes,
           fontsize=16, fontweight='bold', va='top')

# -------- FIX X-AXIS RANGE ----------
ax[1].set_xlim(0, xmax)

# -------- FINALIZE ----------
plt.tight_layout()

# Save outputs
plt.savefig("MD_plot_highres.png", dpi=dpi_value, bbox_inches='tight')
#plt.savefig("MD_plot_highres.pdf", bbox_inches='tight')

#plt.show()

# -------- SUMMARY ----------
print("------ MD SUMMARY ------")
print(f"Steps parsed: {len(steps)}")
print(f"Time range: {time_fs[0]} – {time_fs[-1]} fs")
print(f"Average Temperature: {np.mean(temperatures):.2f} K")
print(f"Energy drift: {(energies[-1] - energies[0]):.6f} eV")
