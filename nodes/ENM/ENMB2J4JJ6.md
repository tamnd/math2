---
tag: ENMB2J4JJ6
kind: definition
name: Arithmetic genus
msc: [14H99, 14C40]
defines: H03GKRVBJ1
uses: [A4H4CZ2V35, PQ6Q143ARJ, RNDDWDAFJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetic_genus
---

## Definition

Let $k$ be a field and let $X$ be a [[projective|A4H4CZ2V35]] scheme over $k$ of dimension $n$.
Let
$$\chi(\mathcal{O}_X) = \sum_{i \ge 0} (-1)^i \dim_k H^i(X, \mathcal{O}_X)$$
be the [[Euler characteristic|RNDDWDAFJ5]] of its structure sheaf, computed with [[sheaf cohomology|PQ6Q143ARJ]].
The *arithmetic genus* of $X$ is
$$p_a(X) = (-1)^n \left( \chi(\mathcal{O}_X) - 1 \right).$$

## Remarks

The sum is finite because $X$ is projective, so each $H^i(X, \mathcal{O}_X)$ is finite-dimensional and vanishes for $i > n$.
Equivalently, $p_a(X) = (-1)^n (P_X(0) - 1)$, where $P_X$ is the Hilbert polynomial of $X$ for a chosen embedding.
For a curve $C$ with $H^0(C, \mathcal{O}_C) = k$, for example a connected reduced projective curve over an algebraically closed field, $p_a(C) = \dim_k H^1(C, \mathcal{O}_C)$.
Example: $H^1(\mathbb{P}^1, \mathcal{O}) = 0$, so $p_a(\mathbb{P}^1) = 0$.
Example: a plane cubic curve, smooth or nodal, has $p_a = 1$; this follows from the exact sequence $0 \to \mathcal{O}_{\mathbb{P}^2}(-3) \to \mathcal{O}_{\mathbb{P}^2} \to \mathcal{O}_C \to 0$.
Non-example: the affine line $\mathbb{A}^1$ is not projective, and $H^0(\mathbb{A}^1, \mathcal{O}) = k[t]$ is infinite-dimensional, so $\chi$ is not defined.
