---
tag: ZR6XXP36X8
kind: definition
name: Drazin inverse
msc: [15A09]
defines: 9FB0AZSEGM
uses: [0JXZKX526R, 0ZC9YTXZRY, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Drazin_inverse
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be an $n \times n$ [[square matrix|0JXZKX526R]] over $F$.
The *index* of $A$ is the least integer $k \ge 0$ such that $\rank(A^{k+1}) = \rank(A^k)$, where $\rank$ is the [[rank|0ZC9YTXZRY]] and $A^0 = I$.
The *Drazin inverse* of $A$ is the $n \times n$ matrix $A^D$ over $F$ such that, with $k$ the index of $A$:

1. $A^{k+1} A^D = A^k$.
2. $A^D A A^D = A^D$.
3. $A A^D = A^D A$.

There is exactly one matrix with these three properties.

## Remarks

Example: if $A$ is invertible, its index is $0$, and $A^D = A^{-1}$; indeed $A \cdot A^{-1} = I$, $A^{-1} A A^{-1} = A^{-1}$, and $A^{-1}$ commutes with $A$.
Example: if $A$ is [[nilpotent|07BSPZPSMF]] with $A^k = 0$ for its index $k$, then $A^D = 0$; each side of each condition is then $0$, because $A^k = 0$.
Non-example: for $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, of index $2$, the matrix $X = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ is not $A^D$, because $AX = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $XA = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ differ, so clause 3 fails.
If $A = P \begin{pmatrix} C & 0 \\ 0 & N \end{pmatrix} P^{-1}$ with $C$ invertible and $N$ nilpotent, then $A^D = P \begin{pmatrix} C^{-1} & 0 \\ 0 & 0 \end{pmatrix} P^{-1}$.
When the index is at most $1$, the Drazin inverse is called the group inverse and written $A^{\#}$.
