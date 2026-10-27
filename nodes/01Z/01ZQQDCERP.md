---
tag: 01ZQQDCERP
kind: definition
name: Open set
msc: [54A05]
defines: 02BH3MCBQB
uses: [0CNQXVBHCX, 0A6YRNZB2R]
sources:
  - url: https://en.wikipedia.org/wiki/Open_set
    locator: Definitions
inventory: [ZJWQG7TFXR]
---

## Definition

Let $(X, \tau)$ be a [[topological space|0CNQXVBHCX]].
A subset $U$ of $X$ is open in $X$ when $U \in \tau$.
A subset of a [[metric space|063W5JMY85]] is open when it is open for the [[metric topology|0A6YRNZB2R]].

## Remarks

In a metric space $(X, d)$, a set $U$ is open if and only if for each $x \in U$ there is $\varepsilon > 0$ with $B(x, \varepsilon) \subseteq U$. This is the statement [[open sets of a metric space|0A26X79RTB]].
In $\mathbb{R}$, each open interval $(a, b)$ is open, but $[0, 1)$ is not open: no ball about $0$ lies in $[0, 1)$.
The empty set and $X$ are always open.

## Explanations

### L1 human

In a metric space, an open set has no edge points. From each of its points, you can move a little in any direction and stay in the set.
The interval $(0, 1)$ is open, because each point has some room on both sides.
