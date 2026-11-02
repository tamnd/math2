---
tag: G02NBNN6CJ
kind: statement
role: theorem
name: Koenigs linearization theorem
msc: [37F50, 30D05]
uses: [0NAHXR1FRH, R6QVS6P21N, HNXXAPQKG3]
about: [R6QVS6P21N]
sources:
  - url: https://en.wikipedia.org/wiki/Koenigs_function
---

## Statement

Let $U \subseteq \C$ be an open set containing $0$, and let $f \colon U \to \C$ be [[holomorphic|0NAHXR1FRH]] with $f(0) = 0$.
Let $\lambda = f'(0)$ and assume $\lambda \ne 0$ and $\abs{\lambda} \ne 1$.
Then there is a holomorphic map $\varphi$ on a neighbourhood $V$ of $0$ with $\varphi(0) = 0$ and $\varphi'(0) = 1$ such that
$$\varphi(f(z)) = \lambda \, \varphi(z) \quad \text{for all } z \in V \text{ with } f(z) \in V.$$
The map $\varphi$ is unique.

## Remarks

In the attracting case $0 < \abs{\lambda} < 1$, the map is given by $\varphi(z) = \lim_{n \to \infty} f^n(z) / \lambda^n$.
The limit converges uniformly near $0$, because $f^n(z) = \lambda^n z (1 + O(\abs{z}))$ with errors that shrink geometrically.
The repelling case $\abs{\lambda} > 1$ follows by applying the attracting case to the local inverse of $f$.
So near a [[fixed point|R6QVS6P21N]] that is attracting but not superattracting, or repelling, $f$ is locally [[conjugate|HNXXAPQKG3]] to its linear part $z \mapsto \lambda z$.
Example: $f(z) = z / (2 - z)$ has $f'(0) = 1/2$, and $\varphi(z) = z / (1 - z)$ satisfies $\varphi(f(z)) = \varphi(z) / 2$.
The hypotheses are needed.
For $\lambda = 0$, the map $z \mapsto z^2$ is not conjugate to $z \mapsto 0$, since it is not constant.
For $\lambda = 1$, the map $z \mapsto z + z^2$ is not conjugate to the identity, since it is not the identity.

## Explanations

### L1 human

Near a fixed point, a smooth map looks like multiplication by its derivative there.
The theorem says that for holomorphic maps this is exactly true after a change of coordinates, as long as the derivative has size neither $0$ nor $1$.
In the new coordinate, iterating the map just means multiplying by $\lambda$ again and again.

### L2 human

The function $\varphi$ is called the Koenigs function of $f$ at the fixed point.
In the attracting case it extends to the whole basin of attraction, where it still satisfies $\varphi \circ f = \lambda \varphi$.
The cases left out lead to other theorems: Böttcher's theorem for $\lambda = 0$, the Leau–Fatou flower theorem for roots of unity, and Siegel and Brjuno's small divisor results for other $\abs{\lambda} = 1$.
