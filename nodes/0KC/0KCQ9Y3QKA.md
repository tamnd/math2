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

A basis is a set of building blocks for a vector space: enough vectors to build every vector, and no vector that the others already build.
Once we fix a basis, each vector becomes a list of numbers, and the whole space behaves like $F^n$.
For a vector space $V$ over a field $F$, a *basis* is a family $(b_i)_{i \in I}$ of vectors of $V$ that is [[linearly independent|0CRMGPAH83]] and [[spans|088RYKAWK9]] $V$, as the [[definition|0VTQTPQGAV]] states.
Equivalently, each $v \in V$ is a finite linear combination
$$v = \sum_{i \in I} a_i b_i$$
for [[exactly one family of scalars|E2ZRZGXSNX]] $(a_i)_{i \in I}$ with only finitely many $a_i \ne 0$.

## Motivation

A spanning set lets us write every vector as a combination, but perhaps in several ways.
An independent set never gives two ways, but perhaps it misses some vectors.
A basis has both properties at once, so every vector has one and only one recipe, and the numbers in that recipe are its [[coordinates|04CYQHN6MC]].
This is what lets us compute with polynomials, matrices or solutions of a differential equation as if they were columns of numbers.

The idea returns throughout linear algebra.
A linear map is [[fixed by its values on a basis|0R8X9XA83A]], so a matrix can record it.
The number of vectors in a basis does not depend on the basis, and this number is the [[dimension|03GSZ8RTZJ]].
Later, eigenvector bases diagonalize matrices and orthonormal bases simplify geometry.

## Notation

A finite basis is often written as a list $B = (b_1, \dots, b_n)$.
The order matters for coordinates, and a list with a fixed order is an *ordered basis*.
The [[standard basis|C5QA672NPH]] of $F^n$ is written $e_1, \dots, e_n$.
In Mathlib, `Module.Basis ι F V` is a basis indexed by the type `ι`, and it is stored as a linear isomorphism from $V$ to the finitely supported functions `ι →₀ F`.

## Remarks

### Three first bases

The standard basis $e_1 = (1, 0)$, $e_2 = (0, 1)$ of $\mathbb{R}^2$ is the one everyone knows, but it is far from the only one.
Take $b_1 = (1, 1)$ and $b_2 = (1, -1)$.
To see that they span, write a general vector $(a, b)$ as a combination:
$$(a, b) = \tfrac{a + b}{2} (1, 1) + \tfrac{a - b}{2} (1, -1).$$
Check: the first entries give $\tfrac{a + b}{2} + \tfrac{a - b}{2} = a$, and the second entries give $\tfrac{a + b}{2} - \tfrac{a - b}{2} = b$.
For independence, $c(1, 1) + d(1, -1) = (c + d, c - d) = 0$ gives $c + d = 0$ and $c - d = 0$, so $c = d = 0$.

In the [[space of polynomials|0JGZCDT5DN]] $P_2(\mathbb{R})$, the polynomials $1, x - 1, (x - 1)^2$ form a basis.
If $a + b(x - 1) + c(x - 1)^2 = 0$, the $x^2$ term forces $c = 0$, then the $x$ term forces $b = 0$, and then $a = 0$.
They span, because $x = 1 + (x - 1)$ and
$$x^2 = 1 + 2(x - 1) + (x - 1)^2.$$
In the [[space of matrices|0RE6X3BGPN]] $M_{m \times n}(F)$, the $mn$ matrix units $E_{ij}$ form a basis.

### The smallest space

The zero space $\{0\}$ has a basis: the empty family.
It is independent, because it has no vectors that could carry a nonzero coefficient.
Its span is $\{0\}$, because the empty sum is the zero vector.
So the zero space has dimension $0$.
The family $(0)$ is not a basis of $\{0\}$, because $1 \cdot 0 = 0$ is a nontrivial relation.

### What is not a basis

The vectors $(1, 0), (0, 1), (1, 1)$ span $\mathbb{R}^2$, but they fail independence, since
$$(1, 0) + (0, 1) - (1, 1) = (0, 0).$$
The vectors $(1, 0, 0), (0, 1, 0)$ are independent in $\mathbb{R}^3$, but they fail to span, since every combination has third entry $0$ and so misses $(0, 0, 1)$.
In the space $\mathbb{R}^{\mathbb{N}}$ of all real sequences, the unit sequences $e_0, e_1, e_2, \dots$ are independent but do not span.
A finite combination of them has only finitely many nonzero terms, so the constant sequence $(1, 1, 1, \dots)$ is not one.

