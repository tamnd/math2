---
tag: 0R74MZYNRB
kind: statement
role: theorem
name: Universal property of the quotient ring
msc: [16D25]
uses: [0VFW4Y69BT, 0GGE0Z0JQ1, 0AAHE7GEW6]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_ring
    locator: Properties
---

## Statement

Let $R$ be a [[ring|0894J980RK]], let $I$ be a two-sided ideal of $R$ and let $\pi \colon R \to R/I$ be the quotient map.
Let $f \colon R \to S$ be a [[ring homomorphism|0GGE0Z0JQ1]] with $I \subseteq \ker f$.
Then there is exactly one ring homomorphism $\bar{f} \colon R/I \to S$ such that $\bar{f} \circ \pi = f$.
It is given by $\bar{f}(a + I) = f(a)$.

## Remarks

The map $\bar{f}$ is well defined: if $a + I = b + I$, then $a - b \in I \subseteq \ker f$, so $f(a) = f(b)$.
The image of $\bar{f}$ is the image of $f$, and $\ker \bar{f} = (\ker f)/I$.
With $I = \ker f$, this gives the [[first isomorphism theorem|0ZMYX7GMH0]].

## Explanations

### L1 human

A homomorphism that sends all of $I$ to zero does not see the difference between $a$ and $a + x$ for $x \in I$.
So it already makes sense on the cosets of $I$.
This gives a homomorphism from the quotient ring.
