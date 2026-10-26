---
tag: 0N1JQXZXHC
kind: definition
name: Riemann integrable function
msc: [26A42]
defines: 0F2QCWVFT7
uses: [0HBY48G8G1, 04GM4NYXJB]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_integral
    locator: Riemann integral
---

## Definition

Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be a function.
The function $f$ is Riemann integrable on $[a, b]$ if there is a real number $I$ with the following property.
For each $\varepsilon > 0$ there is $\delta > 0$ such that $|S(f, P, t) - I| < \varepsilon$ for each tagged partition $(P, t)$ of $[a, b]$ with [[mesh|04GM4NYXJB]] $\| P \| < \delta$.
Here $S(f, P, t)$ is the [[Riemann sum|0HBY48G8G1]] of $f$ for $(P, t)$.

## Remarks

The number $I$ is unique. It is the [[Riemann integral|0QM4TXT3DR]] of $f$.
A Riemann integrable function is bounded.
[[Continuous functions|06SESV7GQY]] and [[monotone functions|04YKAYDQPW]] on $[a, b]$ are Riemann integrable. The [[Dirichlet function|03Z4JC4YRJ]] is not.

## Explanations

### L1 human

A function is Riemann integrable if its Riemann sums settle down to one number as the partitions get finer.
It does not matter which tags we choose in the pieces.
