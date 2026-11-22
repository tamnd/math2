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

When a linear system $Ax = b$ has no solution, least squares picks the $x$ that comes closest, in the sense that the sum of the squared errors is as small as possible.
The answer comes from geometry: $Ax$ should be the point of the column space nearest to $b$, and that point is a projection.
Let $A$ be a real $m \times n$ matrix and let $b \in \R^m$, with the Euclidean norm $\norm{y} = \sqrt{y^{\mathsf{T}} y}$.
A *least-squares solution* of $Ax = b$ is a vector $\hat x \in \R^n$ with
$$\norm{b - A \hat x} \le \norm{b - Ax} \quad \text{for every } x \in \R^n.$$
The vector $b - A \hat x$ is the *residual*, and $\norm{b - A \hat x}^2$ is the sum of the squares of its entries, which gives the method its name.
By the [[best approximation theorem|0MCDDSCB9Z]], $\hat x$ is a least-squares solution exactly when $A \hat x$ is the [[orthogonal projection|0Q8HZTJC7G]] of $b$ onto the [[column space|03AJKXH1AV]] of $A$.

## Motivation

Measurements contain errors, so we usually take more of them than we have unknowns.
The result is an [[overdetermined system|QJ0P26J9BV]], with more equations than unknowns, and such a system almost never has an exact solution.
For example, a straight line has two parameters, and four measured points almost never lie on one line.
An exact solution would not mean much anyway, because the data are not exact.
So we change the question from "solve $Ax = b$" to "make $Ax$ as close to $b$ as possible", and this question always has an answer.

The method is everywhere that a model is fitted to data.
Astronomers fit orbits to observations, statisticians fit regression lines, and engineers fit curves to calibration data.
In each case the model is linear in its unknown parameters, so the fit is a least-squares problem for some matrix $A$.
The [[normal equations|4D7MRG4D91]] and the [[QR decomposition|0ERWG4NXQ9]] are the two standard ways to compute the answer, and the [[minimum-norm solution|QM2Y84VDX8]] settles the case when the answer is not unique.

## Notation

We write $\hat x$ for a least-squares solution and $r = b - A \hat x$ for the residual.
Books also write the problem as $\min_x \norm{Ax - b}_2$ or as $\operatorname{argmin}_x \norm{Ax - b}^2$, where the subscript $2$ marks the Euclidean norm.
Squaring the norm changes the size of the error but not the minimizer, so both forms have the same solutions.
The [[transpose|0W809K6AW0]] is written $A^{\mathsf{T}}$, and Lay writes $A^T$.

## Remarks

### A first fit

Suppose three measurements of one quantity give $1$, $2$ and $6$.
The model "every measurement equals $c$" is the system $c(1, 1, 1) = (1, 2, 6)$, which has no solution.
Here $A$ is the single column $(1, 1, 1)^{\mathsf{T}}$, so the column space is the line through $(1, 1, 1)$.
Project $b = (1, 2, 6)$ onto that line:
$$p = \frac{b \cdot (1, 1, 1)}{(1, 1, 1) \cdot (1, 1, 1)} (1, 1, 1) = \frac{9}{3} (1, 1, 1) = (3, 3, 3).$$
So $\hat c = 3$, the mean of the data, and the residual is $r = (1, 2, 6) - (3, 3, 3) = (-2, -1, 3)$.
Check: $r \cdot (1, 1, 1) = -2 - 1 + 3 = 0$, so the residual is perpendicular to the column space.
The same calculation for $m$ measurements gives $\hat c = \frac{1}{m} \sum_i b_i$, so the mean of a list of numbers is a least-squares solution.

### Why projection gives the answer

As $x$ runs over $\R^n$, the vector $Ax$ runs over the whole column space $\operatorname{Col}(A)$.
So minimizing $\norm{b - Ax}$ over $x$ is the same as finding the point of $\operatorname{Col}(A)$ nearest to $b$.
The best approximation theorem says that this nearest point is the projection $p$ of $b$, and that $b - p$ is orthogonal to the subspace.
Then we solve $Ax = p$, which always has a solution because $p$ lies in the column space.
The theorem on [[existence and uniqueness of least-squares solutions|V9AH43ZY91]] turns this into four exact statements.

### More examples

[[A least-squares line through four points|H2D0QA4AXV]] fits $y = c + st$ to $(0, 1)$, $(1, 2)$, $(2, 2)$ and $(3, 4)$.
The answer is $y = 0.9 + 0.9t$, with residual $(0.1, 0.2, -0.7, 0.4)$ and residual sum of squares $0.7$.
[[Least squares with dependent columns|FM9VEAKSA7]] shows a matrix whose two columns are parallel.
There the least-squares solutions form a whole line, but the closest point $A \hat x$ is still unique.
When $Ax = b$ is consistent, the least-squares solutions are just the exact solutions, with residual $0$, as in [[the consistent overdetermined system|XYTJ19AEKC]].

### What it is not

A line that passes through many of the points is not for that reason a least-squares line.
[[The line through three of the four points|MH3VAGXW9R]] $y = 1 + t$ hits three points exactly, but it misses the fourth by $1$, so its sum of squares is $1 > 0.7$.

Minimizing the sum of absolute errors is a different problem, with different answers.
Fit a constant $c$ to the data $(0, 0, 3)$.
Least squares gives the mean, $\hat c = 1$.
The sum of absolute errors is $3$ at $c = 0$ and $1 + 1 + 2 = 4$ at $c = 1$, so the mean does not minimize it; the median $0$ does.
The projection argument needs the Euclidean norm, and it says nothing about this second problem.

