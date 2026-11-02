---
tag: Z219Y8PJHD
kind: example
name: Lieb–Liniger integral equation
msc: [82B23, 45B05]
instance_of: [DEYYNVCV9J]
sources:
  - url: https://en.wikipedia.org/wiki/Lieb%E2%80%93Liniger_model
---

## Example

Consider the Lieb–Liniger model of bosons on a line with delta interaction of strength $c > 0$, in units with $\hbar = 2m = 1$.
In the thermodynamic limit its ground state is described by a density $\rho$ of quasi-momenta on an interval $[-K, K]$, with $K > 0$.
This density solves
$$\rho(k) = \frac{1}{2\pi} + \frac{1}{\pi} \int_{-K}^{K} \frac{c}{c^2 + (k - q)^2} \, \rho(q) \, dq, \quad -K \le k \le K.$$
The particle density and the ground state energy per length are $n = \int_{-K}^{K} \rho(k) \, dk$ and $e = \int_{-K}^{K} k^2 \rho(k) \, dk$.

The equation is a [[Fredholm equation of the second kind|DEYYNVCV9J]] on $[-K, K]$ with the continuous [[difference kernel|B5AB451TB7]] $\frac{1}{\pi} \frac{c}{c^2 + (k - q)^2}$.
This kernel is positive and $\frac{1}{\pi} \int_{-\infty}^{\infty} \frac{c}{c^2 + u^2} \, du = 1$.
So for each $k$ the integral of the kernel over the bounded interval $[-K, K]$ is strictly less than $1$.
By continuity and compactness, its maximum over $k$ is some $\theta < 1$.
Hence the integral operator has norm $\theta < 1$ on $C[-K, K]$ with the supremum norm.
Then the [[Liouville–Neumann series|H1HWSWME6B]] converges to the unique continuous solution, which is positive.

## Remarks

In the limit $c \to \infty$ the kernel tends to $0$ uniformly on $[-K, K]^2$, so $\rho \to \frac{1}{2\pi}$.
Then $n = \frac{K}{\pi}$ and $e = \frac{K^3}{3\pi} = \frac{\pi^2 n^3}{3}$, the energy of free fermions with the same density.

## Explanations

### L1 human

Bosons that repel each other on a line can be solved exactly with the Bethe ansatz.
For many particles the allowed momenta fill an interval with some density, and this density solves a linear integral equation.
The kernel is a Lorentzian bump of width $c$, so for strong repulsion the integral term is small and the density is almost constant.
