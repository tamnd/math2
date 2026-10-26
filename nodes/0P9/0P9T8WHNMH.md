---
tag: 0P9T8WHNMH
kind: statement
role: theorem
name: Existence of a complementary subspace
msc: [15A03]
uses: [04C3BAHV03]
sources:
  - url: https://en.wikipedia.org/wiki/Complemented_subspace
    locator: Algebraic direct sum
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$, and let $U$ be a subspace of $V$.
Then $U$ has a [[complement|0M83V17KHX]] in $V$: there is a subspace $W$ of $V$ with $V = U \oplus W$.

## Remarks

Proof: extend a basis $B_U$ of $U$ to a basis $B$ of $V$, and let $W$ be the span of $B \setminus B_U$.
For infinite-dimensional $V$, this uses the extension of independent sets to bases, and hence Zorn's lemma.
The statement fails for modules over rings: the submodule $2\Z$ of $\Z$ has no complement.
For closed subspaces of topological vector spaces, a closed complement need not exist.

## Explanations

### L1 human

Every subspace has a partner subspace that fills up the rest of the space.
We find it by completing a basis of the subspace and taking the span of the new vectors.
The partner is not unique, but its dimension is fixed.
