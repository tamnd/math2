---
tag: NXWRDGX8T5
kind: definition
name: Kelvin transform
msc: [31B05, 31A05]
defines: W9YR470VY2
uses: [0DEB0JMN0W, YXST7NGMTC, 02BH3MCBQB, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Kelvin_transform
---

## Definition

Let $n \ge 2$ and, for $x \in \R^n \setminus \set{0}$, let $x^* = x / \abs{x}^2$ be its inversion in the unit sphere.
Let $\Omega \subseteq \R^n \setminus \set{0}$ be an [[open set|02BH3MCBQB]] and let $\Omega^* = \set{x^* : x \in \Omega}$.
The *Kelvin transform* of a function $u \colon \Omega \to \R$ is the function $K[u] \colon \Omega^* \to \R$ given by
$$K[u](x) = \abs{x}^{2-n} \, u(x^*).$$

## Remarks

The map $x \mapsto x^*$ is an involution, so $(\Omega^*)^* = \Omega$ and $K[K[u]] = u$.
For $n = 2$, $K[u] = u \circ {}^*$ is the composition with the [[inversion in the unit circle|YXST7NGMTC]], $z \mapsto 1/\bar z$.
For $u$ twice continuously differentiable, $\Delta(K[u]) = K[\abs{x}^4 \Delta u]$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]]; so $u$ is [[harmonic|0DEB0JMN0W]] on $\Omega$ if and only if $K[u]$ is harmonic on $\Omega^*$.
Example: in $\R^3$, $K[x_1](x) = \abs{x}^{-1} \cdot x_1 \abs{x}^{-2} = x_1 / \abs{x}^3 = -\partial_1(1/\abs{x})$, which is harmonic on $\R^3 \setminus \set{0}$, as a derivative of a harmonic function.
Non-example: without the weight, $u(x^*) = x_1 / \abs{x}^2$ is not harmonic on $\R^3 \setminus \set{0}$; a direct computation gives $\Delta(x_1 \abs{x}^{-2}) = -2 x_1 \abs{x}^{-4}$.
The transform turns the behaviour of $u$ near infinity into the behaviour of $K[u]$ near $0$.
For instance, let $n \ge 3$ and let $u$ be harmonic outside a ball; then $u(x) \to 0$ at infinity if and only if $K[u]$ has a removable singularity at $0$.
Inversion in a sphere of centre $a$ and radius $\rho$ gives the analogous transform $\left(\rho / \abs{x - a}\right)^{n-2} u\left(a + \rho^2 (x - a)/\abs{x - a}^2\right)$.
