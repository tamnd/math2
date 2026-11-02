---
tag: PRC4WH5WYJ
kind: statement
role: theorem
name: Tian–Todorov theorem
msc: [32G05, 32Q25, 14J32]
uses: [X60JG9AEQJ, W05VYY4HBR, R0QABVGPRX, STYAB4PFDW]
about: [STYAB4PFDW, R0QABVGPRX]
sources:
  - url: https://en.wikipedia.org/wiki/Calabi%E2%80%93Yau_manifold
---

## Statement

Let $X$ be a compact [[Kähler manifold|X60JG9AEQJ]] of dimension $n$ whose [[canonical bundle|W05VYY4HBR]] $K_X$ is trivial.
Let $\Theta_X$ be the sheaf of holomorphic vector fields on $X$.
Then the deformations of $X$ are unobstructed: the base of the [[Kuranishi family|R0QABVGPRX]] of $X$ is smooth, of dimension $\dim_\C H^1(X, \Theta_X) = h^{n-1,1}(X)$.

## Remarks

The theorem is also called the Bogomolov–Tian–Todorov theorem: Bogomolov proved the case of hyperkähler manifolds, and Tian and Todorov proved the general case independently.
A nowhere vanishing holomorphic $n$-form $\Omega$ gives an isomorphism $\Theta_X \cong \Omega^{n-1}_X$, $v \mapsto \iota_v \Omega$, which explains the equality of dimensions.
Under this isomorphism the bracket of two vector-valued forms becomes $\partial$-exact (the Tian–Todorov lemma).
The $\partial\bar\partial$-lemma of compact Kähler manifolds then lets one solve the integrability equation $\bar\partial\varphi + \frac12[\varphi, \varphi] = 0$ order by order, so all obstructions vanish.

Example: a K3 surface $X$ has $n = 2$, $\Theta_X \cong \Omega^1_X$ and $h^{1,1}(X) = 20$, so its Kuranishi space is a smooth germ of dimension $20$.

The Kähler hypothesis is used through the $\partial\bar\partial$-lemma.
The Iwasawa manifold is a compact complex manifold with trivial canonical bundle that is not Kähler, and its deformations are obstructed.

## Explanations

### L1 human

Calabi–Yau manifolds are compact Kähler manifolds with a nowhere zero holomorphic volume form.
The theorem says that every first-order deformation of such a manifold extends to an actual family.
So their local moduli spaces are smooth, with a dimension computed from Hodge numbers.

### L2 human

In general the Kuranishi space is cut out by obstructions with values in $H^2(X, \Theta_X)$, and for some manifolds these obstructions are nonzero.
For Calabi–Yau manifolds $H^2(X, \Theta_X) \cong H^{n-1,2}(X)$ is usually nonzero, so the earlier existence theorem of Kodaira, Nirenberg and Spencer does not apply.
The theorem shows that the obstructions vanish anyway.
It is the starting point for the study of moduli of Calabi–Yau threefolds, of their period maps, and of mirror symmetry.
