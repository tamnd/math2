---
tag: 0SXDQ6TN00
kind: statement
role: proposition
name: Dimension of a quotient space
msc: [15A03]
uses: [0SVR29SV1V, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Properties
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $W$ be a subspace of $V$.
Then the [[quotient space|0BR3FY5Q8M]] $V / W$ is finite-dimensional, and
$$\dim(V / W) + \dim W = \dim V,$$
where $\dim$ is the [[dimension|03GSZ8RTZJ]].

## Remarks

The number $\dim(V / W) = \dim V - \dim W$ is the *codimension* of $W$ in $V$.
The formula is the [[rank–nullity theorem|0W4FSW1TVB]] for the [[quotient map|0N4F5FMQZW]] $V \to V / W$.
For example, a plane $W$ in $\R^3$ gives $\dim(\R^3 / W) = 1$.

## Explanations

### L1 human

Dividing by a subspace removes its dimensions.
What remains has the dimension of the space minus the dimension of the subspace.
Ordinary space divided by a plane leaves one dimension.
