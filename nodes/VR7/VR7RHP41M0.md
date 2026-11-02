---
tag: VR7RHP41M0
kind: concept
name: Steenrod square
msc: [55S10, 55S05]
specializes: [K8T15QHN3W]
sources:
  - url: https://en.wikipedia.org/wiki/Steenrod_algebra
---

## Summary

The Steenrod squares $\operatorname{Sq}^i$, $i \ge 0$, are [[cohomology operations|K8T15QHN3W]] on mod $2$ cohomology that raise degree by $i$.
They are additive, stable under suspension, and extend the cup square: $\operatorname{Sq}^n x = x \smile x$ when $x$ has degree $n$.
They generate the [[Steenrod algebra|JWTTXSGD0E]] and give the mod $2$ cohomology of a space the structure of a module over it.
They detect maps that cup products miss, such as the suspensions of the Hopf maps, and they compute [[Stiefel–Whitney classes|JQCK7A210W]] through [[Wu's formula|7KEDZ9TFEE]].

## Explanations

### L1 human

In mod $2$ cohomology, squaring a class with the cup product doubles its degree.
Steenrod squares fill in the steps between: $\operatorname{Sq}^i$ adds $i$ to the degree.
They start with the identity at $i = 0$ and end with the cup square when $i$ equals the degree.
For the complex projective plane, $\operatorname{Sq}^2$ of the degree $2$ generator is the nonzero top class, and this shows that the Hopf map $S^3 \to S^2$ is not null-homotopic.
