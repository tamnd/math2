---
tag: PKS8JE1PW1
kind: statement
role: theorem
name: Atiyah–Bott fixed-point theorem
msc: [58J20, 58J10, 58C30]
uses: [F45VQ47GPV, P4DZM975BV, M8GMH8GQR6, ZSYCA4EGEZ]
about: [M8GMH8GQR6, ZSYCA4EGEZ]
sources:
  - url: https://en.wikipedia.org/wiki/Atiyah–Bott_fixed-point_theorem
same_as:
  wikidata: Q755986
  wikipedia: Atiyah–Bott fixed-point theorem
---

## Statement

Let $X$ be a compact [[smooth manifold|F45VQ47GPV]] without boundary.
Let
$$0 \to \Gamma(E_0) \xrightarrow{d_0} \Gamma(E_1) \xrightarrow{d_1} \cdots \xrightarrow{d_{n-1}} \Gamma(E_n) \to 0$$
be an [[elliptic complex|M8GMH8GQR6]] of smooth sections of [[vector bundles|P4DZM975BV]] $E_i$ over $X$, with cohomology groups $H^i$.
Let $f \colon X \to X$ be a smooth map whose fixed points are all simple, that is, $\det(1 - df_x) \ne 0$ at each fixed point $x$.
For each $i$ let $\varphi_i \colon f^* E_i \to E_i$ be a smooth bundle map, and let $T_i \colon \Gamma(E_i) \to \Gamma(E_i)$ be $T_i s = \varphi_i(s \circ f)$.
Assume $d_i T_i = T_{i+1} d_i$ for all $i$, so that the $T_i$ induce linear maps $H^i(T) \colon H^i \to H^i$.
Then the [[Lefschetz number|ZSYCA4EGEZ]] $L(T) = \sum_i (-1)^i \tr H^i(T)$ satisfies
$$L(T) = \sum_{x \,:\, f(x) = x} \frac{\sum_i (-1)^i \tr \varphi_{i,x}}{\abs{\det(1 - df_x)}},$$
where $\varphi_{i,x} \colon (E_i)_{f(x)} = (E_i)_x \to (E_i)_x$ is the map on the fibre at the fixed point $x$.

## Remarks

The cohomology groups are finite-dimensional because the complex is elliptic, and the fixed points are finitely many because simple fixed points are isolated and $X$ is compact.
The idea of the proof is to write $L(T)$ as an alternating sum of traces of operators of the form $T_i e^{-t \Delta_i}$, where $\Delta_i$ are the Laplacians of the complex.
These traces are integrals of a kernel over the graph of $f$ restricted to the diagonal, and the transversality condition $\det(1 - df_x) \ne 0$ localizes the integral at the fixed points as $t \to 0$.

For the de Rham complex with $\varphi_i = \Lambda^i (df)^*$, the numerator at $x$ is $\det(1 - df_x)$, so each fixed point contributes $\sgn \det(1 - df_x) = \pm 1$.
This recovers the [[Lefschetz fixed-point theorem|G44NQXCWT9]] for maps with simple fixed points.
For the Dolbeault complex of a compact complex manifold and a holomorphic map $f$, it gives the holomorphic Lefschetz formula
$$\sum_q (-1)^q \tr\big(f^* \mid H^{0,q}(X)\big) = \sum_{f(x) = x} \frac{1}{\det_\C(1 - \partial f_x)}.$$

The hypothesis that the fixed points are simple cannot be dropped from the formula as stated.
For the identity map every point is fixed, and the right side is not defined.

## Explanations

### L1 human

The classical Lefschetz theorem counts fixed points of a map with signs and says the count equals a trace computed from cohomology.
Atiyah and Bott replaced the de Rham cohomology by the cohomology of any elliptic complex.
The global side is still a trace on cohomology.
The local side is a sum over the fixed points, where each point contributes a number read off from the derivative of the map at that point.

### L2 human

The theorem is a fixed-point counterpart of the Atiyah–Singer index theorem: for $f = \id$ and no fixed-point condition, $L(T)$ would be the index of the complex.
Applied to the Dolbeault complex, it computes traces of group elements on holomorphic cohomology, which leads to the Weyl character formula for compact Lie groups acting on flag manifolds.
Applied to the spin complex and the signature complex, it gives fixed-point formulas for the $\hat{A}$-genus and the signature.
