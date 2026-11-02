---
tag: SFGFWZ4F5N
kind: definition
name: Transform pair
msc: [44A05]
defines: ZA1HC10WM6
uses: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_transform
---

## Definition

Let $T$ be an [[integral transform|YCK709QB06]], defined on a class $A$ of functions.
A *transform pair* for $T$ is a pair $(f, F)$ with $f \in A$ and $F = Tf$.
It is written $f \leftrightarrow F$.

## Remarks

Example: for the Laplace transform $T$ and a real number $a$, the pair $(e^{at}, 1/(s - a))$ is a transform pair, because $\int_0^\infty e^{at} e^{-st}\, dt = 1/(s - a)$ for $s > a$.
Non-example: $(1, 1/s^2)$ is not a Laplace transform pair, because the Laplace transform of $1$ is $1/s$, not $1/s^2$.
When $T$ is injective on $A$, each $F$ in the image determines $f$, and the pair can be read in both directions.
