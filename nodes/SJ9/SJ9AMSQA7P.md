---
tag: SJ9AMSQA7P
kind: definition
name: Homology sphere
msc: [57N65, 57K30]
defines: HK8NS02NNE
uses: [QQQ9B1DK4P, M0Q5CFJ7ZH, T62369RFH6]
sources:
  - url: https://en.wikipedia.org/wiki/Homology_sphere
---

## Definition

Let $n \ge 1$ be an integer.
A *homology $n$-sphere* is a closed (compact, without boundary) [[topological $n$-manifold|QQQ9B1DK4P]] $X$ whose integral [[singular homology|M0Q5CFJ7ZH]] is that of the [[$n$-sphere|T62369RFH6]]:
$$H_i(X; \Z) \cong \begin{cases} \Z & \text{if } i = 0 \text{ or } i = n, \\ 0 & \text{otherwise.} \end{cases}$$

## Remarks

The condition $H_0(X; \Z) \cong \Z$ says that $X$ is connected, and $H_n(X; \Z) \cong \Z$ says that $X$ is orientable.

Example: the Poincaré homology sphere $P = S^3 / I^\ast$, where $I^\ast \subset S^3$ is the binary icosahedral group of order $120$ acting by left multiplication.
Its fundamental group $I^\ast$ is perfect, so $H_1(P; \Z)$, the abelianisation of $I^\ast$, is $0$; Poincaré duality and the universal coefficient theorem then give $H_2(P; \Z) = 0$ and $H_3(P; \Z) \cong \Z$.

Non-example: the lens space $L(p, q)$ with $p \ge 2$ is a closed orientable $3$-manifold, but $H_1(L(p, q); \Z) \cong \Z/p \neq 0$.

A simply connected homology $n$-sphere is homotopy equivalent to $S^n$, by the Hurewicz and Whitehead theorems.
