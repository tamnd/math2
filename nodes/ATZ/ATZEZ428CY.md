---
tag: ATZEZ428CY
kind: statement
role: theorem
name: Edge-of-the-wedge theorem
msc: [32D15, 32A40]
uses: [507C34W0ZT, 6VE4KA12VD, 02BH3MCBQB]
about: [507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Edge-of-the-wedge_theorem
same_as:
  wikidata: Q4454925
  wikipedia: Edge-of-the-wedge theorem
---

## Statement

Let $C \subseteq \R^n$ be a nonempty open [[convex cone|6VE4KA12VD]] with vertex $0$, let $E \subseteq \R^n$ be a nonempty [[open set|02BH3MCBQB]], and let $\delta > 0$.
Write $\R^n \subseteq \C^n$ as the set of points with zero imaginary part, and define the two wedges
$$W_\pm = \set{x + iy \in \C^n : x \in E, \ \pm y \in C, \ \abs{y} < \delta}.$$
Let $f_+$ and $f_-$ be [[holomorphic functions|507C34W0ZT]] on $W_+$ and $W_-$.
Suppose that $f_+$ extends continuously to $W_+ \cup E$, that $f_-$ extends continuously to $W_- \cup E$, and that the two extensions agree on $E$.
Then there are an open set $G \subseteq \C^n$ with $E \subseteq G$ and a holomorphic function $F$ on $G$ such that $F = f_+$ on $G \cap W_+$ and $F = f_-$ on $G \cap W_-$.

## Remarks

For $n = 1$ the wedges are a rectangle above and a rectangle below the interval $E$.
Then the theorem follows from Morera's theorem: the glued function is continuous, and its integrals over small triangles vanish.
In several variables the edge $E$ has only real dimension $n$ inside $\C^n$, and a direct Morera argument is not available.
Proofs use Cauchy integrals over suitable families of analytic discs, or Fourier analysis.
The theorem also holds when the continuity hypothesis is replaced by the condition that $f_+$ and $f_-$ have the same boundary value on $E$ in the sense of distributions.

The agreement on $E$ is necessary: $f_+ = 0$ and $f_- = 1$ satisfy all other hypotheses but cannot be glued to one holomorphic function.

## Explanations

### L1 human

Take two wedge-shaped regions of $\C^n$ that meet only along a common real edge.
Suppose a holomorphic function on each wedge has boundary values on the edge, and the two sets of boundary values agree.
Then the two functions are pieces of a single holomorphic function on a full neighbourhood of the edge.
The edge acts like a seam that disappears once the two sides match.

### L2 human

In one variable this is the familiar gluing of holomorphic functions across a real interval.
In several variables it is surprising, because the edge has only half the real dimension of the space, yet it still suffices for gluing.
The theorem arose in quantum field theory, where it is used to prove analyticity properties of correlation functions.
It is also a basic tool in the theory of hyperfunctions, where generalised functions on $\R^n$ are represented by boundary values of holomorphic functions on wedges.
