---
tag: 0KCQ9Y3QKA
kind: concept
name: Basis
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
specializes: [088RYKAWK9]
uses: [0CRMGPAH83, 088RYKAWK9, 0EVHJFTG9Z, 0BJKVF90Z6]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 2B
  - book: isbn:9780134860244
    locator: Section 1.6
  - book: isbn:9780135367971
    locator: Section 2.3
same_as:
  wikidata: Q189569
  wikipedia: Basis (linear algebra)
---

## Summary

A basis of a vector space $V$ over $F$ is a family $(b_i)_{i \in I}$ that is [[linearly independent|0CRMGPAH83]] and [[spans|088RYKAWK9]] $V$; see the [[definition|0VTQTPQGAV]].
Each vector of $V$ is then a combination of the basis vectors in [[exactly one way|E2ZRZGXSNX]], and the coefficients are its [[coordinates|04CYQHN6MC]].
Equivalently, a basis is a [[maximal independent family or a minimal spanning family|AP9TD7QF51]].

## Motivation

A spanning set lets us write each vector as a combination, but maybe in several ways.
An independent set gives unique combinations, but maybe not for every vector.
A basis has both properties, so it turns $V$ into a copy of $F^n$, or of $F^{(I)}$, and lets us compute with lists of numbers.

## Notation

A basis is often written as a list $B = (b_1, \dots, b_n)$; the order matters for coordinates, so it is then an *ordered basis*.
The standard basis of $F^n$ is $e_1, \dots, e_n$.
In Mathlib, `Module.Basis ι F V` is a basis indexed by the type `ι`, stored as a linear isomorphism $V \cong F^{(\iota)}$.

## Remarks

### Examples

1. The [[standard basis|C5QA672NPH]] $e_1, \dots, e_n$ of $F^n$.
2. $(1, 1), (1, -1)$ in $\R^2$. Spanning: $(a, b) = \tfrac{a + b}{2}(1, 1) + \tfrac{a - b}{2}(1, -1)$. Independence: $c(1, 1) + d(1, -1) = (c + d, c - d) = 0$ gives $c = d = 0$.
3. $1, x - 1, (x - 1)^2$ in $P_2(\R)$: $a + b(x - 1) + c(x - 1)^2 = 0$ forces $c = 0$ from the $x^2$ term, then $b = 0$, then $a = 0$; spanning holds since $x^2 = 1 + 2(x - 1) + (x - 1)^2$ and $x = 1 + (x - 1)$.
4. The matrix units $E_{ij}$ form a basis of the [[space of matrices|0RE6X3BGPN]].
5. The empty family is a basis of the zero space $\set{0}$: it is independent, and its span is $\set{0}$.

### Non-examples

1. $(1, 0), (0, 1), (1, 1)$ span $\R^2$ but fail independence: $(1, 0) + (0, 1) - (1, 1) = 0$.
2. $(1, 0, 0), (0, 1, 0)$ are independent in $\R^3$ but fail spanning: $(0, 0, 1)$ is not reached.
3. The unit sequences $e_0, e_1, e_2, \dots$ in $\R^{\N}$ are independent but fail spanning: the constant sequence $(1, 1, 1, \dots)$ is not a finite combination of them.

### Basic properties

1. A family is a basis if and only if each vector is a combination of it in exactly one way; see [[unique coordinates|E2ZRZGXSNX]].
2. A basis is a maximal independent family and a minimal spanning family; see [[this statement|AP9TD7QF51]].
3. [[Every spanning set contains a basis|06MRNP4BNT]], and [[every independent set extends to a basis|0M4SXE5WW3]].
4. [[Every vector space has a basis|00MS9VMQ9Z]], and [[all bases of a space have the same cardinality|0WK0Y8RH1M]], which is its [[dimension|03GSZ8RTZJ]].
5. The columns of an $n \times n$ matrix form a basis of $F^n$ exactly when the matrix is invertible; see [[this statement|WFM1CX5PZT]].

### History

Grassmann used systems of independent units to express his quantities in 1844.
The axiom of choice gives a basis for each space.
Hamel used such a basis of $\R$ over $\Q$ in 1905, and these bases are called *Hamel bases*.

### Common errors

1. The zero space has a basis, the empty family, and its dimension is $0$.
2. Sets versus families: the family $(v, v)$ is never a basis, but the set $\set{v}$ may be one. Mathlib uses indexed families.
3. A basis of an infinite-dimensional space uses finite combinations only.
   The orthonormal "bases" of Hilbert spaces and Schauder bases use infinite sums and are different notions.
4. A space has many bases; "the basis" makes sense only for spaces with a chosen one, such as $F^n$ with its standard basis.

## Explanations

### L1 human

A basis is a set of directions that is just right: enough to reach every vector, and none of them redundant.
Once we fix a basis, each vector gets a unique list of coordinates.
A vector space has many bases, but all of them have the same number of vectors.

### L2 human

To check that $n$ vectors form a basis of $F^n$, put them as the columns of a square matrix and row reduce.
They form a basis exactly when there is a pivot in every row and in every column, that is, when the reduced form is $I$.
Example: $(1, 2), (3, 4)$ in $\R^2$ give the rows $(1, 3)$ and $(0, -2)$ after one step, so they form a basis.
In a space of known dimension $n$, by the [[right-size criterion|096V7H13H9]], it is enough to check either independence or spanning.

### L3 human

A basis indexed by $I$ is the same as a linear isomorphism $F^{(I)} \to V$, by $a \mapsto \sum_i a_i b_i$.
So vector spaces are free modules, and bases exist for every space by Zorn's lemma.
For modules over rings, bases may not exist: $\Z/2$ has no basis over $\Z$.
