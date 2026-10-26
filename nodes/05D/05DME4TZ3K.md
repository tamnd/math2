---
tag: 05DME4TZ3K
kind: object
name: Pascal's triangle
msc: [05A10]
sources:
  - url: https://en.wikipedia.org/wiki/Pascal's_triangle
    locator: Formula
same_as:
  wikidata: Q177051
  wikipedia: Pascal's triangle
---

## Description

Pascal's triangle is the triangular array of the [[binomial coefficients|092GEF38YD]].
Its rows are numbered $n = 0, 1, 2, \dots$ from the top.
Row $n$ has $n + 1$ entries, $\binom{n}{0}, \binom{n}{1}, \dots, \binom{n}{n}$, from left to right.

The first five rows are these.
$$\begin{array}{ccccccccc} & & & & 1 & & & & \\ & & & 1 & & 1 & & & \\ & & 1 & & 2 & & 1 & & \\ & 1 & & 3 & & 3 & & 1 & \\ 1 & & 4 & & 6 & & 4 & & 1 \end{array}$$

Each row starts and ends with $1$.
Each other entry is the sum of the two entries next to it in the row above, by [[Pascal's rule|0YRG241HQQ]].

## Remarks

Row $n$ lists the coefficients of $(x + y)^n$, by the [[binomial theorem|0EHWPWGHB2]].
The sum of row $n$ is $2^n$. This is the [[sum of binomial coefficients|0KAMF19NV8]].
Each row is symmetric, by the [[symmetry of binomial coefficients|0R7JS3DP3W]].

## Explanations

### L1 human

Start with a $1$ at the top. Each new row starts and ends with $1$, and each inside number is the sum of the two numbers above it.
Row 4 is $1, 4, 6, 4, 1$, and these are the coefficients of $(x + y)^4$.
