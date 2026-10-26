---
tag: ~38adde5d
kind: statement
role: proposition
name: Dimension of the dual space
msc: [15A03, 15A04]
uses: [~adaeb46b, ~6f014bc8]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Finite-dimensional case
---

## Statement

Let $F$ be a field and let $V$ be a finite-dimensional vector space over $F$.
Then the [[dual space|~d8a7f260]] $V^*$ is finite-dimensional, and
$$\dim V^* = \dim V.$$

## Remarks

The [[dual basis|~46d965a7]] of a basis of $V$ is a basis of $V^*$ with the same number of elements.
This also follows from $\dim \Hom_F(V, W) = \dim V \cdot \dim W$ with $W = F$.
The isomorphism $V \to V^*$ that sends $b_i$ to $b_i^*$ depends on the basis.
For infinite-dimensional $V$, the dimension of $V^*$ is strictly greater than the dimension of $V$.

## Explanations

### L1 human

A linear form on an $n$-dimensional space is fixed by its $n$ values on a basis.
These $n$ values can be any numbers.
So the linear forms make up an $n$-dimensional space too.
