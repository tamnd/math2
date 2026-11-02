---
tag: P3A4XF59FX
kind: definition
name: Resolvent kernel
msc: [45B05, 45P05]
defines: ARTJV1XCRX
uses: [9QNBFERMHD, ZM5G144PZG, 8KJCN49V64, 08VZ57PT26]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%E2%80%93Neumann_series
---

## Definition

Let $a < b$, let $K \colon [a, b] \times [a, b] \to \C$ be a [[continuous kernel|ZM5G144PZG]], let $M = \max \abs{K}$, and let $K_n$ be its [[iterated kernels|9QNBFERMHD]].
For $\lambda \in \C$ with $\abs{\lambda} M (b - a) < 1$, the *resolvent kernel* of $K$ is
$$R(x, s; \lambda) = \sum_{n=1}^{\infty} \lambda^{n-1} K_n(x, s), \quad x, s \in [a, b].$$
The series converges absolutely and [[uniformly|08VZ57PT26]] on $[a, b] \times [a, b]$, because $\abs{\lambda^{n-1} K_n} \le M (\abs{\lambda} M (b - a))^{n-1}$.

## Remarks

Example: $K(x, s) = x s$ on $[0, 1]$, so $M = 1$ and $K_n = x s / 3^{n-1}$.
For $\abs{\lambda} < 1$ the series is $x s \sum_{n \ge 1} (\lambda/3)^{n-1} = 3 x s / (3 - \lambda)$.

Non-example: for $K = 1$ on $[0, 1]$ and $\lambda = 1$, all $K_n = 1$ and the series $\sum 1$ diverges.
This $\lambda$ violates the condition $\abs{\lambda} M (b - a) < 1$, and indeed the homogeneous equation $\varphi = \int_0^1 \varphi$ has the nonzero solution $\varphi = 1$.

The solution of the [[integral equation of the second kind|8KJCN49V64]] $\varphi(x) = f(x) + \lambda \int_a^b K(x, s) \varphi(s) \, ds$ is then $\varphi(x) = f(x) + \lambda \int_a^b R(x, s; \lambda) f(s) \, ds$.
In operator terms, $R = K (I - \lambda K)^{-1}$.
By Fredholm theory, $R$ extends to a meromorphic function of $\lambda$ on $\C$, the quotient of two entire functions.
The resolvent kernel is then defined at every $\lambda$ that is not a pole.
The example shows that the extension can go beyond the disc of the definition: $3 x s / (3 - \lambda)$ has its only pole at $\lambda = 3$.
