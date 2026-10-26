---
tag: 0ATFVE08MW
kind: concept
name: Back substitution
msc: [15A06, 65F05]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Forward and back substitution
---

## Summary

Back substitution is a method to solve a system $Ux = b$, where $U$ is an $n \times n$ [[upper triangular matrix|0N4XY7Z3NN]] with nonzero diagonal entries.
The last equation gives $x_n = b_n / u_{nn}$.
Then, for $i = n-1, \dots, 1$ in this order, equation $i$ gives
$$x_i = \frac{1}{u_{ii}} \left( b_i - \sum_{j = i+1}^{n} u_{ij} x_j \right),$$
which uses only the unknowns that are already known.

## Remarks

Back substitution uses on the order of $n^2$ arithmetic operations.
Forward substitution solves $Lx = b$ for a [[lower triangular matrix|00J3KZP8Y0]] $L$ in the same way, from the first equation down.
After [[Gaussian elimination|0JVJ2WCXZH]], back substitution completes the solution of the system.
With an [[LU decomposition|0RKG5YW66Y]] $A = LU$, the system $Ax = b$ is solved by forward substitution for $Ly = b$ and then back substitution for $Ux = y$.

## Explanations

### L1 human

In a triangular system, the last equation has only one unknown, so we solve it at once.
We put that value into the equation above it, which now has only one new unknown.
We continue upwards until we know all the unknowns.
