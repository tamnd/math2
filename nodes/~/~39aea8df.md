---
tag: ~39aea8df
kind: definition
name: Fundamental solution of Pell's equation
msc: [11D09]
defines: ~c915317f
uses: [~a372665d, ~c8121d6d]
sources:
  - url: https://en.wikipedia.org/wiki/Pell%27s_equation
    locator: Fundamental solution via continued fractions
---

## Definition

Let $d$ be a positive integer that is not a perfect square.
The fundamental solution of [[Pell's equation|~a372665d]] $x^2 - d y^2 = 1$ is the solution $(x_1, y_1)$ with $x_1 > 1$ and $y_1 > 0$ such that $x_1$ is as small as possible.

## Remarks

The fundamental solution exists by the [[existence of nontrivial solutions|~c8121d6d]].
Among the solutions with $x > 1$ and $y > 0$, it also has the smallest $y$ and the smallest value of $x + y \sqrt{d}$.
For example, the fundamental solution for $d = 2$ is $(3, 2)$, and for $d = 7$ it is $(8, 3)$.
It appears among the convergents of the continued fraction of $\sqrt{d}$.

## Explanations

### L1 human

The fundamental solution is the smallest solution with positive entries.
All other solutions come from it by taking [[powers|~d3134314]] of $x_1 + y_1 \sqrt{d}$.
