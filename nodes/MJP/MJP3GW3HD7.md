---
tag: MJP3GW3HD7
kind: definition
name: Stone–Čech compactification
msc: [54D35]
defines: D9MWP5C85W
uses: [0CQHFPGJ45, 0TVJZYB6SH, 0S1FJ8VEX9, 0VGFHTM75Y, Q6XNC8JAZD]
sources:
  - url: https://en.wikipedia.org/wiki/Stone%E2%80%93%C4%8Cech_compactification
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
A *Stone–Čech compactification* of $X$ is a pair $(\beta X, \iota)$ with the following properties.

1. $\beta X$ is a [[compact|0TVJZYB6SH]] [[Hausdorff space|0S1FJ8VEX9]].
2. $\iota \colon X \to \beta X$ is a [[continuous map|0VGFHTM75Y]].
3. For every compact Hausdorff space $K$ and every continuous map $f \colon X \to K$, there is a unique continuous map $g \colon \beta X \to K$ with $g \circ \iota = f$.

## Remarks

Such a pair exists for every $X$ and is unique up to a unique homeomorphism compatible with $\iota$.
The map $\iota$ is an embedding with dense image exactly when $X$ is a [[Tychonoff space|C5N2J2K6Z3]].
Then $(\beta X, \iota)$ is a [[compactification|Q6XNC8JAZD]] of $X$.

Example: if $X$ is compact Hausdorff, then $\beta X = X$ with $\iota$ the identity.
For a continuous $f \colon X \to K$, the map $g = f$ is the required extension, and it is unique.

Non-example: the one-point compactification $\N \cup \set{\infty}$ of $\N$ is not $\beta \N$.
The map $f \colon \N \to \set{0, 1}$, $f(n) = n \bmod 2$, has no continuous extension.
An extension would need $g(\infty) = \lim g(2n) = 0$ and $g(\infty) = \lim g(2n + 1) = 1$.
