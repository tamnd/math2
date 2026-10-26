---
tag: 0XKJPFS2W0
kind: definition
name: Periodic continued fraction
msc: [11A55]
defines: 01GBHQ5ABF
uses: [06XF7BCFFJ]
sources:
  - url: https://en.wikipedia.org/wiki/Periodic_continued_fraction
    locator: Purely periodic and periodic fractions
---

## Definition

An infinite [[simple continued fraction|06XF7BCFFJ]] $[a_0; a_1, a_2, \dots]$ is periodic if there are integers $N \ge 0$ and $k \ge 1$ with $a_{n+k} = a_n$ for all $n \ge N$.
It is purely periodic if this holds with $N = 0$.

## Remarks

One writes the repeating block with a bar, for example $\sqrt{2} = [1; \overline{2}]$ and $\sqrt{3} = [1; \overline{1, 2}]$.
By theorems of Euler and Lagrange, a real number has a periodic continued fraction if and only if it is a quadratic irrational. That is, it is an irrational root of a quadratic equation with integer coefficients.
The period of $\sqrt{d}$ gives the [[fundamental solution of Pell's equation|0KCYJSB9FW]].

## Explanations

### L1 human

A periodic continued fraction repeats the same block of terms forever.
The golden ratio $[1; 1, 1, 1, \dots]$ is the simplest example.
