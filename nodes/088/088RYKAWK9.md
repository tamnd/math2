---
tag: 088RYKAWK9
kind: concept
name: Spanning set
aliases: [generating-set]
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
uses: [0DTY8B9HMS, 0HR573CHNM]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_span
    locator: lead section
  - book: isbn:9783031410253
    locator: Section 2A
  - book: isbn:9780134860244
    locator: Section 1.4
---

## Summary

A spanning set of a vector space $V$ is a subset $S \subseteq V$ whose [[span|0DTY8B9HMS]] is all of $V$; see the [[definition|0BJKVF90Z6]].
Each vector of $V$ is then a finite linear combination of vectors of $S$, maybe in several ways.
Spanning sets are one half of the notion of a basis; the other half is [[linear independence|0CRMGPAH83]].

## Motivation

A spanning set is a finite or infinite set of building blocks for the whole space.
Many spaces are first described by a spanning set, such as the columns of a matrix for its column space.
The size of the smallest spanning set measures how big the space is, and this leads to dimension.

## Notation

We say that $S$ *spans* $V$, or *generates* $V$, and write $\operatorname{span}(S) = V$.
A list $v_1, \dots, v_n$ spans $V$ when the set $\set{v_1, \dots, v_n}$ does.

## Remarks

### Examples

1. $(1, 0), (0, 1), (1, 1)$ span $\R^2$: $(a, b) = a(1, 0) + b(0, 1) + 0(1, 1)$. The representation is not unique: also $(a, b) = (a - b)(1, 0) + 0(0, 1) + b(1, 1)$.
2. $(1, 0, 1), (0, 1, 1), (1, 1, 0)$ span $\R^3$: the [[pivot test|D3PN42EP4X]] gives a pivot in each of the three rows.
3. $1, x, x^2, \dots, x^n$ span $P_n(F)$, and all monomials span $F[x]$.
4. $V$ itself spans $V$, and $\varnothing$ spans the zero space $\set{0}$.

### Non-examples

1. $(1, 2), (2, 4)$ do not span $\R^2$: each combination $a(1, 2) + b(2, 4) = (a + 2b)(1, 2)$ lies on the line $y = 2x$, so $(1, 0)$ is not reached.
2. Two vectors never span $\R^3$: by the [[pivot test|D3PN42EP4X]], a spanning set of $F^m$ has at least $m$ vectors.
3. The monomials $1, x, x^2, \dots$ do not span $F[[x]]$, the formal power series: $1 + x + x^2 + \cdots$ is not a finite combination.

### Basic properties

1. A superset of a spanning set spans.
2. If $S$ spans $V$ and $v \in S$ is a combination of $S \setminus \set{v}$, then $S \setminus \set{v}$ spans $V$.
3. [[Every spanning set contains a basis|06MRNP4BNT]].
4. In $F^m$, vectors span exactly when their matrix has a pivot in every row; see [[the pivot test|D3PN42EP4X]].
5. By the [[Steinitz exchange lemma|08ZDRN6H41]], a spanning set has at least as many vectors as each independent set.
6. A vector space with a finite spanning set is [[finite-dimensional|0ZHWKQMVX5]], and then each spanning set has at least $\dim V$ vectors.

### History

Grassmann expressed each quantity of his systems as a combination of a few basic units in 1844.
The phrase "generating set" is shared with group theory and module theory.

### Common errors

1. A spanning set need not be independent, so coordinates in a spanning set are not unique.
2. Spanning a subspace $W$ is different from spanning $V$; always say which space is spanned.
3. Infinite spanning sets still use only finite combinations.

## Explanations

### L1 human

A spanning set is a set of building blocks from which we can make every vector of the space.
It may contain more vectors than we need.
Removing the extra vectors leaves a basis.

### L2 human

In $F^m$, to test whether given vectors span, place them as columns and row reduce.
A pivot in every row means "yes".
Example: $(1, 2), (3, 4)$ in $\R^2$.
Subtract $2$ times row 1 from row 2 of the matrix with rows $(1, 3)$ and $(2, 4)$: row 2 becomes $(0, -2)$.
Both rows have pivots, so the vectors span $\R^2$.
