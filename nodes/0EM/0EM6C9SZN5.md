---
tag: 0EM6C9SZN5
kind: statement
role: theorem
name: Existence of nontrivial solutions of Pell's equation
msc: [11D09]
uses: [0AF3DANJ76]
sources:
  - url: https://en.wikipedia.org/wiki/Pell%27s_equation
    locator: lead section
---

## Statement

Let $d$ be a positive integer that is not a perfect square.
Then [[Pell's equation|0AF3DANJ76]] $x^2 - d y^2 = 1$ has a solution in integers with $y \neq 0$.
In fact, it has infinitely many solutions in integers.

## Remarks

One proof uses [[Dirichlet's approximation theorem|04JAY9DGB7]] to find infinitely many $x/y$ with $|x^2 - d y^2|$ bounded.
Another proof uses the [[periodic continued fraction|0XKJPFS2W0]] of $\sqrt{d}$.
The smallest solution can be very large. For $d = 61$, it is $(1766319049, 226153980)$.

## History

Indian mathematicians, such as Brahmagupta, studied the equation many centuries before European mathematicians.
Lagrange proved that it always has infinitely many solutions.

## Explanations

### L1 human

For each non-square $d$, there are integers $x$ and $y \neq 0$ with $x^2 - d y^2 = 1$.
They may be hard to find by trial: for $d = 61$, the smallest $x$ has ten digits.
