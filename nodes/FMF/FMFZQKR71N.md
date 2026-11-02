---
tag: FMFZQKR71N
kind: definition
name: System of linear integral equations
msc: [45F05, 45F15]
defines: G9WR1GDE7X
uses: [AYZCKG34QK, GSMBXT7FPK, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $n \ge 1$ and let $\Omega$ be a measurable subset of $\R^m$, for example an interval $[a, b]$.
Let $K_{ij} \colon \Omega \times \Omega \to \C$, for $1 \le i, j \le n$, be [[kernels|GSMBXT7FPK]], let $f_1, \ldots, f_n$ be given functions on $\Omega$, and let $\lambda \in \C$.
A *system of linear integral equations of the second kind* for unknown functions $\varphi_1, \ldots, \varphi_n$ on $\Omega$ is
$$\varphi_i(x) - \lambda \sum_{j=1}^{n} \int_\Omega K_{ij}(x, t)\, \varphi_j(t)\, dt = f_i(x), \quad x \in \Omega, \quad i = 1, \ldots, n.$$
A system *of the first kind* omits the terms $\varphi_i(x)$.
In vector form, with $\varphi = (\varphi_1, \ldots, \varphi_n)$ and the [[matrix|0VD9ZSWWJG]] kernel $K = (K_{ij})$, it reads $\varphi(x) - \lambda \int_\Omega K(x, t)\, \varphi(t)\, dt = f(x)$.

## Remarks

Example: on $\Omega = [0, 1]$ with $n = 2$ and $\lambda = 1$, take $K_{11} = K_{22} = 0$, $K_{12}(x, t) = 1$, $K_{21}(x, t) = x$, $f_1(x) = x$ and $f_2 = 0$.
Put $A = \int_0^1 \varphi_2$ and $B = \int_0^1 \varphi_1$.
The system says $\varphi_1(x) = x + A$ and $\varphi_2(x) = B x$, so $A = B/2$ and $B = \frac{1}{2} + A$, which give $B = 1$ and $A = \frac{1}{2}$.
Check: $\varphi_1(x) = x + \frac{1}{2}$ and $\varphi_2(x) = x$ give $\varphi_1(x) - \int_0^1 \varphi_2 = x$ and $\varphi_2(x) - x \int_0^1 \varphi_1 = x - x = 0$.

Non-example: the pair $\varphi_1(x) - \int_0^1 \varphi_2(t)^2\, dt = x$, $\varphi_2(x) - \int_0^1 \varphi_1(t)\, dt = 0$ is a system of integral equations, but not a linear one, since $\varphi_2$ enters squared.

If $\Omega = [0, 1]$, the substitution $\Phi(x + i - 1) = \varphi_i(x)$ for $x \in [0, 1)$ turns the system into one [[linear integral equation|AYZCKG34QK]] for $\Phi$ on $[0, n)$ with a piecewise defined kernel.
