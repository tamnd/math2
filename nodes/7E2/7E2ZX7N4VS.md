---
tag: 7E2ZX7N4VS
kind: definition
name: Artin–Mazur zeta function
msc: ["37C30", "37C25"]
defines: 2A5Z21CE4P
uses: [R6QVS6P21N, T75CZ5H47N, 033WGN00BF, 0N288P2TB5]
sources:
  - url: https://en.wikipedia.org/wiki/Artin%E2%80%93Mazur_zeta_function
---

## Definition

Let $X$ be a set and let $f \colon X \to X$ be a map.
Assume that, for every $n \ge 1$, the set $\operatorname{Fix}(f^n)$ of [[fixed points|R6QVS6P21N]] of the $n$-th iterate $f^n$ is finite.
Write $N_n = \abs{\operatorname{Fix}(f^n)}$.
The *Artin–Mazur zeta function* of $f$ is the [[formal power series|033WGN00BF]]
$$\zeta_f(z) = \exp\left( \sum_{n=1}^{\infty} \frac{N_n}{n} z^n \right).$$
It has rational coefficients.

## Remarks

Example: let $f(z) = z^2$ on the unit circle in $\C$.
The fixed points of $f^n$ are the solutions of $z^{2^n} = z$ with $\abs{z} = 1$, that is, the $(2^n - 1)$-th roots of unity, so $N_n = 2^n - 1$.
Then
$$\zeta_f(z) = \exp\left( \sum_{n \ge 1} \frac{(2z)^n}{n} - \sum_{n \ge 1} \frac{z^n}{n} \right) = \frac{1 - z}{1 - 2z}.$$

Non-example: the identity map of the circle has infinitely many fixed points, so $N_1$ is not finite and the definition does not apply.

If $N_n \le C a^n$ for constants $C$ and $a$, the series has a positive [[radius of convergence|0N288P2TB5]] and $\zeta_f$ is a holomorphic function near $0$.
For the shift on a subshift of finite type with transition matrix $A$, $N_n = \tr(A^n)$ and $\zeta_f(z) = 1 / \det(I - zA)$.
For an Axiom A diffeomorphism of a compact manifold, the zeta function is rational (Manning).
The function has the product form $\zeta_f(z) = \prod_{\gamma} (1 - z^{\abs{\gamma}})^{-1}$, a product over the periodic orbits $\gamma$ of $f$ with $\abs{\gamma}$ the number of points of $\gamma$.
