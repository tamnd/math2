---
tag: 0Y12QYTJK3
kind: definition
name: Limit at infinity
msc: [26A03]
defines: 01YYRV7S9Z
uses: [0TXTSEMHR5]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_function
    locator: Limits at infinity
---

## Definition

Let $D \subseteq \mathbb{R}$ be a set that is not bounded above, and let $f \colon D \to \mathbb{R}$ be a function.
A real number $L$ is the limit of $f$ at $+\infty$ if for each $\varepsilon > 0$ there is $M$ with $|f(x) - L| < \varepsilon$ for all $x \in D$ with $x > M$.
We then write $\lim_{x \to \infty} f(x) = L$.
The limit at $-\infty$ is defined in the same way, with $x < M$.

## Remarks

A sequence is a function on $\mathbb{N}$. For sequences this definition gives the [[limit of a sequence|0XKWSSY8P2]].
For example, $\lim_{x \to \infty} 1/x = 0$.
Mathlib expresses $x \to \infty$ by the filter `Filter.atTop`.

## Explanations

### L1 human

The limit at infinity is the value that $f(x)$ approaches as $x$ grows without bound.
The graph then gets close to a horizontal line $y = L$.
