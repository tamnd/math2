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

A real quadratic form can be positive everywhere, negative everywhere, never negative, never positive, or of both signs.
These five types describe the shape of its graph, a bowl, an upside-down bowl, a trough or a saddle, and they decide the type of a critical point in calculus.
Let $Q$ be a [[quadratic form|0RBQS1JJCR]] on a finite-dimensional real vector space $V$, for example $Q(x) = x^{\mathsf{T}} A x$ on $\mathbb{R}^n$ with $A$ symmetric.
The form $Q$ is [[positive definite|0RP20HFYM3]] if $Q(v) > 0$ for all $v \ne 0$, and *negative definite* if $Q(v) < 0$ for all $v \ne 0$.
It is *positive semidefinite* if $Q(v) \ge 0$ for all $v$, and *negative semidefinite* if $Q(v) \le 0$ for all $v$.
It is *indefinite* if it takes both a positive and a negative value.
For a symmetric matrix the type is read from the signs of the eigenvalues, or from the [[signature|07EZA80NEH]].

## Motivation

Near a point where the slope of a smooth function is zero, the function looks like its second-order Taylor term.
That term is a quadratic form, the Hessian form, so the question "minimum, maximum or saddle?" becomes the question "which type is this form?".
This is the second derivative test of several-variable calculus.

The same types appear well beyond calculus.
In optimization, a twice differentiable function is convex on an open convex set exactly when its Hessian form is positive semidefinite at every point.
In statistics every covariance matrix is positive semidefinite.
In mechanics, an equilibrium is stable when the second-order term of the potential energy there is positive definite.
The [[principal axis theorem|0PR5P9Z4KM]] later turns each type into a picture, by rotating the form to a sum of squares.

## Notation

For matrices, books write $A \succ 0$, $A \succeq 0$, $A \prec 0$ and $A \preceq 0$ for positive definite, positive semidefinite, negative definite and negative semidefinite.
For forms, the same conditions are written $Q > 0$, $Q \ge 0$, $Q < 0$ and $Q \le 0$.
Some books say "nonnegative definite" in place of "positive semidefinite".
Books also differ on whether a definite form counts as semidefinite.
We use the inclusive convention, so $x^2 + y^2$ is both positive definite and positive semidefinite.

## Remarks

### Five models in the plane

The simplest forms on $\mathbb{R}^2$ show all five types at once.
The form $x^2 + y^2$ is positive definite, $x^2$ is positive semidefinite, $-x^2 - y^2$ is negative definite, $-y^2$ is negative semidefinite, and $x^2 - y^2$ is indefinite.
For example, $x^2$ is $0$ at $(0, 1)$, so it is not definite, and $x^2 - y^2$ is $1$ at $(1, 0)$ and $-1$ at $(0, 1)$.
[[The five types in the plane|T3WM6BXX8W]] checks each one, and it adds the zero form, which is both positive and negative semidefinite.

### Reading the type from a matrix

How do you find the type of a form with cross terms?
Rotate it to principal axes, where the form is $\lambda_1 y_1^2 + \dots + \lambda_n y_n^2$ and the $\lambda_i$ are the eigenvalues of $A$.
In these coordinates the type depends only on the signs of the $\lambda_i$, and the [[signature|07EZA80NEH]] $(p, q, r)$ counts those signs.

| type | eigenvalues | signature |
|---|---|---|
| positive definite | all $> 0$ | $q = r = 0$ |
| positive semidefinite | all $\ge 0$ | $q = 0$ |
| negative definite | all $< 0$ | $p = r = 0$ |
| negative semidefinite | all $\le 0$ | $p = 0$ |
| indefinite | some $> 0$ and some $< 0$ | $p \ge 1$ and $q \ge 1$ |

The table rests on [[the eigenvalue test|0HYC2RHD3M]] and [[the principal axis theorem|0PR5P9Z4KM]].
For example, $3x^2 + 2xy + 3y^2$ has matrix $\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$ with eigenvalues $4$ and $2$, so it is positive definite.
The form $x^2 + 4xy + y^2$ has eigenvalues $3$ and $-1$, so it is indefinite, and indeed it is $1 - 4 + 1 = -2$ at $(1, -1)$.

### The rules you can use

A form $Q$ is negative definite exactly when $-Q$ is positive definite, so every test for the positive types also tests the negative types.
For a $2 \times 2$ symmetric matrix, the determinant is the product of the two eigenvalues.
So $\det A > 0$ means a definite form, $\det A < 0$ means an indefinite form, and $\det A = 0$ means a semidefinite form that is not definite.
When $\det A > 0$, the sign of the top left entry then says positive or negative.
Every nonzero form is of exactly one of four kinds: positive definite, negative definite, indefinite, or semidefinite but not definite.

