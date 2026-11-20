---
tag: WBJGQNKA4A
kind: proof
name: Proof of the invertible matrix theorem
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug1
proves: ACDFDABVQK
methods: [0NTF6DMVAP, TFQ1845T84, 0J0XBKG64S]
uses: [0TWTS88TWN, 1ZK55FS2BF, 3RQX3T70NX, 2ZH4X4Q99D, F7F6AA3XQ7, 0WF5AQYTW6, 0BCMGDHZGR, 0CRMGPAH83, 0DTY8B9HMS, 0KCQ9Y3QKA, 0BJBYCGMWE, 11CSKXQNG3, 0PHDYNR24D, 03AJKXH1AV, 0PDVQEP0ZC, FBSAPTP1PR, 0BQAA2BK3Q, 073E4XC016]
sources:
  - book: isbn:9780321982384
    locator: Section 2.3
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: The invertible matrix theorem
---

## Proof

We first prove the cycle $1 \Rightarrow 2 \Rightarrow 7 \Rightarrow 4 \Rightarrow 6 \Rightarrow 1$ and the cycle $1 \Rightarrow 3 \Rightarrow 8 \Rightarrow 5 \Rightarrow 4$.
These use only elimination.
Then we attach the other conditions one at a time.

**The first cycle.**

1. $1 \Rightarrow 2$: take $C = A^{-1}$, by the [[definition of the inverse|0TWTS88TWN]].
2. $2 \Rightarrow 7$: if $Ax = 0$, then $x = I_n x = (CA)x = C(Ax) = 0$, by [[associativity|073E4XC016]].
3. $7 \Rightarrow 4$, $4 \Rightarrow 6$ and $6 \Rightarrow 1$ are the implications of [[invertibility and row reduction|1ZK55FS2BF]].

**The second cycle.**

4. $1 \Rightarrow 3$: take $D = A^{-1}$.
5. $3 \Rightarrow 8$: for $b \in F^n$, the vector $x = Db$ satisfies $Ax = (AD)b = b$.
6. $8 \Rightarrow 5$: let $R = EA$ be the [[reduced row echelon form|0WF5AQYTW6]] of $A$. Here $E$ is a product of elementary matrices and so invertible, by the [[row operation theorem|F7F6AA3XQ7]]. Suppose that $A$ has $r < n$ [[pivot positions|0BCMGDHZGR]]. Then the pivots of $R$ lie in rows $1, \dots, r$, and row $n$ of $R$ is zero.
7. Let $b = E^{-1} e_n$. By condition 8, some $x$ satisfies $Ax = b$. Then $Rx = EAx = Eb = e_n$.
8. Row $n$ of $Rx$ is $0$, because row $n$ of $R$ is zero, but entry $n$ of $e_n$ is $1$. This contradiction shows $r = n$.
9. $5 \Rightarrow 4$: the $n$ pivots of $R$ lie in $n$ different rows and $n$ different columns, so each column of $R$ is a pivot column. As in [[invertibility and row reduction|1ZK55FS2BF]], the pivot of column $j$ is then a $1$ in row $j$. The other entries of column $j$ are $0$. So $R = I_n$.
10. $4 \Rightarrow 5$: $I_n$ has $n$ pivots. With step 3 this joins both cycles, so conditions 1 to 8 are equivalent.

**Uniqueness of solutions.**

11. $1 \Rightarrow 9$ is the [[solution theorem|3RQX3T70NX]].
12. $9 \Rightarrow 8$ holds because "exactly one" includes "at least one".

**Columns and the linear map.** Write $a_1, \dots, a_n$ for the columns of $A$.

13. By the column rule of the [[matrix-vector product|0PDVQEP0ZC]], $Ax = x_1 a_1 + \dots + x_n a_n$ for each $x \in F^n$.
14. $7 \Leftrightarrow 10$: by step 13, a nonzero $x$ with $Ax = 0$ is the same as a nontrivial relation $\sum x_j a_j = 0$. So condition 7 is the definition of [[linear independence|0CRMGPAH83]] of the columns.
15. $8 \Leftrightarrow 11$: by step 13, $Ax = b$ has a solution exactly when $b$ is a combination of the columns. So condition 8 says that the columns [[span|0DTY8B9HMS]] $F^n$.
16. $12 \Leftrightarrow (10 \text{ and } 11)$ is the definition of a [[basis|0KCQ9Y3QKA]]. Since 10 and 11 are both equivalent to condition 1, so is 12.
17. $13 \Leftrightarrow 7$: $T$ is injective exactly when its kernel is $\set{0}$, by the theorem that [[a linear map is injective iff its kernel is trivial|0BJBYCGMWE]]. The kernel of $T$ is the solution set of $Ax = 0$.
18. $14 \Leftrightarrow 8$: $T$ is surjective exactly when each $b$ is $Ax$ for some $x$, which is condition 8.
19. $15 \Leftrightarrow (13 \text{ and } 14)$ is the definition of a bijection.
20. $17 \Leftrightarrow 7$: the [[null space|0PHDYNR24D]] is the solution set of $Ax = 0$.
21. $18 \Leftrightarrow 11$: the [[column space|03AJKXH1AV]] is the span of the columns.
22. $16 \Leftrightarrow 5$: the rank is the dimension of the column space. This dimension equals the number of pivot columns, by the theorem on the [[pivot basis of the column space|11CSKXQNG3]].

**The transpose.**

23. $1 \Rightarrow 19$: by part 2 of the [[rules for inverses|2ZH4X4Q99D]], $A^{\mathsf{T}}$ is invertible.
24. $19 \Rightarrow 1$: apply the same rule to $A^{\mathsf{T}}$. Then $(A^{\mathsf{T}})^{\mathsf{T}} = A$ is invertible.
25. $20 \Leftrightarrow 19$: the rows of $A$ are the columns of $A^{\mathsf{T}}$. By the equivalence of conditions 10 and 1, proved above for each square matrix, these columns are independent exactly when $A^{\mathsf{T}}$ is invertible.

**The later conditions.**

26. $21 \Leftrightarrow 1$ is the [[determinant criterion|FBSAPTP1PR]].
27. $22 \Leftrightarrow 7$: by the definition of an [[eigenvalue|0BQAA2BK3Q]], $0$ is an eigenvalue of $A$ exactly when $Ax = 0 \cdot x = 0$ for some $x \ne 0$.

So all $22$ conditions are equivalent.

## Idea

Elimination reduces everything to the count of pivots.
If there are $n$ pivots, the reduced form is $I_n$ and every condition holds.
If there are fewer, a free variable gives a nonzero solution of $Ax = 0$, and a zero row gives a right-hand side with no solution.

## Variants

The equivalence $13 \Leftrightarrow 14$ can also be proved directly by [[rank-nullity|0W4FSW1TVB]]: $\dim \ker T + \dim \im T = n$.
This is the route of books such as Axler that start from linear maps.
