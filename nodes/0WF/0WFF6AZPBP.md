---
tag: 0WFF6AZPBP
kind: definition
name: Monotone function
msc: [06A06]
defines: 0A7KV2WB7A
uses: [0RXS8R6K37, 0XHDTE5YMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Monotonic_function
    locator: In order theory
---

## Definition

Let $(P, \le_P)$ and $(Q, \le_Q)$ be [[preorders|0RXS8R6K37]] and let $f \colon P \to Q$ be a [[function|0XHDTE5YMZ]].
The function $f$ is monotone when, for all $a, b \in P$, $a \le_P b$ implies $f(a) \le_Q f(b)$.

## Remarks

Other names are order-preserving and, for real functions, monotonically increasing or non-decreasing.
The function $f$ is antitone when $a \le b$ implies $f(b) \le f(a)$.
The map $S \mapsto f(S)$ on [[power sets|0BC7KX51Z8]] is monotone for $\subseteq$.

## Explanations

### L1 human

A monotone function never reverses the order of two inputs.
On $\mathbb{R}$, $x \mapsto x^3$ is monotone, and $x \mapsto x^2$ is not, because $-2 \le 1$ but $4 > 1$.
