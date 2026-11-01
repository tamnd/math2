---
tag: AH7EW2EHNC
kind: definition
name: Generalized inverse
msc: [15A09]
defines: FPHNJ5AAYF
uses: [0VD9ZSWWJG, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_inverse
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] and let $A$ be an $m \times n$ [[matrix|0VD9ZSWWJG]] over $F$.
A *generalized inverse* of $A$ is an $n \times m$ matrix $G$ over $F$ such that
$$A G A = A.$$

## Remarks

Example: for $A = \begin{pmatrix} 1 & 1 \end{pmatrix}$, the column $G = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ is a generalized inverse, because $AG = (1)$ and so $AGA = A$.
Non-example: for $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, the matrix $G = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix}$ is not one, because $AGA = \begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix} \ne A$.
If $A$ is square and [[invertible|0EB9N0S33C]], then $A^{-1}$ is its only generalized inverse.
If $Ax = b$ has a solution and $G$ is a generalized inverse, then $x = Gb$ is a solution, since $AGb = AGAx = Ax = b$.
A generalized inverse is often written $A^-$ or $A^{(1)}$; it is also called a $\{1\}$-inverse.
A matrix $G$ that satisfies also $GAG = G$ is a reflexive generalized inverse.
