---
tag: 1BYS6TGJH1
kind: proof
name: Proof of the rank normal form by row and column operations
msc: ["15A21"]
topics: [P8J6QR66TJ]
audience: ug1
proves: T2H2QV0M06
methods: [X5HG1RNWQX, 01XM7JEKHY, TFQ1845T84]
uses: [098D6FQN3N, 0NNR68BFRY, F7F6AA3XQ7, 0S4WTRE9GG, 02FDWY55AS, 0EWQEYRVA8, 0P21AVFFSP]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_equivalence
    locator: lead section
---

## Proof

**Part 1.**

1. If $r = 0$, then $A$ has zero column space, so $A = 0 = N_0$, and $P = I_m$, $Q = I_n$ work. Let $r \ge 1$ from now on.
2. By [[Gauss-Jordan elimination|098D6FQN3N]], a finite sequence of row operations turns $A$ into its reduced row echelon form $R$.
3. By the [[theorem on elementary matrices|F7F6AA3XQ7]], each row operation is left multiplication by an elementary matrix $E_l$, and each $E_l$ is invertible. So $R = PA$ with $P = E_k \cdots E_1$, which is invertible as a [[product of invertible matrices|0S4WTRE9GG]].
4. Let $s$ be the number of nonzero rows of $R$, and let $j_1 < \dots < j_s$ be its pivot columns. By the [[definition of the reduced row echelon form|0NNR68BFRY]], column $j_t$ of $R$ is $e_t$.
5. Rows $s + 1, \dots, m$ of $R$ are zero, so each column of $R$ lies in the span of $e_1, \dots, e_s$. With step 4, the column space of $R$ is this span, so $\operatorname{rank} R = s$, by the [[definition of rank|0EWQEYRVA8]].
6. By the [[rank of a product|02FDWY55AS]], $\operatorname{rank}(PA) \le \operatorname{rank} A$ and $\operatorname{rank} A = \operatorname{rank}(P^{-1}PA) \le \operatorname{rank}(PA)$. So $s = \operatorname{rank} R = \operatorname{rank} A = r$.
7. Right multiplication by an exchange matrix $P_{ij}$ exchanges columns $i$ and $j$, by the theorem on elementary matrices. Using such exchanges, move column $j_1$ to position $1$, then column $j_2$ to position $2$, and so on. Let $Q_1$ be the product of these exchange matrices. Then $R Q_1 = \begin{pmatrix} I_r & X \\ 0 & 0 \end{pmatrix}$ for some $r \times (n - r)$ matrix $X$.
8. For each $t \le r$ and each column $j > r$, multiply on the right by $T_{tj}(-x)$, where $x$ is the current entry $(t, j)$. This subtracts $x$ times column $t$ from column $j$. Column $t$ is $e_t$, so only entry $(t, j)$ changes, and it becomes $0$.
9. Let $Q_2$ be the product of the matrices in step 8. Then $R Q_1 Q_2 = N_r$.
10. Put $Q = Q_1 Q_2$. It is a product of elementary matrices, so it is invertible, and $PAQ = RQ = N_r$.

**Part 2.**

11. Let $B = PAQ$ with invertible $P$ and $Q$. By the rank of a product, $\operatorname{rank} B \le \operatorname{rank}(AQ) \le \operatorname{rank} A$.
12. Also $A = P^{-1} B Q^{-1}$, so in the same way $\operatorname{rank} A \le \operatorname{rank} B$. So equivalent matrices have the same rank.
13. Conversely, let $A$ and $B$ be $m \times n$ matrices of the same rank $r$. By part 1, $PAQ = N_r = P'BQ'$ for invertible $P, Q, P', Q'$.
14. Then $B = (P'^{-1}P)\, A\, (QQ'^{-1})$. The factors $P'^{-1}P$ and $QQ'^{-1}$ are invertible as products of invertible matrices. So $A$ and $B$ are [[equivalent|0P21AVFFSP]].

## Idea

Row operations bring $A$ to reduced row echelon form, where the pivot columns are standard basis vectors.
Column exchanges put these columns first, and column replacements clear the rest of the pivot rows.
Invertible factors do not change the rank, so the size $r$ of the identity block is the rank.

## Variants

A proof with linear maps: choose a basis $v_{r+1}, \dots, v_n$ of the kernel of $A$ and extend it by $v_1, \dots, v_r$ to a basis of $F^n$.
The vectors $Av_1, \dots, Av_r$ form a basis of the column space, and one extends them to a basis of $F^m$.
In these bases the matrix of $A$ is $N_r$, and the change of basis matrices give $P$ and $Q$.
