---
tag: 0RZCTT30H5
kind: statement
role: theorem
name: A nontrivial finite p-group has nontrivial centre
msc: [20D15]
uses: [06DAH3VS6M, 08BPSC6YTE, 0S7Y9Q990Q]
sources:
  - url: https://en.wikipedia.org/wiki/P-group
    locator: Non-trivial center
---

## Statement

Let $p$ be a prime number and let $G$ be a finite [[p-group|06QYRTX9KQ]] with $G \neq \{e\}$.
Then the [[centre|0DZ93493VN]] $Z(G)$ is not $\{e\}$.

## Remarks

In the [[class equation|08BPSC6YTE]] $|G| = |Z(G)| + \sum [G : C_G(a_i)]$, the left side and each term of the sum are divisible by $p$.
So $p$ divides $|Z(G)|$, and $|Z(G)| \geq p$.
Equivalently, apply the [[fixed point lemma|098D2E7DEH]] to the action of $G$ on itself by conjugation.
A consequence is that each finite $p$-group is [[nilpotent|0Q7MMQHC1P]].

## Explanations

### L1 human

The conjugacy classes of a $p$-group that have more than one element all have sizes divisible by $p$.
The order of the group is also divisible by $p$.
So the classes with one element, which form the centre, cannot be just the identity.
