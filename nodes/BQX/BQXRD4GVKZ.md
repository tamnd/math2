---
tag: BQXRD4GVKZ
kind: example
name: Blancmange curve
msc: [26A27]
instance_of: [0P27W9RW0G]
uses: [0NX5NWAFC9, 0A61B60B5R, 01A0MK1730]
sources:
  - url: https://en.wikipedia.org/wiki/Blancmange_curve
same_as:
  wikidata: Q3001209
  wikipedia: Blancmange curve
---

## Example

For $x \in \R$, let $s(x)$ be the distance from $x$ to the nearest integer, so $0 \le s(x) \le 1/2$.
The *Takagi function* is
$$T(x) = \sum_{n=0}^{\infty} \frac{s(2^n x)}{2^n}.$$
Its graph is the blancmange curve.

Each term is continuous and bounded by $2^{-n-1}$.
By the [[Weierstrass M-test|0NX5NWAFC9]], the series converges uniformly on $\R$, so $T$ is [[continuous|0P27W9RW0G]].
The function $T$ has period $1$ and satisfies $T(0) = 0$ and $T(1/2) = 1/2$.
At $x = 1/3$, each $2^n/3$ has distance $1/3$ to the nearest integer, so $T(1/3) = \sum_{n \ge 0} \frac{1}{3 \cdot 2^n} = \frac 23$.
The maximum value of $T$ is $2/3$.

## Remarks

The function $T$ is [[differentiable|0A61B60B5R]] at no point of $\R$.
The idea of the proof: the partial sum $T_N = \sum_{n < N} s(2^n x)/2^n$ is linear on each interval $[k 2^{-N}, (k+1) 2^{-N}]$.
Its slope there is an integer that changes by $\pm 1$ from $T_N$ to $T_{N+1}$.
So the slopes of $T$ on small dyadic intervals around a point cannot converge.
It is a simpler companion of the [[Weierstrass function|01A0MK1730]], built from tent functions instead of cosines.

## Explanations

### L1 human

Start with a tent of height $1/2$ over each unit interval.
Add tents half as tall and half as wide, then tents a quarter as tall and a quarter as wide, and so on forever.
The sum is a continuous curve that looks like a pudding with ripples at every scale.
Because it has corners at every scale, it has no tangent line anywhere.
It is a concrete continuous nowhere differentiable function.
