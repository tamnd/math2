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

Let $D \colon P_2 \to P_1$ be the derivative, from real polynomials of degree at most $2$ to those of degree at most $1$.
Take the bases $B = (1, x, x^2)$ and $B' = (1, x - 1, (x - 1)^2)$ of $P_2$, and $C = (1, x)$ and $C' = (1, x - 1)$ of $P_1$.

1. $D(1) = 0$, $D(x) = 1$ and $D(x^2) = 2x$. So the [[matrix|0YYMY95FWS]] is $A = [D]_{C,B} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$.
2. The [[change of basis matrix|0KWXYZPJKN]] from $B$ to $B'$ is $P = \begin{pmatrix} 1 & -1 & 1 \\ 0 & 1 & -2 \\ 0 & 0 & 1 \end{pmatrix}$, from $x - 1 = -1 + x$ and $(x - 1)^2 = 1 - 2x + x^2$.
3. The change of basis matrix from $C$ to $C'$ is $Q = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$, and $Q^{-1} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.
4. With the [[matrix product|076JGP6R3T]], $AP$ has row 1 equal to row 2 of $P$, that is $(0, 1, -2)$. Its row 2 is $2$ times row 3 of $P$, that is $(0, 0, 2)$.
5. $Q^{-1}(AP)$ has row 1 equal to $(0, 1, -2) + (0, 0, 2) = (0, 1, 0)$, and row 2 equal to $(0, 0, 2)$.
6. So the formula gives $[D]_{C',B'} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix}$.
7. Direct check: $D(1) = 0$, $D(x - 1) = 1$ and $D((x - 1)^2) = 2(x - 1)$. In the basis $C'$ these have coordinates $(0, 0)$, $(1, 0)$ and $(0, 2)$. This agrees with step 6.
8. Coordinates: $p = x^2$ has $[p]_B = (0, 0, 1)$ and $[p]_{B'} = P^{-1}(0, 0, 1) = (1, 2, 1)$, with $P^{-1}$ from the [[Taylor coordinates example|F4TC36FYWW]].
9. Then $[D]_{C',B'}(1, 2, 1) = (2, 2)$, so $D(p) = 2 + 2(x - 1) = 2x$. This is the derivative of $x^2$.

## Remarks

- Here the matrix does not change, because the derivative commutes with the shift $x \mapsto x - 1$.
- For a single change of basis on one side only, the matrix does change. With $B'$ and $C$, it is $AP = \begin{pmatrix} 0 & 1 & -2 \\ 0 & 0 & 2 \end{pmatrix}$.

## Explanations

### L1 human

The change of basis formula predicts the matrix of the derivative in the new bases.
A direct computation in the new bases gives the same matrix.

### L2 human

The factor $P$ on the right changes the input basis, and the factor $Q^{-1}$ on the left changes the output basis.
Changing only the input basis gives $AP$, which is the matrix of $D$ from $B'$ to $C$.
