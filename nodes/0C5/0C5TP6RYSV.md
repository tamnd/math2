---
tag: 0C5TP6RYSV
kind: statement
role: proposition
name: Polynomial functions are continuous
msc: [26A15]
uses: [0P27W9RW0G, 0VGMHCF4SC]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial
    locator: Polynomial functions
---

## Statement

Let $a_0, a_1, \dots, a_n$ be real numbers.
Then the function $p \colon \mathbb{R} \to \mathbb{R}$ given by $p(x) = a_0 + a_1 x + \cdots + a_n x^n$ is [[continuous|0P27W9RW0G]].

## Remarks

Constant functions and the identity $x \mapsto x$ are continuous. Sums and [[products of continuous functions are continuous|0VGMHCF4SC]], so induction on $n$ gives the result.
Mathlib states it as `Polynomial.continuous`.

## Explanations

### L1 human

Polynomials are built from $x$ and constants by addition and multiplication.
These operations keep continuity, so each polynomial is continuous.
