---
tag: WM4QWH5F65
kind: definition
name: Pseudocompact space
msc: [54D30]
defines: HBGCDP2BRN
uses: [0CQHFPGJ45, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudocompact_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
The space $X$ is *pseudocompact* if every [[continuous map|0VGFHTM75Y]] $f \colon X \to \R$ is bounded, that is, there is a real number $M$ with $\abs{f(x)} \le M$ for all $x \in X$.

## Remarks

Example: a [[compact space|0TVJZYB6SH]] $X$ is pseudocompact.
The image $f(X)$ of a continuous $f \colon X \to \R$ is compact in $\R$, so it is bounded.

Non-example: the real line $\R$ is not pseudocompact.
The identity map $f(x) = x$ is continuous and takes arbitrarily large values.

Some authors require in addition that $X$ be a [[Tychonoff space|C5N2J2K6Z3]].
A normal Hausdorff pseudocompact space is [[countably compact|S3N3CHZV89]].
