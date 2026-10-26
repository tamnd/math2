---
tag: 0P7PTC8DDE
kind: statement
role: theorem
name: Linearity of expectation
aliases: [expectation-is-linear]
msc: [60A05]
uses: [0DCT0QZVQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Expected_value
    locator: Properties
---

## Statement

Let $X$ and $Y$ be integrable real random variables on one probability space, and let $a, b \in \mathbb{R}$.
Then $aX + bY$ is integrable and
$$E[aX + bY] = a \, E[X] + b \, E[Y].$$

## Remarks

The statement is the linearity of the Lebesgue integral. It holds for all integrable $X$ and $Y$, also when they are not independent.
By induction, $E[X_1 + \dots + X_n] = E[X_1] + \dots + E[X_n]$.
A standard use is the method of indicators. If $N$ counts how many of the events $A_1, \dots, A_n$ occur, then $N = \sum_i 1_{A_i}$ and $E[N] = \sum_i P(A_i)$.
For nonnegative random variables, additivity $E[X + Y] = E[X] + E[Y]$ holds without integrability, in $[0, \infty]$.

## Explanations

### L1 human

The average of a sum is the sum of the averages, always.
If a random permutation of $n$ letters goes into $n$ envelopes, each letter is in its own envelope with probability $1/n$. So the expected number of correct letters is $n \cdot 1/n = 1$.
