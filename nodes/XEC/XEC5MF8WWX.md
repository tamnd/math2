---
tag: XEC5MF8WWX
kind: definition
name: Square root of a matrix
msc: [15A16, 15A24]
defines: 63FAKMYZ2E
uses: [0JXZKX526R, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Square_root_of_a_matrix
---

## Definition

Let $\mathbb{K}$ be a field, let $n \ge 1$, and let $A$ be an $n \times n$ [[matrix|0JXZKX526R]] over $\mathbb{K}$.
A *square root* of $A$ is an $n \times n$ matrix $B$ over $\mathbb{K}$ such that $B^2 = A$, where $B^2 = BB$ is the [[matrix product|032Q9FB8MT]].

## Remarks

Example: for every real $\theta$, $B = \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}$ is a square root of $I_2$.
Check: the entries of $B^2$ are $\cos^2\theta + \sin^2\theta = 1$ on the diagonal and $\cos\theta\sin\theta - \sin\theta\cos\theta = 0$ off it.
Non-example: $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has no square root.
If $B^2 = N$, then $B^4 = 0$, so $B$ is [[nilpotent|07BSPZPSMF]]; a nilpotent $2 \times 2$ matrix satisfies $B^2 = 0 \ne N$.
A [[positive semidefinite matrix|01MMVW8CKC]] has a unique positive semidefinite square root, written $A^{1/2}$; see [[square root of a positive semidefinite matrix|0BJVDCF38Y]].
A complex matrix with no eigenvalue in $(-\infty, 0]$ has a unique square root whose eigenvalues have positive real part, the *principal square root*.
