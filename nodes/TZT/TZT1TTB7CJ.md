---
tag: TZT1TTB7CJ
kind: statement
role: theorem
name: Cohen's theorem on Noetherian rings
msc: ["13E05"]
uses: [0GYGHKX834, 06HC6HK0Z8, 030TZ0DQWT, 0MVH4Y1CRZ]
about: [0670T59HGE, 00MHHZ9SNE]
sources:
  - url: https://en.wikipedia.org/wiki/Noetherian_ring
---

## Statement

Let $R$ be a [[commutative ring|0GYGHKX834]].
Then $R$ is [[Noetherian|0MVH4Y1CRZ]] if and only if every [[prime ideal|06HC6HK0Z8]] of $R$ is [[finitely generated|030TZ0DQWT]].

## Remarks

One direction is clear, since in a Noetherian ring every ideal is finitely generated.
For the other, suppose that some ideal is not finitely generated.
By Zorn's lemma there is an ideal $I$ that is maximal among the ideals that are not finitely generated.
Let $a, b \notin I$ with $ab \in I$.
Then $I + (a)$ and the ideal quotient $(I : a) = \set{r \in R : ra \in I}$ are strictly larger than $I$, hence finitely generated.
One checks that $I$ would then be finitely generated, which is impossible; so $I$ is prime.
This prime ideal is not finitely generated, against the hypothesis.
For example, to show that $\Z[x]$ is Noetherian it would be enough to check its prime ideals, although [[Hilbert's basis theorem|0YKA9J3XEE]] gives this more directly.

## Explanations

### L1 human

To check that every ideal of a commutative ring is finitely generated, it is enough to check the prime ideals.
The prime ideals are often easier to list, so this saves work.

### L2 human

The proof is a model of a common method: an ideal maximal for not having a property is often prime.
The same method shows that a commutative ring in which every prime ideal is principal is a principal ideal ring.
The theorem is a test for the [[Noetherian|0670T59HGE]] property, for example for rings of power series and rings of integers.
