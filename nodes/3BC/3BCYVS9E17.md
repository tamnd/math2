---
tag: 3BCYVS9E17
kind: concept
name: Discriminant of a field extension
msc: [11R29, 12F10]
sources:
  - url: https://en.wikipedia.org/wiki/Discriminant_of_an_algebraic_number_field
---

## Summary

The discriminant of a basis $b_1, \ldots, b_n$ of a finite extension $L/K$ is the determinant of the matrix $\left(\mathrm{Tr}_{L/K}(b_i b_j)\right)$, the Gram matrix of the [[trace form|YWX2R53ED6]].
Changing the basis multiplies it by the square of a nonzero element of $K$, so its class modulo squares depends only on the extension.
It is nonzero exactly when $L/K$ is separable.
For a power basis $1, \alpha, \ldots, \alpha^{n-1}$ it equals the [[discriminant of the minimal polynomial|0VVK64Q4JK]] of $\alpha$.
For an integral basis of a number field it gives the discriminant of the number field.

## Explanations

### L1 human

Pick a basis of the extension and pair basis elements with the trace form.
The determinant of the resulting square table is the discriminant.
It is nonzero exactly when the trace pairing is nondegenerate.
For $\Q(i)$ with basis $1, i$, the table is $\begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}$, so the discriminant is $-4$.
For the basis $1, \alpha$ of $\Q(\alpha)$ with $\alpha^2 = d$, it is $4d$, the discriminant $b^2 - 4ac$ of $x^2 - d$.
