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

The dimension of a vector space $V$ over a field $F$ is the cardinality of a [[basis|0KCQ9Y3QKA]] of $V$; see the [[definition|05G2G0P224]].
It does not depend on the basis, by the [[dimension theorem|0WK0Y8RH1M]].
Dimension is the only invariant of a vector space: two spaces over $F$ are isomorphic exactly when they have the same dimension.

## Motivation

A line, a plane and ordinary space differ in the number of independent directions.
Dimension makes this number precise for every vector space, including spaces of polynomials and functions.
Many questions, such as whether a linear system has a nonzero solution, reduce to a comparison of dimensions.

## Notation

We write $\dim V$, or $\dim_F V$ when the field matters.
In Mathlib, `Module.rank F V` is the dimension as a cardinal.
The natural number `Module.finrank F V` is the dimension, with the value $0$ for infinite-dimensional spaces.

## Remarks

### Examples

1. $\dim F^n = n$: the [[standard basis|C5QA672NPH]] has $n$ vectors.
2. $\dim M_{m \times n}(F) = mn$ and $\dim P_n(F) = n + 1$; see the [[space of matrices|0RE6X3BGPN]] and the [[space of polynomials|0JGZCDT5DN]].
3. $\dim_\R \C = 2$, with basis $1, i$; and $\dim_\C \C = 1$, with basis $1$.
4. $\dim \set{0} = 0$, because the empty family is a basis of the zero space.
5. The plane $W = \set{(x, y, z) \in \R^3 : x + y + z = 0}$ has dimension $2$: the vectors $(1, -1, 0)$ and $(0, 1, -1)$ lie in $W$, are independent, and $(x, y, z) = x(1, -1, 0) + (x + y)(0, 1, -1)$ for $z = -x - y$.
6. $\dim F[x] = \aleph_0$, and $\dim_\Q \R = 2^{\aleph_0}$; see the [[Hamel basis example|ZCBD0GRGVA]].

### Non-examples

1. The size of a spanning set is not the dimension: $(1, 0), (0, 1), (1, 1)$ span $\R^2$, but $\dim \R^2 = 2$, because the set fails independence.
2. The size of an independent set is not the dimension: $(1, 0, 0)$ is independent in $\R^3$, but the set fails spanning.
3. The number of coordinates used to describe a set is not its dimension: the circle $x^2 + y^2 = 1$ is not a subspace at all.

### Basic properties

1. Two spaces over $F$ are isomorphic if and only if they have the same dimension; see [[this statement|0VJBSK15SN]].
2. For a subspace $U \subseteq V$, $\dim U \le \dim V$; in finite dimension, equality forces $U = V$; see [[dimension of a subspace|0QW084460E]].
3. In dimension $n$, each independent list has at most $n$ vectors, and each spanning list has at least $n$.
   A list of exactly $n$ vectors is a basis if it is independent or spanning; see [[the right-size criterion|096V7H13H9]].
4. $\dim(U + W) + \dim(U \cap W) = \dim U + \dim W$ for finite-dimensional subspaces; see [[Grassmann's formula|06HTJNCMPA]].
5. For a [[linear map|0NRYHJPQG2]] $T$ on a finite-dimensional space, $\dim V = \dim \ker T + \dim \operatorname{im} T$, by [[rank-nullity|0W4FSW1TVB]].
6. If $V$ is a complex space, then $\dim_\R V = 2 \dim_\C V$; see [[complexification and realification|CT2F31EDH8]].

### History

Grassmann counted the independent units of his systems in 1844.
Steinitz proved the invariance of the number of basis vectors by the exchange method in 1913.

### Common errors

1. $\dim \set{0} = 0$, not $1$; the zero vector is not a basis of the zero space, because the family $(0)$ is dependent.
2. Dimension depends on the field: $\dim_\R \C^n = 2n$ but $\dim_\C \C^n = n$.
3. Mathlib's `finrank` is $0$ for infinite-dimensional spaces, so `finrank F V = 0` does not imply $V = 0$ without finiteness.
4. Vector space dimension is not the topological dimension of a set, and not the number of entries of a vector in an infinite-dimensional space.

## Explanations

### L1 human

The dimension counts the independent directions in a space.
A line has dimension $1$, a plane has dimension $2$, and ordinary space has dimension $3$.
Every basis of a space has this same number of vectors.

### L2 human

To compute the dimension of a subspace of $F^n$ given by a spanning list, put the vectors as rows of a matrix and row reduce.
The number of nonzero rows of the echelon form is the dimension.
For a subspace given by equations $Ax = 0$, the dimension is the number of free variables, that is, $n$ minus the number of pivots.
Example 5 above: the equation $x + y + z = 0$ has one pivot and two free variables, so $\dim W = 3 - 1 = 2$.

### L3 human

The dimension of an infinite-dimensional space is a cardinal, and it can be large: $\dim_F F^{\N} = \abs{F}^{\aleph_0}$ by the [[Erdős-Kaplansky theorem|~ecdd288b]].
For modules over rings, the analogue is the rank of a free module, which is well defined over nonzero commutative rings.
