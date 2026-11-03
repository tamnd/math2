---
tag: Y23SAQAWAK
kind: definition
name: Horndeski's theory
msc: [83D05]
defines: BJRKMC8Q5E
uses: [MWX9XPYEYY, BY4QYYS788, ZHX2VYQDZ3, P13KTBC7MH, 5FZDQQHQKM]
sources:
  - url: https://en.wikipedia.org/wiki/Horndeski%27s_theory
---

## Definition

Let $g$ be a [[Lorentzian metric|BY4QYYS788]] on a four-dimensional manifold and $\phi$ a real scalar field.
Write $\nabla$ for the [[covariant derivative|5FZDQQHQKM]] of $g$, $\square\phi = \nabla^a\nabla_a\phi$, $X = -\frac12 g^{ab}\partial_a\phi\,\partial_b\phi$, $R$ for the [[scalar curvature|ZHX2VYQDZ3]] and $G_{ab}$ for the [[Einstein tensor|P13KTBC7MH]].
Let $G_2, G_3, G_4, G_5$ be smooth functions of $(\phi, X)$, and write $G_{iX} = \partial G_i/\partial X$.
*Horndeski's theory* is the [[scalar–tensor theory|MWX9XPYEYY]] with action $S = \int (L_2 + L_3 + L_4 + L_5)\sqrt{-g}\,d^4x + S_m[g, \psi]$, where

1. $L_2 = G_2(\phi, X)$;
2. $L_3 = -G_3(\phi, X)\,\square\phi$;
3. $L_4 = G_4(\phi, X)\,R + G_{4X}\left[(\square\phi)^2 - \nabla_a\nabla_b\phi\,\nabla^a\nabla^b\phi\right]$;
4. $L_5 = G_5(\phi, X)\,G_{ab}\nabla^a\nabla^b\phi - \frac{1}{6} G_{5X}\left[(\square\phi)^3 - 3\,\square\phi\,\nabla_a\nabla_b\phi\,\nabla^a\nabla^b\phi + 2\,\nabla_a\nabla^b\phi\,\nabla_b\nabla^c\phi\,\nabla_c\nabla^a\phi\right]$;

and the matter action $S_m$ depends on $g$ and the matter fields $\psi$ but not on $\phi$.

## Remarks

This is the form of the Lagrangian found by Kobayashi, Yamaguchi and Yokoyama, which is equivalent to Horndeski's original one.
Although the Lagrangian contains second derivatives of $\phi$ and of $g$, the combinations above are chosen so that the field equations contain no derivatives higher than the second.
Example: $G_4 = 1/(16\pi G)$, $G_2 = X - V(\phi)$ and $G_3 = G_5 = 0$ give general relativity with a minimally coupled scalar field with potential $V$.
Example: $G_4 = \phi/(16\pi)$, $G_2 = 2\omega X/(16\pi\phi)$ and $G_3 = G_5 = 0$ give Brans–Dicke theory.
Non-example: the Lagrangian $(\square\phi)^2$ alone gives a fourth-order equation for $\phi$, so it is not in the class.
The observed equality of the speeds of gravitational waves and light constrains the theory strongly, essentially forcing $G_{4X} \approx 0$ and $G_5$ to be nearly constant.

## Explanations

### L1 human

Horndeski's theory is a recipe with four free functions.
Every scalar–tensor theory in four dimensions with healthy second-order equations comes from some choice of these functions.
