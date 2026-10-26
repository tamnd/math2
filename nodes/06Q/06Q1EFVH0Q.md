---
tag: 06Q1EFVH0Q
kind: statement
role: proposition
name: Dimension of the annihilator
msc: [15A03, 15A04]
uses: [0R6M158SQ9, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Quotient spaces and annihilators
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $W$ be a subspace of $V$.
Then
$$\dim W + \dim W^0 = \dim V,$$
where $W^0 \subseteq V^*$ is the [[annihilator|0ASHNYF7AG]] of $W$.

## Remarks

A proof extends a basis $b_1, \dots, b_k$ of $W$ to a basis $b_1, \dots, b_n$ of $V$.
Then the dual basis forms $b_{k+1}^*, \dots, b_n^*$ are a basis of $W^0$.
Another proof uses the isomorphism $W^0 \cong (V / W)^*$.
With the double dual isomorphism, it gives $(W^0)^0 = W$ in finite dimensions.

## Explanations

### L1 human

The more directions a subspace has, the fewer independent linear forms vanish on it.
In $\R^3$, a line is killed by a plane of forms, and a plane is killed by a line of forms.
The two dimensions always add up to the dimension of the space.
