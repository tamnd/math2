---
tag: 4F7GWKTQ1H
kind: example
name: The trace pairing on square matrices
msc: ["15A04", "15A15"]
topics: [9K7FFF26QR]
audience: ug1
instance_of: [07JBSZE0V4]
uses: [0M856Q1AMZ, 07PTPSZPME, 0RE6X3BGPN, 4H93XF4RVH, 032Q9FB8MT, 0B8T10CE7N]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_form
    locator: Trace of a square matrix
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Definition
---

## Example

Let $F$ be a field and let $M_n(F)$ be the [[space of $n \times n$ matrices|0RE6X3BGPN]] over $F$.
For $A \in M_n(F)$, define $\tau_A \colon M_n(F) \to F$ by
$$\tau_A(X) = \tr(AX),$$
where $\tr$ is the [[trace|07PTPSZPME]].
We show that $A \mapsto \tau_A$ is a [[linear isomorphism|0B8T10CE7N]] from $M_n(F)$ onto the [[dual space|0M856Q1AMZ]] $M_n(F)^*$.
The plan is to compute $\tau_A$ on the matrix units and then use that they form a basis.

1. Each $\tau_A$ is a linear form, because [[matrix multiplication|032Q9FB8MT]] distributes over sums of matrices and the trace is linear.
2. The map $A \mapsto \tau_A$ is linear, since $\tr((A + B)X) = \tr(AX) + \tr(BX)$ and $\tr((cA)X) = c \tr(AX)$.
3. Let $E_{ij}$ be the [[matrix unit|4H93XF4RVH]] with $1$ at place $(i, j)$ and $0$ elsewhere. Entry $(k, l)$ of $AE_{ij}$ is $\sum_m a_{km} (E_{ij})_{ml} = a_{ki}$ when $l = j$, and $0$ otherwise.
4. So column $j$ of $AE_{ij}$ is column $i$ of $A$, and the other columns are zero. The only diagonal entry that can be nonzero is entry $(j, j)$, which is $a_{ji}$, so
$$\tau_A(E_{ij}) = a_{ji}.$$
5. The map is injective. If $\tau_A = 0$, then step 4 gives $a_{ji} = 0$ for all $i$ and $j$, so $A = 0$.
6. The map is surjective. Given $f \in M_n(F)^*$, define $A$ by $a_{ji} = f(E_{ij})$. By step 4, $\tau_A$ and $f$ agree on the basis $(E_{ij})$, so they are equal.
7. By steps 2, 5 and 6, $A \mapsto \tau_A$ is a linear isomorphism $M_n(F) \to M_n(F)^*$.

Here is a check of step 4 with $n = 2$, $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $X = E_{12}$:
$$AE_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 3 \end{pmatrix}, \qquad \tau_A(E_{12}) = 0 + 3 = 3 = a_{21}.$$

Now we find the matrix of one form by step 6.
Let $f(X) = x_{11} + 2x_{12}$ on $M_2(F)$.
Then $f(E_{11}) = 1$ and $f(E_{12}) = 2$, while $f(E_{21}) = f(E_{22}) = 0$, so $a_{11} = 1$, $a_{21} = 2$ and the other entries are $0$.
Check by multiplying:
$$\begin{pmatrix} 1 & 0 \\ 2 & 0 \end{pmatrix} \begin{pmatrix} x_{11} & x_{12} \\ x_{21} & x_{22} \end{pmatrix} = \begin{pmatrix} x_{11} & x_{12} \\ 2x_{11} & 2x_{12} \end{pmatrix},$$
whose trace is $x_{11} + 2x_{12} = f(X)$.

## Remarks

The example shows a dual space that is identified with the space itself without a choice of basis.
The formula $\tr(AX)$ uses only the product of matrices, which $M_n(F)$ has and a general space does not have.
The form $\tau_I$ is the trace itself, and $\tau_{E_{ij}}(X) = x_{ji}$, so the forms of the matrix units are the coordinate forms with the two indices swapped.

The pairing $(A, X) \mapsto \tr(AX)$ is a symmetric bilinear form, since $\tr(AX) = \tr(XA)$, and step 5 says that it is nondegenerate.
Over $\R$ one often uses $\tr(A^{\mathsf{T}} X) = \sum_{i, j} a_{ij} x_{ij}$ instead, the Frobenius inner product, and then no index swap is needed.
If we replace $\tr(AX)$ by the determinant $\det(AX)$, the result is not linear in $X$, so it gives no element of the dual.

## Explanations

### L1 human

Every linear way to get one number from a square matrix has the same shape: multiply by a fixed matrix $A$, then add the diagonal entries.
For example, the rule $x_{11} + 2x_{12}$ comes from $A = \begin{pmatrix} 1 & 0 \\ 2 & 0 \end{pmatrix}$.
Different matrices $A$ give different rules, and every rule arises.

### L2 human

To find $A$ for a given form $f$ on $M_n(F)$, evaluate $f$ on the matrix units.

1. Compute the number $f(E_{ij})$ for every pair $i, j$.
2. Put $f(E_{ij})$ at place $(j, i)$ of $A$, that is, with the indices swapped.
3. Then $f(X) = \tr(AX)$ for every $X$, by step 6 of the example.

For the form $f(X) = 3x_{21} - x_{22}$ on $M_2(F)$, we get $f(E_{21}) = 3$ and $f(E_{22}) = -1$, so $a_{12} = 3$ and $a_{22} = -1$.
Check: $A = \begin{pmatrix} 0 & 3 \\ 0 & -1 \end{pmatrix}$ gives $AX$ with diagonal entries $3x_{21}$ and $-x_{22}$.
The typical use is in matrix calculus, where the derivative of a function of a matrix is a form on $M_n(F)$ and is written as a matrix in this way.
Watch out: forgetting the index swap gives $A^{\mathsf{T}}$ in place of $A$.
