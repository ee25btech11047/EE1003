import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(0.1, 10, 500)
s = 1j * w

K = 1e5  # very large gain

# Fixed H(s)
H = 1 / (s + 2)

# Two very different G(s)
G1 = 1 / (s + 1)
G2 = 5 / (s + 0.2)

# Closed-loop T(s)
T1 = (K * G1) / (1 + K * G1 * H)
T2 = (K * G2) / (1 + K * G2 * H)

plt.figure()

# Magnitude
plt.subplot(2,1,1)
plt.plot(w, abs(T1), label="|T| with G1")
plt.plot(w, abs(T2), '--', label="|T| with G2")
plt.title("Magnitude (Changing G)")
plt.legend()
plt.grid()

# Phase
plt.subplot(2,1,2)
plt.plot(w, np.angle(T1), label="Phase with G1")
plt.plot(w, np.angle(T2), '--', label="Phase with G2")
plt.title("Phase (Changing G)")
plt.xlabel("Frequency (rad/s)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
