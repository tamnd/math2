---
tag: R1EXRPQGQ0
kind: example
name: Representation theory of the Lorentz group
msc: ["22E43", "22E70"]
illustrates: [7JA7WH92K0]
uses: [QWK3BYVJ9W, J58ED1GV6N, 7JA7WH92K0, FX3NEFYFFN, E5P8AG6CK7]
sources:
  - url: https://en.wikipedia.org/wiki/Representation_theory_of_the_Lorentz_group
same_as:
  wikidata: Q7314228
  wikipedia: Representation theory of the Lorentz group
---

## Example

Let $G = \mathrm{SO}^+(1, 3)$ be the restricted [[Lorentz group|QWK3BYVJ9W]]: the linear maps of $\R^4$ that preserve $t^2 - x^2 - y^2 - z^2$, have determinant $1$ and preserve the direction of time.
Its universal cover is the group [[SL(2, C)|J58ED1GV6N]] $\mathrm{SL}_2(\C)$, a double cover with kernel $\set{\pm I}$.

For half-integers $m, n \in \set{0, \frac12, 1, \frac32, \dots}$, let $V_{2m}$ be the space of homogeneous polynomials of degree $2m$ in two variables, with $\mathrm{SL}_2(\C)$ acting by $(\pi_{2m}(g) P)(z) = P(g^{-1} z)$.
Restricted to [[SU(2)|E5P8AG6CK7]], this is the irreducible representation of dimension $2m + 1$.
Put
$$\pi_{m,n}(g) = \pi_{2m}(g) \otimes \pi_{2n}(\bar g) \quad \text{on} \quad V_{2m} \otimes V_{2n},$$
where $\bar g$ is the matrix with complex conjugate entries.
This is a continuous homomorphism, so it is a [[representation|7JA7WH92K0]] of $\mathrm{SL}_2(\C)$ of dimension $(2m + 1)(2n + 1)$.

The classification: the $\pi_{m,n}$ are [[irreducible|FX3NEFYFFN]] and pairwise non-isomorphic.
View $\mathrm{SL}_2(\C)$ as a real Lie group.
Then each irreducible finite-dimensional complex representation of it is isomorphic to exactly one $\pi_{m,n}$.
The element $-I$ acts by $(-1)^{2m + 2n}$, so $\pi_{m,n}$ is a representation of $G$ exactly when $m + n$ is an integer.

Check on the Lie algebra: the complexification of $\mathfrak{so}(1, 3)$ is $\mathfrak{sl}_2(\C) \oplus \mathfrak{sl}_2(\C)$.
On it, $\pi_{m,n}$ becomes the tensor product of the irreducible representations of highest weights $2m$ and $2n$ of the two factors.

## Remarks

The named cases are used throughout physics.
The representation $(0, 0)$ is the scalar one, $(\frac12, 0)$ and $(0, \frac12)$ are the left- and right-handed Weyl spinors, and $(\frac12, \frac12)$ is the defining action on four-vectors, after complexification.
The sum $(1, 0) \oplus (0, 1)$ is the action on antisymmetric tensors such as the electromagnetic field tensor, and $(\frac12, 0) \oplus (0, \frac12)$ is the Dirac spinor.

None of the $\pi_{m,n}$ other than $(0, 0)$ is unitary, because $G$ is a noncompact simple Lie group.
The irreducible unitary representations of $\mathrm{SL}_2(\C)$ are infinite-dimensional, apart from the trivial one, and they were classified by Gelfand and Naimark.

## Explanations

### L1 human

The Lorentz group is the group of changes of reference frame in special relativity.
Physical quantities change in definite ways under it: numbers stay put, vectors rotate and boost, spinors change by a "square root" of this rule.
The finite-dimensional ways in which the group can act are labelled by two half-integers $(m, n)$.
Each label gives one kind of field or particle, from scalars to spinors to the electromagnetic field.
