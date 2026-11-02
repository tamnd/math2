---
tag: J0MHS4ZCKR
kind: definition
name: Fourier series method
msc: [35C10, 35K05, 42A16]
defines: JYEV0Q7T4Z
uses: [G12KXDHPPS, 47NFRVB564, VP2HN86VAG, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Definition

Let $L > 0$ and let $A$ be a linear differential operator in $x$, with boundary conditions at $0$ and $L$.
Consider the linear evolution equation $u_t = A u$ for $u \colon [0, L] \times [0, \infty) \to \R$.
Assume that $L^2(0, L)$ has an [[orthonormal basis|0S9GGTR0EX]] $(\varphi_k)_{k \ge 1}$ of functions that satisfy the boundary conditions and $A \varphi_k = -\mu_k \varphi_k$ with $\mu_k \in \R$.
Typically the $\varphi_k$ are sines or cosines, so that expansions in them are [[Fourier series|G12KXDHPPS]].
The *Fourier series method* for the initial value $u(\cdot, 0) = f$ consists of three steps.

1. Expand $f = \sum_k b_k \varphi_k$ with $b_k = \int_0^L f \varphi_k \, dx$.
2. Seek $u(x, t) = \sum_k c_k(t) \varphi_k(x)$, which turns the equation into the ordinary differential equations $c_k' = -\mu_k c_k$ with $c_k(0) = b_k$.
3. Solve them, which gives $u(x, t) = \sum_k b_k e^{-\mu_k t} \varphi_k(x)$.

The same steps apply to second-order equations in time, such as the wave equation $u_{tt} = A u$, with two initial values.

## Remarks

Example: the [[heat equation|VP2HN86VAG]] $u_t = u_{xx}$ on $(0, \pi)$ with $u(0, t) = u(\pi, t) = 0$.
Here $\varphi_k(x) = \sqrt{2/\pi}\, \sin(kx)$ and $\mu_k = k^2$, since $(\sin kx)'' = -k^2 \sin kx$.
For $f(x) = \sin x + \sin 3x$, the method gives $u(x, t) = e^{-t} \sin x + e^{-9t} \sin 3x$.
Check: $u_t = -e^{-t} \sin x - 9 e^{-9t} \sin 3x = u_{xx}$, and $u$ vanishes at $0$ and $\pi$.

Non-example: the nonlinear equation $u_t = u_{xx} + u^2$ with the same boundary conditions does not decouple.
The product of two sine modes contains other modes, so the coefficient equations form an infinite coupled system.

Each term $c_k(t) \varphi_k(x)$ is a product solution, so the method is [[separation of variables|47NFRVB564]] followed by superposition.
For $f \in L^2(0, L)$ and $\mu_k \ge 0$, the series for $u$ converges in $L^2$ for each $t \ge 0$.

## Explanations

### L1 human

The method writes the initial state as a sum of basic shapes that the equation only rescales in time.
Each shape is then evolved by a simple exponential factor, and the pieces are added back together.
