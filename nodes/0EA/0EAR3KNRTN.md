---
tag: 0EAR3KNRTN
kind: concept
name: Trigonometric substitution
msc: [26A36]
uses: [0D37QFPEZE, 03H7WZ4T3K]
sources:
  - url: https://en.wikipedia.org/wiki/Trigonometric_substitution
    locator: lead section
same_as:
  wikidata: Q1191963
  wikipedia: Trigonometric substitution
---

## Summary

Trigonometric substitution is a [[substitution|0D37QFPEZE]] method for integrals that contain $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$, or $\sqrt{x^2 - a^2}$. We set $x$ equal to $a \sin \theta$, $a \tan \theta$, or $a \sec \theta$. The [[Pythagorean identity|03H7WZ4T3K]] then removes the square root.

## Remarks

With $x = a \sin \theta$ for $\theta \in [-\pi/2, \pi/2]$, we get $\sqrt{a^2 - x^2} = a \cos \theta$, for $a > 0$.
For example, this substitution gives $\int_{-1}^{1} \sqrt{1 - x^2} \, dx = \pi/2$, the area of a half disc.
Hyperbolic functions can replace the trigonometric functions in the second and the third case.

## Explanations

### L1 human

A square root such as $\sqrt{1 - x^2}$ is the side of a right triangle.
Writing $x$ as the sine of an angle turns the root into a cosine.
