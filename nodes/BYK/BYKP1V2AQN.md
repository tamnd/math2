---
tag: BYKP1V2AQN
kind: statement
role: theorem
name: Wiener–Hopf factorization
msc: ["45E10", 47A68, 47B35]
uses: [QYY4NMDY5H, DPVM34ADZV, NC768TWZ3D, 0X7SBS8E0F, 0NAHXR1FRH, 8HWGKWD6ZM, 2V9Q4KHY1T]
about: [QYY4NMDY5H]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener%E2%80%93Hopf_method
---

## Statement

Let $k \in L^1(\R)$ and write $\hat g(\xi) = \int_{\R} g(x)\, e^{i\xi x}\, dx$ for the [[Fourier transform|DPVM34ADZV]].
Assume that $1 - \hat k(\xi) \ne 0$ for all $\xi \in \R$.
Since $\hat k(\xi) \to 0$ as $\abs{\xi} \to \infty$, the curve $\xi \mapsto 1 - \hat k(\xi)$, $\xi \in [-\infty, \infty]$, is closed; let $\nu$ be its [[winding number|0X7SBS8E0F]] about $0$.
Let $r(\xi) = (\xi - i)/(\xi + i)$.

1. There are $k_+, k_- \in L^1(\R)$, with $k_+ = 0$ on $(-\infty, 0)$ and $k_- = 0$ on $(0, \infty)$, and
$$1 - \hat k(\xi) = \bigl(1 - \hat k_-(\xi)\bigr)\, r(\xi)^{\nu}\, \bigl(1 - \hat k_+(\xi)\bigr), \quad \xi \in \R.$$
Here $1 - \hat k_+$ has no zeros in the closed upper half-plane and $1 - \hat k_-$ has no zeros in the closed lower half-plane.
2. Let $1 \le p < \infty$ and $W \varphi(x) = \varphi(x) - \int_0^\infty k(x - t) \varphi(t)\, dt$ on $L^p(0, \infty)$. Then $W$ is a [[Fredholm operator|8HWGKWD6ZM]] of [[index|2V9Q4KHY1T]] $-\nu$. If $\nu = 0$ it is invertible. If $\nu > 0$ it is injective and its range has codimension $\nu$. If $\nu < 0$ it is surjective and its kernel has dimension $-\nu$.

## Remarks

The functions $1 - \hat k_\pm$ extend [[holomorphically|0NAHXR1FRH]] to the corresponding half-planes, because $k_\pm$ vanish on a half-line.
When $\nu = 0$, a continuous branch of $\log\bigl(1 - \hat k\bigr)$ on $\R$ tends to $0$ at infinity; splitting it into an upper and a lower part and exponentiating gives the two factors.
The difficult point is that the split pieces again come from $L^1$ functions, which uses [[Wiener's lemma|NC768TWZ3D]] on absolutely convergent Fourier integrals.
For $\nu \ne 0$ one first divides by $r^\nu$, whose winding number is $\nu$.

Example: $k(x) = 2 e^{-x}$ for $x > 0$ and $k = 0$ otherwise gives $1 - \hat k(\xi) = 1 - \frac{2}{1 - i\xi} = \frac{\xi - i}{\xi + i} = r(\xi)$.
So $\nu = 1$, $k_\pm = 0$, and $W$ is injective with range of codimension $1$.

The hypothesis $1 - \hat k \ne 0$ on $\R$ is needed: for $k(x) = \frac{1}{2} e^{-\abs{x}}$ the symbol $\frac{\xi^2}{1 + \xi^2}$ vanishes at $0$, and then $W$ is not Fredholm on $L^p(0, \infty)$.

## Explanations

### L1 human

A Wiener–Hopf equation is a convolution equation cut off at $0$.
Its Fourier symbol can be written as a product of a part that "looks only forward" and a part that "looks only backward".
A simple extra factor counts how many times the symbol winds around $0$.
This winding number decides everything: if it is $0$ the equation has exactly one solution for each right side.

### L2 human

The theorem is the continuous analogue of the theory of Toeplitz operators, where the symbol lives on the unit circle instead of the real line.
It turns the Wiener–Hopf method into a complete solvability theory for kernels in $L^1(\R)$.
The sign convention of the Fourier transform matters.
With the kernel $e^{-i\xi x}$ the half-planes swap roles and the winding number changes sign, so the index becomes $+\nu$.
For systems of equations the symbol is a matrix function, and a single winding number is replaced by several partial indices, which is the matrix Wiener–Hopf factorization.
