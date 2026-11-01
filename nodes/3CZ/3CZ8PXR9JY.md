---
tag: 3CZ8PXR9JY
kind: statement
role: theorem
name: Nilradical is the intersection of the prime ideals
msc: [13A15]
uses: [0GYGHKX834, QQDN6EYQNJ, 06HC6HK0Z8, 0N9R5NN6TW, 04RXTQA5ZA]
about: [QQDN6EYQNJ, 06HC6HK0Z8]
sources:
  - url: https://en.wikipedia.org/wiki/Nilradical_of_a_ring
---

## Statement

Let $R$ be a [[commutative ring|0GYGHKX834]].
Then the [[nilradical|QQDN6EYQNJ]] of $R$ is the intersection of all [[prime ideals|06HC6HK0Z8]] of $R$:
$$N(R) = \bigcap_{P \text{ prime}} P.$$

## Remarks

One inclusion is direct: if $r^n = 0$, then $r^n$ lies in every prime ideal $P$, so $r \in P$.
For the other inclusion, let $f$ be an element that is not [[nilpotent|0N9R5NN6TW]].
Then the set $S = \set{1, f, f^2, \ldots}$ does not contain $0$, and [[Zorn's lemma|04RXTQA5ZA]] gives an ideal $P$ that is maximal among the ideals disjoint from $S$.
Such an ideal is prime, and $f \notin P$.
Example: in $\Z/12\Z$ the prime ideals are $2\Z/12\Z$ and $3\Z/12\Z$, and their intersection $6\Z/12\Z = \set{0, 6}$ is the set of nilpotent elements.
If $R$ is the zero ring, it has no prime ideals, the empty intersection is $R$, and every element of $R$ is nilpotent, so the statement still holds.
Applied to $R/I$, the statement shows that the [[radical|437YRCNYRJ]] of an ideal $I$ is the intersection of the prime ideals that contain $I$.

## Explanations

### L1 human

An element of a commutative ring is nilpotent exactly when it lies in every prime ideal.
Being nilpotent is an algebraic property: some power is zero.
Lying in every prime ideal is a geometric property: the element, seen as a function on the [[spectrum|FB45BHHA2J]], vanishes at every point.
The theorem says that these two properties agree.

### L2 human

The theorem is the starting point of the link between ideals and closed subsets of the spectrum.
It gives $\sqrt{I} = \bigcap_{P \supseteq I} P$, so two ideals have the same zero locus in $\operatorname{Spec} R$ exactly when they have the same radical.
The proof is a standard use of Zorn's lemma, in the same style as the [[existence of maximal ideals|02HJYT53F7]].
Over a polynomial ring over an algebraically closed field, [[Hilbert's Nullstellensatz|D85VZWS9QK]] sharpens it: maximal ideals alone already suffice.
Compare the [[Jacobson radical|XA0DCNH7WY]], which is the intersection of the maximal ideals only and contains the nilradical.
