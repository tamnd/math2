---
tag: KTG9DV4B9V
kind: definition
name: Luttinger liquid
msc: [81V74, 82D20, 81T40]
defines: AS696NEAGP
uses: [FW27X1KB37]
sources:
  - url: https://en.wikipedia.org/wiki/Luttinger_liquid
---

## Definition

Consider a one-dimensional system of interacting particles (fermions or bosons) on a line, with units where $\hbar = 1$.
Let $\phi(x)$ and $\theta(x)$ be real boson fields with $[\phi(x), \partial_y \theta(y)] = i\pi\,\delta(x - y)$, where $\partial_x \phi$ measures the density fluctuation and $\theta$ is the phase field.
The *Tomonaga–Luttinger Hamiltonian* with velocity $u > 0$ and Luttinger parameter $K > 0$ is
$$H = \frac{u}{2\pi} \int \Big( K \big(\partial_x \theta(x)\big)^2 + \frac{1}{K} \big(\partial_x \phi(x)\big)^2 \Big) \, dx.$$
The system is a *Luttinger liquid* if it is gapless and its low-energy properties are those of this Hamiltonian for some $u$ and $K$.
In this description the particle operators are expressed through $e^{\pm i\phi}$ and $e^{i\theta}$ (bosonization).

## Remarks

The Hamiltonian is quadratic, so its correlation functions are computed exactly; they decay as powers of distance with exponents depending on $K$.
For spin-$1/2$ fermions there are separate charge and spin fields with their own velocities, which is spin-charge separation.
Conventions for $\phi$, $\theta$ and $K$ differ between sources; in the convention above, spinless fermions have $K = 1$ when free and $K < 1$ for repulsive interactions.

Example: free spinless fermions with Fermi velocity $v_F$ are a Luttinger liquid with $u = v_F$ and $K = 1$.
The gapless phase of the [[XXZ model|NR4JGQ7XTB]], mapped to fermions by the [[Jordan–Wigner transformation|94PEKQHHHT]], is a Luttinger liquid with $K$ depending on the anisotropy.

Non-example: a three-dimensional metal is a [[Fermi liquid|FW27X1KB37]], whose momentum distribution has a jump at $k_F$.
In a Luttinger liquid with $K \ne 1$ the momentum distribution is continuous at $k_F$, with only a power-law singularity.
