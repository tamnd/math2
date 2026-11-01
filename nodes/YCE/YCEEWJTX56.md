---
tag: YCEEWJTX56
kind: concept
name: Hessenberg matrix
msc: [15B99, 65F15]
specializes: [0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Hessenberg_matrix
same_as:
  wikidata: Q428813
  wikipedia: Hessenberg matrix
---

## Summary

An upper Hessenberg matrix is a square matrix whose entries below the first subdiagonal are zero; a lower Hessenberg matrix is its transpose.
It is almost [[triangular|GTG8MJGDKC]], with one extra diagonal.
Every complex square matrix is unitarily similar to an upper Hessenberg matrix, and this reduction takes finitely many steps.
For this reason the [[QR algorithm|B6F8YWHYZ5]] for eigenvalues first brings a matrix to Hessenberg form.

## Explanations

### L1 human

Start from an upper triangular matrix and allow one more diagonal of nonzero entries just below the main diagonal.
The result is an upper Hessenberg matrix, such as $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 0 & 7 & 8 \end{pmatrix}$.
Exact triangular form usually needs the eigenvalues, which are hard to find.
Hessenberg form is the closest one can get with a fixed, finite amount of work, and it makes each later step of eigenvalue algorithms much cheaper.
