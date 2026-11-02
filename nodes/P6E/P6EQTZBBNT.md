---
tag: P6EQTZBBNT
kind: definition
name: Equicontinuous system
msc: [37B05, 37B02]
defines: NSVEH6VMX8
uses: [0VKD1TP7F3, 0TVJZYB6SH, 0VGFHTM75Y, 0XN66MZN0Y, 02HPP5VCZH]
sources:
  - url: https://en.wikipedia.org/wiki/Equicontinuity
---

## Definition

Let $(X, d)$ be a [[compact|0TVJZYB6SH]] [[metric space|0VKD1TP7F3]] and let $f \colon X \to X$ be a [[continuous map|0VGFHTM75Y]].
The system $(X, f)$ is *equicontinuous* if the family $\set{f^n : n \ge 0}$ is [[equicontinuous|0XN66MZN0Y]].
Since $X$ is compact, this means uniform equicontinuity: for every $\varepsilon > 0$ there is $\delta > 0$ with $d(f^n(x), f^n(y)) < \varepsilon$ for all $n \ge 0$ and all $x, y \in X$ with $d(x, y) < \delta$.

## Remarks

For a homeomorphism one often asks the same of the family $\set{f^n : n \in \Z}$.
Example: every [[isometry|02HPP5VCZH]] $f$ is equicontinuous with $\delta = \varepsilon$, since $d(f^n(x), f^n(y)) = d(x, y)$; for instance the rotation $x \mapsto x + \alpha \bmod 1$ of the circle.
Non-example: the doubling map $f(x) = 2x \bmod 1$ on the circle $\R / \Z$.
Given $\delta > 0$, take $x = 0$ and $y$ with $0 < y < \min(\delta, 1/4)$, and let $n$ be the first integer with $2^n y \ge 1/4$.
Then $f^n(y) = 2^n y$ lies in $[1/4, 1/2)$, at distance at least $1/4$ from $f^n(0) = 0$, so the condition fails for $\varepsilon = 1/4$.

## Explanations

### L1 human

A system is equicontinuous when nearby points stay nearby under all iterates, with one closeness threshold that works for all times.
