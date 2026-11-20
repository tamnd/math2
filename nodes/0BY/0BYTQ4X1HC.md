---
tag: 0BYTQ4X1HC
kind: concept
name: Least squares
msc: [65F20, 15A06]
topics: [8GQVME4SZZ]
audience: ug1
uses: [0MCDDSCB9Z, 0Q8HZTJC7G, 0W809K6AW0, 03AJKXH1AV]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_least_squares
    locator: Basic formulation
  - url: https://en.wikipedia.org/wiki/Least_squares
    locator: History
  - book: isbn:9780321982384
    locator: Section 6.5
  - book: isbn:9781733146678
    locator: Chapter 4
same_as:
  wikidata: Q6553462
  wikipedia: Linear least squares
---

## Summary

Let $A$ be a real $m \times n$ matrix and let $b \in \R^m$, with the Euclidean norm $\norm{y} = \sqrt{y^{\mathsf{T}} y}$.
A *least-squares solution* of $Ax = b$ is a vector $\hat x \in \R^n$ with $\norm{A \hat x - b} \le \norm{Ax - b}$ for every $x \in \R^n$.
The vector $b - A \hat x$ is the *residual*, and $\norm{b - A \hat x}^2$ is the sum of the squares of its entries, which gives the method its name.
By the [[best approximation theorem|0MCDDSCB9Z]], $\hat x$ is a least-squares solution exactly when $A \hat x$ is the [[orthogonal projection|0Q8HZTJC7G]] of $b$ onto the [[column space|03AJKXH1AV]] of $A$.
Least squares is the standard way to fit a model with few parameters to many inexact measurements.

## Motivation

A system with more equations than unknowns, an [[overdetermined system|QJ0P26J9BV]], usually has no solution.
For example, no line passes through four points that are not on one line.
Measured data always contain errors, so an exact solution would not be meaningful anyway.
The least-squares method replaces "solve $Ax = b$" by "make $Ax$ as close as possible to $b$".
It turns a problem with no answer into a problem of projection, which has an answer.

## Notation

We write $\hat x$ for a least-squares solution and $r = b - A \hat x$ for the residual.
Some books write $\min_x \norm{Ax - b}_2$ or $\operatorname{argmin}_x \norm{Ax - b}^2$.
The [[transpose|0W809K6AW0]] is written $A^{\mathsf{T}}$; Lay writes $A^T$.

## Remarks

### Examples

1. [[A least-squares line through four points|H2D0QA4AXV]]: the line $y = 0.9 + 0.9 t$ fits $(0, 1)$, $(1, 2)$, $(2, 2)$, $(3, 4)$ with residual sum of squares $7/10$.
2. [[Least squares with dependent columns|FM9VEAKSA7]]: for $A$ with two parallel columns, the least-squares solutions form a line, and the closest point $A \hat x$ is still unique.
3. If $Ax = b$ has a solution, then the least-squares solutions are the exact solutions, and the residual is $0$; see [[the consistent overdetermined system|XYTJ19AEKC]].
4. For $A = (1, 1, \dots, 1)^{\mathsf{T}}$, an $m \times 1$ column, the least-squares solution of $Ax = b$ is the mean $\frac{1}{m} \sum_i b_i$.
5. [[Least squares by QR|JAHVYKS2VQ]] and [[least squares by the SVD|SBP2PCHH9M]] compute the same $\hat x$ by other routes.

### Non-examples

1. [[A line through three of the four points|MH3VAGXW9R]]: the line $y = 1 + t$ fits three points exactly but has residual sum of squares $1 > 7/10$, so it is not a least-squares solution.
2. Minimizing the sum of absolute values $\sum_i \abs{(Ax - b)_i}$ is a different problem. Its solutions need not be least-squares solutions, and the method of projection does not apply to it.

### Basic properties

- A least-squares solution always exists, and it is unique exactly when the columns of $A$ are linearly independent, by [[existence and uniqueness of least-squares solutions|V9AH43ZY91]].
- The least-squares solutions are exactly the solutions of the [[normal equations|4D7MRG4D91]] $A^{\mathsf{T}} A \hat x = A^{\mathsf{T}} b$, and the residual is orthogonal to every column of $A$.
- With a [[QR decomposition|0ERWG4NXQ9]] $A = QR$, the solution is found from $R \hat x = Q^{\mathsf{T}} b$, which is preferred in computation.
- Among all least-squares solutions, exactly one lies in the row space, and it has the smallest norm; it is $A^+ b$ with the [[Moore-Penrose pseudoinverse|0YY8VX28JR]].

### History

The cited Wikipedia article on least squares says that Legendre published the method in 1805.
It also says that Gauss published it in 1809 and claimed to have used it since 1795.

### Common errors

- Solving $A \hat x = b$ by row reduction when the system is inconsistent. Row reduction then reports "no solution", and one must pass to the normal equations or to QR.
- Thinking that the least-squares line must pass through some of the data points. In the four-point example it passes through none of them.
- Minimizing the vertical distances and believing that this also minimizes the perpendicular distances. These are different problems; the second one is solved with the SVD.

## Explanations

### L1 human

We have more measurements than unknowns, and the measurements disagree a little.
The least-squares method picks the answer that makes the total squared error as small as possible.
For points in the plane, it gives the line that fits the points best in this sense.

### L2 human

We fit a constant $c$ to the measurements $b = (1, 2, 6)$.

1. The model is $c(1, 1, 1) \approx b$, so $A = (1, 1, 1)^{\mathsf{T}}$.
2. The projection of $b$ onto the line $\R(1, 1, 1)$ is $\frac{b \cdot (1, 1, 1)}{3} (1, 1, 1) = 3 (1, 1, 1)$.
3. So $\hat c = 3$, the mean of the data, and the residual is $(-2, -1, 3)$.
4. Check: $(-2, -1, 3) \cdot (1, 1, 1) = 0$, so the residual is orthogonal to the column space.

The typical use is curve fitting: a line, a polynomial, or any model that is linear in its parameters.
The trap is to forget the column of ones in a line fit $y = c + s t$, which forces the line through the origin.

### L3 human

The least-squares solution is a projection, so it is linear in $b$: $\hat x = A^+ b$ with the [[Moore-Penrose pseudoinverse|0YY8VX28JR]].
In statistics, under the Gauss-Markov assumptions, the least-squares estimator is the best linear unbiased estimator; this is the subject of [[ordinary least squares|YM708KHV2W]] and [[linear regression|41FVC4P5JB]], which we only name here.
In numerical analysis, [[numerical methods for least squares|AWQA2Y30N4]] compare the normal equations, QR by Householder reflections and the SVD.
In infinite dimension, the same idea gives best approximation in $L^2$, as in [[the polynomial and Fourier example|899D63WW04]].
