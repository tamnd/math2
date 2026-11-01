---
tag: RQ44FKS5QM
kind: concept
name: Dodgson condensation
msc: [15A15, 65F40]
sources:
  - url: https://en.wikipedia.org/wiki/Dodgson_condensation
same_as:
  wikidata: Q4230490
  wikipedia: Dodgson condensation
---

## Summary

Dodgson condensation is a method to compute the [[determinant|00KDZRW4C0]] of a square matrix by repeatedly replacing it with a smaller matrix of connected $2 \times 2$ minors.
Each step divides by interior entries of the matrix from two steps before.
It rests on the Desnanot–Jacobi identity, a case of [[Sylvester's determinant identity|7SSKBQYFW1]].
It was proposed by Charles Dodgson, better known as Lewis Carroll.

## Explanations

### L1 human

Start with an $n \times n$ matrix and replace each $2 \times 2$ block of neighbouring entries by its determinant.
This gives an $(n-1) \times (n-1)$ matrix.
Repeat, but now divide each new entry by the matching inner entry of the matrix two steps back.
After $n - 1$ steps a single number is left, and it is the determinant.
For $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix}$, the first step gives $\begin{pmatrix} -3 & -3 \\ -3 & 2 \end{pmatrix}$, and the second gives $(-6 - 9)/5 = -3 = \det A$.
