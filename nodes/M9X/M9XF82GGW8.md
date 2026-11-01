---
tag: M9XF82GGW8
kind: statement
role: theorem
name: Fisher's inequality
msc: [05B05]
uses: [TGZATGBHTH, 9DNFN8M83X, 0C3CFHDN6R]
about: [4JCSS2Z1BA]
sources:
  - url: https://en.wikipedia.org/wiki/Fisher%27s_inequality
same_as:
  wikidata: Q5454735
  wikipedia: Fisher's inequality
---

## Statement

Let $v, k, \lambda$ be positive integers with $k < v$.
Let $(X, \mathcal{B})$ be a $2$-$(v, k, \lambda)$ [[block design|TGZATGBHTH]] with $b$ blocks.
Then $b \ge v$.

## Remarks

Proof idea: let $r$ be the number of blocks through a point, and let $N$ be the $v \times b$ [[incidence matrix|9DNFN8M83X]] of points against blocks.
Then $N N^{T} = (r - \lambda) I + \lambda J$, where $I$ is the identity matrix and $J$ is the all-ones matrix of size $v$.
Its [[determinant|0C3CFHDN6R]] is $rk (r - \lambda)^{v - 1}$.
From $r(k - 1) = \lambda(v - 1)$ and $k < v$ one gets $r > \lambda$, so the determinant is not zero.
So $N$ has rank $v$, and a $v \times b$ matrix of rank $v$ needs $b \ge v$.
Example: the [[Fano plane|QQ8GW1ASZM]] is a $2$-$(7, 3, 1)$ design with $b = v = 7$, so the bound is sharp.
The designs with $b = v$ are the symmetric designs; the [[Bruck–Ryser–Chowla theorem|R43K0GTTDS]] restricts their parameters.
The hypothesis $k < v$ is needed.
If $k = v$, every block is the whole set $X$, and $\lambda$ copies of $X$ form a design with $b = \lambda$ blocks, which can be less than $v$.

## Explanations

### L1 human

In a balanced design where every two points share the same number of blocks, there are at least as many blocks as points.
So one cannot save on blocks: balance costs at least one block per point.

### L2 human

Fisher's inequality is a necessary condition for the existence of a design, beyond the divisibility conditions $bk = vr$ and $r(k-1) = \lambda(v-1)$.
Its proof by the rank of the incidence matrix is a model of the [[linear algebra method|DMYGZ3YZ6V]] in combinatorics.
The equality case $b = v$ leads to symmetric designs, such as [[finite projective planes|2HWB7P1DZN]] and the designs built from [[difference sets|MG1KM4S1BV]].
