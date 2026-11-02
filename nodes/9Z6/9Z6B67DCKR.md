---
tag: 9Z6B67DCKR
kind: definition
name: Difference kernel
msc: ["45E10", 45P05]
defines: B5AB451TB7
uses: [GSMBXT7FPK, 2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution
---

## Definition

Let $J \subseteq \R$ be an interval, possibly unbounded.
A *difference kernel* on $J$ is a [[kernel|GSMBXT7FPK]] $K \colon J \times J \to \C$ for which there is a function $k \colon \set{x - s : x, s \in J} \to \C$ such that
$$K(x, s) = k(x - s) \quad \text{for all } x, s \in J.$$

## Remarks

Example: $K(x, s) = \cos(x - s)$ with $k = \cos$.

Non-example: $K(x, s) = x s$ on $[0, 1]$.
If $x s = k(x - s)$, then putting $s = x$ gives $x^2 = k(0)$ for all $x \in [0, 1]$, which is impossible.

On $J = \R$, the integral operator is the [[convolution|2Z29JN3VES]] $\int_{\R} k(x - s) \varphi(s) \, ds = (k * \varphi)(x)$.
On $J = [0, \infty)$ with upper limit $x$, it is the one-sided convolution $\int_0^x k(x - s) \varphi(s) \, ds$, which the Laplace transform turns into a product.
Equations with a difference kernel are called *convolution equations*.
The equation $\varphi(x) = f(x) + \int_0^{\infty} k(x - s) \varphi(s) \, ds$ for $x \ge 0$ is the Wiener–Hopf equation.
