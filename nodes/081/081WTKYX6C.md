---
tag: 081WTKYX6C
kind: statement
role: theorem
name: Finite p-groups are nilpotent
msc: [20D15, 20F18]
uses: [06DAH3VS6M, 0RZCTT30H5, 0DJ9Y9V610, 0DZPD2MG33]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_group
    locator: Examples
  - url: https://en.wikipedia.org/wiki/P-group
    locator: Non-trivial center
---

## Statement

Let $p$ be a prime number and let $G$ be a finite [[p-group|06QYRTX9KQ]].
Then $G$ is [[nilpotent|0Q7MMQHC1P]].

## Remarks

Each quotient $G/Z_i$ of the [[upper central series|0XW54DH28V]] is a $p$-group, so it has a [[nontrivial centre|0RZCTT30H5]] when it is not trivial.
So the upper central series grows strictly until it reaches $G$, and $G$ is finite.
For $|G| = p^n$ with $n \geq 2$, the nilpotency class of $G$ is at most $n - 1$.

## Explanations

### L1 human

A nontrivial finite $p$-group always has a nontrivial centre.
Divide by it, and the quotient is again a $p$-group with a nontrivial centre.
Repeat this, and you climb the upper central series to the whole group.
