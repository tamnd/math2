---
tag: NXTV4Y81ZJ
kind: definition
name: Brody hyperbolicity
msc: [32Q45]
defines: Y7W36GJDJD
uses: [JSGWAN2RJV, 3MQTWKBBBT, 0EHKVRF4J6, HRPAX8V7HA]
sources:
  - url: https://en.wikipedia.org/wiki/Kobayashi_metric
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]].
An *entire curve* in $X$ is a nonconstant [[holomorphic map|3MQTWKBBBT]] $f \colon \C \to X$.
The manifold $X$ is *Brody hyperbolic* if there is no entire curve in $X$, that is, if every holomorphic map $\C \to X$ is constant.

## Remarks

Example: the unit disc $\mathbb{D}$ is Brody hyperbolic, since a holomorphic map $\C \to \mathbb{D}$ is a bounded entire function, hence constant by [[Liouville's theorem|0EHKVRF4J6]].
Example: a compact Riemann surface of genus $g \ge 2$ is Brody hyperbolic, because an entire curve would lift to a holomorphic map from $\C$ to its universal covering, the unit disc.
Non-example: $\C^n$ and the complex projective space $\mathbb{P}^n$ contain lines $t \mapsto (t, 0, \dots, 0)$ and $t \mapsto [1 : t : 0 : \cdots : 0]$, so they are not Brody hyperbolic.
Every [[Kobayashi hyperbolic manifold|HRPAX8V7HA]] is Brody hyperbolic, since an entire curve $f$ gives $k_X(f(a), f(b)) \le k_\C(a, b) = 0$.
For compact $X$ the two notions agree by [[Brody's lemma|VEV5E2077C]]; for noncompact $X$ they can differ.
