---
tag: BRHQQTZB9K
kind: definition
name: Extraspecial group
msc: [20D15]
defines: 7YE4TAG5GE
uses: [06QYRTX9KQ, 0DZ93493VN, 0KYX2N69J0, DZSZ8ZS554]
sources:
  - url: https://en.wikipedia.org/wiki/Extraspecial_group
---

## Definition

Let $p$ be a prime and let $P$ be a finite [[$p$-group|06QYRTX9KQ]].
Let $Z(P)$ be the [[centre|0DZ93493VN]] of $P$.
The group $P$ is *extraspecial* when:

1. $Z(P)$ has order $p$;
2. the [[quotient group|0KYX2N69J0]] $P/Z(P)$ is a nontrivial [[elementary abelian|DZSZ8ZS554]] $p$-group.

## Remarks

In an extraspecial group, the centre, the [[commutator subgroup|0ASGSTXSBW]] and the [[Frattini subgroup|KXJG5VV340]] coincide.
The order of an extraspecial group is $p^{1+2n}$ for some $n \ge 1$, and for each $p$ and $n$ there are exactly two extraspecial groups of that order up to isomorphism.
Example: the [[quaternion group|0NRJGW864D]] $Q_8$ is extraspecial with $p = 2$.
Its centre is $\{\pm 1\}$, of order $2$, and $Q_8/\{\pm 1\}$ has order $4$ with every element of order at most $2$, so it is the Klein four-group, which is elementary abelian.
Non-example: the cyclic group $\Z/p^2\Z$ is not extraspecial, because its centre is the whole group, of order $p^2$, so clause 1 fails.

## Explanations

### L1 human

An extraspecial group is a $p$-group with a centre of order $p$ such that the group becomes elementary abelian, and not trivial, once the centre is factored out.
