---
tag: E61BVD6G2D
kind: proof
name: Proof of the order of the general linear group over a finite field by counting columns
msc: [20G40]
proves: 0JQ1KNQW2K
uses: [08RTDHX1SK, 0TWTS88TWN, 0EVHJFTG9Z, 0HR573CHNM, 0QK7FPE6VE, 096V7H13H9, 0SEX9F9J5Z]
sources:
  - url: https://en.wikipedia.org/wiki/General_linear_group
    locator: Over finite fields
---

## Proof

We count the ordered families of linearly independent columns. Let $F = \F_q$ be the [[finite field|08RTDHX1SK]] with $q$ elements and let $V = F^n$, so $\abs{V} = q^n$.

1. An $n \times n$ matrix $A$ over $F$ is the same as the ordered family $(a_1, \dots, a_n)$ of its columns, with $a_j \in V$. For $c \in V$ with entries $c_j$, we have $A c = \sum_{j} c_j a_j$.
2. Claim: $A$ is [[invertible|0TWTS88TWN]] if and only if its columns are [[linearly independent|0EVHJFTG9Z]]. First let $A$ be invertible with inverse $A^{-1}$.
3. If $\sum_j c_j a_j = 0$, then $A c = 0$ by step 1, so $c = A^{-1} A c = 0$. So the columns are linearly independent.
4. Conversely, let the columns be linearly independent. The space $V$ has [[dimension $n$|0QK7FPE6VE]], so the $n$ columns form a [[basis|096V7H13H9]] of $V$.
5. Let $e_1, \dots, e_n$ be the standard basis vectors. By step 4, for each $i$ there is $b_i \in V$ with $A b_i = e_i$. The matrix $B$ with columns $b_1, \dots, b_n$ satisfies $A B = I_n$.
6. The columns of $B$ are linearly independent: if $B c = 0$, then $c = A B c = 0$. By steps 4 and 5 applied to $B$, there is a matrix $C$ with $B C = I_n$.
7. Then $A = A (B C) = (A B) C = C$, so $B A = I_n$. Thus $A$ is invertible, and the claim holds.
8. By steps 1 and 7, $\abs{\mathrm{GL}_n(F)}$ is the number $N_n$ of linearly independent families $(u_1, \dots, u_n)$ in $V$. For $0 \leq k \leq n$, let $N_k$ be the number of linearly independent families of $k$ vectors.
9. Let $(u_1, \dots, u_k)$ be linearly independent with [[span|0HR573CHNM]] $W$. The map $F^k \to W$, $c \mapsto \sum_i c_i u_i$, is onto by the definition of the span.
10. It is injective: equal images give $\sum_i (c_i - c'_i) u_i = 0$, so $c = c'$ by independence. Hence $\abs{W} = \abs{F^k} = q^k$.
11. With $(u_1, \dots, u_k)$ as in step 9, let $u \in V$. If $u \in W$, say $u = \sum_i c_i u_i$, then $\sum_i c_i u_i - u = 0$ is a nontrivial relation. So $(u_1, \dots, u_k, u)$ is dependent.
12. If $u \notin W$ and $\sum_i c_i u_i + c u = 0$, then $c = 0$, since otherwise $u = -c^{-1} \sum_i c_i u_i \in W$. Then all $c_i = 0$ by independence. So $(u_1, \dots, u_k, u)$ is independent exactly when $u \notin W$.
13. If $(u_1, \dots, u_{k+1})$ is linearly independent, so is $(u_1, \dots, u_k)$, since a relation among the first $k$ vectors extends by the coefficient $0$.
14. By steps 10, 12 and 13, each independent family of $k$ vectors extends in exactly $q^n - q^k$ ways. All independent families of $k + 1$ vectors arise in this way. So $N_{k+1} = N_k (q^n - q^k)$ for $0 \leq k < n$.
15. The empty family is linearly independent, so $N_0 = 1$. By induction on $k$ with step 14, $N_k = \prod_{j=0}^{k-1} (q^n - q^j)$.
16. For $k = n$ and step 8, the [[order|0SEX9F9J5Z]] of $\mathrm{GL}_n(\F_q)$ is $\prod_{k=0}^{n-1} (q^n - q^k) = (q^n - 1)(q^n - q) \cdots (q^n - q^{n-1})$.

## Idea

A matrix is invertible exactly when its columns are linearly independent, so we choose the columns one at a time. The $(k+1)$-th column must avoid the span of the first $k$ columns, which has $q^k$ elements. That leaves $q^n - q^k$ choices at each stage.
