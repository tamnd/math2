---
tag: 04SW7WECS8
kind: definition
name: Solution of an ordinary differential equation
msc: [34A99]
defines: 07VX34QXAV
uses: [0P97V20RW7, 0Q1D85B8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinary_differential_equation
    locator: Solutions
  - url: https://en.wikipedia.org/wiki/Integral_curve
    locator: Definition
---

## Definition

Let $F\left(x, y, y', \dots, y^{(n)}\right) = 0$ be an [[ordinary differential equation|0P97V20RW7]] of order $n$, with $F$ defined on a set $U \subseteq \mathbb{R}^{n+2}$.
Let $I$ be an open [[interval|0Q1D85B8G6]] of $\mathbb{R}$.
A solution of the equation on $I$ is a function $u : I \to \mathbb{R}$ with these two properties.
The function $u$ is $n$ times differentiable on $I$, and $\left(x, u(x), u'(x), \dots, u^{(n)}(x)\right) \in U$ for each $x \in I$.
For each $x \in I$, $F\left(x, u(x), u'(x), \dots, u^{(n)}(x)\right) = 0$.
For a system, $u$ takes values in $\mathbb{R}^m$ and the same two conditions hold.

## Remarks

Consider the first-order system $x' = f(x)$, with a vector field $f$ on an open set of $\mathbb{R}^m$. A solution is a curve whose velocity at each time is the value of $f$ at its position. Such a curve is an integral curve of $f$.
The function $u(x) = e^{2x}$ is a solution of $y' = 2y$ on $\mathbb{R}$.
A solution on $I$ restricts to a solution on each open subinterval of $I$. A [[maximal solution|01J7FZ65J0]] is a solution that has no extension to a larger interval.

## Explanations

### L1 human

To check that a function is a solution, put it and its derivatives into the equation.
If both sides are equal at each point of the interval, the function is a solution there.
For example, $u(x) = \sin x$ gives $u'' + u = -\sin x + \sin x = 0$, so it solves $y'' + y = 0$.