### The rules you can use

A least-squares solution always exists, and it is unique exactly when the columns of $A$ are linearly independent, by [[existence and uniqueness|V9AH43ZY91]].
The least-squares solutions are exactly the solutions of the [[normal equations|4D7MRG4D91]] $A^{\mathsf{T}} A x = A^{\mathsf{T}} b$, which say that the residual is orthogonal to every column of $A$.
With a [[QR decomposition|0ERWG4NXQ9]] $A = QR$ and independent columns, the solution comes from the triangular system $R \hat x = Q^{\mathsf{T}} b$, and computers prefer this route.
When the columns are dependent, exactly one least-squares solution lies in the row space, and it is the shortest one: $\hat x = A^+ b$ with the [[Moore-Penrose pseudoinverse|0YY8VX28JR]].

### Watch out

The model must contain every parameter that you want to fit.
For a line $y = c + st$ the matrix $A$ needs a column of ones for $c$.
If you drop it, you fit the line $y = st$ through the origin instead.
For the four points above, that fit gives
$$\hat s = \frac{\sum t_i y_i}{\sum t_i^2} = \frac{18}{14} = \frac{9}{7},$$
which is a different line from $y = 0.9 + 0.9t$.

Watch out also for row reduction.
If you row reduce $Ax = b$ itself, it reports "no solution", and that is where the least-squares problem starts.
The next step is to pass to the normal equations or to QR.
Finally, least squares measures vertical misses $y_i - (c + st_i)$, not perpendicular distances to the line; the perpendicular version is a different problem, solved with the SVD.

### History

Legendre published the method of least squares in 1805.
Gauss published his account in 1809 and stated that he had used the method since 1795, which led to a dispute about priority.

### Try it

First, find the least-squares solution of the two equations $2x = 4$ and $x = 1$.
Here $A = (2, 1)^{\mathsf{T}}$ and $b = (4, 1)$, so $A^{\mathsf{T}} A = 5$, $A^{\mathsf{T}} b = 9$ and $\hat x = 9/5$; the residual $(2/5, -4/5)$ is orthogonal to $(2, 1)$.

Second, is $x = (1, 1)$ a least-squares solution for the line fit through $(0, 1)$, $(1, 2)$, $(2, 2)$, $(3, 4)$?
No: its residual is $(0, 0, -1, 0)$, and the dot product with the column $(0, 1, 2, 3)$ is $-2 \ne 0$.

## Explanations

### L1 human

You weigh a parcel three times and read $1$, $2$ and $6$ kilograms.
The readings disagree, so no single weight fits all three.
Least squares picks the weight that makes the sum of the squared misses as small as possible.
For a guess of $3$, the misses are $2$, $1$ and $3$, and their squares add up to $4 + 1 + 9 = 14$.
Any other guess gives a larger total, and $3$ is just the average of the readings.

### L2 human

Here is a typical fit: find the line $y = c + st$ closest to the points $(0, 0)$, $(1, 1)$ and $(2, 3)$.
The model gives one equation for each point:
$$A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \end{pmatrix}, \quad x = \begin{pmatrix} c \\ s \end{pmatrix}, \quad y = \begin{pmatrix} 0 \\ 1 \\ 3 \end{pmatrix}.$$
The normal equations need $A^{\mathsf{T}} A$ and $A^{\mathsf{T}} y$:
$$A^{\mathsf{T}} A = \begin{pmatrix} 3 & 3 \\ 3 & 5 \end{pmatrix}, \qquad A^{\mathsf{T}} y = \begin{pmatrix} 4 \\ 7 \end{pmatrix}.$$
The determinant is $15 - 9 = 6$, and Cramer's rule gives
$$c = \frac{4 \cdot 5 - 3 \cdot 7}{6} = -\frac{1}{6}, \qquad s = \frac{3 \cdot 7 - 3 \cdot 4}{6} = \frac{3}{2}.$$
The fitted values at $t = 0, 1, 2$ are $-\tfrac{1}{6}$, $\tfrac{4}{3}$ and $\tfrac{17}{6}$, so the residual is $r = (\tfrac{1}{6}, -\tfrac{1}{3}, \tfrac{1}{6})$.
Check: $r \cdot (1, 1, 1) = 0$ and $r \cdot (0, 1, 2) = -\tfrac{1}{3} + \tfrac{1}{3} = 0$, so $r$ is orthogonal to both columns.
The residual sum of squares is $\tfrac{1}{36} + \tfrac{4}{36} + \tfrac{1}{36} = \tfrac{1}{6}$.
The same three steps (write $A$, solve the normal equations, check $A^{\mathsf{T}} r = 0$) fit every model that is linear in its parameters, such as a parabola $c_0 + c_1 t + c_2 t^2$.

### L3 human

The least-squares solution is built from a projection, so it depends linearly on $b$: in general $\hat x = A^+ b$, with the [[Moore-Penrose pseudoinverse|0YY8VX28JR]].
In statistics, under the Gauss-Markov assumptions on the errors, the least-squares estimator is the best linear unbiased estimator; this is the subject of [[ordinary least squares|YM708KHV2W]] and [[linear regression|41FVC4P5JB]].
In numerical analysis, [[numerical methods for least squares|AWQA2Y30N4]] compare the normal equations, QR by Householder reflections and the SVD, and the choice depends on the condition number of $A$.
In infinite dimension the same idea gives best approximation in a space of functions, as in [[the polynomial and Fourier example|899D63WW04]], where the columns of $A$ become orthogonal polynomials or sines and cosines.
