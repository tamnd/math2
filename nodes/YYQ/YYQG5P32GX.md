---
tag: YYQG5P32GX
kind: statement
role: theorem
name: Laplace's integral for Legendre polynomials
msc: [33C45]
uses: [QFYGJVA996]
about: [QFYGJVA996]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_polynomials
---

## Statement

Let $n \ge 0$ be an integer and let $P_n$ be the [[Legendre polynomial|QFYGJVA996]] of degree $n$.
For every $x \in \C$,
$$P_n(x) = \frac{1}{\pi} \int_0^\pi \left( x + \sqrt{x^2 - 1} \, \cos \varphi \right)^n \, d\varphi,$$
where $\sqrt{x^2 - 1}$ is either square root of $x^2 - 1$.

## Remarks

The choice of square root does not matter: the substitution $\varphi \mapsto \pi - \varphi$ changes the sign of $\cos \varphi$.
Proof idea: multiply by $t^n$ and sum over $n$ for small $t$.
The integral $\int_0^\pi \frac{d\varphi}{a - b \cos \varphi} = \frac{\pi}{\sqrt{a^2 - b^2}}$ with $a = 1 - tx$ and $b = t \sqrt{x^2 - 1}$ gives $(1 - 2xt + t^2)^{-1/2}$.
This is the generating function of the Legendre polynomials, so the coefficients agree.
Check for $n = 2$: the integral equals $x^2 + \frac{x^2 - 1}{2} = \frac{3x^2 - 1}{2} = P_2(x)$, since the mean of $\cos \varphi$ is $0$ and the mean of $\cos^2 \varphi$ is $\frac12$.
For $-1 \le x \le 1$ the integrand is $\left( x + i \sqrt{1 - x^2} \cos \varphi \right)^n$, whose modulus is at most $\left( x^2 + (1 - x^2) \right)^{n/2} = 1$.
Hence $\abs{P_n(x)} \le 1$ on $[-1, 1]$.

## Explanations

### L1 human

The formula writes each Legendre polynomial as an average of $n$-th powers.
The quantity being raised to the power moves along a segment as the angle $\varphi$ goes from $0$ to $\pi$.
It turns a polynomial into an integral that is easy to bound, which is useful for estimates.

### L2 human

Laplace's integral is one of the standard integral representations of $P_n$, next to Rodrigues' formula and the generating function.
Its main use is in estimates: it gives the bound $\abs{P_n(x)} \le 1$ on $[-1, 1]$ in one line.
For $x > 1$ and the positive root, the integrand is largest at $\varphi = 0$, where it equals $\left( x + \sqrt{x^2 - 1} \right)^n$.
So $P_n(x) \le \left( x + \sqrt{x^2 - 1} \right)^n$, and [[Laplace's method|9G7K8DBT9Y]] gives the precise growth as $n \to \infty$.
The same idea, with Gegenbauer or Jacobi weights, gives integral representations for those families.
