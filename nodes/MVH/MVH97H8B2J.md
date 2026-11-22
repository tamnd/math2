---
tag: MVH97H8B2J
kind: topic
name: Vector spaces, span, independence, bases and dimension
msc: ["15A03"]
topics: [GN8GYSDZFX]
---

## Summary

This part of [[linear algebra|GN8GYSDZFX]] steps back from columns of numbers and asks what all the objects of linear algebra have in common.
It starts with the axioms of a vector space and a gallery of examples: lists, matrices, polynomials, functions and sequences, and spaces over finite fields.
Inside a space we find subspaces, and from a set of vectors we build its span, the smallest subspace that contains it.
Linear independence says when a set has no redundant vector, and a basis is a set that spans without redundancy, so that every vector gets unique coordinates.
The Steinitz exchange lemma then shows that all bases of a space have the same size, and that size is the dimension, the one number that classifies a space over a given field up to isomorphism.
The last pages count with dimensions, in subspaces, in sums of subspaces and over finite fields, and they treat infinite dimension, where Zorn's lemma gives bases without any explicit description.
Everything later in the area, from linear maps and eigenvalues to inner products and duality, takes place in the spaces built here.

## Remarks

### Reading order

1. [[Vector space|000AYPA9AJ]]: the eight axioms, why each is needed, and a strange example whose zero vector is the number $1$.
2. [[Coordinate space F^n|713F6AM1X1]]: the prototype of every finite-dimensional space, with the axioms checked entry by entry.
3. [[Space of matrices|0RE6X3BGPN]]: matrices as vectors, with the matrix units as a basis of size $mn$.
4. [[Space of polynomials|0JGZCDT5DN]]: the monomial basis, the dimension $n + 1$, and the gap between a polynomial and its function.
5. [[Spaces of functions and sequences|0GZB2SN0PH]]: pointwise operations, and why the point masses span only the finitely supported functions.
6. [[Subspace|00YC1D652K]]: the subspace test with its three conditions, which saves checking eight axioms.
7. [[Intersection and union of subspaces|0V33SPH7RR]]: why intersections are subspaces and unions almost never are.
8. [[Sum of subspaces|0JMTY8MF54]]: the smallest subspace that contains two given ones.
9. [[Linear combination|0V8F3E48E6]]: the one operation from which span, independence and bases are all built.
10. [[Span|0DTY8B9HMS]]: all the combinations of a set, and why that is the smallest subspace containing it.
11. [[Spanning set|088RYKAWK9]]: how to test with pivots whether a set reaches every vector of $F^m$.
12. [[Linear independence|0CRMGPAH83]]: no redundant vector, sets versus families, and the dependence lemma.
13. [[Linear dependence of the columns of a matrix|76GG9B25A1]]: the column test by row reduction, and why $m + 1$ vectors in $F^m$ are dependent.
14. [[Basis|0KCQ9Y3QKA]]: unique coordinates, the three equivalent descriptions, and the empty basis of the zero space.
15. [[Standard basis|C5QA672NPH]]: the bases that every computation starts from, in $F^n$, in matrices and in polynomials.
16. [[Coordinate vector|04CYQHN6MC]]: how a basis turns any space of dimension $n$ into $F^n$.
17. [[Steinitz exchange lemma|08ZDRN6H41]]: the exchange argument that an independent list is never longer than a spanning list.
18. [[Dimension theorem|0WK0Y8RH1M]]: all bases have the same size, with an exchange proof, a row reduction proof and the infinite case.
19. [[Dimension|03GSZ8RTZJ]]: the size of a basis, and why it depends on the field of scalars.
20. [[Finite-dimensional vector space|0ZHWKQMVX5]]: the equivalent conditions, and $F[x]$ as the first infinite-dimensional space.
21. [[Every spanning set contains a basis|06MRNP4BNT]]: how to thin a spanning set to a basis, and the pivot columns as a basis of the column space.
22. [[Extension of an independent set to a basis|0M4SXE5WW3]]: how to grow an independent set to a basis, by hand or by Zorn's lemma.
23. [[Every vector space has a basis|00MS9VMQ9Z]]: the Zorn's lemma proof, and why the result needs the axiom of choice.
24. [[Hamel basis|ZCBD0GRGVA]]: a basis of $\mathbb{R}$ over $\mathbb{Q}$, whose existence rests on the axiom of choice.
25. [[Dimension of a subspace|0QW084460E]]: why a subspace is never bigger, and why equal dimension forces equality in finite dimension.
26. [[Right-size criterion for a basis|096V7H13H9]]: a shortcut that halves the work of checking a basis.
27. [[Dimension formula for sums of subspaces|06HTJNCMPA]]: how to count the dimension of $U + W$, and why the formula breaks for three subspaces.
28. [[Vector spaces over finite fields|J9VE1X14PV]]: finite spaces, where bases and subspaces can be counted.
29. [[Complexification and realification|CT2F31EDH8]]: how to move between real and complex spaces, and what a complex structure is.

### Prerequisites

- [[Field|04C5ZBG1WT]]: the scalars, including $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{F}_q$.
- [[Vectors in the plane and in space|VKVAJ94SKZ]]: vectors in coordinates, the picture behind the axioms.
- [[Systems of linear equations|DXSXFVDMXQ]]: row reduction and pivots, which the column tests use.
- [[Cardinal number|0EBACQFAZW]] and [[Zorn's lemma|04RXTQA5ZA]]: for the results in infinite dimension.
