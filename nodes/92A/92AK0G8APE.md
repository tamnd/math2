---
tag: 92AK0G8APE
kind: proof
name: Proof that the trace is the sum of the eigenvalues by comparing coefficients
msc: ["15A15", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: 0NMXDCNNKR
methods: [0NTF6DMVAP, 0ASJVEFA9J]
uses: [0FRYPZ6D0X, 039HF58KQ5, 0DPF6WRZW6, 0363JMQ42Y, 45RET2Y995, 0Y4NF1DRKD, 0K1KKMFHYH, 0TYMASG33Y]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace as the sum of eigenvalues
---

## Proof

Part 1.
We compute the coefficient of $t^{n-1}$ of $p_A$ in two ways.

1. Assume that the [[characteristic polynomial|039HF58KQ5]] is $p_A(t) = (t - \lambda_1) \cdots (t - \lambda_n)$ with $\lambda_i \in F$.
2. Claim: for $k \ge 1$, $\prod_{i=1}^{k} (t - \lambda_i) = t^k - (\lambda_1 + \cdots + \lambda_k) t^{k-1} + r_k$, where $r_k$ is $0$ or has [[degree|0DPF6WRZW6]] at most $k - 2$.
3. For $k = 1$, the claim holds with $r_1 = 0$.
4. Suppose the claim holds for $k$, and let $s = \lambda_1 + \cdots + \lambda_k$ and $c = \lambda_{k+1}$. Multiply both sides by $t - c$.
5. This gives $t^{k+1} - (s + c) t^k + r_{k+1}$, with $r_{k+1} = c s\, t^{k-1} + t\, r_k - c\, r_k$.
6. Each of the three terms of $r_{k+1}$ is $0$ or has degree at most $k - 1$. So the claim holds for $k + 1$, and by induction for all $k$.
7. By step 2 with $k = n$, the coefficient of $t^{n-1}$ in $p_A$ is $-(\lambda_1 + \cdots + \lambda_n)$.
8. By the theorem on the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]], the same coefficient is $-\tr A$.
9. By steps 7 and 8, $\tr A = \lambda_1 + \lambda_2 + \cdots + \lambda_n$.

Part 2.
Let $k \ge 1$.

10. Since $p_A$ splits, [[triangularisation|0363JMQ42Y]] gives an invertible $P$ and an upper triangular $U$ with $A = P U P^{-1}$.
11. $U$ is similar to $A$, so $p_U = p_A$, by the theorem that the [[characteristic polynomial does not depend on the basis|0TYMASG33Y]].
12. $tI - U$ is upper triangular with diagonal $t - u_{11}, \dots, t - u_{nn}$. By the [[determinant of a triangular matrix|0K1KKMFHYH]] over $F[t]$, $p_U = \prod_i (t - u_{ii})$.
13. By steps 1, 11 and 12, $\prod_i (t - u_{ii}) = \prod_i (t - \lambda_i)$. Unique factorization in $F[t]$ shows that $u_{11}, \dots, u_{nn}$ is a reordering of $\lambda_1, \dots, \lambda_n$.
14. $A^k = P U^k P^{-1}$, because the inner factors $P^{-1} P$ cancel in $(P U P^{-1})^k$.
15. By the theorem that a [[product of upper triangular matrices is upper triangular|45RET2Y995]], with induction on $k$, $U^k$ is upper triangular with diagonal entries $u_{11}^k, \dots, u_{nn}^k$.
16. By the [[cyclic property of the trace|0Y4NF1DRKD]], $\tr(P U^k P^{-1}) = \tr(U^k P^{-1} P) = \tr(U^k)$.
17. So $\tr(A^k) = \tr(U^k) = \sum_i u_{ii}^k = \sum_i \lambda_i^k$, by steps 13 to 16.

## Idea

Multiplying out $(t - \lambda_1) \cdots (t - \lambda_n)$ gives $t^n - (\lambda_1 + \cdots + \lambda_n) t^{n-1} + \cdots$.
The same coefficient of $t^{n-1}$ is $-\tr A$ when $\det(t I - A)$ is expanded.
For powers, a triangular form shows the eigenvalues on the diagonal, and taking powers keeps them there as $\lambda_i^k$.

## Variants

- Part 1 is also the case $k = 1$ of part 2, so the triangular proof gives both parts.
- Part 2 also follows from part 1 applied to $A^k$, once one knows that $p_{A^k} = \prod_i (t - \lambda_i^k)$. This product formula is itself proved by triangularisation.
- Over a field where $p_A$ does not split, apply the theorem in a splitting field $E$ of $p_A$. The trace and $p_A$ do not change when $A$ is viewed over $E$.
