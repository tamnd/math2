---
tag: 0VDD7W0EKZ
kind: statement
role: theorem
name: Morera's theorem
aliases: [moreras-theorem]
msc: ["30E20"]
uses: [0DG0Z72CQD, 00FWNP9TXY, 02AC7JR6G6]
sources:
  - url: https://en.wikipedia.org/wiki/Morera%27s_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Morera%27s_theorem
    locator: Weakening of hypotheses
same_as:
  wikidata: Q1140119
  wikipedia: Morera's theorem
---

## Statement

Let $U \subseteq \mathbb{C}$ be an open set and let $f : U \to \mathbb{C}$ be continuous.
Assume that $\oint_{\partial T} f(z) \, dz = 0$ for each closed triangle $T \subseteq U$, where $\partial T$ is the boundary of $T$ traveled once and the integral is a [[contour integral|00FWNP9TXY]].
Then $f$ is [[holomorphic|0DG0Z72CQD]] on $U$.

## Remarks

It is enough to know that $\oint_\gamma f(z) \, dz = 0$ for each closed piecewise continuously differentiable path $\gamma$ in $U$, because the boundary of a triangle is such a path.
Proof idea: on each disc in $U$, $F(z) = \int_{[c, z]} f(w) \, dw$ is a primitive of $f$. So $F$ is holomorphic, and $f = F'$ is holomorphic because [[derivatives of holomorphic functions are holomorphic|0QEBN8DGVE]].
Together with [[Goursat's theorem|0BRG85WXYC]], this shows: a continuous $f$ is holomorphic on $U$ if and only if its integrals over all triangles in $U$ are zero.
A main use is the theorem on [[uniform limits of holomorphic functions|0431RN0R1N]].

## Explanations

### L1 human

Morera's theorem is a converse of Cauchy's theorem.
If the integral of a continuous function around each small triangle is zero, then the function is holomorphic.
