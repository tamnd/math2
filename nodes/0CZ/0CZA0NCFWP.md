---
tag: 0CZA0NCFWP
kind: definition
name: Singular solution
msc: [34A09]
defines: 0Q2MDD13G4
uses: [04SW7WECS8, 075VBY4K4X, 0SKYFQAFYD]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_solution
    locator: lead section
---

## Definition

Let $F(x, y, y') = 0$ be a first-order [[ordinary differential equation|0P97V20RW7]], and let $y_s : I \to \mathbb{R}$ be a [[solution|04SW7WECS8]] on an open interval $I$.
The solution $y_s$ is singular if uniqueness fails at each point of its graph.
This means the following. For each $x_0 \in I$, there is another solution $y$ on an open interval containing $x_0$ with $y(x_0) = y_s(x_0)$ and $y'(x_0) = y_s'(x_0)$. This solution differs from $y_s$ on each neighbourhood of $x_0$.

## Remarks

Some authors use a weaker meaning: a solution at which the [[initial value problem|075VBY4K4X]] fails to have a unique solution at some point.
A singular solution is often the envelope of a family of solutions. It is not a member of the [[general solution|0SKYFQAFYD]] for any value of the constants.
Example: for $(y')^2 = 4 y$, the solutions $y = (x - C)^2$ are tangent to the solution $y = 0$, so $y = 0$ is singular. [[Clairaut's equation|0T6D4PE51C]] gives other examples.
By the [[uniqueness theorem|025PKW8AMR]], an equation $y' = f(x, y)$ with $f$ Lipschitz in $y$ has no singular solution.

## Explanations

### L1 human

A singular solution is a solution that touches other solutions at each of its points.
It often appears when the method of solution divides by an expression that can be zero.
So after you solve an equation, check what happens when the divisor is zero.
