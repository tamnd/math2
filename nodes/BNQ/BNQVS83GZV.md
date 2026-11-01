---
tag: BNQVS83GZV
kind: concept
name: Hilbert–Samuel function
msc: [13D40, 13H15]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert–Samuel_function
same_as:
  wikidata: Q5761248
  wikipedia: Hilbert–Samuel function
---

## Summary

Let $M$ be a finitely generated module over a Noetherian [[local ring|MZ02BKPHJA]], and let $I$ be an ideal primary to the maximal ideal.
The Hilbert–Samuel function of $M$ is $n \mapsto \ell(M/I^n M)$, where $\ell$ is the [[length|CZSCNZH8VY]].
For large $n$ it agrees with a polynomial, the Hilbert–Samuel polynomial.
If $M \neq 0$, the degree of this polynomial is the dimension of $M$, and its leading coefficient gives the [[multiplicity|JX20MNDDXT]].

## Explanations

### L1 human

Look at a ring near a point and ask how much information is visible up to order $n$.
The Hilbert–Samuel function counts this, as a length, for each $n$.
For the plane at the origin, the polynomials up to degree $n - 1$ are spanned by $n(n+1)/2$ monomials, so the function is $n(n+1)/2$.
Its growth like $n^2$ reveals that the plane has dimension $2$.
The [[definition|22J8E7AB8V]] makes this precise.
