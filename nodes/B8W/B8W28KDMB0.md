---
tag: B8W28KDMB0
kind: concept
name: Numerical linear algebra
msc: [65F99, 65F05, 65F15]
sources:
  - url: https://en.wikipedia.org/wiki/Numerical_linear_algebra
same_as:
  wikidata: Q2004891
  wikipedia: Numerical linear algebra
---

## Summary

Numerical linear algebra is the study of algorithms that solve problems of linear algebra on a computer, with floating-point numbers.
Its main problems are linear systems, least squares, [[eigenvalues|0BQAA2BK3Q]] and [[singular values|09VMDSRXWJ]].
It asks how much work an algorithm needs and how rounding errors affect the answer, using notions such as the [[condition number|AB3S6MHJ8X]] and backward stability.
Most computations in science and engineering end in one of its problems.

## Explanations

### L1 human

On paper, linear algebra is exact; on a computer, every number is rounded to a fixed number of digits.
Numerical linear algebra designs methods that stay accurate despite these small errors and that stay fast for matrices with millions of rows.
For example, [[Gaussian elimination|0JVJ2WCXZH]] with row exchanges solves a linear system reliably.
On the other hand, eigenvalues are almost never computed as roots of the [[characteristic polynomial|0VSSPAFM2C]], because those roots react strongly to tiny errors in the coefficients.
Methods such as [[LU decomposition|0RKG5YW66Y]], the [[QR algorithm|B6F8YWHYZ5]] and [[power iteration|H4MQD841BR]] belong to this field.
