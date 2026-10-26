---
tag: 0ZMT1GP4KM
kind: statement
role: proposition
name: Path-connected spaces are connected
msc: [54D05]
uses: [0K0GE6BCYW, 0D939CMME7, 0EPD87YVG8, 0B9ZQFMQNV]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: Path connectedness
---

## Statement

Let $X$ be a [[path-connected space|0K0GE6BCYW]].
Then $X$ is [[connected|0D939CMME7]].

## Remarks

Proof: suppose open sets $U$ and $V$ split $X$, with $x \in U$ and $y \in V$. Take a path $\gamma$ from $x$ to $y$. Then $\gamma([0, 1])$ is connected, by [[continuous image of a connected set is connected|0EPD87YVG8]] and [[connectedness of intervals|0B9ZQFMQNV]]. But $U$ and $V$ split it, a contradiction.
The converse fails, as the [[topologist's sine curve|0K3T4A659R]] shows. It holds for [[open subsets of R^n|0MXN7AFBPE]].

## Explanations

### L1 human

If you can walk between any two points, the space cannot be split into two separate open parts.
