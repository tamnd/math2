---
tag: W7MPTRPXYD
kind: concept
name: Matrix function
msc: [15A16, 47A60]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_function_of_a_matrix
same_as:
  wikidata: Q2699958
  wikipedia: Analytic function of a matrix
---

## Summary

A matrix function extends a scalar function $f$ to square matrices, giving a matrix $f(A)$ for a matrix $A$.
For a function given by a [[power series|0MZB06ST2B]], $f(A)$ is obtained by putting $A$ into the series.
The [[matrix exponential|020M04FN1H]], the [[logarithm of a matrix|FS339MCFEQ]] and the [[square root of a matrix|63FAKMYZ2E]] are the main examples.
They are used to solve linear differential equations and in numerical analysis, control theory and quantum mechanics.

## Explanations

### L1 human

Many functions are sums of powers, like $e^x = 1 + x + x^2/2 + \cdots$.
Powers of a square matrix make sense, so one can put a matrix in place of $x$.
For a diagonal matrix, this simply applies $f$ to each diagonal entry.
For a general matrix, $f(A)$ acts on each eigenvector of $A$ by multiplying it by $f$ of the eigenvalue.
