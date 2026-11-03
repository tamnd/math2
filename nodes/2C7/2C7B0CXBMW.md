---
tag: 2C7B0CXBMW
kind: concept
name: BFGS method
msc: [90C53, 65K05]
specializes: [JEEEH7757R]
sources:
  - url: https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm
same_as:
  wikidata: Q2877013
  wikipedia: Broyden–Fletcher–Goldfarb–Shanno algorithm
---

## Summary

The BFGS method, named after Broyden, Fletcher, Goldfarb and Shanno, is the most widely used [[quasi-Newton method|JEEEH7757R]] for unconstrained minimization.
Its rank-two update keeps the Hessian approximation symmetric and positive definite as long as the curvature condition $y_k^T s_k > 0$ holds.
So every search direction is a descent direction.
With a line search that satisfies the Wolfe conditions, it converges superlinearly near a minimizer with a positive definite Hessian.
Its limited-memory variant L-BFGS handles problems with very many variables.

## Explanations

### L1 human

BFGS keeps a matrix that plays the role of the curvature of the function.
After each step it removes the old curvature information in the step direction and puts in the curvature it has just observed from the change of the gradient.
The matrix always stays "bowl-shaped" (positive definite), so the method always walks downhill.
On a quadratic function in $n$ variables with exact line searches, it finds the minimizer in at most $n$ steps.
