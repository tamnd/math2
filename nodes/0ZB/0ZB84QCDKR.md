---
tag: 0ZB84QCDKR
kind: definition
name: Bernoulli equation
msc: [34A34]
defines: 0T92VGGVWP
uses: [0P97V20RW7, 0Z3YKRQZ48]
sources:
  - url: https://en.wikipedia.org/wiki/Bernoulli_differential_equation
    locator: lead section
---

## Definition

Let $I$ be an open interval, let $P, Q : I \to \mathbb{R}$ be continuous functions, and let $n$ be a real number.
A Bernoulli equation is an [[ordinary differential equation|0P97V20RW7]] of the form
$$y' + P(x)\, y = Q(x)\, y^{n}$$
for an unknown function $y$ on a subinterval of $I$, with $y > 0$ when $n$ is not an integer.

## Remarks

For $n = 0$ and $n = 1$ the equation is [[linear|0Z3YKRQZ48]]. Some authors exclude these two values.
For $n \ne 1$, the substitution $v = y^{1 - n}$ changes the equation, on the set where $y \ne 0$, into the linear equation $v' + (1 - n) P(x)\, v = (1 - n) Q(x)$.
For $n > 0$, the function $y = 0$ is also a solution.
The [[logistic equation|0CC4VC7KR3]] is a Bernoulli equation with $n = 2$.

## Explanations

### L1 human

A Bernoulli equation is a linear equation with an extra power of $y$ on the right side.
It is not linear, but a change of the unknown makes it linear.
Then the [[solution formula|06B9W45XV0]] for linear equations solves it.
