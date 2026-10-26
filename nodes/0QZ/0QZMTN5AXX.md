---
tag: 0QZMTN5AXX
kind: definition
name: Cauchy sequence
msc: [40A05]
defines: 0PWX18FM4G
uses: [0CTV783HYT]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_sequence
    locator: In real numbers
  - url: https://en.wikipedia.org/wiki/Cauchy_sequence
    locator: In a metric space
---

## Definition

Let $(a_n)$ be a [[real sequence|0CTV783HYT]].
The sequence is a Cauchy sequence if the following holds for each real number $\varepsilon > 0$.
There is a natural number $N$ such that $|a_m - a_n| < \varepsilon$ for all natural numbers $m, n \ge N$.

## Remarks

In a metric space $(X, d)$, the definition is the same with $d(a_m, a_n)$ in place of $|a_m - a_n|$.
The definition does not mention a limit. In $\mathbb{R}$, the [[Cauchy criterion|0ZA4AX4MW3]] shows that the Cauchy sequences are exactly the convergent sequences.
It is not enough that $|a_{n+1} - a_n| \to 0$. The sequence $a_n = \sqrt{n}$ has this property, but it is not Cauchy.

## Explanations

### L1 human

In a Cauchy sequence, the terms become close to each other, not only to their neighbours.
From some index on, any two terms differ by less than the error that you allow.
