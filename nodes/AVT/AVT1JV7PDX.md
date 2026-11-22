---
tag: AVT1JV7PDX
kind: proof
name: Proof of the pivot test for spanning F^m
msc: ["15A03", "15A06"]
topics: [MVH97H8B2J]
audience: ug1
proves: D3PN42EP4X
methods: [0NTF6DMVAP, TFQ1845T84]
uses: [E7SAHXQEVC, K41GT10YM6, FCM29NQ6DN, BKA191KD1S, 0BCMGDHZGR]
sources:
  - url: https://en.wikipedia.org/wiki/Row_echelon_form
    locator: Systems of linear equations
  - book: isbn:9780321982384
    locator: Section 1.4
---

## Proof

We turn spanning into the consistency of the systems $Ax = b$, and then read consistency from the echelon form.
Let $R$ be a row echelon form of $A$, reached by a sequence of elementary row operations, which exists by [[the echelon form theorem|FCM29NQ6DN]].

1. By [[linear systems as vector equations|E7SAHXQEVC]], $x_1 v_1 + \dots + x_n v_n = Ax$ for every $x \in F^n$. So a vector $b$ lies in $\operatorname{span}(v_1, \dots, v_n)$ exactly when the system $Ax = b$ has a solution.
2. Fix $b \in F^m$ and apply the same row operations to the augmented matrix $[A \mid b]$. Row operations act on whole rows, so the left part becomes $R$, and the result is $[R \mid c]$ for some $c \in F^m$.
3. By [[the reversibility of row operations|K41GT10YM6]], the systems $Ax = b$ and $Rx = c$ have the same solutions.
4. For the "if" direction, assume that every row of $R$ has a pivot. Then $[R \mid c]$ is in echelon form with the same pivots as $R$, so its last column holds no pivot.
5. By [[the consistency criterion|BKA191KD1S]], $Rx = c$ has a solution, so $Ax = b$ has one by step 3. Since $b$ was arbitrary, the vectors span $F^m$ by step 1.
6. For the "only if" direction, assume that some row of $R$ has no pivot. A row without a pivot is a zero row, and in echelon form the zero rows come last, so row $m$ of $R$ is zero.
7. Let $e_m = (0, \dots, 0, 1)$ and start from the matrix $[R \mid e_m]$. Undo the row operations in reverse order; each has an inverse row operation by [[reversibility|K41GT10YM6]], so this gives a matrix $[A \mid b]$ for some $b \in F^m$.
8. The last row of $[R \mid e_m]$ reads $0 = 1$, so $Rx = e_m$ has no solution. By step 3, $Ax = b$ has no solution either.
9. So $b$ is not in the span by step 1, and the vectors do not span $F^m$. This proves part 1.
10. For part 2, each pivot of $R$ is the leading entry of its row and lies in its own column, so $R$ has at most $n$ pivots. If the vectors span $F^m$, then part 1 gives a pivot in each of the $m$ rows, so $m \le n$.

## Idea

Spanning means that every system $Ax = b$ is solvable, and row operations do not change which systems are solvable, only how they look.
In echelon form the answer is visible.
A pivot in every row leaves no room for an equation $0 = 1$.
A zero row lets us put a $1$ next to it, and running the row operations backward turns that bad right side into a vector $b$ that the columns of $A$ cannot reach.

## Variants

With matrices, the row operations are a product $E$ of elementary matrices with $EA = R$, and $E$ is invertible.
The bad right side of step 7 is then $b = E^{-1} e_m$, and $Ax = b$ is equivalent to $Rx = EAx = e_m$.
A proof by rank also works: the columns span $F^m$ exactly when the column space has dimension $m$, and the rank of $A$ equals the number of pivots of $R$.
