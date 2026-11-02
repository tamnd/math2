---
tag: 38CEJPFESJ
kind: definition
name: Minkowski functional
msc: [46A03, 52A07]
defines: PAX9SHDHDW
uses: [NM1BCK3ZX9, 05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski_functional
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, let $V$ be a [[vector space|05EGHEQZAW]] over $\mathbb{K}$, and let $K \subseteq V$ be an [[absorbing set|NM1BCK3ZX9]].
The *Minkowski functional* (or *gauge*) of $K$ is the map $p_K \colon V \to [0, \infty)$ given by
$$p_K(x) = \inf \set{t > 0 : x \in t K}.$$

## Remarks

Since $K$ is absorbing, the set $\set{t > 0 : x \in tK}$ is nonempty, so $p_K(x)$ is a finite number.
If $K$ is convex, then $p_K$ is sublinear: $p_K(x + y) \le p_K(x) + p_K(y)$ and $p_K(s x) = s \, p_K(x)$ for $s \ge 0$.
If $K$ is convex and [[balanced|2TDSHJJYS4]], then $p_K$ is a [[seminorm|FP5GVCN8GV]].
Example: let $\norm{\cdot}$ be a norm on $V$ and $K = \set{x : \norm{x} \le 1}$; then $x \in tK$ if and only if $\norm{x} \le t$, so $p_K(x) = \norm{x}$.
Non-example: in $\R^2$ the segment $K = [-1, 1] \times \set{0}$ is not absorbing, and for $x = (0, 1)$ the set $\set{t > 0 : x \in tK}$ is empty, so no finite value $p_K(x)$ is defined.
Some authors allow any set $K$ and set $p_K(x) = \infty$ when no $t$ exists.
In a topological vector space, the Minkowski functional of a convex open neighbourhood $K$ of $0$ is continuous, and $K = \set{x : p_K(x) < 1}$.
