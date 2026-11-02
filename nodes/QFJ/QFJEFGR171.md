---
tag: QFJEFGR171
kind: definition
name: Spectral method
msc: [65N35, 65M70]
defines: MYV657YRDW
uses: [G12KXDHPPS, M6EAR1JHPP, QFYGJVA996, Y5B0PEBKE8]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_method
---

## Definition

Let $L$ be a linear differential operator on an interval or a box $\Omega$, and consider $L u = f$ with boundary or periodicity conditions.
Fix a family of smooth functions $\varphi_k$ on all of $\Omega$, each nonzero on most of $\Omega$.
Typical choices are $e^{ikx}$ for periodic problems, [[Chebyshev polynomials|M6EAR1JHPP]] or [[Legendre polynomials|QFYGJVA996]] otherwise.
Let $I_N$ be a finite set of $n$ indices.
A *spectral method* seeks $u_N = \sum_{k \in I_N} a_k \varphi_k$ and fixes the $a_k$ by one of three conditions:

1. Galerkin: $\ip{L u_N - f}{\varphi_j} = 0$ for all $j \in I_N$, with the $\varphi_k$ satisfying the boundary conditions;
2. tau: the same equations for all but $m$ indices $j$, plus the $m$ boundary conditions written as equations on the $a_k$;
3. collocation: $L u_N(x_j) = f(x_j)$ at chosen points $x_j$, together with the boundary conditions, with $n$ equations in all.

Here $\ip{\cdot}{\cdot}$ is the $L^2$ inner product, with the weight of the chosen polynomial family.

## Remarks

Example: on $[0, 2\pi]$ with periodic conditions, solve $-u'' + u = f$ with the Fourier basis $e^{ikx}$, $\abs{k} \le N$.
The Galerkin condition gives $(k^2 + 1) a_k = \hat f_k$, where $\hat f_k$ are the [[Fourier coefficients|G12KXDHPPS]] of $f$.
So $u_N$ is the truncation of the exact Fourier series of $u$.
If $f$ is analytic, $\hat f_k$ decays like $e^{-c \abs{k}}$, and so does the error of $u_N$.

Non-example: the finite element method with hat functions uses basis functions that vanish outside two mesh cells.
These are not global functions, so it is not a spectral method; its error for smooth $u$ decreases only like a fixed power of $1/N$.
