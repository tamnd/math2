---
tag: 0BR3FY5Q8M
kind: concept
name: Quotient space
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
specializes: [000AYPA9AJ]
uses: [000AYPA9AJ, 00YC1D652K]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 3E
  - book: isbn:9780134860244
    locator: Section 1.3
same_as:
  wikidata: Q1393796
  wikipedia: Quotient space (linear algebra)
---

## Summary

Let $U$ be a [[subspace|00YC1D652K]] of a [[vector space|000AYPA9AJ]] $V$.
The *quotient space* $V / U$ is the set of cosets $v + U = \{v + u : u \in U\}$, with the operations $(v + U) + (w + U) = (v + w) + U$ and $a(v + U) = av + U$.
Two vectors give the same coset exactly when their difference lies in $U$.
So $V / U$ is the space $V$ in which the vectors of $U$ are treated as zero.

## Motivation

Often we want to ignore some information in a vector.
For a linear map $f$, the vectors $v$ and $v + k$ with $k \in \ker f$ have the same image, so $f$ cannot tell them apart.
For an integral, two functions that differ by a constant have the same derivative.
The quotient $V / U$ is the space in which differences in $U$ are ignored, and it is again a vector space.
This makes it the right home for the [[first isomorphism theorem|0MTBGVZ4XJ]], where $V / \ker f$ becomes isomorphic to the image of $f$.

## Notation

We write $V / U$, read "$V$ modulo $U$", and $v + U$ or $[v]$ or $\bar v$ for the coset of $v$.
The [[quotient map|0N4F5FMQZW]] $\pi \colon V \to V / U$ sends $v$ to $v + U$.
Mathlib writes `V ⧸ U` with the special slash `⧸`, and `Submodule.mkQ U` for the quotient map.

## Remarks

### Examples

- [[The plane modulo a line|PEPJFPPRDK]]: $\R^2 / \R(1, 1)$ is the set of lines $x - y = c$, and it is isomorphic to $\R$.
- [[Polynomials modulo multiples of x²|PHA4SATHWE]]: $\R[x] / x^2 \R[x]$ has the basis $1 + U$, $x + U$, so it has dimension $2$.
- $V / \{0\}$ is isomorphic to $V$, and $V / V$ is the zero space.
- If $V = U \oplus W$, then $V / U \cong W$, by the [[theorem on complements and quotients|244KTXDJHW]].
- Functions modulo constants: on the space of differentiable functions, the derivative $f \mapsto f'$ factors through the quotient by the constant functions.

### Non-examples

- [[A quotient by a line not through the origin|E3MQ50YQNR]] is not defined: the rule "$u \sim v$ when $u - v \in S$" is not an equivalence relation when $S$ is not a subspace.
- A coset $v + U$ with $v \notin U$ is not a subspace of $V$, since it does not contain $0$. The elements of $V / U$ are cosets, and $V / U$ is not a subspace of $V$.

### Basic properties

- The [[operations on cosets are well defined|YYH67TQ9GV]], $V / U$ is a vector space with zero $0 + U = U$, and the quotient map is linear and surjective with kernel $U$.
- The [[dimension of a quotient|0SXDQ6TN00]]: if $V$ is finite-dimensional, then $\dim(V / U) = \dim V - \dim U$.
- The [[universal property|0ZERJX6PH6]]: a linear map $f \colon V \to X$ with $U \subseteq \ker f$ factors uniquely as $f = \bar f \circ \pi$.
- The [[isomorphism theorems|0MTBGVZ4XJ]]: $V / \ker f \cong \operatorname{im} f$, $(U + W)/W \cong U / (U \cap W)$, and $(V / W)/(U / W) \cong V / U$.
- The subspaces of $V / U$ correspond to the subspaces of $V$ that contain $U$, by the [[correspondence theorem|GCHY414Y11]].

### History

Quotients first appeared for groups: Galois and Jordan studied quotients by normal subgroups in the nineteenth century.
Dedekind formed quotients of rings by ideals, and the notion for modules and vector spaces became standard with Noether's abstract algebra in the 1920s.
Quotient spaces of normed spaces, such as $L^p$ spaces as functions modulo null functions, became central in functional analysis.

### Common errors

- Forgetting that a coset has many representatives. A rule on $V / U$ given by a formula in $v$ must give the same result for $v$ and $v + u$.
- Thinking that $V / U$ is a subspace of $V$. It is a new space, isomorphic to a complement of $U$ but not equal to one.
- Writing $\dim(V / U) = \dim V - \dim U$ in infinite dimension. For $V = \R[x]$ and $U = x^2 \R[x]$, both $\dim V$ and $\dim U$ are infinite, while $\dim(V / U) = 2$.

## Explanations

### L1 human

The quotient $V / U$ is what you see when you stop paying attention to the directions in $U$.
In the plane with $U$ the $x$-axis, two points look the same when they have the same height.
So each horizontal line becomes a single point of the quotient, and the quotient looks like a line of heights.

### L2 human

Let $V = \R^3$ and $U$ the $z$-axis.

1. The coset of $(1, 2, 3)$ is $\{(1, 2, t) : t \in \R\}$, the vertical line through $(1, 2, 0)$.
2. $(1, 2, 3) + U = (1, 2, -5) + U$, since the difference $(0, 0, 8)$ lies in $U$.
3. $((1, 2, 3) + U) + ((0, 1, 7) + U) = (1, 3, 10) + U = (1, 3, 0) + U$.
4. The map $(x, y, z) + U \mapsto (x, y)$ is an isomorphism $V / U \cong \R^2$.

The trap is to work with a chosen representative and forget to check that the result does not depend on the choice.

### L3 human

The quotient $V / U$ is the cokernel of the inclusion $U \to V$.
It is characterized by its [[universal property|0ZERJX6PH6]], which is the dual of the property of the kernel.
In categorical terms, $0 \to U \to V \to V / U \to 0$ is a short exact sequence, and every short exact sequence of vector spaces has this form up to isomorphism.
Quotient spaces are essential in infinite dimension, for example in the definition of $L^p$ spaces, of the Calkin algebra $B(H)/K(H)$, and of homology groups $\ker \partial / \operatorname{im} \partial$.
