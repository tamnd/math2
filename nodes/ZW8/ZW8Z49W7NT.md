---
tag: ZW8Z49W7NT
kind: proof
name: Proof of the constant multiple rule
msc: [26A24]
proves: 0Z9JB71BS0
uses: [0M0TKFRX2A]
sources:
  - url: https://en.wikipedia.org/wiki/Linearity_of_differentiation
    locator: Constant coefficient
---

## Proof

We deduce the rule from the [[linearity of differentiation|0M0TKFRX2A]].

1. Apply linearity to the functions $f$ and $g = f$, which are both differentiable at $a$, with $\alpha = c$ and $\beta = 0$.
2. For each $x \in I$, $(c f + 0 \cdot f)(x) = c f(x)$. So $c f + 0 \cdot f = c f$.
3. Linearity gives that $c f$ is differentiable at $a$, with $(c f)'(a) = c f'(a) + 0 \cdot f'(a) = c f'(a)$.

## Idea

A constant multiple is the special case of a linear combination where the second coefficient is zero. So the rule is a direct case of linearity.
