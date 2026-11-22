---
tag: 06HTJNCMPA
kind: statement
role: theorem
name: Dimension formula for sums of subspaces
aliases: [grassmann-formula, dimension-formula]
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [03GSZ8RTZJ]
uses: [0RMKABS2S5, 0V33SPH7RR, 05G2G0P224]
proofs: [75VVYAZBK3]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.finrank_sup_add_finrank_inf_eq
    match: weaker
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Facts
  - book: isbn:9783031410253
    locator: Section 2C
  - book: isbn:9780134860244
    locator: Section 1.6, exercises
---

## Statement

Dimensions of subspaces add like the sizes of two overlapping sets: the overlap is counted twice, so we take it away once.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $U$ and $W$ be finite-dimensional [[linear subspaces|0EPTJA5QV4]] of $V$.
Then the [[sum|0RMKABS2S5]] $U + W$ is finite-dimensional, and
$$\dim(U + W) + \dim(U \cap W) = \dim U + \dim W,$$
where $\dim$ is the [[dimension|05G2G0P224]] and $U \cap W$ is the [[intersection|0V33SPH7RR]].

## Remarks

### Two planes in space

Let $U$ be the plane $z = 0$ and $W$ the plane $x = 0$ in $\mathbb{R}^3$.
Each has dimension $2$.
Their sum contains $e_1$ and $e_2$ from $U$ and $e_3$ from $W$, so $U + W = \mathbb{R}^3$ and $\dim(U + W) = 3$.
Their intersection is the set of vectors with $x = z = 0$, the $y$-axis, of dimension $1$.
The formula checks out:
$$3 + 1 = 4 = 2 + 2.$$

The same count works for any two different planes $U$ and $W$ through the origin in $\mathbb{R}^3$.
The sum $U + W$ is a subspace that strictly contains the plane $U$, so it has dimension $3$.
Then $\dim(U \cap W) = 2 + 2 - 3 = 1$, so two different planes through the origin always meet in a line.

### What it gives you

The formula gives $\dim(U + W) \le \dim U + \dim W$, with equality exactly when $U \cap W = \{0\}$.
So the sum is direct exactly when the dimensions add, and this is the usual test for an [[internal direct sum|0XYYT5KNTX]].

It also forces intersections in small spaces.
In a space $V$ of dimension $n$, we have $\dim(U + W) \le n$, so
$$\dim(U \cap W) \ge \dim U + \dim W - n.$$
For example, two subspaces of dimension $3$ in $\mathbb{R}^5$ share at least a line, because $3 + 3 - 5 = 1$.

### Why each hypothesis is needed

Finite dimension is needed for the form with subtraction, $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$.
In $F[x]$, let $U$ be the span of the even powers $1, x^2, x^4, \dots$ and $W$ the span of the odd powers $x, x^3, \dots$.
Then $U + W = F[x]$ and $U \cap W = \{0\}$, while for $U = W = F[x]$ the intersection is all of $F[x]$.
In both cases $\dim U$, $\dim W$ and $\dim(U + W)$ equal $\aleph_0$, so these three numbers cannot determine $\dim(U \cap W)$.

The formula is for two subspaces only.
Take the three lines $U_1$, $U_2$, $U_3$ in $\mathbb{R}^2$ spanned by $(1, 0)$, $(0, 1)$ and $(1, 1)$.
Every pairwise intersection is $\{0\}$, so the pattern of inclusion and exclusion would predict
$$\dim(U_1 + U_2 + U_3) = 1 + 1 + 1 - 0 - 0 - 0 + 0 = 3,$$
but the sum is $\mathbb{R}^2$, of dimension $2$; see [[three lines in the plane|38AKN9MG6J]].
The reason is that the subspaces do not behave like sets: $U_1 \cap (U_2 + U_3) = U_1$, while $(U_1 \cap U_2) + (U_1 \cap U_3) = \{0\}$.

### Watch out

Do not confuse $U + W$ with the union $U \cup W$.
For the two planes above, the union is not a subspace, and the formula is about the sum, which is the smallest subspace that contains both.
Also, $\dim(U + W) = \dim U + \dim W$ is not true in general; it needs $U \cap W = \{0\}$.

### Generalizations

For subspaces of any dimension the formula holds as an equation of cardinal numbers, by the same proof with bases extended by Zorn's lemma.
The [[rank-nullity theorem|0W4FSW1TVB]], applied to the map $U \times W \to V$, $(u, w) \mapsto u - w$, gives a second proof.
Its image is $U + W$, and its kernel is the set of pairs $(z, z)$ with $z \in U \cap W$, which is a copy of $U \cap W$.
In the language of lattices, the subspaces of $V$ form a modular lattice, and the formula says that the dimension is a valuation on it.

## History

The formula is often called Grassmann's formula, after Hermann Grassmann, whose Ausdehnungslehre of 1844, revised in 1862, studied linear spaces of any finite dimension.

## Explanations

### L1 human

Think of two clubs with some members in common.
To count all members, add the sizes of the two clubs and subtract the common members once, because they were counted twice.
Dimensions of subspaces work the same way.
Two planes through the origin in space have dimension $2$ each, together they fill space, of dimension $3$, so they share $2 + 2 - 3 = 1$ dimension: a line.

### L2 human

Here is a typical use: find the dimension of $U \cap W$ in $\mathbb{R}^4$, where $U = \operatorname{span}(e_1, e_2, e_3)$ and $W = \operatorname{span}(e_3 + e_4, e_1 + e_4)$.
The two spanning vectors of $W$ are independent, so $\dim W = 2$, and $\dim U = 3$.
The sum contains $e_1, e_2, e_3$ and $(e_3 + e_4) - e_3 = e_4$, so $U + W = \mathbb{R}^4$.
The formula gives
$$\dim(U \cap W) = 3 + 2 - 4 = 1.$$
Check: a vector $a(e_3 + e_4) + b(e_1 + e_4)$ of $W$ lies in $U$ exactly when its fourth entry $a + b$ is $0$, so $U \cap W$ is the line spanned by $e_3 - e_1$.
The trap is to forget the intersection term, which would give the impossible answer $\dim(U + W) = 5$ in $\mathbb{R}^4$.

### L3 human

The formula is the linear version of inclusion and exclusion for two sets, and it fails for three subspaces because the lattice of subspaces is modular but not distributive.
It is the statement that $\dim$ is a valuation on this lattice, and the same structure appears in projective geometry, where two planes in projective $3$-space meet in a line.
A third proof uses quotients: $(U + W)/W \cong U/(U \cap W)$ by the [[second isomorphism theorem for vector spaces|0APN65D6Y6]], and counting dimensions on both sides gives the formula, as the [[proof by quotients|MKF2J8YS8H]] shows.
Later, the formula returns in the theory of [[direct sums|0XYYT5KNTX]] and in the [[rank-nullity theorem|0W4FSW1TVB]], of which it is a special case.
