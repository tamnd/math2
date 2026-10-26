---
tag: 067F8YVYMH
kind: statement
role: theorem
name: Repeated roots and the derivative
msc: [13F20]
uses: [03XVP8Q4GY, 0AD4VS02H3, 00EHX6FWC0]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_derivative
    locator: Application to finding repeated factors
---

## Statement

Let $R$ be a [[commutative ring|0GYGHKX834]], let $f \in R[x]$ with $f \neq 0$ and let $c \in R$.
Then $c$ is a root of $f$ with [[multiplicity|03XVP8Q4GY]] at least $2$ if and only if $f(c) = 0$ and $f'(c) = 0$.
Here $f'$ is the [[formal derivative|0AD4VS02H3]] of $f$.

## Remarks

The proof: write $f = (x - c) g$. The product rule gives $f' = g + (x - c) g'$, so $f'(c) = g(c)$. And $g(c) = 0$ exactly when $(x - c)^2$ divides $f$.
For example, $f = x^3 - 3x + 2 = (x - 1)^2 (x + 2)$. Here $f(1) = 0$ and $f'(1) = 3 - 3 = 0$.

## Explanations

### L1 human

At a repeated root, the graph of a real polynomial touches the axis and has a horizontal tangent.
So the polynomial and its derivative are both zero there.
The algebraic statement is true over every commutative ring.
