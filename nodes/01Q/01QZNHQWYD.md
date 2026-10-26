---
tag: 01QZNHQWYD
kind: statement
role: theorem
name: Sum of the first n natural numbers
msc: [05A19]
uses: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_number
    locator: Formula
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Sum of consecutive natural numbers
---

## Statement

For every natural number $n$,
$$0 + 1 + 2 + \dots + n = \sum_{k=0}^{n} k = \frac{n(n + 1)}{2}.$$

## Remarks

The number $n(n + 1)/2$ is the $n$th triangular number. For $n = 1, 2, 3, 4$ it is $1, 3, 6, 10$.
A proof by [[induction|0ASJVEFA9J]] uses $\frac{n(n+1)}{2} + (n + 1) = \frac{(n+1)(n+2)}{2}$.
An equivalent form without division is $2 \sum_{k=0}^{n} k = n(n + 1)$.

## Explanations

### L1 human

Write the sum $1 + 2 + \dots + n$ two times, once forward and once backward.
Each column then adds up to $n + 1$, and there are $n$ columns.
So two copies of the sum give $n(n + 1)$, and one copy is half of that.
