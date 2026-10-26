---
tag: 0SJ7Z6VKWK
kind: definition
name: Continued fraction expansion of a real number
msc: [11A55]
defines: 04VA28F3HB
uses: [06XF7BCFFJ]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_continued_fraction
    locator: Calculating continued fraction representations
---

## Definition

Let $x$ be a real number.
Put $x_0 = x$ and $a_0 = \lfloor x_0 \rfloor$.
For $n \ge 0$, if $x_n \neq a_n$, put $x_{n+1} = \dfrac{1}{x_n - a_n}$ and $a_{n+1} = \lfloor x_{n+1} \rfloor$. If $x_n = a_n$, the process stops.
The continued fraction expansion of $x$ is the [[simple continued fraction|06XF7BCFFJ]] $[a_0; a_1, a_2, \dots]$, finite or infinite.

## Remarks

Here $\lfloor y \rfloor$ is the largest integer that is at most $y$. Since $0 < x_n - a_n < 1$, each $a_{n+1}$ with $n \ge 0$ is a positive integer.
For example, $\frac{43}{19} = [2; 3, 1, 4]$, and $\sqrt{2} = [1; 2, 2, 2, \dots]$.
The process stops if and only if $x$ is rational, by the [[termination theorem|0PMY0YQYXX]].
For a rational $x$, the steps are the steps of the [[Euclidean algorithm|0TRNT4X7J0]] on its numerator and denominator.

## Explanations

### L1 human

Take the integer part of $x$, then flip the remaining fractional part, and repeat.
The integer parts that you collect are the terms of the continued fraction of $x$.
