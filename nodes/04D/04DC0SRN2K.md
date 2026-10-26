---
tag: 04DC0SRN2K
kind: statement
role: theorem
name: Order of a group is the index times the order of the subgroup
msc: [20D60]
uses: [04QEBF8S49, 0DKMBWTD7P, 0SEX9F9J5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange's_theorem_(group_theory)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: lead section
---

## Statement

Let $G$ be a finite [[group|G5S1M9]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
Then $|G| = [G : H] \cdot |H|$, where $[G : H]$ is the [[index|0DTXBQPA2S]] of $H$ in $G$.

## Remarks

The left cosets of $H$ partition $G$, and [[each coset has $|H|$ elements|0DKMBWTD7P]].
This statement gives [[Lagrange's theorem|3C53TD]]: the order of $H$ divides the order of $G$.
The formula $|G| = [G : H] \cdot |H|$ is also true for infinite groups as an equation of cardinal numbers.

## Explanations

### L1 human

Cut a finite group into the left cosets of a subgroup.
Each piece has the same size as the subgroup, and the number of pieces is the index.
So the size of the group is the number of pieces times the size of one piece.
