---
tag: 0M98XYVX6S
kind: definition
name: Coefficient of a power series
msc: [13F25]
defines: 0R0D0XY4HT
uses: [072W67KFYK]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_power_series
    locator: Extracting coefficients
---

## Definition

Let $R$ be a commutative ring and let $n$ be a natural number.
The coefficient of $X^n$ is the map $[X^n] : R[\![X]\!] \to R$ that sends a [[formal power series|072W67KFYK]] $f = \sum_{m \ge 0} a_m X^m$ to $a_n$.

## Remarks

The map $[X^n]$ is $R$-linear: $[X^n](f + g) = [X^n] f + [X^n] g$ and $[X^n](r f) = r\, [X^n] f$.
Two series are equal if and only if all their coefficients are equal.
The coefficient of a product is given by the node [[product of power series|0H6KWAYS87]].

## Explanations

### L1 human

The coefficient $[X^n] f$ is the number in front of $X^n$ in the series $f$.
For $f = 1 + 2X + 3X^2 + \dots$, the coefficient $[X^2] f$ is $3$.
