---
tag: DMYGZ3YZ6V
kind: concept
name: Linear algebra method
msc: [05D40, 05D05]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_method_in_combinatorics
---

## Summary

The linear algebra method bounds the size of a combinatorial family by attaching to each member a vector, or a polynomial, in a [[vector space|000AYPA9AJ]].
One then proves that these vectors are [[linearly independent|0CRMGPAH83]].
The size of the family is then at most the [[dimension|03GSZ8RTZJ]] of the space.
Classic results proved this way include [[Fisher's inequality|M9XF82GGW8]] and the Oddtown theorem.
Its polynomial versions, such as the [[combinatorial Nullstellensatz|9ZW7BCJMDT]] and the slice rank argument for the [[cap set problem|1SF8Y9M8YB]], form the polynomial method in combinatorics.

## Explanations

### L1 human

To show that a family cannot be large, turn each of its members into a vector and show that no vector is a combination of the others.
Then there can be no more vectors than the dimension of the space.
A standard example is the Oddtown theorem.
Let $\mathcal{F}$ be a family of subsets of $\set{1, \ldots, n}$ in which every set has odd size and any two distinct sets meet in an even number of elements.
Over the [[finite field|0ZXZ82FTX2]] $\F_2$, the indicator vectors $v_A$ satisfy $v_A \cdot v_A = 1$ and $v_A \cdot v_B = 0$ for $A \ne B$, so they are linearly independent, and $|\mathcal{F}| \le n$.
