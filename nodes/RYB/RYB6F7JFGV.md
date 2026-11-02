---
tag: RYB6F7JFGV
kind: statement
role: theorem
name: Adjunction formula
msc: [14C20, 14F10]
uses: [EXKGG9X6J0, W05VYY4HBR, FHV05ZK99F, 7JCF2TE3V5]
about: [W05VYY4HBR]
sources:
  - url: https://en.wikipedia.org/wiki/Adjunction_formula
same_as:
  wikidata: Q4683187
  wikipedia: Adjunction formula
---

## Statement

Let $k$ be a field and let $X$ be a variety that is [[smooth|EXKGG9X6J0]] over $k$.
Let $Y \subseteq X$ be a closed subvariety that is smooth over $k$ and of codimension $1$.
Then $Y$ is an effective [[Cartier divisor|FHV05ZK99F]] on $X$, with [[invertible sheaf|7JCF2TE3V5]] $\mathcal{O}_X(Y)$.
The [[canonical bundles|W05VYY4HBR]] satisfy
$$\omega_Y \cong \left(\omega_X \otimes \mathcal{O}_X(Y)\right)|_Y.$$
In terms of divisors, $K_Y = (K_X + Y)|_Y$.

## Remarks

The idea of the proof: for $Y$ smooth with ideal sheaf $\mathcal{I}$, the conormal sequence $0 \to \mathcal{I}/\mathcal{I}^2 \to \Omega_X|_Y \to \Omega_Y \to 0$ is an exact sequence of vector bundles.
Taking top exterior powers gives $\omega_X|_Y \cong \omega_Y \otimes \mathcal{I}/\mathcal{I}^2$.
Since $\mathcal{I} = \mathcal{O}_X(-Y)$, the conormal bundle is $\mathcal{I}/\mathcal{I}^2 \cong \mathcal{O}_X(-Y)|_Y$, and the formula follows.

Example: let $C \subseteq \mathbb{P}^2_k$ be a smooth plane curve of degree $d$.
Then $K_{\mathbb{P}^2} = -3H$ for a line $H$ and $C \sim dH$, so $K_C = (d-3)H|_C$ has degree $d(d-3)$.
Since $\deg K_C = 2g - 2$, this gives the genus $g = (d-1)(d-2)/2$.

For a smooth closed subvariety $Y$ of any codimension $r$, the same argument gives $\omega_Y \cong \omega_X|_Y \otimes \det N_{Y/X}$, where $N_{Y/X}$ is the normal bundle.

## Explanations

### L1 human

The adjunction formula computes the canonical bundle of a hypersurface from that of the ambient space.
One only needs to add the hypersurface itself, viewed as a divisor, and restrict.
This turns questions about a subvariety into questions about the bigger space, where computations are often easy.

### L2 human

The formula is the standard way to compute the genus of curves on surfaces and the canonical class of complete intersections.
For a smooth hypersurface of degree $d$ in $\mathbb{P}^n$ it gives $\omega_Y \cong \mathcal{O}_Y(d - n - 1)$, which decides whether $Y$ is Fano, Calabi–Yau or of general type.
On a surface $X$ it gives the genus formula $2g - 2 = C \cdot (C + K_X)$ for a smooth curve $C$.
