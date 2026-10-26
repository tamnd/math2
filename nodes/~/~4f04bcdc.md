---
tag: ~4f04bcdc
kind: definition
name: Reduced row echelon form
msc: [15A06]
defines: ~ca88f169
uses: [~47c92361]
sources:
  - url: https://en.wikipedia.org/wiki/Row_echelon_form
    locator: Reduced row echelon form
---

## Definition

Let $F$ be a field and let $A$ be a matrix over $F$.
The matrix $A$ is in *reduced row echelon form* when these three conditions hold:

1. $A$ is in [[row echelon form|~a56c300b]].
2. The leading entry of each nonzero row is $1$.
3. In each column that has a leading entry, all the other entries are $0$.

## Remarks

The matrix $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$ is in reduced row echelon form.
Each matrix is [[row equivalent|~0ffdcb60]] to exactly one matrix in reduced row echelon form.
[[Gauss–Jordan elimination|~3de2cc1b]] computes this matrix.
The number of nonzero rows of the reduced row echelon form of $A$ is the [[rank|~802904f9]] of $A$.

## Explanations

### L1 human

Reduced row echelon form is the simplest form that row operations can reach.
Each pivot is a $1$, and it has zeros above it and below it.
From this form we can read the solutions of the system directly.
