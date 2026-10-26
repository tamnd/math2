---
tag: 0BYTQ4X1HC
kind: concept
name: Least squares
msc: [65F20, 15A06]
uses: [0MCDDSCB9Z, 0Q8HZTJC7G, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_least_squares
    locator: Basic formulation
same_as:
  wikidata: Q6553462
  wikipedia: Linear least squares
---

## Summary

Let $A$ be a real $m \times n$ matrix and let $b \in \R^m$.
A *least squares solution* of $Ax = b$ is a vector $\hat x \in \R^n$ that minimises $\norm{Ax - b}$, for the Euclidean norm.
The vectors $\hat x$ that do this are exactly the solutions of the *normal equations*
$$A^T A \hat x = A^T b.$$
If the columns of $A$ are linearly independent, then $A^T A$ is invertible, and $\hat x = (A^T A)^{-1} A^T b$ is unique.

## Remarks

The vector $A \hat x$ is the [[orthogonal projection|0B8KZRT28M]] of $b$ onto the column space of $A$, see [[the closest point property|0MCDDSCB9Z]].
The normal equations say that the residual $b - A\hat x$ is orthogonal to each column of $A$.
Fitting a line $y = c_0 + c_1 t$ to data points $(t_i, y_i)$ is a least squares problem.
In practice, the [[QR decomposition|0ERWG4NXQ9]] gives a more stable method than the normal equations.

## Explanations

### L1 human

A system $Ax = b$ with more equations than unknowns usually has no solution.
The least squares method finds the $x$ that makes $Ax$ as close as possible to $b$.
It is the standard way to fit a model to noisy data.
