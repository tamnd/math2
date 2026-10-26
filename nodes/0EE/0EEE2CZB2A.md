---
tag: 0EEE2CZB2A
kind: definition
name: Continuity at a point
msc: [26A15]
defines: 0KRMJRDRZT
uses: [0TXTSEMHR5]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Definition in terms of neighborhoods
---

## Definition

Let $D \subseteq \mathbb{R}$, let $f \colon D \to \mathbb{R}$ be a function, and let $a \in D$.
The function $f$ is continuous at $a$ if the following holds.
For each open interval $V$ containing $f(a)$ there is an open interval $U$ containing $a$ with $f(x) \in V$ for all $x \in U \cap D$.

## Remarks

If $a$ is a limit point of $D$, then $f$ is continuous at $a$ if and only if $\lim_{x \to a} f(x) = f(a)$. See [[limit of a function|0TXTSEMHR5]].
If $a$ is an isolated point of $D$, then each function on $D$ is continuous at $a$.
The [[epsilon-delta form|0W8YHHGCJG]] states the same condition with numbers.
Mathlib defines it for topological spaces, as `ContinuousAt`.

## Explanations

### L1 human

A function is continuous at $a$ if small changes of $x$ near $a$ give small changes of $f(x)$.
The graph has no jump or gap at $a$.
