---
tag: 4MBYAVB0PY
kind: concept
name: Commuting probability
msc: [20D60, 20P05]
sources:
  - url: https://en.wikipedia.org/wiki/Commuting_probability
same_as:
  wikidata: Q56887820
  wikipedia: Commuting probability
---

## Summary

The commuting probability of a finite group is the probability that two elements chosen independently and uniformly at random commute.
It equals $1$ exactly for abelian groups, and it equals the number of conjugacy classes divided by the order of the group.
A non-abelian finite group has commuting probability at most $5/8$.
So the value measures how far a group is from being abelian.

## Explanations

### L1 human

Pick two elements of a finite group at random, with repetition allowed, and ask whether $xy = yx$.
In an abelian group the answer is always yes.
In the symmetric group $S_3$, of the $36$ ordered pairs exactly $18$ commute, so the probability is $1/2$.
A group cannot be "almost abelian" in this sense: once some pair fails to commute, at least $3/8$ of all pairs fail.
