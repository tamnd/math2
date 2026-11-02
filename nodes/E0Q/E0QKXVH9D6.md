---
tag: E0QKXVH9D6
kind: definition
name: Del Pezzo surface
msc: [14J26, 14J45]
defines: AV2ZAAZXN9
uses: [KFTECAATKG, W05VYY4HBR, RRK8P6TXG2, C4KGYAFPN7]
sources:
  - url: https://en.wikipedia.org/wiki/Del_Pezzo_surface
---

## Definition

Let $X$ be a smooth projective [[algebraic surface|KFTECAATKG]] over an algebraically closed field, with [[canonical divisor|W05VYY4HBR]] $K_X$.
$X$ is a *del Pezzo surface* if the anticanonical divisor $-K_X$ is [[ample|RRK8P6TXG2]].
Its *degree* is the self-intersection number $d = K_X^2$.

## Remarks

The degree satisfies $1 \le d \le 9$.
Classification: $X$ is either $\mathbb{P}^1 \times \mathbb{P}^1$, of degree $8$, or the [[blow-up|C4KGYAFPN7]] of $\mathbb{P}^2$ at $9 - d$ points in general position.
Here general position means three conditions.
No three of the points lie on a line, and no six lie on a conic.
No eight lie on a cubic that is singular at one of them.
Example: $\mathbb{P}^2$ has $K = -3L$ for a line $L$, so $-K = 3L$ is ample and $\mathbb{P}^2$ is a del Pezzo surface of degree $9$.
Example: a smooth cubic surface $X \subset \mathbb{P}^3$ has $K_X = -H$ by adjunction, where $H$ is a plane section, so $-K_X$ is ample and $d = H^2 = 3$.
Non-example: blow up $\mathbb{P}^2$ at three points on a line $L$, and let $\tilde L$ be the strict transform of $L$.
Then $\tilde L^2 = 1 - 3 = -2$, and adjunction gives $K \cdot \tilde L = -2 - \tilde L^2 = 0$.
So $-K \cdot \tilde L = 0$, and $-K$ is not ample.
Some authors allow mild singularities, such as ADE singularities, and call the smooth ones nonsingular del Pezzo surfaces.
