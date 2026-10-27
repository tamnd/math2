---
tag: 0M9XEDF1HJ
kind: definition
name: Step function
msc: [26A42]
defines: 0AJXYH4DDQ
uses: [069P20KYQT]
sources:
  - url: https://en.wikipedia.org/wiki/Step_function
    locator: Definition and first consequences
inventory: [ZXGSFK61TQ]
---

## Definition

Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be a function.
The function $f$ is a step function if it is constant on each open subinterval of some [[partition|069P20KYQT]] $(x_0, \dots, x_n)$ of $[a, b]$.
That is, there are real numbers $c_1, \dots, c_n$ with $f(x) = c_i$ for all $x \in (x_{i-1}, x_i)$.

## Remarks

The values of $f$ at the points $x_i$ are arbitrary.
A step function is Riemann integrable, and $\int_a^b f = \sum_{i=1}^{n} c_i (x_i - x_{i-1})$.
The floor function $\lfloor x \rfloor$ restricted to $[a, b]$ is a step function.

## Explanations

### L1 human

The graph of a step function looks like a staircase.
It is flat on each piece of a partition, and it can jump at the cut points.
