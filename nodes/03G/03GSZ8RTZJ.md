---
tag: 03GSZ8RTZJ
kind: concept
name: Dimension
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
uses: [0KCQ9Y3QKA, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: lead section
  - book: isbn:9783031410253
    locator: Section 2C
  - book: isbn:9780134860244
    locator: Section 1.6
  - book: isbn:9780135367971
    locator: Section 2.3
same_as:
  wikidata: Q929302
  wikipedia: Dimension (vector space)
---

## Summary

The dimension of a vector space counts its independent directions: a line has one, a plane has two, and ordinary space has three.
It is the one number that tells two vector spaces over the same field apart.
For a vector space $V$ over a field $F$, the *dimension* $\dim_F V$ is the number of vectors in a [[basis|0KCQ9Y3QKA]] of $V$, or the cardinality of a basis when the basis is infinite.
The [[formal definition|05G2G0P224]] states this, and the [[dimension theorem|0WK0Y8RH1M]] shows that all bases have the same size, so the number does not depend on the basis.
Two spaces over $F$ are isomorphic exactly when they have the same dimension.

## Motivation

A plane through the origin in $\mathbb{R}^3$ is described by one equation, by two spanning vectors, or by a parametrization with two parameters.
These descriptions look different, but they agree on one number: two directions are needed, and two are enough.
Dimension makes this number precise for every vector space, including spaces of matrices, polynomials and functions.

Many questions then reduce to counting.
A homogeneous system with more unknowns than equations has a nonzero solution, because its solution space has positive dimension.
Four vectors in $\mathbb{R}^3$ are always dependent, because $4 > 3$.
In data analysis, the dimension of the span of a set of measurements says how many independent quantities they really contain.
Later sub-areas use dimension all the time, starting with the [[rank-nullity theorem|0W4FSW1TVB]] for [[linear maps|0NRYHJPQG2]].

## Notation

Most books write $\dim V$, and $\dim_F V$ when the field must be named, as in $\dim_{\mathbb{R}} \mathbb{C} = 2$.
For an infinite-dimensional space, some books only write $\dim V = \infty$, while others give the cardinal of a basis.
In Mathlib, `Module.rank F V` is the dimension as a cardinal, and `Module.finrank F V` is the dimension as a natural number.
Watch out for the convention that `Module.finrank F V = 0` when $V$ is infinite-dimensional.

## Remarks

### Counting a basis

For the [[coordinate space|713F6AM1X1]] $F^n$, the [[standard basis|C5QA672NPH]] $e_1, \dots, e_n$ has $n$ vectors, so $\dim F^n = n$.
For the [[space of polynomials|0JGZCDT5DN]] $P_2(F)$ of degree at most $2$, the basis $1, x, x^2$ has three vectors, so $\dim P_2(F) = 3$, and in general $\dim P_n(F) = n + 1$.
For the [[space of matrices|0RE6X3BGPN]] $M_{2 \times 2}(F)$, the four matrix units form a basis, so the dimension is $4$, and in general $\dim M_{m \times n}(F) = mn$.

A subspace given by an equation needs one more step.
Let $W$ be the plane $x + y + z = 0$ in $\mathbb{R}^3$.
Solve for $z = -x - y$ and split the general point by its free variables:
$$(x, y, -x - y) = x (1, 0, -1) + y (0, 1, -1).$$
The two vectors span $W$, and they are independent because their first two entries are $(1, 0)$ and $(0, 1)$.
So $\dim W = 2$, one less than $3$ because one equation cuts out one direction.

### Over the reals and over the complex numbers

Dimension depends on the field of scalars.
Over $\mathbb{C}$, the single vector $1$ is a basis of $\mathbb{C}$, so $\dim_{\mathbb{C}} \mathbb{C} = 1$.
Over $\mathbb{R}$, the number $i$ is not a real multiple of $1$, and $1, i$ is a basis, so $\dim_{\mathbb{R}} \mathbb{C} = 2$.
In the same way $\dim_{\mathbb{R}} \mathbb{C}^n = 2n$, with the basis $e_1, i e_1, \dots, e_n, i e_n$.
This doubling is studied in [[complexification and realification|CT2F31EDH8]].

### What it is not

The size of a spanning set is not the dimension.
The vectors $(1, 0)$, $(0, 1)$ and $(1, 1)$ span $\mathbb{R}^2$, but they are three vectors and $\dim \mathbb{R}^2 = 2$; they fail independence, since $(1, 1) = (1, 0) + (0, 1)$.
The size of an independent set is not the dimension either: $(1, 0, 0)$ is independent in $\mathbb{R}^3$, but it fails to span.
Only a set with both properties gives the right count.

### The rules you can use

A subspace $U$ of $V$ has $\dim U \le \dim V$, and in finite dimension equality forces $U = V$, by the [[dimension of a subspace|0QW084460E]].
In dimension $n$, an independent list has at most $n$ vectors and a spanning list has at least $n$, by the [[Steinitz exchange lemma|08ZDRN6H41]].
A list of exactly $n$ vectors is a basis as soon as it is independent or spanning, by the [[right-size criterion|096V7H13H9]].
For two finite-dimensional subspaces, $\dim (U + W) + \dim (U \cap W) = \dim U + \dim W$, by [[Grassmann's formula|06HTJNCMPA]].
Two spaces over $F$ are isomorphic exactly when their dimensions agree, by the [[classification by dimension|0VJBSK15SN]].

### Watch out

The zero space $\{0\}$ has dimension $0$, not $1$.
Its basis is the empty family, which is independent and spans $\{0\}$, since the empty sum is $0$.
The family $(0)$ is not a basis, because $1 \cdot 0 = 0$ is a nontrivial relation.

### History

The exchange lemma that makes the number well defined carries the name of Steinitz, who used it in a paper of 1913.
In 1905 Hamel gave a basis of $\mathbb{R}$ over $\mathbb{Q}$, so infinite dimensions were in use early.

### Try it

First, find the dimension of $U = \{ (x, y, z, w) \in \mathbb{R}^4 : x = y, \ z = 0 \}$.
The free variables are $y$ and $w$, and $(y, y, 0, w) = y (1, 1, 0, 0) + w (0, 0, 0, 1)$, so $\dim U = 2$.

Second, find the dimension of the space of real symmetric $2 \times 2$ matrices.
Such a matrix is $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$ with three free entries, so the dimension is $3$.

## Explanations

### L1 human

The dimension of a space is the number of independent directions in it.
On a line you can only move forward or back, so a line has dimension $1$.
On a flat sheet you can move in two independent directions, east and north, so a plane has dimension $2$.
In a room you can also move up, so space has dimension $3$.
Any basis of the space, any set of building blocks for all its vectors, has exactly this many vectors.

### L2 human

Here is a typical problem: find the dimension of the span of $v_1 = (1, 2, 3)$, $v_2 = (2, 4, 6)$ and $v_3 = (1, 0, 1)$.
Put the vectors as rows of a matrix and row reduce, which does not change the span of the rows:
$$\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 0 & 1 \end{pmatrix} \to \begin{pmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & -2 & -2 \end{pmatrix}.$$
We subtracted $2$ times row $1$ from row $2$, and row $1$ from row $3$.
The two nonzero rows are independent, because of their pivots in columns $1$ and $2$, so the span has dimension $2$.
Check: $v_2 = 2 v_1$, so $v_2$ adds no new direction.
This is the standard way to compute dimensions in $F^n$: the count of pivots is the dimension.

### L3 human

For infinite-dimensional spaces the dimension is a cardinal, and it can be large.
The space $F[x]$ has the countable basis $1, x, x^2, \dots$, so $\dim F[x] = \aleph_0$, while $\dim_{\mathbb{Q}} \mathbb{R}$ is the cardinality of the continuum, as the [[Hamel basis example|ZCBD0GRGVA]] shows.
The space $F^{\mathbb{N}}$ of all sequences has dimension $|F|^{\aleph_0}$, by the [[Erdős-Kaplansky theorem|S5ET1HG2ZX]].
For a free module over a nonzero commutative ring, the size of a basis is again well defined and is called the rank.
Topology has its own notion of dimension, and the topological dimension of $\mathbb{R}^n$ is again $n$, but the two notions are defined in different ways and apply to different objects.
