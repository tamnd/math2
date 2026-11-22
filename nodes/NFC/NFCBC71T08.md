---
tag: NFCBC71T08
kind: proof
name: Proof of the determinant of a scalar multiple
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 01EXSMK864
methods: [0NTF6DMVAP]
uses: [09V6DDACXR, 009CY8JXFX]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Proof

We scale the rows of $A$ one at a time and count the factors $c$ by induction.

1. For $0 \le k \le n$, let $A_k$ be the matrix whose rows $1, \dots, k$ are $c$ times the rows of $A$ and whose other rows are those of $A$.
2. No row is scaled in $A_0$, so $A_0 = A$.
   By the definition of the [[scalar multiple|09V6DDACXR]], every entry of $cA$ is $c$ times the entry of $A$, so $A_n = cA$.
3. For $1 \le k \le n$, the matrix $A_k$ results from $A_{k-1}$ when row $k$ is multiplied by $c$.
4. By the rule for [[scaling a row|009CY8JXFX]], $\det A_k = c \det A_{k-1}$ for $1 \le k \le n$.
5. We show $\det A_k = c^k \det A$ by induction on $k$.
   For $k = 0$ it is $\det A_0 = \det A$, by step 2.
   If it holds for $k - 1$, then step 4 gives $\det A_k = c \cdot c^{k-1} \det A = c^k \det A$.
6. For $k = n$, step 2 gives $\det(cA) = \det A_n = c^n \det A$.

## Idea

Multiplying a matrix by $c$ is the same as multiplying each of its $n$ rows by $c$.
Each row scaling brings out one factor $c$, so in total we get $c^n$.
The matrices $A_k$ only make the order of the $n$ scalings explicit.

## Variants

The Leibniz sum gives a one-line proof.
Each term of $\det(cA)$ is a product of $n$ entries of $cA$, so it is $c^n$ times the matching term of $\det A$.
Another route uses [[multiplicativity|04CPJ6AF00]]: $cA = (c I_n) A$, and $\det(c I_n) = c^n$ because $c I_n$ is diagonal.
