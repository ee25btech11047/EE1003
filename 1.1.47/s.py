import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(0.1, 10, 500)
s = 1j * w

K = 1e5

# Fixed G
G = 1 / (s + 1)

# Two H(s)
H1 = 1 / (s + 2)
H2 = 5 / (s + 0.2)

# Closed-loop
T1 = (K * G) / (1 + K * G * H1)
T2 = (K * G) / (1 + K * G * H2)

plt.figure(figsize=(10,8))

# --- H magnitude ---
plt.subplot(2,2,1)
plt.plot(w, abs(H1), label="H1")
plt.plot(w, abs(H2), '--', label="H2")
plt.title("H(s) Magnitude")
plt.legend()
plt.grid()

# --- H phase ---
plt.subplot(2,2,2)
plt.plot(w, np.angle(H1, deg=True), label="H1")
plt.plot(w, np.angle(H2, deg=True), '--', label="H2")
plt.title("H(s) Phase")
plt.legend()
plt.grid()

# --- T magnitude ---
plt.subplot(2,2,3)
plt.plot(w, abs(T1), label="T with H1")
plt.plot(w, abs(T2), '--', label="T with H2")
plt.title("T(s) Magnitude")
plt.xlabel("Frequency (rad/s)")
plt.legend()
plt.grid()

# --- T phase ---
plt.subplot(2,2,4)
plt.plot(w, np.angle(T1, deg=True), label="T with H1")
plt.plot(w, np.angle(T2, deg=True), '--', label="T with H2")
plt.title("T(s) Phase")
plt.xlabel("Frequency (rad/s)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
