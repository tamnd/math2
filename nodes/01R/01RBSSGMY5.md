---
tag: 01RBSSGMY5
kind: concept
name: Definite and indefinite quadratic forms
aliases: [definite-quadratic-form]
msc: [15A63]
topics: [6TSCEW8QMK]
audience: ug1
uses: [0RBQS1JJCR, 0RP20HFYM3, 07EZA80NEH]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: Matrix form
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-2.xml#L1073
    locator: src/section7-2.xml:1073
same_as:
  wikidata: Q1182685
  wikipedia: Definite quadratic form
---

## Summary

Let $Q$ be a real [[quadratic form|0RBQS1JJCR]] on a finite-dimensional real vector space $V$, for example $Q(x) = x^T A x$ on $\R^n$ with $A$ symmetric.
$Q$ is [[positive definite|0RP20HFYM3]] if $Q(v) > 0$ for all $v \ne 0$, and negative definite if $Q(v) < 0$ for all $v \ne 0$.
It is positive semidefinite if $Q(v) \ge 0$ for all $v$, and negative semidefinite if $Q(v) \le 0$ for all $v$.
It is indefinite if it takes both positive and negative values.
These five types describe the shape of the graph of $Q$ near $0$.
They decide the type of a critical point in the second derivative test.

## Motivation

The graph of $Q(x, y)$ over the plane is a bowl, an upside-down bowl, a trough or a saddle.
The type of $Q$ says which one.
At a critical point of a smooth function, the second-order Taylor term is a quadratic form, the Hessian form.
So the five types give the local behaviour of the function: minimum, maximum or saddle, when the Hessian is nondegenerate.

## Notation

- $Q > 0$, $Q \ge 0$, $Q < 0$, $Q \le 0$ for the four definite and semidefinite types; for matrices, $A \succ 0$, $A \succeq 0$, $A \prec 0$, $A \preceq 0$.
- Some books say "nonnegative definite" for positive semidefinite.
- Some books count the definite forms as semidefinite, and others use "semidefinite" only for forms that are not definite. This page uses the first convention.

## Remarks

### Examples

- On $\R^2$, the forms $x^2 + y^2$, $x^2$, $-x^2 - y^2$, $-y^2$ and $x^2 - y^2$ show the five types in the order of the table. See [[the five types in the plane|~265ce1cc]].
- The zero form is both positive semidefinite and negative semidefinite.
- [[The second derivative test for $x^3 - 3x + y^2$|~3f51fbd9]] uses a positive definite Hessian at one critical point and an indefinite one at the other.
- The form $xy$ is indefinite: $Q(1, 1) = 1$ and $Q(1, -1) = -1$.

### Non-examples

- [[A complex quadratic form such as $z^2$|~ee2bc073]] has no type, because its values are not real: $Q(e^{i\pi/4}) = i$.
- A function that is not a quadratic form, such as $x^4 + y^4$, is positive at every nonzero vector, but the words apply only to quadratic forms. Its Hessian at $0$ is the zero matrix.

### Basic properties

For $Q(x) = x^T A x$ with $A$ symmetric, the type is read from the signs of the eigenvalues of $A$, or from the [[signature|07EZA80NEH]] $(p, q, r)$.

| type | eigenvalues | signature |
|---|---|---|
| positive definite | all $> 0$ | $q = r = 0$ |
| positive semidefinite | all $\ge 0$ | $q = 0$ |
| negative definite | all $< 0$ | $p = r = 0$ |
| negative semidefinite | all $\le 0$ | $p = 0$ |
| indefinite | some $> 0$ and some $< 0$ | $p \ge 1$ and $q \ge 1$ |

The table follows from [[the eigenvalue test|0HYC2RHD3M]] and from [[the principal axis theorem|0PR5P9Z4KM]].
$Q$ is negative definite if and only if $-Q$ is positive definite.
Every form is exactly one of: positive definite, negative definite, indefinite, or semidefinite but not definite.

### History

We found no source in the reading list of this topic that dates these terms, so we give no date.

### Common errors

- Reading the type from the diagonal entries of a non-diagonal matrix.
- Using the leading minors for semidefinite forms. For $\operatorname{diag}(0, -1)$ both leading minors are $0$, but the form is negative semidefinite, not positive semidefinite.
- Concluding "saddle" from a semidefinite Hessian. For $x^4 + y^2$ and $-x^4 + y^2$ the Hessian at $0$ is $\operatorname{diag}(0, 2)$, but the first has a minimum and the second a saddle.

## Explanations

### L1 human

A positive definite form is a bowl: it is zero at the origin and positive everywhere else.
A negative definite form is an upside-down bowl.
A semidefinite form is a trough: it is zero along a line or a plane.
An indefinite form is a saddle: it goes up in some directions and down in others.

### L2 human

Worked example: classify $Q = 3x^2 + 2xy + 3y^2$, $Q' = x^2 + 2xy + y^2$ and $Q'' = x^2 + 4xy + y^2$.

1. $Q$ has matrix $\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$ with eigenvalues $4$ and $2$. It is positive definite.
2. $Q' = (x + y)^2$ has eigenvalues $2$ and $0$. It is positive semidefinite, and $Q'(1, -1) = 0$.
3. $Q''$ has eigenvalues $3$ and $-1$. It is indefinite, and $Q''(1, -1) = -2$.

A trap: for $2 \times 2$ forms the sign of $\det A$ already separates definite ($\det A > 0$) from indefinite ($\det A < 0$); the sign of $a$ then separates positive from negative.

### L3 human

The type of the Hessian form is the second-order information in Morse theory.
At a nondegenerate critical point, the number $q$ of negative eigenvalues is the Morse index.
In optimization, a function is convex on an open convex set if and only if its Hessian is positive semidefinite at every point.
Semidefinite matrices are the feasible sets of semidefinite programming.