### Three descriptions of the same thing

A basis has three faces, and each is useful.
It is an independent spanning family, by definition.
It is a family that gives [[unique coordinates|E2ZRZGXSNX]] to every vector.
It is a [[maximal independent family and a minimal spanning family|AP9TD7QF51]]: adding any vector destroys independence, and removing any vector destroys spanning.

The third face explains how bases are found.
[[Every spanning set contains a basis|06MRNP4BNT]], obtained by removing redundant vectors, and [[every independent set extends to a basis|0M4SXE5WW3]], obtained by adding new directions.
[[Every vector space has a basis|00MS9VMQ9Z]], by Zorn's lemma, and [[all bases of one space have the same size|0WK0Y8RH1M]].
In $F^n$, the columns of an $n \times n$ matrix form a basis exactly when the [[matrix is invertible|WFM1CX5PZT]].

### Watch out

The first trap is sets versus families.
The family $(v, v)$ is never a basis, because $1 \cdot v - 1 \cdot v = 0$ is a nontrivial relation, while the set $\{v, v\}$ is just $\{v\}$ and can be a basis of a line.
Mathlib and most modern books use families, so a repeated vector always makes a family dependent.

The second trap is infinite sums.
A basis of an infinite-dimensional space uses finite combinations only.
The [[Schauder bases|528G11SDWR]] of analysis and the orthonormal bases of Hilbert spaces allow convergent infinite sums, and they are different notions.

The third trap is the word "the".
A space has many bases, and only spaces such as $F^n$ come with a preferred one.

### History

Grassmann expressed his quantities as linear combinations of independent units in his *Ausdehnungslehre* of 1844.
Hamel used a basis of $\mathbb{R}$ over $\mathbb{Q}$ in 1905 to build discontinuous solutions of $f(x + y) = f(x) + f(y)$, and such bases are now called [[Hamel bases|ZCBD0GRGVA]].

### Try it

First, decide whether $(1, 1, 0), (0, 1, 1), (1, 0, 1)$ is a basis of $\mathbb{R}^3$.
Expanding the determinant of the matrix with these columns along its first row gives $1 \cdot 1 + 1 \cdot 1 = 2 \ne 0$, so the matrix is invertible and the three vectors form a basis.

Second, decide the same question over the field $\mathbb{F}_2$ with two elements.
Now the sum of the three vectors is $(2, 2, 2) = (0, 0, 0)$, so they are dependent and do not form a basis.

## Explanations

### L1 human

A basis is a set of directions that is just right.
It has enough directions to reach every vector, and none of them is a mix of the others.
In the plane, "one step east" and "one step north" form a basis: the point $(3, 2)$ is three steps east and two steps north, and there is no other way to get there with these two steps.
The pair "east" and "north-east" is another basis, and it gives other numbers for the same point.
Every basis of the plane has exactly two directions.

### L2 human

Here is the typical test: do $(1, 2)$ and $(3, 4)$ form a basis of $\mathbb{R}^2$?
Put them as the columns of a matrix and row reduce, subtracting twice row 1 from row 2:
$$\begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} \to \begin{pmatrix} 1 & 3 \\ 0 & -2 \end{pmatrix}.$$
There is a pivot in every column, so the vectors are independent, and a pivot in every row, so they span.
So they form a basis.
In a space whose dimension $n$ is known, the [[right-size criterion|096V7H13H9]] saves half the work: $n$ vectors that are independent, or $n$ vectors that span, already form a basis.
Watch out: three vectors in $\mathbb{R}^2$ are never a basis, however nicely they spread out.

### L3 human

A basis indexed by $I$ is the same thing as a linear isomorphism $F^{(I)} \to V$, given by $(a_i) \mapsto \sum_i a_i b_i$, where $F^{(I)}$ is the space of finitely supported families.
So every vector space is a [[free module|0DZ9DKAKZR]], and this is special to fields: over the ring $\mathbb{Z}$, the module $\mathbb{Z}/2$ has no basis, since $2x = 0$ for every element $x$.
The equivalence of maximal independent and minimal spanning sets is the axiom system of a [[matroid|PX31ZNYS3Z]], where bases are studied without any vector space.
The sub-area on linear maps uses bases to turn maps into matrices, and the sub-area on eigenvalues looks for bases in which a map is as simple as possible.
