---
tag: 02DTRYKGE8
kind: definition
name: Transposition
aliases: [two-cycle]
msc: [20B30]
defines: 0FWVRHBRWM
uses: [0RJMNEN3BJ, 0ZKPH2BD1T]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_permutation
    locator: Transpositions
---

## Definition

Let $X$ be a set and let $a, b \in X$ with $a \neq b$.
The transposition $(a\ b)$ is the permutation of $X$ that sends $a$ to $b$, sends $b$ to $a$, and fixes each other element of $X$.

## Remarks

A transposition is a $2$-cycle in [[cycle notation|0ZKPH2BD1T]], and $(a\ b) = (b\ a)$.
Each transposition is its own inverse, so it has [[order|0WE2NHZJ7B]] $2$.
The symmetric group $S_n$ contains exactly $\binom{n}{2}$ transpositions.

## Explanations

### L1 human

A transposition swaps two things and leaves everything else in place.
If you do the same swap two times, you are back at the start.
All permutations can be built from transpositions.
