---
tag: VM7M0PJTD4
kind: definition
name: Pesin theory
msc: ["37D25", "37C40"]
defines: ZHKS81A7QN
uses: [F45VQ47GPV, 0KZZ70ZHXP, B232EZ1FMB, NJ1FJSNK6A, NJ1PDJ3S4R]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov_exponent
---

## Definition

Let $M$ be a compact Riemannian [[manifold|F45VQ47GPV]] and let $f \colon M \to M$ be a $C^{1+\alpha}$ [[diffeomorphism|0KZZ70ZHXP]] for some $\alpha > 0$.
Let $\mu$ be an $f$-[[invariant|B232EZ1FMB]] Borel probability measure on $M$.
Let $x \in M$ and let $v \in T_x M$ be nonzero.
The [[Lyapunov exponent|NJ1FJSNK6A]] of $v$ is
$$\lambda(x, v) = \lim_{n \to \infty} \frac{1}{n} \log \norm{D f^n_x \, v}$$
when the limit exists.
By the [[Oseledets theorem|NJ1PDJ3S4R]], for $\mu$-almost every $x$ the limit exists for every $v$ and takes finitely many values.
The measure $\mu$ is *hyperbolic* if, for $\mu$-almost every $x$, the number $0$ is not among the values $\lambda(x, v)$.
*Pesin theory* is the theory of the pairs $(f, \mu)$ of this kind with $\mu$ hyperbolic, also called *nonuniformly hyperbolic* systems.

## Remarks

Example: let $f$ be the linear map of the torus $\R^2 / \Z^2$ given by the matrix $\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$, and let $\mu$ be Lebesgue measure.
The exponents are $\log \frac{3 + \sqrt 5}{2} > 0$ and $\log \frac{3 - \sqrt 5}{2} < 0$ at every point, so $\mu$ is hyperbolic.

Non-example: an irrational rotation of the torus $\R^2/\Z^2$ with Lebesgue measure is an isometry, so both exponents are $0$ everywhere and the measure is not hyperbolic.

The main results of the theory, for hyperbolic $\mu$ and $C^{1+\alpha}$ maps, include the following.
Local stable and unstable manifolds exist at $\mu$-almost every point.
If $\mu$ is absolutely continuous with respect to volume, the entropy of $\mu$ equals the integral of the sum of the positive exponents, counted with multiplicity (the Pesin entropy formula).
The hypothesis $\alpha > 0$ is needed for the stable manifold theorem: the theory does not extend in general to $C^1$ maps.
