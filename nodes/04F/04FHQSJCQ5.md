---
tag: 04FHQSJCQ5
kind: definition
name: Modulo operation
aliases: [mod, remainder]
msc: [11A07]
defines: 03BR7SAX0Q
uses: [0CHQKZFK5S]
sources:
  - url: https://en.wikipedia.org/wiki/Modulo
    locator: Variants of the definition
inventory: [Z384AR9VSY]
---

## Definition

Let $a$ and $n$ be integers with $n \neq 0$.
The integer $a \bmod n$ is the remainder $r$ of the [[division of $a$ by $n$|0CHQKZFK5S]].
Thus $a \bmod n$ is the unique integer $r$ such that $0 \le r < |n|$ and $a - r$ is a multiple of $n$.

## Remarks

For example, $17 \bmod 5 = 2$ and $(-17) \bmod 5 = 3$.
Many programming languages use a different convention. In them, the remainder has the sign of $a$, so the result for $-17$ and $5$ is $-2$.
The Lean library Mathlib sets $a \bmod 0 = a$.

## Explanations

### L1 human

The value $a \bmod n$ is what is left after you take away from $a$ as many copies of $n$ as you can.
A clock uses this operation: $15$ hours after $0$ o'clock, a $12$-hour clock shows $15 \bmod 12 = 3$.
