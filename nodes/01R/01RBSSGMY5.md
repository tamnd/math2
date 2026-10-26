---
tag: 01RBSSGMY5
kind: concept
name: Definite and indefinite quadratic forms
aliases: [definite-quadratic-form, positive-definite-quadratic-form]
msc: [15A63]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: Matrix form
same_as:
  wikidata: Q1182685
  wikipedia: Definite quadratic form
---

## Summary

Let $A$ be a symmetric $n \times n$ matrix, and let $Q(x) = x^{\mathsf{T}} A x$ be its real quadratic form on $\mathbb{R}^n$. The form $Q$ is positive definite if $Q(x) > 0$ for all $x \ne 0$. It is negative definite if $Q(x) < 0$ for all $x \ne 0$.
It is positive or negative semidefinite if $Q(x) \ge 0$ or $Q(x) \le 0$ for all $x$, and indefinite if it takes both positive and negative values.

## Remarks

The form $Q$ is positive definite if and only if all eigenvalues of $A$ are positive. It is indefinite if and only if $A$ has a positive and a negative eigenvalue.
On $\mathbb{R}^2$, $x_1^2 + x_2^2$ is positive definite, $x_1^2$ is positive semidefinite but not definite, and $x_1^2 - x_2^2$ is indefinite.
In the [[second derivative test|0GYDV9FE98]], the matrix $A$ is the Hessian matrix of a function at a critical point.

## Explanations

### L1 human

A positive definite form is a bowl: it is zero at the origin and positive everywhere else.
An indefinite form is a saddle: it goes up in some directions and down in others.
