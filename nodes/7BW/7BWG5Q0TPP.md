---
tag: 7BWG5Q0TPP
kind: definition
name: Cavity resonator
msc: [78A50, 35Q61, 35P05]
defines: Y3AYSV8AWD
uses: [9BWWD4QK8Y, F768YN0P2V, 5MJQ5J5H8Z, 4F812GHFZK]
sources:
  - url: https://en.wikipedia.org/wiki/Microwave_cavity
---

## Definition

Let $\Omega \subset \R^3$ be a bounded connected domain with Lipschitz boundary, bounded by a perfect electric conductor.
Let $\Omega$ be filled with a homogeneous lossless medium with [[permittivity|F768YN0P2V]] $\varepsilon > 0$ and [[permeability|5MJQ5J5H8Z]] $\mu > 0$.
A *cavity mode* is a nonzero time-harmonic solution $(\mathbf{E}, \mathbf{H}) e^{-i\omega t}$, with $\omega > 0$, of the source-free [[Maxwell's equations|9BWWD4QK8Y]] in $\Omega$ with the boundary condition $\hat{\mathbf{n}} \times \mathbf{E} = 0$ on $\partial\Omega$.
Equivalently, $\mathbf{E} \neq 0$ satisfies
$$\nabla \times \nabla \times \mathbf{E} = \omega^2 \mu\varepsilon \, \mathbf{E}, \qquad \nabla \cdot \mathbf{E} = 0 \ \text{in } \Omega, \qquad \hat{\mathbf{n}} \times \mathbf{E} = 0 \ \text{on } \partial\Omega.$$
The values of $\omega$ for which a cavity mode exists are the *resonant frequencies*, and the region $\Omega$ with its walls is a *cavity resonator*.

## Remarks

The resonant frequencies form a discrete sequence $0 < \omega_1 \le \omega_2 \le \cdots$ tending to infinity, each with finite multiplicity, since the problem is a self-adjoint eigenvalue problem with compact resolvent on divergence-free fields.
Example: for the box $(0, a) \times (0, b) \times (0, d)$ the resonant frequencies are
$$\omega = \frac{1}{\sqrt{\mu\varepsilon}} \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2 + \left(\frac{p\pi}{d}\right)^2}$$
with integers $m, n, p \ge 0$ of which at most one is zero.
For an air-filled cube of side $a$ the lowest is $f = c/(\sqrt{2}\, a)$, about $2.1$ GHz for $a = 10$ cm.
Non-example: the radial electrostatic field between two concentric conducting spheres satisfies the equations with $\omega = 0$, but it is not a cavity mode, because $\omega > 0$ is required.
With lossy walls the [[resonance|4F812GHFZK]] is broadened, and the quality factor $Q = \omega W / P_{\mathrm{loss}}$ compares the stored energy $W$ with the power lost per radian of oscillation.
