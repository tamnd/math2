---
tag: FXT3N6QMEX
kind: definition
name: Normal coordinates
msc: [53B20, 53C22]
defines: RRHKMGNKG9
uses: [7CBT4SM83Y, Y7Z0AGY1A7, 0FWJ0VW561, 0KZZ70ZHXP]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_coordinates
---

## Definition

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] of dimension $n$ and $p \in M$.
Let $V \subseteq T_pM$ be an open neighbourhood of $0$, star-shaped about $0$.
Assume that the [[exponential map|Y7Z0AGY1A7]] $\exp_p$ restricts to a [[diffeomorphism|0KZZ70ZHXP]] from $V$ onto an open set $U \subseteq M$.
Let $(e_1, \ldots, e_n)$ be an [[orthonormal basis|0FWJ0VW561]] of $T_pM$ for $g_p$, and let $E \colon \R^n \to T_pM$ be $E(x) = \sum_i x^i e_i$.
The *normal coordinates* centred at $p$ are the chart
$$\varphi = E^{-1} \circ (\exp_p|_V)^{-1} \colon U \to \R^n.$$

## Remarks

Example: in $\R^n$ with the Euclidean metric and the standard basis, $\exp_p(v) = p + v$, so the normal coordinates centred at $p$ are $\varphi(q) = q - p$, defined on all of $\R^n$.

Non-example: in $\R^2$ with the Euclidean metric, the chart $\psi(q) = 2(q - p)$ has the form $E^{-1} \circ \exp_p^{-1}$ only for the basis $e_i = \tfrac{1}{2} \varepsilon_i$, where $\varepsilon_1, \varepsilon_2$ is the standard basis.
This basis is orthogonal but not orthonormal, so $\psi$ is not a normal coordinate chart; indeed, in $\psi$ the metric has matrix $\tfrac{1}{4} I$ at $p$, not $I$.

In normal coordinates centred at $p$: $g_{ij}(p) = \delta_{ij}$, $\partial_k g_{ij}(p) = 0$ and $\Gamma^k_{ij}(p) = 0$.
The geodesics through $p$ are the lines $t \mapsto t x$ in these coordinates.
Different orthonormal bases give normal coordinates that differ by an orthogonal matrix.
