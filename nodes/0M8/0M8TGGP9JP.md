---
tag: 0M8TGGP9JP
kind: statement
role: proposition
name: Approximation property of the supremum
msc: [26A03]
uses: [0BTMQ04556, 0AXWET80YW]
sources:
  - url: https://en.wikipedia.org/wiki/Infimum_and_supremum
    locator: Identifying infima and suprema
---

## Statement

Let $S$ be a nonempty subset of the real numbers that is bounded above, and let $b = \sup S$ be its [[supremum|0BTMQ04556]].
For each real number $c < b$, there is an element $s$ of $S$ with $c < s \le b$.

## Remarks

Proof: if no such $s$ exists, then $c$ is an upper bound of $S$ that is less than $b$. This contradicts the definition of the supremum.
An equivalent form: for each $\varepsilon > 0$, there is $s$ in $S$ with $b - \varepsilon < s$.
For an infimum $a = \inf S$ and each $c > a$, there is $s$ in $S$ with $a \le s < c$.

## Explanations

### L1 human

You can find elements of a set as close to its supremum as you want.
If you lower the ceiling even a little, then some element of the set sticks out above it.
