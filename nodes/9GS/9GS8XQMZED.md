---
tag: 9GS8XQMZED
kind: definition
name: Jacobian variety
msc: [14H40, 14K30]
defines: ZQ84M9D9TC
uses: [5K0N8QMV6Q, P014C13K5H, Y7MA6KBE9M, WN9V7WSJKF, NJ787GZS1N]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobian_variety
---

## Definition

Let $X$ be a compact connected [[Riemann surface|5K0N8QMV6Q]] of [[genus|NJ787GZS1N]] $g \ge 1$.
Let $\Omega(X)$ be the complex vector space of holomorphic [[Abelian differentials|P014C13K5H]] on $X$, which has dimension $g$, and let $\Omega(X)^*$ be its dual space.
Each class $\gamma \in H_1(X, \Z)$ gives the linear form $\omega \mapsto \int_\gamma \omega$ on $\Omega(X)$, and this defines a map $H_1(X, \Z) \to \Omega(X)^*$ whose image $\Lambda$ is a [[lattice|WN9V7WSJKF]] of rank $2g$.
The *Jacobian variety* of $X$ is the [[complex torus|Y7MA6KBE9M]]
$$J(X) = \Omega(X)^* / \Lambda.$$

## Remarks

Choosing a basis $\omega_1, \ldots, \omega_g$ of $\Omega(X)$ identifies $J(X)$ with $\C^g / \Lambda$, where $\Lambda$ is spanned by the period vectors $\left( \int_\gamma \omega_1, \ldots, \int_\gamma \omega_g \right)$.
The Riemann bilinear relations give $J(X)$ a principal polarization, so it is an abelian variety.
By the Abel–Jacobi theorem, $J(X)$ is isomorphic to the group $\operatorname{Pic}^0(X)$ of divisor classes of degree $0$; this description defines the Jacobian of a smooth projective curve over any field.
Example: for $X = \C / \Lambda_0$ with $g = 1$ and $\omega_1 = dz$, the periods of $dz$ are the elements of $\Lambda_0$, so $J(X) \cong \C / \Lambda_0 \cong X$.
Non-example: a general complex torus $\C^2 / \Lambda$ of dimension $2$ admits no nonconstant meromorphic functions, so it is not an abelian variety and is not the Jacobian of any curve.
Torelli's theorem says that $X$ is determined by $J(X)$ together with its principal polarization.
