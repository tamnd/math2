---
tag: EYA944RVSY
kind: definition
name: Born series
msc: [81U05, 45B05]
defines: 2PCVRG9NBN
uses: [8KJCN49V64, 06GZ956657, 06EKW1AKXF]
sources:
  - url: https://en.wikipedia.org/wiki/Born_series
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]] of functions on $\R^n$, and let $\phi \in X$ be an incoming wave.
Let $V$ be multiplication by a potential.
Let $G_0$ be the outgoing free resolvent, the convolution with the outgoing Green's function of $\Delta + k^2$.
Assume that $T = G_0 V$ is a bounded linear operator on $X$.
Consider the scattering equation $\psi = \phi + T \psi$, an [[integral equation of the second kind|8KJCN49V64]].
The *Born series* of $\psi$ is the formal series
$$\psi = \sum_{n = 0}^{\infty} T^n \phi = \phi + G_0 V \phi + G_0 V G_0 V \phi + \cdots.$$
Its partial sum $\phi + G_0 V \phi$ is the *(first) Born approximation*.

## Remarks

If the [[operator norm|06EKW1AKXF]] satisfies $\norm{T} < 1$, the series converges in $X$ and its sum is the unique solution of $\psi = \phi + T \psi$, by the [[Neumann series|8QJ91709V2]].
Replacing $V$ by $g V$ with a coupling constant $g$, this holds for all small enough $\abs{g}$.

Example: in one dimension, take the point interaction $V = g \delta_0$ with $g \in \R$; then the outgoing Green's function is $\frac{e^{ik\abs{x}}}{2ik}$, and $G_0 V \psi(x) = \frac{g}{2ik} e^{ik\abs{x}} \psi(0)$.
For $\phi(x) = e^{ikx}$ each term is a multiple of $e^{ik\abs{x}}$, and the series sums to $\psi(x) = e^{ikx} + \frac{g/(2ik)}{1 - g/(2ik)} e^{ik\abs{x}}$ when $\abs{g} < 2k$.
At $x = 0$ this gives $\psi(0) = \frac{1}{1 - g/(2ik)}$, which solves $\psi(0) = 1 + \frac{g}{2ik} \psi(0)$, as it must.

Non-example: for $\abs{g} > 2k$ in the same model the geometric series diverges, although the equation still has the solution given by the closed formula.
So the Born series may fail to converge even when the scattering problem is well posed.
