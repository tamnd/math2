---
tag: WC8M1YAYCD
kind: definition
name: Hyperelliptic curve
msc: [14H45, 14H55]
defines: 5SB8EKSQRN
uses: [XJM2MT4S3Y, 6W8TDV9VVN, ZT9A6JK8QF, CDS1VWB7A3, 0PF6TM8TWT]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperelliptic_curve
---

## Definition

Let $k$ be an [[algebraically closed field|0PF6TM8TWT]], and let $\mathbb{P}^1$ be the [[projective line|ZT9A6JK8QF]] over $k$.
A smooth projective [[algebraic curve|XJM2MT4S3Y]] $X$ over $k$ is *hyperelliptic* if:

1. its [[genus|6W8TDV9VVN]] $g$ satisfies $g \ge 2$, and
2. there is a finite [[morphism|CDS1VWB7A3]] $X \to \mathbb{P}^1$ of degree $2$.

## Remarks

If the characteristic of $k$ is not $2$, such an $X$ is the smooth projective model of an affine curve $y^2 = f(x)$.
Here $f \in k[x]$ is squarefree of degree $2g + 1$ or $2g + 2$, and the degree-$2$ map is $(x, y) \mapsto x$.
The degree-$2$ map is unique up to automorphisms of $\mathbb{P}^1$, and it defines the hyperelliptic involution $y \mapsto -y$.
Example: $y^2 = x^5 - x$ over $\C$ has $f$ squarefree of degree $5 = 2 \cdot 2 + 1$, so it defines a hyperelliptic curve of genus $2$.
In fact every curve of genus $2$ is hyperelliptic, because its canonical divisor gives a map of degree $2$ to $\mathbb{P}^1$.
Non-example: a smooth plane quartic has genus $3$ but is not hyperelliptic, because its canonical map is the embedding into the plane and so has degree $1$, not $2$.
Curves of genus $1$ with a point are also double covers of $\mathbb{P}^1$, but they fail clause 1 and are called elliptic curves.
