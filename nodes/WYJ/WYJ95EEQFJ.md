---
tag: WYJ95EEQFJ
kind: example
name: The 1 × 1 matrices behave like their entries
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
instance_of: [0JXZKX526R]
uses: [0CP7YY6NAG, 076JGP6R3T, 0BVXADM10P]
sources:
  - url: https://en.wikipedia.org/wiki/Square_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: Definition
---

## Example

Let $R$ be a ring.
A $1 \times 1$ matrix over $R$ is a [[square matrix|0CP7YY6NAG]] $\begin{pmatrix} a \end{pmatrix}$ with one entry.

1. By the rule for [[addition|0BVXADM10P]], $\begin{pmatrix} a \end{pmatrix} + \begin{pmatrix} b \end{pmatrix} = \begin{pmatrix} a + b \end{pmatrix}$.
2. By the rule for [[multiplication|076JGP6R3T]], the product has the single entry $\sum_{k=1}^{1} a_{1k} b_{k1} = ab$. So $\begin{pmatrix} a \end{pmatrix}\begin{pmatrix} b \end{pmatrix} = \begin{pmatrix} ab \end{pmatrix}$.
3. By steps 1 and 2, the map $a \mapsto \begin{pmatrix} a \end{pmatrix}$ is a ring isomorphism from $R$ to $M_1(R)$.
4. For example, $\begin{pmatrix} 3 \end{pmatrix}\begin{pmatrix} -2 \end{pmatrix} = \begin{pmatrix} -6 \end{pmatrix}$ over $\mathbb{Z}$.
5. For the column $u = (1, 2)^{\mathsf{T}}$, the product $u^{\mathsf{T}}u = \begin{pmatrix} 5 \end{pmatrix}$ is a $1 \times 1$ matrix. We identify it with the dot product $5$.

## Remarks

The identification of $\begin{pmatrix} a \end{pmatrix}$ with $a$ is safe inside $M_1(R)$, but not inside larger products.
The product $\begin{pmatrix} 2 \end{pmatrix} B$ is not defined for a $2 \times 2$ matrix $B$, because $\begin{pmatrix} 2 \end{pmatrix}$ has 1 column and $B$ has 2 rows.
The scalar multiple $2B$ is defined, and it is a different operation.

## Explanations

### L1 human

A $1 \times 1$ matrix is one number in brackets.
Adding and multiplying such matrices is the same as adding and multiplying the numbers.

### L2 human

This is why the expression $u^{\mathsf{T}} v$ for two columns is often read as a number.
The reading is correct for $u^{\mathsf{T}} v$ alone, but $(u^{\mathsf{T}} v) B$ needs the scalar reading, not the matrix reading.
