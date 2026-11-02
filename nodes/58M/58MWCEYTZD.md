---
tag: 58MWCEYTZD
kind: definition
name: Expansive homeomorphism
msc: [37B05]
defines: TAFJV2YWKR
uses: [0VKD1TP7F3, 0QT00PB5G2, A1XE59ZHNM, 02HPP5VCZH, BDZYBXBFDE]
sources:
  - url: https://en.wikipedia.org/wiki/Expansive_homeomorphism
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] and let $f \colon X \to X$ be a [[homeomorphism|0QT00PB5G2]].
The map $f$ is *expansive* if there is a constant $c > 0$ such that for all $x, y \in X$ with $x \neq y$ there is an integer $n \in \Z$ with $d(f^n(x), f^n(y)) > c$.
Such a $c$ is an *expansivity constant* of $f$.

## Remarks

On a compact metric space, expansiveness does not depend on the choice of a metric that gives the topology, although the constant does.
Example: the two-sided full [[shift|A1XE59ZHNM]] $\sigma$ on $\set{0, 1}^{\Z}$ with $d(x, y) = 2^{-\min\set{\abs{i} : x_i \neq y_i}}$ and $c = 1/2$.
If $x \neq y$, pick $i$ with $x_i \neq y_i$; then $\sigma^i(x)$ and $\sigma^i(y)$ differ at coordinate $0$, so their distance is $1 > 1/2$.
Non-example: an [[isometry|02HPP5VCZH]] such as the rotation $x \mapsto x + \alpha \bmod 1$ of the circle.
For any $c > 0$, two distinct points at distance less than $c$ stay at that distance for all $n \in \Z$.
An expansive homeomorphism of a compact metric space has finite [[topological entropy|BDZYBXBFDE]].

## Explanations

### L1 human

A homeomorphism is expansive when any two distinct points are pushed at least a fixed distance apart at some time, past or future.
