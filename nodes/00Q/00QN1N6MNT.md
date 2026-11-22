---
tag: 00QN1N6MNT
kind: definition
name: Positive definite quadratic form
msc: [15A63, "11E04"]
defines: 0RP20HFYM3
topics: [6TSCEW8QMK]
audience: ug1
uses: [0HZNE5QZDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: lead section
inventory: [R63EXRT7EA]
---

## Definition

A positive definite quadratic form is a real quadratic form that is positive at every nonzero vector.

Let $V$ be a finite-dimensional real vector space, and let $Q$ be a [[quadratic form|0HZNE5QZDJ]] on $V$.
The form $Q$ is *positive definite* when
$$Q(v) > 0 \qquad \text{for all } v \in V \text{ with } v \ne 0.$$

## Remarks

The field is $\mathbb{R}$ because the condition compares values with $0$, and that needs an ordered field.
Over $\mathbb{C}$ a quadratic form has no sign at all, as [[the form z squared|AWMEN8EZJ6]] shows: $z^2$ is $1$ at $z = 1$ and $-1$ at $z = i$.
The condition excludes $v = 0$ because every quadratic form has $Q(0) = 0$.

For $Q(x) = x^{\mathsf{T}} A x$ on $\mathbb{R}^n$ with $A$ symmetric, the definition says that $A$ is a [[positive definite matrix|0KX66CZMBB]].
For example, $x^2 + y^2$ is positive definite on $\mathbb{R}^2$, since it is a sum of two squares that vanish together only at the origin.
The form $x^2$ fails the condition at the nonzero vector $(0, 1)$, where it is $0$.
An equivalent condition is that the [[signature|07EZA80NEH]] of $Q$ is $(n, 0, 0)$ with $n = \dim V$.
Another is that the polar form of $Q$ is an inner product on $V$.
The tests and the examples are with [[the concept of a positive definite form|0RP20HFYM3]].

## Explanations

### L1 human

A positive definite form is positive everywhere except at the origin.
Its graph over the plane is a bowl with its lowest point at the origin.
For $x^2 + y^2$, the point $(1, 2)$ gives $1 + 4 = 5$, and only $(0, 0)$ gives $0$.
