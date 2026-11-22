---
tag: 0W4FSW1TVB
kind: statement
role: theorem
name: Rank-nullity theorem
aliases: [dimension-theorem-for-linear-maps]
msc: ["15A03", "15A04"]
topics: [9080WQTZ3M]
audience: ug1
about: [0ZZXSBTR4J, 0APCFW7639]
uses: [0JGB7A6GTS, 00K4FK4NBH, 0RJF668P1T, 018W3V3TCT]
formal:
  - system: lean4
    library: mathlib
    decl: LinearMap.finrank_range_add_finrank_ker
    match: stronger
sources:
  - url: https://en.wikipedia.org/wiki/Rank–nullity_theorem
    locator: Stating the theorem
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Kernel, image and the rank–nullity theorem
  - book: isbn:9783031410253
    locator: Chapter 3
  - book: isbn:9780134860244
    locator: Section 2.1
same_as:
  wikidata: Q303402
  wikipedia: Rank–nullity theorem
---

## Statement

Each dimension of the source of a linear map either survives in the image or is lost in the kernel, so the two dimensions add up to the dimension of the source.

Let $F$ be a field, let $V$ be a [[finite-dimensional|018W3V3TCT]] vector space over $F$, let $W$ be a vector space over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].
Then $\im T$ and $\ker T$ are finite-dimensional, and
$$\dim \im T + \dim \ker T = \dim V.$$
That is, $\rank T + \operatorname{nullity} T = \dim V$, with the [[rank|0JGB7A6GTS]] and the [[nullity|00K4FK4NBH]] of $T$.

## Remarks

### Why the hypotheses are needed

The source $V$ must be finite-dimensional for an equation of numbers, while $W$ may have any dimension, since only the image matters.
The right side is $\dim V$, not $\dim W$.
For the inclusion $\R \to \R^2$, rank plus nullity is $1 + 0 = 1 = \dim \R$, while $\dim \R^2 = 2$.
Linearity is needed as well.
The map $x \mapsto x^3 - x$ on $\R$ has zero set $\{-1, 0, 1\}$ and image $\R$, and neither the zero set nor the image of a non-linear map need be a subspace.

### What it gives you

If $\dim V > \dim W$, then $T$ is not injective, so a homogeneous system with more unknowns than equations has a nonzero solution.
If $\dim V < \dim W$, then $T$ is not surjective.
If $\dim V = \dim W$ is finite, then $T$ is injective exactly when it is surjective, by the [[theorem on endomorphisms|0912EEEVCT]].
For an $m \times n$ matrix $A$, the [[rank-nullity theorem for matrices|TR48YQGCCA]] reads $\rank A + \dim \operatorname{Nul} A = n$.
For a nonzero linear form $f$ on $V$, the image is $F$, so the kernel is a hyperplane with $\dim \ker f = \dim V - 1$.

### The converse

Every split allowed by the theorem occurs.
For $n = \dim V$ and each $r \le \min(n, \dim W)$, there is a linear map of rank $r$ and nullity $n - r$.
Send $r$ basis vectors of $V$ to independent vectors of $W$ and the others to $0$, by the [[theorem on bases|0R8X9XA83A]].

### Infinite dimension

For any linear map $T \colon V \to W$, there is a subspace $U$ with $V = \ker T \oplus U$ and $U \cong \im T$.
So $\dim V = \dim \ker T + \dim \im T$ holds as an equation of cardinals.
In this form the equation cannot be solved for one term.
The [[right shift|N1G1WQW59J]] on sequences has nullity $0$, and its image has the same infinite dimension as the whole space, but the shift is not surjective.

### Generalizations

The [[first isomorphism theorem|0MTBGVZ4XJ]] $V / \ker T \cong \im T$ is the form of the theorem without dimensions.
For an exact sequence $0 \to V_1 \to \dots \to V_k \to 0$ of finite-dimensional spaces, the alternating sum of the dimensions is $0$.
Rank-nullity is the case of the sequence $0 \to \ker T \to V \to \im T \to 0$.
Mathlib states the theorem for modules over a division ring, which covers every field.

## History

The matrix form belongs to the 19th-century theory of linear systems, where the number of free unknowns is $n$ minus the rank.
Sylvester's law of nullity of 1884 is a related statement about the nullity of a product of matrices.

## Explanations

### L1 human

Each dimension of the source either survives in the image or is crushed into the kernel.
So the dimensions of the image and the kernel add up to the dimension of the source.
A map from $\R^5$ to $\R^3$ has rank at most $3$, so its kernel has dimension at least $2$.

### L2 human

The theorem is a counting tool.
Take the map $T \colon \R^4 \to \R^2$ with matrix $\begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \end{pmatrix}$.

1. The first two columns are $e_1$ and $e_2$, so the image is $\R^2$ and the rank is $2$.
2. Rank-nullity gives nullity $4 - 2 = 2$, without solving any system.
3. Check: $(1, 0, -1, 0)$ and $(0, 1, 0, -1)$ are independent vectors in the kernel.

Watch out: the formula uses $\dim V$, the dimension of the source, not $\dim W$.

### L3 human

Rank-nullity follows from the fact that every short exact sequence of vector spaces splits.
For modules over a ring, sequences need not split, but additive invariants such as length still satisfy the same equation for modules of finite length.
Over a field, the theorem is equivalent to the [[dimension formula for quotients|0SXDQ6TN00]], through the first isomorphism theorem.
