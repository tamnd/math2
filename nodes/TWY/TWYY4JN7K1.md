---
tag: TWYY4JN7K1
kind: statement
role: proposition
name: Diffraction grating equation
msc: [78A45, 78A10]
uses: [NM024G378A, JE101TDP4Q, MNXKTXJ35G, VT8YK4WC0H]
about: [FSCTVTQQF2]
sources:
  - url: https://en.wikipedia.org/wiki/Diffraction_grating
---

## Statement

Let a grating in the plane $z = 0$ be invariant in $y$ and periodic in $x$ with period $d > 0$.
Let it be surrounded by a homogeneous medium of index $1$.
Let a monochromatic [[plane wave|NM024G378A]] of wavelength $\lambda$ fall on it, with wave vector in the $xz$-plane.
Let $\sin\theta_i$ be the $x$-component of its unit direction of propagation.
Then the transmitted field and the reflected field are each a sum of plane waves and [[evanescent waves|VT8YK4WC0H]], indexed by the diffraction orders $m \in \Z$.
For $m \in \Z$, define the number $\sin\theta_m$ by
$$d \, (\sin\theta_m - \sin\theta_i) = m \lambda.$$
The order $m$ is a propagating plane wave exactly when $\abs{\sin\theta_m} \le 1$.
In that case $\sin\theta_m$ is the $x$-component of its unit direction of propagation.

## Remarks

The idea of the proof: the grating is invariant under the shift $x \mapsto x + d$, and the incident wave is multiplied by $e^{i k d \sin\theta_i}$ under this shift, with $k = 2\pi/\lambda$.
So the total field satisfies $u(x + d, z) = e^{i k d \sin\theta_i} u(x, z)$, and its Fourier series in $x$ only contains the wavenumbers $k \sin\theta_i + 2\pi m / d$.
Each Fourier term solving the [[Helmholtz equation|MNXKTXJ35G]] away from the grating is a plane wave when this wavenumber is at most $k$ in absolute value, and an evanescent wave otherwise.
Example: at normal incidence, $\sin\theta_i = 0$, a grating with $d = 2 \lambda$ has propagating orders $m = -2, \dots, 2$ at angles with $\sin\theta_m = m/2$, that is $0^\circ$, $\pm 30^\circ$ and $\pm 90^\circ$.
The equation fixes only the directions of the orders; how much light each order receives depends on the profile of the grating.

## Explanations

### L1 human

A grating is a surface with a fine, regular pattern of lines.
Light leaving it goes only into a few special directions, the orders, where the waves from neighbouring lines arrive in step.
The grating equation gives these directions: the path difference between neighbouring lines must be a whole number of wavelengths.

### L2 human

Since the angles depend on $\lambda$, a grating sends different colours into different directions, which is the basis of the grating spectrometer.
The equation is the one-dimensional case of Bloch–Floquet theory for periodic structures, and the same reasoning gives the Laue conditions for diffraction by crystals.
When an order moves from propagating to evanescent, at $\abs{\sin\theta_m} = 1$, the efficiency of the grating can change abruptly; these are Wood's anomalies.
