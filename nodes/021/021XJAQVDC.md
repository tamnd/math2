---
tag: 021XJAQVDC
kind: statement
role: theorem
name: Darboux and Riemann integrals agree
msc: [26A42]
uses: [09FQT057T7, 0N1JQXZXHC, 0QM4TXT3DR]
sources:
  - url: https://en.wikipedia.org/wiki/Darboux_integral
    locator: Refinement of a partition and relation to Riemann integration
---

## Statement

Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be bounded.
Then $f$ is [[Riemann integrable|0N1JQXZXHC]] if and only if its upper and lower [[Darboux integrals|09FQT057T7]] are equal.
In this case the common value is the [[Riemann integral|0QM4TXT3DR]] $\int_a^b f(x)\, dx$.

## Remarks

Each Riemann sum lies between the lower and upper Darboux sums. This gives one direction.
For the other direction, one shows that Darboux sums for partitions of small mesh are close to the Darboux integrals.
So the Riemann and the Darboux approaches define the same integral.

## Explanations

### L1 human

There are two standard ways to define the integral, with Riemann sums or with upper and lower sums.
They give the same integrable functions and the same values.
