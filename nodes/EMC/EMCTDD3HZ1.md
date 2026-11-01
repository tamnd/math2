---
tag: EMCTDD3HZ1
kind: concept
name: Rank of an abelian group
msc: [20K15, 20K20]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_of_an_abelian_group
same_as:
  wikidata: Q1260803
  wikipedia: Rank of an abelian group
---

## Summary

The rank of an [[abelian group|082GHNPJ53]] is the largest number of its elements that are independent over the integers.
It equals the [[dimension|03GSZ8RTZJ]] of the rational vector space obtained by tensoring the group with $\Q$.
It plays for abelian groups the role that dimension plays for vector spaces, but it ignores torsion: finite groups have rank $0$.
For a finitely generated abelian group, the rank is the number of copies of $\Z$ in its decomposition.

## Explanations

### L1 human

The rank counts how many independent directions an abelian group has, the way $\Z^n$ has $n$ coordinate directions.
Elements of finite order do not count as directions, so $\Z \oplus \Z/2\Z$ has rank $1$.
The group $\Q$ also has rank $1$: any two nonzero rationals $a, b$ satisfy a relation $ma - nb = 0$ with integers $m, n$ not both zero.
So $\Q$, though not finitely generated, has only one direction.
