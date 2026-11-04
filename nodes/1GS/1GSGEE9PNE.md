---
tag: 1GSGEE9PNE
kind: proof
name: Proof of the Lagrange multiplier rule with one constraint
msc: ["90C46"]
proves: 04A2XEX4D4
uses: [0VKKP8X6Q6, 0NS2QYVC4Y, 0Y5Q8Q9WJ7, 0EVHJFTG9Z, 0TCBZMEYGN]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_multiplier
    locator: Single constraint
---

## Proof

We apply the theorem with several constraints to the single constraint $g - c$.

1. Let $U$, $n \ge 2$, $f$, $g$, $c$ and $a$ be as in the statement. Define $G = g - c$ on $U$. It is of [[class C^1|0TCBZMEYGN]], since $g$ is.
2. The [[level set|0Y5Q8Q9WJ7]] $\set{x \in U : g(x) = c}$ is the set $M = \set{x \in U : G(x) = 0}$.
3. The [[gradient|0NS2QYVC4Y]] of $G$ is $\nabla G = \nabla g$, since $c$ is constant. So $\nabla G(a) \ne 0$.
4. A single nonzero vector is [[linearly independent|0EVHJFTG9Z]]. Also $m = 1 < n$, since $n \ge 2$.
5. The restriction of $f$ to $M$ has a local extremum at $a$. By the [[Lagrange multiplier theorem|0VKKP8X6Q6]] with $m = 1$ and the constraint $G$, there is a unique $\lambda \in \R$ with $\nabla f(a) = \lambda \nabla G(a)$.
6. By step 3, this says $\nabla f(a) = \lambda \nabla g(a)$, and $\lambda$ is unique.

## Idea

A level set $g = c$ is the zero set of $g - c$, which has the same gradient as $g$. One nonzero gradient is a linearly independent family, so the general theorem applies with one multiplier.
