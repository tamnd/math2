---
tag: AN7QEWTNBT
kind: definition
name: Arnold diffusion
msc: [37J40, 70H08]
defines: ZVY046R4XB
uses: [0EDKGA2FAK, M3T81YNSKC, N0N7CMRCMH]
sources:
  - url: https://en.wikipedia.org/wiki/Arnold_diffusion
---

## Definition

Let $n \ge 1$, let $D \subseteq \R^n$ be open and let $\mathbb{T}^n = \R^n / 2\pi \Z^n$.
Use [[action-angle coordinates|M3T81YNSKC]] $(I, \theta)$ on $D \times \mathbb{T}^n$.
Consider the family of [[Hamiltonian systems|0EDKGA2FAK]] with Hamiltonians
$$H_\varepsilon(I, \theta, t) = H_0(I) + \varepsilon H_1(I, \theta, t),$$
where $H_1$ is smooth and may depend periodically on time $t$.
The family exhibits *Arnold diffusion* if there is a constant $\delta > 0$ with the following property.
For every sufficiently small $\varepsilon > 0$ there are a solution $(I(t), \theta(t))$ of the system of $H_\varepsilon$ and a time $T > 0$ with
$$\abs{I(T) - I(0)} \ge \delta.$$

## Remarks

The point is that $\delta$ does not depend on $\varepsilon$: the actions drift by an amount of order one, while for $\varepsilon = 0$ they are constant.
The time $T$ needed tends to infinity as $\varepsilon \to 0$.

Example: Arnold's 1964 example is the time-periodic Hamiltonian
$$H(I, \theta, t) = \tfrac{1}{2}(I_1^2 + I_2^2) + \varepsilon (\cos \theta_1 - 1)\big(1 + \mu (\sin \theta_2 + \cos t)\big)$$
with two angles and periodic time.
Arnold proved that for suitable small $\mu$ depending on $\varepsilon$ there are orbits along which $I_2$ changes by an amount of order one.

Non-example: an autonomous real-analytic system with $n = 2$ degrees of freedom and isoenergetically nondegenerate $H_0$ has no Arnold diffusion.
By the [[KAM theorem|3ZZSXKM16Z]], each $3$-dimensional energy level contains invariant $2$-tori that cut it into regions.
The action of an orbit is trapped between two such tori, so the drift tends to $0$ with $\varepsilon$.

For real-analytic $H_\varepsilon$ with steep $H_0$, the [[Nekhoroshev estimates|PYEN6SFS9P]] show that the drift time $T$ grows at least exponentially in a power of $1/\varepsilon$.
