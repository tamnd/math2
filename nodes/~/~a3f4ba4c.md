---
tag: ~a3f4ba4c
kind: statement
role: theorem
name: Universal property of the quotient group
aliases: [factorization-through-the-quotient]
msc: [20A05]
uses: [~7fdf454c, ~f060c64f, ~73adfcd7]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Properties
---

## Statement

Let $G$ and $H$ be [[groups|G5S1M9]], let $N$ be a [[normal subgroup|~ebf813cb]] of $G$, and let $\pi \colon G \to G/N$ be the projection $\pi(g) = gN$ to the [[quotient group|~592bfb26]].
Let $\varphi \colon G \to H$ be a [[group homomorphism|~c666c876]] with $N \subseteq \ker \varphi$.
Then there is exactly one group homomorphism $\bar{\varphi} \colon G/N \to H$ with $\bar{\varphi} \circ \pi = \varphi$, and it is given by $\bar{\varphi}(gN) = \varphi(g)$.

## Remarks

The map $\bar{\varphi}$ is well defined because $\varphi$ is constant on each coset of $N$.
The image of $\bar{\varphi}$ is the image of $\varphi$, and the kernel of $\bar{\varphi}$ is $(\ker \varphi)/N$.
With $N = \ker \varphi$, this gives the [[first isomorphism theorem|~6f634155]].

## Explanations

### L1 human

A homomorphism that sends all of $N$ to the identity cannot tell apart elements of the same coset of $N$.
So it already makes sense on the cosets, that is, on the quotient group.
This is the standard way to define a homomorphism out of a quotient group.
