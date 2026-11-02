---
tag: JV4H0R6GZM
kind: definition
name: Local trivialization
msc: [55R10, 57R22]
defines: JTCQT4NQ79
uses: [0CQHFPGJ45, 0X3WGX95FE, 0QT00PB5G2, 0GBG8B49AA]
sources:
  - url: https://en.wikipedia.org/wiki/Fiber_bundle
---

## Definition

Let $E$, $B$ and $F$ be [[topological spaces|0CQHFPGJ45]] and let $\pi \colon E \to B$ be a [[continuous map|0X3WGX95FE]].
Let $U$ be an open subset of $B$, and give $U \times F$ the [[product topology|0GBG8B49AA]].
A *local trivialization* of $\pi$ over $U$ with fiber $F$ is a [[homeomorphism|0QT00PB5G2]]
$$\varphi \colon \pi^{-1}(U) \to U \times F$$
such that $\operatorname{pr}_1 \circ \varphi = \pi$ on $\pi^{-1}(U)$, where $\operatorname{pr}_1 \colon U \times F \to U$ is the first projection.

## Remarks

Example: let $E = \R \times S^1$, $B = S^1$ and $\pi(s, z) = z$.
Then $\varphi(s, z) = (z, s)$ over $U = S^1$ is a local trivialization with fiber $\R$, since it is a homeomorphism and its first coordinate is $\pi(s, z) = z$.

Non-example: for the double cover $\pi \colon S^1 \to S^1$, $\pi(z) = z^2$, there is no local trivialization over $U = S^1$ with fiber a two-point space, since $\pi^{-1}(S^1) = S^1$ is connected and $S^1 \times F$ is not.
Over each proper open arc, however, such a trivialization exists.

The map $\pi$ is a [[fiber bundle|CX4M8K61AB]] with fiber $F$ exactly when the open sets carrying a local trivialization cover $B$.
If $\varphi_U$ and $\varphi_V$ are local trivializations, then $\varphi_U \circ \varphi_V^{-1}$ on $(U \cap V) \times F$ has the form $(b, f) \mapsto (b, g_{UV}(b)(f))$, and the maps $g_{UV}$ are the transition functions.
