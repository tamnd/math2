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

Let $F$ be a field and let $M_n(F)$ be the [[space of $n \times n$ matrices|0RE6X3BGPN]].
For $A \in M_n(F)$, define $\tau_A \colon M_n(F) \to F$ by $\tau_A(X) = \tr(AX)$, where $\tr$ is the [[trace|07PTPSZPME]].
We show that $A \mapsto \tau_A$ is a [[linear isomorphism|0B8T10CE7N]] from $M_n(F)$ onto the [[dual space|0M856Q1AMZ]] $M_n(F)^*$.

1. Each $\tau_A$ is linear in $X$, because [[matrix multiplication|032Q9FB8MT]] distributes over sums and the trace is linear. So $\tau_A \in M_n(F)^*$.
2. The map $A \mapsto \tau_A$ is linear, since $\tr((A + B)X) = \tr(AX) + \tr(BX)$ and $\tr((cA)X) = c \tr(AX)$.
3. Let $E_{ij}$ be the [[matrix unit|4H93XF4RVH]] with $1$ at place $(i, j)$ and $0$ elsewhere. The product $AE_{ij}$ has column $j$ equal to column $i$ of $A$, and all other columns zero.
4. So the only possibly nonzero diagonal entry of $AE_{ij}$ is at place $(j, j)$, and it is $a_{ji}$. Hence $\tau_A(E_{ij}) = a_{ji}$.
5. Injectivity: if $\tau_A = 0$, then step 4 gives $a_{ji} = 0$ for all $i, j$. So $A = 0$.
6. Surjectivity: let $f \in M_n(F)^*$. Define $A$ by $a_{ji} = f(E_{ij})$. By step 4, $\tau_A$ and $f$ agree on the basis $(E_{ij})$, so $\tau_A = f$.
7. By steps 2, 5 and 6, $A \mapsto \tau_A$ is a linear isomorphism $M_n(F) \to M_n(F)^*$.
8. A check with $n = 2$: for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $X = E_{12}$, we get $AX = \begin{pmatrix} 0 & 1 \\ 0 & 3 \end{pmatrix}$, so $\tau_A(E_{12}) = 0 + 3 = 3 = a_{21}$.
9. A form found by step 6: let $f(X) = x_{11} + 2x_{12}$ on $M_2(F)$. Then $a_{11} = 1$, $a_{21} = f(E_{12}) = 2$, and the other entries are $0$.
10. Check: with $A = \begin{pmatrix} 1 & 0 \\ 2 & 0 \end{pmatrix}$, the product $AX$ has diagonal entries $x_{11}$ and $2x_{12}$. So $\tr(AX) = x_{11} + 2x_{12} = f(X)$.

## Remarks

- The form $\tau_I$ is the trace itself. The forms $\tau_A$ with $A$ a matrix unit are the coordinate forms of $M_n(F)$, with indices swapped.
- The isomorphism does not depend on a choice of basis of $M_n(F)$. It uses the product of matrices, which the space $F^n$ itself does not have.
- The symmetric form $(A, X) \mapsto \tr(AX)$ is nondegenerate by step 5. Over $\R$, the form $\tr(A^{\mathsf{T}} X) = \sum_{i,j} a_{ij} x_{ij}$ is the Frobenius inner product.

## Explanations

### L1 human

Every linear way to get one number from a square matrix has the shape "multiply by a fixed matrix $A$, then take the trace".
For example, $x_{11} + 2x_{12}$ comes from $A = \begin{pmatrix} 1 & 0 \\ 2 & 0 \end{pmatrix}$.
Different matrices $A$ give different forms.

### L2 human

To find $A$ for a given form $f$, evaluate $f$ on the matrix units.

1. Compute $f(E_{ij})$ for all $i, j$.
2. Put the value $f(E_{ij})$ at place $(j, i)$ of $A$, that is, with the indices swapped.
3. Then $f(X) = \tr(AX)$ for every $X$.

The typical use is to identify $M_n(F)^*$ with $M_n(F)$ in matrix calculus, where a derivative of a function of a matrix is again written as a matrix.
A trap: forgetting the index swap gives $A^{\mathsf{T}}$ in place of $A$.
