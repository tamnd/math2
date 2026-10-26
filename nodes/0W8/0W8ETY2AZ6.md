---
tag: 0W8ETY2AZ6
kind: concept
name: Tangent half-angle substitution
aliases: [weierstrass-substitution]
msc: [26A36]
uses: [0D37QFPEZE, 0WB57D9488]
sources:
  - url: https://en.wikipedia.org/wiki/Tangent_half-angle_substitution
    locator: The substitution
same_as:
  wikidata: Q663628
  wikipedia: Tangent half-angle substitution
---

## Summary

The tangent half-angle substitution sets $t = \tan(x/2)$ in an integral. It turns each rational expression in $\sin x$ and $\cos x$ into a rational function of $t$. Partial fractions then finish the computation.

## Remarks

The substitution gives $\sin x = \frac{2t}{1 + t^2}$, $\cos x = \frac{1 - t^2}{1 + t^2}$ and $dx = \frac{2 \, dt}{1 + t^2}$.
It works on intervals where $x/2$ stays inside $(-\pi/2, \pi/2)$.
For example, it gives $\int \frac{dx}{\sin x} = \ln |\tan(x/2)| + C$.

## Explanations

### L1 human

This substitution turns trigonometric integrals into integrals of fractions of polynomials.
Those integrals are always solvable by partial fractions.
