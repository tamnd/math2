---
tag: JTA7F0KBMD
kind: definition
name: Bergman metric
msc: [32F45, 32A36]
defines: BB7S4NTZ6V
uses: [8RWDHW0CXC, 2D619WTPYC, CK1DCPC3D3]
sources:
  - url: https://en.wikipedia.org/wiki/Bergman_metric
---

## Definition

Let $\Omega \subseteq \C^n$ be a bounded domain.
Let $K(z, w)$ be its [[Bergman kernel|8RWDHW0CXC]], the reproducing kernel of the [[Bergman space|2D619WTPYC]] $A^2(\Omega)$ of holomorphic functions in $L^2(\Omega)$.
The *Bergman metric* of $\Omega$ is the [[Hermitian metric|CK1DCPC3D3]]
$$ds^2 = \sum_{j,k=1}^n g_{j\bar k}(z) \, dz_j \, d\bar z_k, \qquad g_{j\bar k}(z) = \frac{\partial^2}{\partial z_j \partial \bar z_k} \log K(z, z) .$$

## Remarks

On a bounded domain $K(z, z) > 0$, so $\log K(z, z)$ is defined and smooth.
The matrix $(g_{j\bar k})$ is positive definite at every point; the bounded functions $1$ and $z_j$ in $A^2(\Omega)$ give this positivity.
If $F \colon \Omega_1 \to \Omega_2$ is a biholomorphism, then $K_1(z, w) = \det F'(z) \, K_2(F(z), F(w)) \, \overline{\det F'(w)}$, and the factors $\det F'$ disappear under $\partial\bar\partial \log$, so $F$ is an isometry.
Example: for the unit disc, $K(z, w) = \frac{1}{\pi (1 - z \bar w)^2}$, so $\log K(z, z) = -\log \pi - 2 \log(1 - \abs{z}^2)$ and $g_{1\bar 1} = \frac{2}{(1 - \abs{z}^2)^2}$.
Example: for the unit ball of $\C^n$, the Bergman metric is $n + 1$ times the metric with potential $-\log(1 - \abs{z}^2)$.
Non-example: for $\Omega = \C^n$ the Bergman space is $\set{0}$, so $K \equiv 0$ and the definition does not apply.
The Bergman metric is a Kähler metric, since it has a global potential.
