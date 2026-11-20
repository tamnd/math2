---
tag: 0ZHWKQMVX5
kind: concept
name: Finite-dimensional vector space
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
specializes: [000AYPA9AJ]
uses: [000AYPA9AJ, 088RYKAWK9, 0BJKVF90Z6]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: lead section
  - book: isbn:9783031410253
    locator: Section 2A
  - book: isbn:9780134860244
    locator: Section 1.6
---

## Summary

A vector space $V$ over $F$ is finite-dimensional when it has a finite [[spanning set|088RYKAWK9]]; see the [[definition|018W3V3TCT]].
This holds exactly when $V$ has a finite basis, and exactly when $V \cong F^n$ for some $n$; see [[equivalent conditions|HW9HN5A5HJ]].
Most of undergraduate linear algebra, such as matrices of linear maps, determinants and eigenvalues, works in finite-dimensional spaces.

## Motivation

In a finite-dimensional space, a basis turns each vector into a list of $n$ numbers and each linear map into a matrix.
So every question becomes a computation with matrices, which row reduction can answer.
Infinite-dimensional spaces, such as spaces of functions, need other tools, often from analysis.

## Notation

We write $\dim V < \infty$.
In Mathlib, the class is `FiniteDimensional F V`, which is `Module.Finite F V`.

## Remarks

### Examples

1. $F^n$, with the spanning set $e_1, \dots, e_n$.
2. $M_{m \times n}(F)$ and $P_n(F)$.
3. $\C$ over $\R$, spanned by $1$ and $i$.
4. Each subspace of $F^n$, such as the solution set of $Ax = 0$.
5. The zero space $\set{0}$, spanned by the empty set.

### Non-examples

1. $F[x]$ fails the definition: finitely many polynomials have a largest degree $d$, and $x^{d + 1}$ is not in their span.
2. The sequence space $F^{\N}$ contains the independent family $e_0, e_1, e_2, \dots$, so it has no finite spanning set, by the Steinitz lemma.
3. $\R$ over $\Q$: each finite set $S$ spans a countable set $\operatorname{span}_\Q(S)$, but $\R$ is uncountable.
4. $C[0, 1]$ contains the independent family $1, x, x^2, \dots$, so it is infinite-dimensional.

### Basic properties

1. A finite-dimensional space has a finite basis, and all bases have the same number $\dim V$ of vectors.
2. Each subspace of a finite-dimensional space is finite-dimensional, with smaller or equal dimension; see [[dimension of a subspace|0QW084460E]].
3. Each independent list extends to a basis, and each spanning list shrinks to a basis.
4. A linear map between spaces of the same finite dimension is injective if and only if it is surjective.
5. A space is infinite-dimensional exactly when it contains an infinite independent family.

### History

Grassmann studied spaces spanned by finitely many units in 1844.
Peano gave the axiomatic definition of a vector space in 1888, and his axioms include infinite-dimensional spaces such as spaces of functions.

### Common errors

1. A finite-dimensional space over $\R$ has infinitely many vectors; "finite" refers to a spanning set, not to the space.
2. An infinite-dimensional space can have a countable basis, as $F[x]$ does, but then it is still not finite-dimensional.
3. Results such as "injective iff surjective" fail in infinite dimension: the shift $(a_0, a_1, \dots) \mapsto (0, a_0, a_1, \dots)$ on $F^{\N}$ is injective but not surjective.

## Explanations

### L1 human

A space is finite-dimensional when finitely many vectors are enough to build every vector.
The plane needs two vectors, and ordinary space needs three.
The space of all polynomials needs infinitely many, because the degrees have no bound.

### L2 human

To show that a space is infinite-dimensional, find an infinite independent family.
Example: in $C[0, 1]$, the monomials $1, x, \dots, x^n$ are independent for each $n$.
The reason: a nonzero polynomial of degree at most $n$ has at most $n$ roots, so it is not the zero function.
So no finite set spans $C[0, 1]$.
