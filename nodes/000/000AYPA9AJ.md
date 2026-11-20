---
tag: 000AYPA9AJ
kind: concept
name: Vector space
aliases: [linear-space]
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
specializes: [0NZ8JA25WK]
uses: [04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: Definition and basic properties
  - book: isbn:9783031410253
    locator: Section 1B
  - book: isbn:9780134860244
    locator: Section 1.2
  - book: isbn:9780135367971
    locator: Section 2.1
same_as:
  wikidata: Q125977
  wikipedia: Vector space
inventory: [FS3H3KZHNY]
---

## Summary

Let $F$ be a [[field|04C5ZBG1WT]].
A *vector space* over $F$ is a set $V$ with an addition $V \times V \to V$ and a scalar multiplication $F \times V \to V$ that satisfy eight axioms.
For all $u, v, w \in V$ and $a, b \in F$, the axioms for addition are $u + (v + w) = (u + v) + w$ and $u + v = v + u$.
There is a zero vector $0$ with $v + 0 = v$, and each $v$ has a vector $-v$ with $v + (-v) = 0$.
The axioms for scalars are $a(bv) = (ab)v$, $1v = v$, $a(u + v) = au + av$ and $(a + b)v = av + bv$.
The full list, with numbers, is in the [[definition|05EGHEQZAW]].
Vector spaces are the setting of linear algebra.
The same theory of span, bases and dimension applies to arrows, lists of numbers, matrices, polynomials and functions.

## Motivation

Arrows in the plane, columns of numbers, polynomials and continuous functions look different.
In each case we can add two objects and multiply an object by a number, and the usual rules of arithmetic hold.
The solutions of a [[homogeneous system|04KGXJG1A2]] and the solutions of a linear differential equation behave in the same way.
A vector space keeps only these two operations and their rules.
A theorem proved from the axioms then holds in every one of these settings at once.

## Notation

The elements of $V$ are *vectors* and the elements of $F$ are *scalars*.
We write $0$ for the zero vector and also for the zero of $F$; the context shows which one is meant.
A *real vector space* has $F = \R$, and a *complex vector space* has $F = \C$.
Some books write "linear space" for "vector space".
In Mathlib, a vector space over a field $F$ is a module: `[Field F] [AddCommGroup V] [Module F V]`.

## Remarks

### Examples

1. The [[coordinate space|~9949dfd5]] $F^n$ of $n$-tuples, with entrywise operations, is the prototype of a finite-dimensional space.
2. The [[space of matrices|0RE6X3BGPN]] $M_{m \times n}(F)$, with entrywise addition and scaling, is a vector space of dimension $mn$.
3. The [[space of polynomials|0JGZCDT5DN]] $F[x]$, and its part of degree at most $n$, are vector spaces under the usual sum and scaling.
4. The [[spaces of functions and sequences|0GZB2SN0PH]] $F^S$, with pointwise operations, include $\R^\N$ and the continuous functions on $[0, 1]$.
5. The [[positive real numbers with product as addition|~fb18a251]] form a real vector space, with $0$ played by the number $1$.
6. The field $\C$ is a vector space over $\R$, and $\R$ is a vector space over $\Q$; the scalars come from a subfield.

### Non-examples

1. On $\R^2$, the rule $a(x, y) = (ax, 0)$ breaks only the axiom $1v = v$; see [[this non-example|~f227008c]].
2. On $\R^2$, the rule $a(x, y) = (a^2 x, a^2 y)$ breaks only the axiom $(a + b)v = av + bv$; see [[this non-example|~607e7b30]].
3. The set $\Z^2$ with real scalars is not a vector space: $\tfrac12 (1, 0) = (\tfrac12, 0)$ is not in $\Z^2$, so scalar multiplication does not map into the set.
4. The polynomials of degree exactly $2$ do not form a vector space: $(x^2 + x) + (-x^2) = x$ has degree $1$, so the sum leaves the set.

### Basic properties

1. The zero vector is unique, and each vector has exactly one negative.
2. For all $v \in V$ and $a \in F$: $0v = 0$, $a0 = 0$ and $(-1)v = -v$.
3. If $av = 0$, then $a = 0$ or $v = 0$.

The proofs from the axioms are in [[first consequences of the axioms|~2d07617c]].
Each [[subspace|00YC1D652K]] of a vector space is again a vector space, with the same operations.
Each vector space has a [[basis|0KCQ9Y3QKA]], and its [[dimension|03GSZ8RTZJ]] classifies it up to isomorphism.

### History

Grassmann studied linear combinations of abstract quantities in his *Ausdehnungslehre* of 1844.
Peano gave an axiomatic definition of a real vector space in 1888.
The modern abstract theory became standard in algebra in the twentieth century.

### Common errors

1. Forgetting to check that the operations map into the set: a set with operations inherited from a larger space can fail closure.
2. Assuming that the zero vector must be the number $0$ or the tuple $(0, \dots, 0)$: in the example of positive reals it is the number $1$.
3. Forgetting the field: $\C$ over $\R$ and $\C$ over $\C$ are different vector spaces, with dimensions $2$ and $1$.

## Explanations

### L1 human

A vector space is a collection of objects that we can add and stretch by numbers.
Arrows in the plane are the standard picture.
We add two arrows head to tail, and we stretch an arrow by a number.
Lists of numbers, such as $(2, 5, 1)$, also work: we add them position by position.
The eight axioms are the usual rules of arithmetic, for example "order does not matter in a sum".
Once these rules hold, everything we prove about arrows also holds for lists, polynomials and functions.

### L2 human

We check that $V = \R^2$ is a real vector space with the entrywise operations, at a few sample vectors.

1. Take $u = (1, 2)$, $v = (3, -1)$, $a = 2$ and $b = 5$.
2. Commutativity: $u + v = (4, 1) = v + u$.
3. Zero: $(0, 0)$ satisfies $u + (0, 0) = u$, and $-u = (-1, -2)$ gives $u + (-u) = (0, 0)$.
4. Distributivity over vectors: $a(u + v) = 2(4, 1) = (8, 2)$, and $au + av = (2, 4) + (6, -2) = (8, 2)$.
5. Distributivity over scalars: $(a + b)u = 7(1, 2) = (7, 14)$, and $au + bu = (2, 4) + (5, 10) = (7, 14)$.
6. Compatibility: $a(bu) = 2(5, 10) = (10, 20)$, and $(ab)u = 10(1, 2) = (10, 20)$.
7. Each identity holds in general because it holds in each entry, where it is a rule of the field $\R$.

The typical use of the definition is to recognize a new set as a vector space, so that the whole theory applies to it.
A trap: checking the axioms at a few vectors is not a proof; the proof must use arbitrary vectors and scalars.

### L3 human

A vector space over $F$ is a [[module|0NZ8JA25WK]] over the ring $F$, and Mathlib uses one notion for both.
Over a field every module is free, because [[every vector space has a basis|00MS9VMQ9Z]]; over a general ring this fails, as $\Z/2$ over $\Z$ shows.
The axioms say that scalar multiplication is a ring homomorphism $F \to \End(V, +)$ from $F$ to the endomorphisms of the abelian group $(V, +)$.
Vector spaces over $F$ and [[linear maps|0NRYHJPQG2]] form a category, and the dimension classifies its objects up to isomorphism.
Later sub-areas build new spaces from old ones: [[direct sums|0XYYT5KNTX]], [[quotient spaces|0BR3FY5Q8M]], [[dual spaces|07JBSZE0V4]] and [[tensor products|0BF2DE2SYK]].
