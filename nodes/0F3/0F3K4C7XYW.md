---
tag: 0F3K4C7XYW
kind: statement
role: theorem
name: Bounded linear maps are continuous
msc: [47B01]
uses: [0S3SMRH0Z5, 0TMZ21WKCN, 07DCKDXRBP]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_operator
    locator: Equivalence of boundedness and continuity
---

## Statement

Let $V$ and $W$ be normed spaces and let $T \colon V \to W$ be linear.
Then $T$ is [[continuous|0S3SMRH0Z5]] if and only if $T$ is bounded, that is, there is a real $C \ge 0$ with $\|Tx\|_W \le C \|x\|_V$ for all $x \in V$.

## Remarks

If $T$ is bounded, then $\|Tx - Ty\|_W = \|T(x - y)\|_W \le C \|x - y\|_V$. Thus $T$ is [[Lipschitz|0TMZ21WKCN]], and so [[uniformly continuous|07DCKDXRBP]].
Conversely, if $T$ is continuous at $0$, there is $\delta > 0$ with $\|Tx\|_W \le 1$ when $\|x\|_V \le \delta$. By linearity, $\|Tx\|_W \le \|x\|_V / \delta$ for all $x$.
Thus, for a linear map, continuity at one point already gives continuity everywhere.
The name bounded means that $T$ maps bounded sets to bounded sets. It does not mean that $T(V)$ is bounded.

## Explanations

### L1 human

For linear maps, continuity is the same as a simple estimate. The length of $Tx$ is at most a fixed multiple of the length of $x$.
