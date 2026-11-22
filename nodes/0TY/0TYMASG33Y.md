---
tag: 0TYMASG33Y
kind: statement
role: proposition
name: Characteristic polynomial does not depend on the basis
msc: ["15A15", "15A18"]
topics: [6R1D6QPY3S]
audience: ug1
uses: [039HF58KQ5, 027KDW2K72]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
---

## Statement

Similar matrices have the same characteristic polynomial.
Let $K$ be a commutative ring, let $n \ge 1$, let $A$ be an $n \times n$ matrix over $K$, and let $P$ be an invertible $n \times n$ matrix over $K$.
Then the [[characteristic polynomials|0VSSPAFM2C]] of $A$ and $P^{-1} A P$ are equal:
$$p_{P^{-1} A P}(t) = p_A(t).$$
In particular, [[similar matrices|0E89HQATM8]] have the same characteristic polynomial.

## Remarks

### Why it holds

The scalar matrix $tI$ commutes with every matrix, so $P^{-1}(tI)P = tI$.
Then the product rule for determinants over $K[t]$ gives
$$\det(tI - P^{-1}AP) = \det\big(P^{-1}(tI - A)P\big) = \det(P^{-1}) \det(tI - A) \det P = \det(tI - A).$$
The [[proof|ZWPWDMZKD2]] checks each step.

### A check with numbers

Take $A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$ and $P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, with $P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$.
Multiply out:
$$P^{-1} A P = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 3 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}.$$
Both matrices have trace $4$ and determinant $3$, so both have $p(t) = t^2 - 4t + 3 = (t - 1)(t - 3)$.

### What it gives you

Each matrix of a linear map $T$ in a basis is similar to every other one, so the [[characteristic polynomial of a linear map|0J5EMJRRFM]] is well defined.
Everything read from the polynomial is then an invariant of the map: the eigenvalues, their algebraic multiplicities, the trace and the determinant.

### The converse

The converse is false.
The matrices $I_2$ and $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ both have $p(t) = (t - 1)^2$.
They are not similar, because $P^{-1} I_2 P = I_2$ for every invertible $P$.

## Explanations

### L1 human

A change of basis does not change the characteristic polynomial.
So the eigenvalues, the trace and the determinant, which we read from it, are the same in every basis.
They describe the linear map itself, not one table of numbers for it.
