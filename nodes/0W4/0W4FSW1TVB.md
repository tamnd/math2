---
tag: 0W4FSW1TVB
kind: statement
role: theorem
name: Rank–nullity theorem
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

Let $F$ be a field, let $V$ be a [[finite-dimensional|018W3V3TCT]] vector space over $F$, and let $W$ be a vector space over $F$.
Let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].
Then $\im T$ and $\ker T$ are finite-dimensional, and
$$\dim \im T + \dim \ker T = \dim V.$$
That is, $\rank T + \operatorname{nullity} T = \dim V$, with the [[rank|0JGB7A6GTS]] and the [[nullity|00K4FK4NBH]] of $T$.

## Remarks

### Why each hypothesis is needed

- $V$ must be finite-dimensional for the equation of numbers. $W$ may have any dimension, since only the image matters.
- The two sides involve $\dim V$, not $\dim W$. For the inclusion $\R \to \R^2$, rank plus nullity is $1 + 0 = 1 = \dim \R$, but $\dim \R^2 = 2$.
- Linearity is needed. The map $x \mapsto x^3 - x$ on $\R$ has the zero set $\{-1, 0, 1\}$ and image $\R$. For non-linear maps, the zero set and the image are not subspaces and have no such relation.

### Consequences

- If $\dim V > \dim W$, then $T$ is not injective. So a homogeneous system with more unknowns than equations has a nonzero solution.
- If $\dim V < \dim W$, then $T$ is not surjective.
- If $\dim V = \dim W$ is finite, then $T$ is injective if and only if it is surjective, by the [[theorem on endomorphisms|0912EEEVCT]].
- For an $m \times n$ matrix $A$, $\rank A + \dim \operatorname{Nul} A = n$, the [[rank-nullity theorem for matrices|TR48YQGCCA]].
- For a linear form $f \ne 0$ on $V$, the kernel is a hyperplane: $\dim \ker f = \dim V - 1$.

### Converse

For given $n = \dim V$ and $r \le \min(n, \dim W)$, there is a linear map of rank $r$ and nullity $n - r$.
Send $r$ basis vectors of $V$ to independent vectors of $W$ and the others to $0$, by the [[theorem on bases|0R8X9XA83A]].

### Generalizations

- Infinite-dimensional form. For any vector spaces $V$ and $W$ and a linear map $T \colon V \to W$, there is a subspace $U$ with $V = \ker T \oplus U$ and $U \cong \im T$. So $\dim V = \dim \ker T + \dim \im T$ as cardinal numbers.
- In the infinite case the equation cannot be solved for one term. The [[right shift|N1G1WQW59J]] on sequences has nullity $0$ and image of the same infinite dimension as $V$, but it is not surjective.
- The [[first isomorphism theorem|0MTBGVZ4XJ]] $V / \ker T \cong \im T$ is the form of the theorem without dimensions.
- For an exact sequence $0 \to V_1 \to \dots \to V_k \to 0$ of finite-dimensional spaces, the alternating sum of the dimensions is $0$. Rank-nullity is the case of $0 \to \ker T \to V \to \im T \to 0$.
- Mathlib states the theorem for modules over a division ring, which is more general than a field.

## History

The matrix form is part of the 19th-century theory of linear systems: the number of free unknowns is $n$ minus the rank.
Sylvester's law of nullity of 1884 is a related statement about the nullity of a product of matrices.

## Explanations

### L1 human

Each dimension of the source either survives in the image or is crushed into the kernel.
So the dimensions of the image and the kernel add up to the dimension of the source.
A map from $\R^5$ to $\R^3$ has rank at most $3$, so its kernel has dimension at least $2$.

### L2 human

The theorem is a counting tool.
For the map $T \colon \R^4 \to \R^2$ with matrix $\begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \end{pmatrix}$:

1. The first two columns are $e_1$ and $e_2$, so the image is $\R^2$ and the rank is $2$.
2. Rank-nullity gives nullity $4 - 2 = 2$, without solving any system.
3. Check: $(1, 0, -1, 0)$ and $(0, 1, 0, -1)$ are independent vectors in the kernel.

The trap is to use $\dim W$ in place of $\dim V$.

### L3 human

Rank-nullity is the statement that every short exact sequence of vector spaces splits.
For modules over a ring, sequences need not split, but additive invariants such as length still satisfy the same equation for modules of finite length.
Over a field, the theorem is equivalent to the [[dimension formula for quotients|0SXDQ6TN00]], via the first isomorphism theorem.
