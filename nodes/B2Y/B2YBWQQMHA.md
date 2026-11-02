---
tag: B2YBWQQMHA
kind: statement
role: theorem
name: Poincaré–Lelong formula
msc: [32U40, 32C30]
uses: [JSGWAN2RJV, 507C34W0ZT, 360H7MD9RD, BYJHP6A906, FF2P7ER3QT]
about: [BYJHP6A906]
sources:
  - url: https://en.wikipedia.org/wiki/Lelong_number
---

## Statement

Let $X$ be a connected [[complex manifold|JSGWAN2RJV]] and let $f$ be a [[holomorphic function|507C34W0ZT]] on $X$ that is not identically $0$.
Let $Z_1, Z_2, \dots$ be the irreducible components of the hypersurface $f^{-1}(0)$.
Let $m_j \ge 1$ be the order of vanishing of $f$ at a general point of $Z_j$.
Let $[Z_j]$ be the current of integration over the regular part of $Z_j$, and let $[Z_f] = \sum_j m_j [Z_j]$.
Then, in the sense of [[currents|360H7MD9RD]] on $X$,
$$\frac{i}{\pi} \partial\bar\partial \log\abs{f} = [Z_f] .$$

## Remarks

Proof idea: off $f^{-1}(0)$ the function $\log\abs{f}$ is pluriharmonic, so both sides vanish there.
Near a regular point of $f^{-1}(0)$ one can choose coordinates with $f = u \, z_1^{m}$ for a holomorphic unit $u$.
Then $\log\abs{u}$ is pluriharmonic, and the claim reduces to the one-variable identity $\Delta \log\abs{z_1} = 2\pi \delta_0$ on each line $z' = \text{const}$.
The difference of the two sides is then a closed current of order zero supported in the singular set of $f^{-1}(0)$.
This set has codimension at least $2$, so such a current of bidegree $(1, 1)$ vanishes by Federer's support theorem.
Example: for $X = \C$ and $f(z) = z^2 (z - 1)$ the formula says $\frac{1}{2\pi} \Delta \log\abs{f} = 2 \delta_0 + \delta_1$, the classical statement that $\log\abs{f}$ has Riesz measure given by the zeros with multiplicity.
Consequence: $[Z_f]$ is $dd^c$ of a [[plurisubharmonic function|FF2P7ER3QT]], so it is a closed [[positive current|BYJHP6A906]].
Let $s$ be a holomorphic section of a holomorphic line bundle with a smooth Hermitian metric.
The same argument shows that $\frac{i}{\pi} \partial\bar\partial \log\abs{s}$ equals $[Z_s]$ minus a smooth closed form that represents the first Chern class of the bundle.

## Explanations

### L1 human

In one complex variable, $\log\abs{f}$ for a polynomial $f$ is harmonic except at the zeros, where it behaves like $m \log\abs{z - a}$.
Its Laplacian is a sum of point masses at the zeros, weighted by their multiplicities.
The Poincaré–Lelong formula says the same in several variables.
The complex second derivative of $\log\abs{f}$ is concentrated on the zero set of $f$, and it equals integration over it, counted with multiplicity.

### L2 human

The formula is the bridge between divisors and positive currents.
It shows that every effective divisor gives a closed positive $(1,1)$-current, and it lets one compute with zero sets through the plurisubharmonic function $\log\abs{f}$.
It is used in Nevanlinna theory in several variables and in the theory of [[Lelong numbers|WVB60RKC3Z]].
For example, the Lelong number of $\log\abs{f}$ at a point is the multiplicity of $f$ there.
The line bundle version links the zero divisor of a section with the curvature of the bundle, which is the starting point of many vanishing and extension theorems.
