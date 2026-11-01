---
tag: GTG8MJGDKC
kind: concept
name: Triangular matrix
msc: [15B99, 15A23]
specializes: [0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
same_as:
  wikidata: Q506265
  wikipedia: Triangular matrix
---

## Summary

A triangular matrix is a square matrix that is either [[upper triangular|0N4XY7Z3NN]] or [[lower triangular|00J3KZP8Y0]].
All its entries on one side of the main diagonal are zero.
Linear systems with a triangular matrix are solved quickly by substitution.
The [[determinant of a triangular matrix|0K1KKMFHYH]] is the product of its diagonal entries, and these entries are its eigenvalues.
Many factorisations, such as LU, QR and the [[Schur decomposition|V1JG4C7R7B]], produce triangular factors.

## Explanations

### L1 human

Picture a square table of numbers cut along its main diagonal.
A triangular matrix has only zeros in one of the two halves, so its nonzero entries fill a triangle.
For example, $\begin{pmatrix} 1 & 4 \\ 0 & 2 \end{pmatrix}$ is upper triangular and $\begin{pmatrix} 3 & 0 \\ 5 & 1 \end{pmatrix}$ is lower triangular.
In a system with such a matrix, one equation has a single unknown, and each next equation adds only one new unknown.
