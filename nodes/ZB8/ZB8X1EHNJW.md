---
tag: ZB8X1EHNJW
kind: example
name: The change of basis formula for the derivative on quadratic polynomials
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
illustrates: [0MQXVZEBMT]
uses: [0YYMY95FWS, 0KWXYZPJKN, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Change_of_basis
    locator: Change-of-basis formula
---

## Example

We test the [[change of basis formula|0MQXVZEBMT]] on a map between two different spaces, so that both factors $P$ and $Q^{-1}$ appear.
Let $D \colon P_2 \to P_1$ be the derivative, from real polynomials of degree at most $2$ to those of degree at most $1$.
Take the bases $B = (1, x, x^2)$ and $B' = (1, x - 1, (x - 1)^2)$ of $P_2$, and $C = (1, x)$ and $C' = (1, x - 1)$ of $P_1$.

1. In the old bases, $D(1) = 0$, $D(x) = 1$ and $D(x^2) = 2x$.
   Their $C$-coordinates $(0, 0)$, $(1, 0)$ and $(0, 2)$ are the columns of the [[matrix|0YYMY95FWS]]
   $$A = [D]_{C,B} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}.$$
2. From $x - 1 = -1 + x$ and $(x - 1)^2 = 1 - 2x + x^2$, the [[change of basis matrix|0KWXYZPJKN]] from $B$ to $B'$ is
   $$P = \begin{pmatrix} 1 & -1 & 1 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix}.$$
3. From $1 = 1$ and $x - 1 = -1 + x$, the change of basis matrix from $C$ to $C'$ and its inverse are
   $$Q = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}, \qquad Q^{-1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$$
4. We form $AP$ with the [[matrix product|076JGP6R3T]].
   Row 1 of $A$ picks out row 2 of $P$, and row 2 of $A$ picks out twice row 3 of $P$:
   $$AP = \begin{pmatrix} 0 & 1 & -2 \\ 0 & 0 & 2 \end{pmatrix}.$$
5. Multiplying by $Q^{-1}$ on the left adds row 2 to row 1:
   $$Q^{-1}AP = \begin{pmatrix} 0 & 1 & -2 + 2 \\ 0 & 0 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}.$$
6. Direct check in the new bases: $D(1) = 0$, $D(x - 1) = 1$ and $D\bigl((x - 1)^2\bigr) = 2(x - 1)$.
   Their $C'$-coordinates are $(0, 0)$, $(1, 0)$ and $(0, 2)$, so $[D]_{C',B'}$ is the matrix of step 5.
7. Check on a vector: $p = x^2$ has $[p]_{B'} = (1, 2, 1)$, from the [[Taylor coordinates example|F4TC36FYWW]].
   Then $[D]_{C',B'}(1, 2, 1) = (2, 2)$, and $2 + 2(x - 1) = 2x = D(x^2)$.

## Remarks

The matrix did not change, because the derivative does not care where we center the polynomials.
The new bases are the old ones shifted by $x \mapsto x - 1$, and the derivative of $(x - 1)^k$ is $k(x - 1)^{k - 1}$, exactly as for $x^k$.

If we change the basis on one side only, the matrix does change.
With $B'$ in the domain and $C$ in the target, the matrix is $AP$ from step 4.
Its third column $(-2, 2)$ says that $D\bigl((x - 1)^2\bigr) = -2 + 2x$ in the basis $C$, which is correct.
A center other than $1$ in only one of the two spaces would also change the matrix.

## Explanations

### L1 human

The formula predicts the matrix of the derivative in the new bases, and a direct computation in the new bases gives the same matrix.
Here both computations give the same matrix as in the old bases, because shifting every polynomial by one step does not change how it differentiates.

### L2 human

Read $Q^{-1}AP$ from right to left.
The factor $P$ changes the input basis from $B'$ to $B$, the matrix $A$ differentiates, and $Q^{-1}$ changes the output basis from $C$ to $C'$.
Watch out: using $Q$ in place of $Q^{-1}$ subtracts row 2 from row 1 of $AP$, and the result $\begin{pmatrix} 0 & 1 & -4 \\ 0 & 0 & 2 \end{pmatrix}$ is wrong, since its third column would give $D\bigl((x - 1)^2\bigr) = -4 + 2(x - 1)$.
