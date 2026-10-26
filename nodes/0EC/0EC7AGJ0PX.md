---
tag: 0EC7AGJ0PX
kind: definition
name: Exact equation
msc: [34A05]
defines: 0Q1FKQKTKJ
uses: [0P97V20RW7, 04SW7WECS8]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_differential_equation
    locator: First-order exact differential equations
---

## Definition

Let $D$ be an open subset of $\mathbb{R}^2$ and let $M, N : D \to \mathbb{R}$ be continuous functions.
The equation
$$M(x, y) + N(x, y)\, y' = 0,$$
also written $M\, dx + N\, dy = 0$, is exact on $D$ if there is a differentiable function $\psi : D \to \mathbb{R}$ with
$$\frac{\partial \psi}{\partial x} = M \quad \text{and} \quad \frac{\partial \psi}{\partial y} = N \quad \text{on } D.$$
Such a function $\psi$ is a potential function of the equation.

## Remarks

Let the equation be exact. Then a differentiable function $y$ on an interval, with graph in $D$, is a [[solution|04SW7WECS8]] if and only if $\psi(x, y(x))$ is constant. This follows from the chain rule: $\frac{d}{dx} \psi(x, y(x)) = M + N y'$.
So the solutions are given implicitly by $\psi(x, y) = C$.
Example: $2 x y + x^2 y' = 0$ is exact with $\psi = x^2 y$, and its solutions satisfy $x^2 y = C$.
The [[test for exactness|0MSCQNFTM8]] decides whether an equation is exact.

## Explanations

### L1 human

An exact equation is the total derivative of one function $\psi$ set to zero.
So $\psi$ stays constant along each solution, and the solution curves are the level curves of $\psi$.
To solve the equation, you find $\psi$ by integration.
