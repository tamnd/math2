---
tag: 0PFPWKBDTJ
kind: definition
name: Restriction of an endomorphism to an invariant subspace
msc: [15A04, 47A15]
defines: 0KN7EPH7Z0
uses: [0EP59ESQ94]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_subspace
    locator: For a single operator
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be an endomorphism.
Let $W$ be a $T$-[[invariant subspace|0ACX5QT8TE]] of $V$.
The *restriction* of $T$ to $W$ is the endomorphism
$$T|_W \colon W \to W, \qquad T|_W(w) = T(w).$$

## Remarks

The map is well defined because $T(W) \subseteq W$, and it is linear.
If $V$ is finite-dimensional, then the characteristic polynomial of $T|_W$ divides that of $T$.
Take a basis of $V$ that extends a basis of $W$.
In this basis, the matrix of $T$ is block upper triangular, and its first diagonal block is the matrix of $T|_W$.

## Explanations

### L1 human

If a map keeps a subspace inside itself, then it is also a map of that subspace.
This smaller map is the restriction.
Its eigenvalues are some of the eigenvalues of the original map.
