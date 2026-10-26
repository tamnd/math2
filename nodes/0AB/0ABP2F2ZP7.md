---
tag: 0ABP2F2ZP7
kind: statement
role: theorem
name: Finite-dimensional normed spaces are complete
msc: [46B99]
uses: [03MC70ZRNR, 0BDTTM24DP, 08EWT7J0SC]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_space
    locator: Complete norms and equivalent norms
---

## Statement

Let $V$ be a finite-dimensional vector space over $\mathbb{R}$ or $\mathbb{C}$, with a norm $\|\cdot\|$.
Then $V$ is a [[Banach space|0BDTTM24DP]].

## Remarks

Proof: by [[equivalence of norms in finite dimension|03MC70ZRNR]], the norm is equivalent to the sup norm of the coordinates in a basis. Equivalent norms have the same Cauchy sequences and the same convergent sequences. With the sup norm, completeness follows from the completeness of $\mathbb{R}$ in each coordinate.
A consequence: each finite-dimensional subspace of a normed space is complete, and thus [[closed|0W41XG4W60]].

## Explanations

### L1 human

In finite dimensions, a Cauchy sequence is Cauchy in each coordinate, so each coordinate converges.
This works for each norm, because all norms are equivalent there.
