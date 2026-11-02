---
tag: MME2BSPTZG
kind: definition
name: Schwarz triangle function
msc: ["33C05", "30C20"]
defines: XMD3Q49Z2C
uses: [W8VE25R5A7, 463X5V31D9, 0YYT36R4YD]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarz_triangle_function
---

## Definition

Let $a, b, c \in \C$, and let $w_1, w_2$ be two linearly independent solutions of the [[hypergeometric differential equation|W8VE25R5A7]] on the upper half-plane $\mathbb{H} = \set{z \in \C : \operatorname{Im} z > 0}$.
A *Schwarz triangle function* is the ratio
$$s(z) = \frac{w_2(z)}{w_1(z)}, \qquad z \in \mathbb{H}.$$
When $c \notin \Z$, the standard choice uses the two solutions at $0$:
$$s(z) = \frac{z^{1-c} \, {}_2F_1(a - c + 1, b - c + 1; 2 - c; z)}{{}_2F_1(a, b; c; z)},$$
with the principal branch of $z^{1-c}$ and the [[hypergeometric function|463X5V31D9]] ${}_2F_1$.

## Remarks

Changing the pair of solutions replaces $s$ by $(\alpha s + \beta)/(\gamma s + \delta)$ with $\alpha\delta - \beta\gamma \neq 0$, so $s$ is well defined up to a Möbius transformation.

Let $a, b, c$ be real and set $\lambda = 1 - c$, $\mu = c - a - b$, $\nu = a - b$.
If $0 \le \lambda, \mu, \nu < 1$, then $s$ is a [[conformal map|0YYT36R4YD]] from $\mathbb{H}$ onto a triangle bounded by circular arcs or segments.
Its angles are $\pi\lambda$, $\pi\mu$, $\pi\nu$ at the images of $0$, $1$, $\infty$.

Example: for $a = b = \frac12$, $c = 1$ all three angles are $0$.
Here $c \in \Z$, so the ratio is formed with the logarithmic second solution.
Up to a Möbius transformation it equals $\tau = i \, K(1 - z)/K(z)$.
Here $K(m) = \frac{\pi}{2} {}_2F_1(\frac12, \frac12; 1; m)$ is the complete elliptic integral of the first kind.
Its inverse is the modular lambda function.

Non-example: a ratio $w_2 / w_1$ of two proportional solutions is constant, so it is not a triangle function; independence of $w_1$ and $w_2$ is needed.
