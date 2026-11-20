---
tag: 0ZJM9D7NPS
kind: statement
role: theorem
name: Canonical isomorphism with the double dual
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug2
about: [07JBSZE0V4]
uses: [0M856Q1AMZ, 00889YD15K, 018W3V3TCT, 0RJF668P1T]
formal:
  - system: lean4
    library: mathlib
    decl: Module.evalEquiv
    match: weaker
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Injection into the double-dual
  - book: isbn:9783031410253
    locator: Section 3F
  - book: isbn:9780134860244
    locator: Section 2.6
---

## Statement

Let $F$ be a field and let $V$ be a vector space over $F$, of any dimension.
Let $V^{**} = (V^*)^*$ be the dual of the [[dual space|0M856Q1AMZ]] $V^*$.
The *evaluation map* $\operatorname{ev}_V \colon V \to V^{**}$ is defined by
$$\operatorname{ev}_V(v)(f) = f(v) \qquad (v \in V,\ f \in V^*).$$

1. $\operatorname{ev}_V(v)$ is a linear form on $V^*$, and $\operatorname{ev}_V$ is a [[linear map|0RJF668P1T]].
2. $\operatorname{ev}_V$ is injective.
3. $\operatorname{ev}_V$ is an isomorphism if and only if $V$ is [[finite-dimensional|018W3V3TCT]].

## Remarks

### Why each hypothesis is needed

- In part 3, finite dimension is needed. For $V = F^{(\N)}$, the form on $V^*$ that is $0$ on all coordinate forms and $1$ on the sum of coordinates is not an evaluation; see the proof.
- In part 2, the scalars must form a field, or at least each nonzero vector must be detected by some form. For the $\Z$-module $\Z/2\Z$, every $\Z$-linear form to $\Z$ is $0$, so the evaluation map $\Z/2\Z \to (\Z/2\Z)^{**} = 0$ is not injective.

### Consequences

- In finite dimension, each element of $V^{**}$ is $\operatorname{ev}_V(v)$ for exactly one $v$. So $V$ may be treated as the dual of $V^*$, and the roles of $V$ and $V^*$ are symmetric.
- If $V$ is finite-dimensional and $\varphi_1, \dots, \varphi_n$ is a basis of $V^*$, then there is a unique basis $v_1, \dots, v_n$ of $V$ whose dual basis is $\varphi_1, \dots, \varphi_n$. Take $v_i = \operatorname{ev}_V^{-1}(\varphi_i^*)$.
- The dual basis of a dual basis $b_1^*, \dots, b_n^*$ is $\operatorname{ev}_V(b_1), \dots, \operatorname{ev}_V(b_n)$, since $\operatorname{ev}_V(b_j)(b_i^*) = b_i^*(b_j) = \delta_{ij}$.
- The map is natural: for each linear map $f \colon V \to W$, we have $f^{**} \circ \operatorname{ev}_V = \operatorname{ev}_W \circ f$, by the [[naturality lemma|~f17af3fe]]. The [[example of the canonical evaluation map|J3X26BSQEY]] discusses why it is called canonical.

### Converse

If $\operatorname{ev}_V$ is surjective, then $V$ is finite-dimensional; this is the "only if" of part 3.
The [[Erdős-Kaplansky theorem|~ecdd288b]] gives a second proof: for infinite-dimensional $V$, $\dim V^{**} > \dim V^* > \dim V$.

### Generalizations

- For a finitely generated free module over a commutative ring, the evaluation map is an isomorphism. Mathlib states this as `Module.evalEquiv`, which does not cover the injectivity in infinite dimension.
- For normed spaces, the evaluation map into the continuous bidual is an isometric embedding, by the Hahn-Banach theorem. Spaces where it is onto are called reflexive. This belongs to functional analysis; see the [[continuous dual space|4A82S5FVRT]].
- In the language of category theory, $\operatorname{ev}$ is a natural transformation from the identity functor to the double dual functor; see [[natural transformation|KYCPCC57FT]].

## History

The term "natural" for maps such as $V \to V^{**}$ was the starting point of category theory.
Eilenberg and Mac Lane used this example in 1945 to explain what a natural transformation is.

## Explanations

### L1 human

A vector $v$ can act on linear forms: it sends each form $f$ to the number $f(v)$.
This turns each vector into an element of the double dual.
Different vectors give different elements.
In finite dimension, every element of the double dual comes from exactly one vector in this way.

### L2 human

We compute the evaluation map on $V = \R^2$ in coordinates.

1. A basis of $V^*$ is $e_1^* = x$, $e_2^* = y$. A form on $V^*$ is fixed by its values on $e_1^*$ and $e_2^*$.
2. Take $v = (3, -1)$. Then $\operatorname{ev}(v)(e_1^*) = 3$ and $\operatorname{ev}(v)(e_2^*) = -1$.
3. For the form $f = 2x + 5y$, linearity gives $\operatorname{ev}(v)(f) = 2 \cdot 3 + 5 \cdot (-1) = 1$, and directly $f(3, -1) = 6 - 5 = 1$.
4. Conversely, let $\Phi \in V^{**}$ with $\Phi(x) = 4$ and $\Phi(y) = 7$. Then $\Phi = \operatorname{ev}(4, 7)$, since both agree on a basis of $V^*$.

The typical use is to identify $V$ with $V^{**}$ in finite dimension, with no choice of basis.
A trap: this does not give a preferred isomorphism $V \to V^*$; only $V \to V^{**}$ is canonical.

### L3 human

The evaluation maps make the double dual functor naturally isomorphic to the identity functor on finite-dimensional spaces.
No natural isomorphism $V \to V^*$ exists, because the dual is contravariant and the identity is covariant.
For infinite-dimensional $V$, the double dual is a much larger space, and $\operatorname{ev}_V(V)$ is a proper subspace.
In functional analysis, the analogous question for the continuous bidual leads to the notion of a reflexive space.
