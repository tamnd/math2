---
tag: 4G7BGMGGK2
kind: definition
name: Smale's degree for proper Fredholm maps
msc: [58C25, 58B15, 47H11]
defines: GVR54SZFX4
uses: [9K15AMGBV9, GFXQ6HEM65, 2V9Q4KHY1T, 15XEBGNGHC]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_operator
---

## Definition

Let $M$ and $N$ be connected $C^2$ [[Banach manifolds|9K15AMGBV9]], with $M$ separable.
Let $f \colon M \to N$ be a $C^2$ [[Fredholm map|GFXQ6HEM65]] of [[Fredholm index|2V9Q4KHY1T]] $0$ that is [[proper|15XEBGNGHC]].
A point $y \in N$ is a *regular value* of $f$ if $df_x$ is surjective for every $x \in f^{-1}(y)$.
For a regular value $y$, the fibre $f^{-1}(y)$ is finite.
The *Smale degree* of $f$ is
$$\deg_2 f = \# f^{-1}(y) \bmod 2 \in \Z/2,$$
for any regular value $y$ of $f$.

## Remarks

The definition makes sense because regular values exist and the parity does not depend on $y$.
Regular values form a residual subset of $N$ by the [[Sard–Smale theorem|Z0NPFYDVP2]].
At a point of $f^{-1}(y)$ the derivative is a surjective Fredholm operator of index $0$, hence an isomorphism, so $f^{-1}(y)$ is discrete; properness makes it compact, hence finite.
The degree is also unchanged under a $C^2$ homotopy $H \colon M \times [0, 1] \to N$ that is proper and is Fredholm of index $0$ at each time.

Example: $f \colon \R \to \R$, $f(x) = x^3$, is proper, and every smooth map between manifolds of the same finite dimension is Fredholm of index $0$.
The value $y = 1$ is regular with the single preimage $x = 1$, so $\deg_2 f = 1$.

Non-example: $g \colon \R \to \R$, $g(x) = e^x$, is Fredholm of index $0$ but not proper.
The regular value $1$ has one preimage and the regular value $-1$ has none, so the parity depends on the point, and no degree is defined.

In finite dimensions, for compact connected manifolds of the same dimension, $\deg_2 f$ is the mod $2$ reduction of the [[degree of a continuous map|TMFG2P912R]].
For compact perturbations of the identity on a Banach space, the [[Leray–Schauder degree|3VJC5Q9MYA]] gives an integer-valued theory.
