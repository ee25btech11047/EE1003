import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(0.1, 10, 500)
s = 1j * w

K = 1e5

# Fixed H
H = 1 / (s + 2)

# Two G(s)
G1 = 1 / (s + 1)
G2 = 5 / (s + 0.2)

# Closed-loop
T1 = (K * G1) / (1 + K * G1 * H)
T2 = (K * G2) / (1 + K * G2 * H)

plt.figure(figsize=(10,8))

# --- G magnitude ---
plt.subplot(2,2,1)
plt.plot(w, abs(G1), label="G1")
plt.plot(w, abs(G2), '--', label="G2")
plt.title("G(s) Magnitude")
plt.legend()
plt.grid()

# --- G phase ---
plt.subplot(2,2,2)
plt.plot(w, np.angle(G1, deg=True), label="G1")
plt.plot(w, np.angle(G2, deg=True), '--', label="G2")
plt.title("G(s) Phase")
plt.legend()
plt.grid()

# --- T magnitude ---
plt.subplot(2,2,3)
plt.plot(w, abs(T1), label="T with G1")
plt.plot(w, abs(T2), '--', label="T with G2")
plt.title("T(s) Magnitude")
plt.xlabel("Frequency (rad/s)")
plt.legend()
plt.grid()

# --- T phase ---
plt.subplot(2,2,4)
plt.plot(w, np.angle(T1, deg=True), label="T with G1")
plt.plot(w, np.angle(T2, deg=True), '--', label="T with G2")
plt.title("T(s) Phase")
plt.xlabel("Frequency (rad/s)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
