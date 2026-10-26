---
tag: 0TWTS88TWN
kind: definition
name: Invertible matrix
msc: [15A09]
defines: 0EB9N0S33C
uses: [0CP7YY6NAG, 06DW9BAWB1, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Definition
---

## Definition

Let $R$ be a commutative ring and let $A$ be an $n \times n$ [[square matrix|0JXZKX526R]] over $R$.
The matrix $A$ is *invertible* when there is an $n \times n$ matrix $B$ over $R$ such that
$$AB = BA = I_n,$$
where $I_n$ is the [[identity matrix|06DW9BAWB1]].
The matrix $B$ is then unique; it is the *inverse* of $A$, written $A^{-1}$.

## Remarks

Over a field, other names are *nonsingular* and *nondegenerate*.
A matrix over $R$ is invertible if and only if its [[determinant is a unit|0783S9D0ZH]] of $R$.
Over a field, a [[one-sided inverse is two-sided|0753Y2X5K6]], and $A$ is invertible if and only if $Ax = 0$ has only the solution $x = 0$.
The matrix $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ is not invertible over $\R$, because its determinant is $0$.

## Explanations

### L1 human

A matrix is invertible when another matrix undoes it.
If $A$ sends $x$ to $y$, then $A^{-1}$ sends $y$ back to $x$.
For $2 \times 2$ matrices, $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ when $ad - bc \ne 0$.
