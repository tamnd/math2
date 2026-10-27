---
tag: 0DPF6WRZW6
kind: definition
name: Degree of a polynomial
msc: [13F20]
defines: 0P4JRMSWNH
uses: [0Q9EZS90GY]
sources:
  - url: https://en.wikipedia.org/wiki/Degree_of_a_polynomial
    locator: Degree of the zero polynomial
inventory: [QNZX912T8Z]
---

## Definition

Let $R$ be a [[ring|0894J980RK]] and let $f = a_0 + a_1 x + \dots + a_n x^n$ be a [[polynomial|0Q9EZS90GY]] in $R[x]$.
If $f \neq 0$, the degree $\deg f$ of $f$ is the largest integer $d$ with $a_d \neq 0$.
The degree of the zero polynomial is $\deg 0 = -\infty$.

## Remarks

The degree of $3x^4 - x + 2$ in $\mathbb{Z}[x]$ is $4$. A nonzero constant polynomial has degree $0$.
Some authors leave $\deg 0$ undefined, or set it to $-1$. The convention $-\infty$ makes the formula $\deg(f g) = \deg f + \deg g$ hold also for $f = 0$ or $g = 0$.
For all $f, g \in R[x]$, $\deg(f + g) \le \max(\deg f, \deg g)$.
The coefficient $a_d$ with $d = \deg f$ is the [[leading coefficient|0P05RJC5XA]] of $f$.

## Explanations

### L1 human

The degree is the highest power of $x$ that really appears in the polynomial.
For example, $x^3 + 5x$ has degree $3$.
The zero polynomial has no nonzero coefficient, so it needs a special convention.
