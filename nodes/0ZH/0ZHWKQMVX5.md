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

A vector space is finite-dimensional when finitely many of its vectors are enough to build all the others.
Such a space behaves like $F^n$: every vector becomes a list of $n$ numbers, and every question about it becomes a question about matrices.
A [[vector space|000AYPA9AJ]] $V$ over a field $F$ is *finite-dimensional* when it has a finite [[spanning set|088RYKAWK9]], and *infinite-dimensional* otherwise; the [[formal definition|018W3V3TCT]] states this.
By the [[equivalent conditions|HW9HN5A5HJ]], this holds exactly when $V$ has a finite basis, exactly when independent lists in $V$ have bounded length, and exactly when $V \cong F^n$ for some $n$.

## Motivation

Once a finite-dimensional space has a basis of $n$ vectors, each vector has $n$ coordinates and each [[linear map|0NRYHJPQG2]] has a matrix.
So questions about polynomials of bounded degree, about matrices or about solution sets of linear systems all become computations that row reduction can answer.
Most of a first course, including determinants and eigenvalues, works in this setting.

Infinite-dimensional spaces behave differently.
A linear map of such a space to itself can be injective without being surjective, and the spaces of functions that occur in analysis need limits and norms, not only finite sums.
Knowing which side of the line a space is on tells you which tools apply.

## Notation

Books write $\dim V < \infty$ for "finite-dimensional" and $\dim V = \infty$ for "infinite-dimensional".
In Mathlib, the class is `FiniteDimensional F V`, which is defined as `Module.Finite F V`, the statement that $V$ is finitely generated as a module.

## Remarks

### Spaces that are finite-dimensional

The [[coordinate space|713F6AM1X1]] $F^n$ is spanned by the $n$ standard vectors $e_1, \dots, e_n$.
The [[space of matrices|0RE6X3BGPN]] $M_{m \times n}(F)$ is spanned by its $mn$ matrix units, and the space $P_n(F)$ of polynomials of degree at most $n$ is spanned by $1, x, \dots, x^n$.
The complex numbers form a finite-dimensional space over $\mathbb{R}$, spanned by $1$ and $i$.
The zero space $\{0\}$ is spanned by the empty set, so it is finite-dimensional, of dimension $0$.
Every subspace of a finite-dimensional space is again finite-dimensional, by the [[dimension of a subspace|0QW084460E]], so for example every solution set of $Ax = 0$ in $F^n$ is.

### All polynomials at once

The [[space of polynomials|0JGZCDT5DN]] $F[x]$, with no bound on the degree, is the standard infinite-dimensional space.
Take any finite list of polynomials, for example $1 + x$, $x^3$ and $2x - x^2$.
Every combination of them has degree at most $3$, the largest degree in the list.
So $x^4$ is not in their span, and the list does not span $F[x]$.
The same argument works for every finite list: if $d$ is the largest degree in it, then $x^{d + 1}$ is missing.

### Other spaces without a finite spanning set

The space $F^{\mathbb{N}}$ of all sequences contains the vectors $e_0, e_1, e_2, \dots$, where $e_k$ has a $1$ in place $k$ and $0$ elsewhere.
Any finite number of them are independent, so by the [[Steinitz exchange lemma|08ZDRN6H41]] no finite list can span $F^{\mathbb{N}}$.
The space $C[0, 1]$ of continuous functions contains the monomials $1, x, x^2, \dots$, which are independent for the same reason as in $F[x]$, so it is infinite-dimensional too.
The real numbers over $\mathbb{Q}$ give a third case: a finite set of reals spans only a countable set of rational combinations, but $\mathbb{R}$ is uncountable.

### The rules you can use

A finite-dimensional space has a finite basis, and all its bases have the same number $\dim V$ of vectors, by the [[dimension theorem|0WK0Y8RH1M]].
Every independent list [[extends to a basis|0M4SXE5WW3]], and every spanning list [[contains a basis|06MRNP4BNT]].
For a linear map $T \colon V \to V$ of a finite-dimensional space, injective, surjective and bijective are [[the same condition|0912EEEVCT]].

### Watch out

"Finite-dimensional" does not mean "finite".
The plane $\mathbb{R}^2$ is finite-dimensional and has infinitely many vectors; the word "finite" refers to a spanning set.
A countable basis is not enough either: $F[x]$ has the countable basis $1, x, x^2, \dots$, and it is still infinite-dimensional.
Finally, the rules above can fail in infinite dimension.
The shift $(a_0, a_1, \dots) \mapsto (0, a_0, a_1, \dots)$ on $F^{\mathbb{N}}$ is injective, but the sequence $(1, 0, 0, \dots)$ is not in its image.

### History

Peano gave an axiomatic definition of a real vector space in 1888.

### Try it

First, is the space of real sequences with only finitely many nonzero entries finite-dimensional?
No: it contains the independent vectors $e_0, e_1, e_2, \dots$, so by the exchange lemma no finite list spans it.

Second, is the space of polynomials $p$ of degree at most $3$ with $p(1) = 0$ finite-dimensional, and what is its dimension?
Yes, since it is a subspace of $P_3$; it has the basis $x - 1$, $x^2 - 1$, $x^3 - 1$, so its dimension is $3$.

## Explanations

### L1 human

A space is finite-dimensional when a fixed, finite set of building blocks is enough to make every vector.
In the plane, two arrows pointing east and north are enough, so the plane is finite-dimensional.
Polynomials are different.
Any finite set of polynomials has a highest power of $x$, and you can never build a higher power from them.
So the space of all polynomials needs infinitely many building blocks.

### L2 human

Here is a typical check: decide whether the space of polynomials $a + bx + cx^2$ with $a + b + c = 0$ is finite-dimensional, and find a spanning set.
Solve the condition for $a = -b - c$ and split the general element:
$$-b - c + bx + cx^2 = b (x - 1) + c (x^2 - 1).$$
So $x - 1$ and $x^2 - 1$ span the space, and it is finite-dimensional.
The two are independent, because they have different degrees, so the dimension is $2$.
Check: $x - 1$ and $x^2 - 1$ both vanish at $x = 1$, which is the condition $a + b + c = 0$.
The pattern is general: to show finite dimension, write down a finite spanning set; to show infinite dimension, find infinitely many independent vectors.

### L3 human

For modules over a ring, the analogue of finite dimension is "finitely generated", and it no longer gives a basis: $\mathbb{Z}/2$ is finitely generated over $\mathbb{Z}$ but has no basis.
Over a field the two notions agree, because every finite spanning set shrinks to a basis.
In analysis, the finite-dimensional normed spaces are exactly those in which the closed unit ball is compact, by a theorem of Riesz, and on them all norms are equivalent.
The sub-areas on linear maps and on eigenvalues work mostly in finite dimension, where matrices describe everything.
