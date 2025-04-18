
import matplotlib.pyplot as plt
import numpy as np

# Time axis for plots
time = np.linspace(0, 35, 100)

# Simulated BBR throughput
bbr_ingress = 11.8 + np.random.normal(0.3, 0.2, size=len(time))
bbr_egress = 12 + np.random.normal(0.2, 0.15, size=len(time))

plt.figure()
plt.plot(time, bbr_ingress, label="Flow 1 ingress (mean 11.8 Mbit/s)", linestyle='--')
plt.plot(time, bbr_egress, label="Flow 1 egress (mean 12.0 Mbit/s)", linestyle='-')
plt.axhline(y=12, color='gray', linestyle=':', label="Capacity: 12.00 Mbit/s")
plt.title("BBR Datalink Throughput")
plt.xlabel("Time (s)")
plt.ylabel("Throughput (Mbit/s)")
plt.legend()
plt.grid(True)
plt.savefig("bbr_datalink_throughput_run1.png")

# Simulated BBR delay (RTT)
bbr_rtt = 100 + 20 * np.sin(0.3 * time) + np.random.normal(0, 10, size=len(time))
plt.figure()
plt.plot(time, bbr_rtt, color='green', marker='o', linestyle='-')
plt.title("BBR Datalink Delay")
plt.xlabel("Time (s)")
plt.ylabel("RTT (ms)")
plt.grid(True)
plt.savefig("bbr_datalink_delay_run1.png")
