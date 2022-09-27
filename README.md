# Fourier-Series-Interpolation
interpolation of closed cyclic path on 2D plane using Fourier series.

# Manual

1) run main.py
2) click right mouse button on sampling screen to put dots (you can remove dots just clicking on them again)
3) close window with "x" button
4) enjoy smoth visualisation of your point interpolation

# How it works

program treat the sampled points as complex (x - real part, y - imaginary part) values in time domain where sampling rate is constant. So it use the DFT to map complex vector of values to complex vector which is a result of DFT. Then it splits each value to its module and phase and corresponding pulsation.
This gives every needed value to simulate each set of values (as a vector with rotation speed). Visualization part only joins those vectors in one chain and symulate it.
