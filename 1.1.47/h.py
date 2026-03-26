import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(0.1, 10, 500)
s = 1j * w

K = 1e5  # very large gain

# Fixed G(s)
G = 1 / (s + 1)

# Two very different H(s)
H1 = 1 / (s + 2)
H2 = 5 / (s + 0.2)

# Closed-loop T(s)
T1 = (K * G) / (1 + K * G * H1)
T2 = (K * G) / (1 + K * G * H2)

plt.figure()

# Magnitude
plt.subplot(2,1,1)
plt.plot(w, abs(T1), label="|T| with H1")
plt.plot(w, abs(T2), '--', label="|T| with H2")
plt.title("Magnitude (Changing H)")
plt.legend()
plt.grid()

# Phase
plt.subplot(2,1,2)
plt.plot(w, np.angle(T1), label="Phase with H1")
plt.plot(w, np.angle(T2), '--', label="Phase with H2")
plt.title("Phase (Changing H)")
plt.xlabel("Frequency (rad/s)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
