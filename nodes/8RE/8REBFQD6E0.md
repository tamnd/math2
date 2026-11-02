---
tag: 8REBFQD6E0
kind: problem
name: Catenary problem
msc: [49K05, 49K21, 49-03]
uses: [6FY0KHMK5A, F7EKTEESQ5, 036696EMG2, 0TH78S7GBZ]
about: [PQ25NHV0KS]
sources:
  - url: https://en.wikipedia.org/wiki/Catenary
history:
  posed_by: "Jacob Bernoulli"
  first_stated: "1690"
---

## Problem

A uniform, perfectly flexible and inextensible chain of length $\ell$ hangs under constant gravity from two fixed points $(a, A)$ and $(b, B)$.
Here $a < b$, and $\ell$ is larger than the distance between the points.
What shape does the chain take?

As a variational problem: among $y \in C^1([a, b])$ with $y(a) = A$, $y(b) = B$ and [[arc length|0TH78S7GBZ]]
$$\int_a^b \sqrt{1 + y'(x)^2} \, dx = \ell,$$
find one that minimises the potential energy, which is proportional to
$$U(y) = \int_a^b y(x) \sqrt{1 + y'(x)^2} \, dx.$$

## Remarks

This is an [[isoperimetric problem|6FY0KHMK5A]].
With a multiplier $\lambda$, the Lagrangian is $(y - \lambda) \sqrt{1 + y'^2}$, which does not depend on $x$.
The [[Beltrami identity|F7EKTEESQ5]] gives $(y - \lambda) / \sqrt{1 + y'^2} = c$, and the solutions with $c > 0$ are the catenaries
$$y(x) = \lambda + c \cosh\Big(\frac{x - d}{c}\Big),$$
where the constants $c$, $d$, $\lambda$ are fixed by the two end conditions and the length.
Here $\cosh$ is the [[hyperbolic cosine|036696EMG2]].
Jacob Bernoulli posed the problem in Acta Eruditorum, and solutions by Leibniz, Huygens and Johann Bernoulli were published in 1691.

## Explanations

### L1 human

Hold a chain or a necklace by its two ends and let it hang.
The curve it forms looks like a parabola but is a different curve, the catenary, given by the hyperbolic cosine.
The chain settles in the shape that puts its centre of mass as low as possible, given its length.
