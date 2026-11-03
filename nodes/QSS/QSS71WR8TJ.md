---
tag: QSS71WR8TJ
kind: statement
role: theorem
name: Matrix exponential of a sum, commuting and non-commuting cases
msc: [15A16]
uses: [020M04FN1H, 8G3X8MPG7E]
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-systems.tex#L5203
    locator: ch-systems.tex:5203
---

## Statement

Let $A$ and $B$ be square matrices of the same size, with real or complex entries. Write $e^A$ for the [[matrix exponential|020M04FN1H]].

1. If $A$ and $B$ [[commute|8G3X8MPG7E]], that is $AB = BA$, then $e^{A+B} = e^A e^B$.

2. If $AB \neq BA$, the equality $e^{A+B} = e^A e^B$ does not hold in general. There are non-commuting pairs $A$, $B$ for which $e^{A+B} \neq e^A e^B$.

## Remarks

For the pair $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ we get $e^A e^B = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$.
But $e^{A+B}$ has diagonal entries $\cosh 1$, so the two sides differ.

Some non-commuting pairs still satisfy the equality, so part 2 does not say that it always fails.