### Use in the second derivative test

Let $f$ be a smooth function with a critical point $c$, and let $H$ be its [[Hessian matrix|0693Y2METT]] at $c$.
Taylor's formula gives $f(c + h) = f(c) + \tfrac{1}{2} h^{\mathsf{T}} H h + o(\lVert h \rVert^2)$.
If the form $h^{\mathsf{T}} H h$ is positive definite, $c$ is a strict local minimum, and if it is negative definite, $c$ is a strict local maximum.
If it is indefinite, $c$ is a saddle point.
For $f(x, y) = x^3 - 3x + y^2$ the critical point $(1, 0)$ has Hessian $\operatorname{diag}(6, 2)$ and is a minimum, while $(-1, 0)$ has Hessian $\operatorname{diag}(-6, 2)$ and is a saddle.
[[The worked example|Z4F0TEHBP1]] checks both points.

### What it is not

The five words apply only to real quadratic forms.
A complex form such as $z^2$ on $\mathbb{C}$ has [[no type at all|AWMEN8EZJ6]], because its value at $e^{i\pi/4}$ is $i$, which is neither positive nor negative.
A function that is not quadratic, such as $x^4 + y^4$, is positive at every nonzero vector, but it is not a positive definite form.
Its Hessian at the origin is the zero matrix, so the second derivative test says nothing about it.

### Watch out

Do not read the type from the diagonal entries.
The form $x^2 + 4xy + y^2$ has diagonal entries $1$ and $1$, and it is still indefinite.

Do not use leading minors for the semidefinite types.
The matrix $\operatorname{diag}(0, -1)$ has leading minors $0$ and $0$, but its form is negative semidefinite, not positive semidefinite.

Do not conclude "saddle" from a semidefinite Hessian.
The functions $x^4 + y^2$ and $-x^4 + y^2$ both have Hessian $\operatorname{diag}(0, 2)$ at the origin.
The first has a minimum there, and the second has a saddle.

### Try it

First, find the type of $x^2 - 6xy + 9y^2$.
It equals $(x - 3y)^2$, so it is at least $0$, and it is $0$ at $(3, 1)$: it is positive semidefinite and not definite.

Second, find the type of $-2x^2 + 2xy - y^2$.
The matrix $\begin{pmatrix} -2 & 1 \\ 1 & -1 \end{pmatrix}$ has determinant $2 - 1 = 1 > 0$ and top left entry $-2 < 0$, so the form is negative definite.

## Explanations

### L1 human

Think of the graph of the form as a landscape over the plane.
A positive definite form is a bowl: it is $0$ at the origin and goes up in every direction.
A negative definite form is an upside-down bowl.
A semidefinite form is a trough, flat along a line, as $x^2$ is flat along the $y$-axis.
An indefinite form is a saddle: $x^2 - y^2$ goes up along the $x$-axis and down along the $y$-axis.

### L2 human

Here is a typical task: classify the three forms $3x^2 + 2xy + 3y^2$, $x^2 + 2xy + y^2$ and $x^2 + 4xy + y^2$.
Their matrices have the same diagonal and the off-diagonal entries $1$, $1$ and $2$:
$$\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}, \qquad \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}.$$
The determinants are $8$, $0$ and $-3$.
So the first form is definite, and its top left entry $3$ makes it positive definite.
The second is semidefinite and not definite, and indeed it is $(x + y)^2$, which is $0$ at $(1, -1)$.
The third is indefinite, and it is $-2$ at $(1, -1)$.
Watch out: the determinant shortcut works only for $2 \times 2$ matrices, since in higher dimensions two negative eigenvalues also give a positive product.

### L3 human

At a nondegenerate critical point of a smooth function, the number $q$ of negative eigenvalues of the Hessian is the [[Morse index|MAX2ZYG6H9]], and the [[Morse lemma|ERSD8D4HWX]] says that in suitable coordinates the function is exactly $c - y_1^2 - \dots - y_q^2 + y_{q+1}^2 + \dots + y_n^2$.
So the type of the Hessian form is the local shape of the function, not only an approximation of it.
The positive semidefinite matrices form a closed convex cone, and optimization over this cone is [[semidefinite programming|2RTN2X4R2N]].
Over a field with no order, such as $\mathbb{C}$ or a finite field, the five types disappear, and the invariants of the sub-area, such as the [[discriminant|MZFRXECCMC]], take their place.
