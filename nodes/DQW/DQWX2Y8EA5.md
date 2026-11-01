---
tag: DQWX2Y8EA5
kind: definition
name: Trace form
msc: [12F10, "11E04", 11R29]
defines: YWX2R53ED6
uses: [0NRYPM9Y27, 73XV4RP5PT, 0744CN4MDA, 0KAN330PAH]
sources:
  - url: https://en.wikipedia.org/wiki/Field_trace
---

## Definition

Let $L/K$ be a [[finite extension|0NRYPM9Y27]] and let $\mathrm{Tr}_{L/K}$ be the [[field trace|73XV4RP5PT]].
The *trace form* of $L/K$ is the map
$$B \colon L \times L \to K, \qquad B(x, y) = \mathrm{Tr}_{L/K}(xy).$$

## Remarks

Since $\mathrm{Tr}_{L/K}$ is $K$-linear and multiplication is commutative and distributive, $B$ is a [[symmetric bilinear form|0744CN4MDA]] on the $K$-vector space $L$.
It is [[nondegenerate|0KAN330PAH]] if and only if $L/K$ is separable.
Its quadratic form is $x \mapsto \mathrm{Tr}_{L/K}(x^2)$.

Example: $L = \Q(i)$ over $K = \Q$.
Check: $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$, so $B(a + bi, c + di) = 2(ac - bd)$; in the basis $1, i$ the matrix of $B$ is $\begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}$, which is invertible.

Non-example of nondegeneracy: let $K = \F_p(t)$ and $L = K(s)$ with $s^p = t$.
The trace of every element of $L$ is $0$, so the trace form of $L/K$ is identically zero and degenerate, as expected for an inseparable extension.
