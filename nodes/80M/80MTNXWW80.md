---
tag: 80MTNXWW80
kind: concept
name: Levi form
msc: [32T05, 32V05]
specializes: [48P4A1CX85]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoconvexity
---

## Summary

The Levi form is a [[Hermitian form|48P4A1CX85]] built from the mixed second derivatives $\partial^2 \rho / \partial z_j \partial \bar z_k$ of a real function $\rho$ on a complex domain.
For the boundary of a domain in $\C^n$ one restricts it to the complex tangent directions of the boundary.
Its sign decides the convexity notions of [[several complex variables|BH57D2FBNR]]: pseudoconvexity, strong pseudoconvexity and plurisubharmonicity.

## Explanations

### L1 human

Ordinary convexity of a boundary is measured by the real second derivatives of a function that cuts out the domain.
In complex analysis only the part of this second derivative that is unchanged by holomorphic changes of coordinates matters, and this part is the Levi form.
One also looks only along the directions of the boundary that are complex lines, because these are the directions a holomorphic disc can move in.
For the unit ball in $\C^n$, cut out by $\rho(z) = \abs{z_1}^2 + \cdots + \abs{z_n}^2 - 1$, the Levi form is $\abs{w_1}^2 + \cdots + \abs{w_n}^2$, which is positive.
So the sphere curves "the right way" in every complex direction.
