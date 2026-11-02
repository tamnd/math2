---
tag: DXZP6V23Z7
kind: concept
name: Hypergeometric function of a matrix argument
msc: [33C70, 33C80, 62H10]
sources:
  - url: https://en.wikipedia.org/wiki/Hypergeometric_function_of_a_matrix_argument
same_as:
  wikidata: Q5958021
  wikipedia: Hypergeometric function of a matrix argument
---

## Summary

A hypergeometric function of a matrix argument ${}_pF_q^{(\alpha)}(a; b; X)$ is a generalisation of the [[generalized hypergeometric function|VDBAW9PN88]] in which the variable is a matrix $X$.
The series runs over [[integer partitions|0JV30XN73Z]].
The powers $z^k$ are replaced by Jack polynomials in the eigenvalues of $X$, and the rising factorials by generalized Pochhammer symbols.
These functions appear in multivariate statistics and random matrix theory, where densities of eigenvalues of Wishart and related matrices are written with them.

## Explanations

### L1 human

For a number $z$, the series ${}_pF_q$ is a sum over $k$ of rational coefficients times $z^k / k!$.
For a matrix, the role of $z^k$ is played by a family of symmetric polynomials of degree $k$ in the eigenvalues, one for each way of splitting $k$ into parts.
These polynomials add up to $(\operatorname{tr} X)^k$, so the matrix series keeps track of finer information than the trace alone.
The simplest case is ${}_0F_0(X) = e^{\operatorname{tr} X}$, which comes out because the polynomials of degree $k$ sum to $(\operatorname{tr} X)^k$.
The parameter $\alpha$ selects the setting: $\alpha = 2$ for real symmetric matrices and $\alpha = 1$ for complex Hermitian matrices.
