---
tag: 0S3SMRH0Z5
kind: definition
name: Continuous linear map
msc: [47B01]
defines: 03TM135G0N
uses: [0J3578562S, 0SY9ECQ19Q]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_operator
    locator: In normed vector spaces
---

## Definition

Let $V$ and $W$ be vector spaces over $\mathbb{R}$ or $\mathbb{C}$, with [[norms|0J3578562S]] $\|\cdot\|_V$ and $\|\cdot\|_W$.
A map $T \colon V \to W$ is a continuous linear map when $T$ is linear and [[continuous|0SY9ECQ19Q]] for the metrics $\|x - y\|_V$ and $\|x - y\|_W$.

## Remarks

A linear map is continuous if and only if it is bounded, that is, $\|Tx\|_W \le C \|x\|_V$ for some constant $C$ and all $x$. This is [[bounded linear maps are continuous|0F3K4C7XYW]].
The smallest such $C$ is the [[operator norm|0ZTEH055YF]] of $T$.
On a finite-dimensional space, [[each linear map is continuous|0C13E623WD]].
The derivative $p \mapsto p'$ on polynomials, with the sup norm on $[0, 1]$, is linear but not continuous: $\|x^n\|_\infty = 1$ but $\|n x^{n-1}\|_\infty = n$.

## Explanations

### L1 human

A continuous linear map respects the vector space structure and also the notion of closeness.
In infinite dimensions, a linear map can fail to be continuous, so this is a real condition.
