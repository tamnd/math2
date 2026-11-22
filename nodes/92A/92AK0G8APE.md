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

For part 1 we compute the coefficient of $t^{n-1}$ in $p_A$ in two ways, from the factored form and from the determinant.
For part 2 we put $A$ in triangular form, where the powers are easy to read.

*Part 1.*

1. By hypothesis the [[characteristic polynomial|039HF58KQ5]] is $p_A(t) = (t - \lambda_1) \cdots (t - \lambda_n)$ with all $\lambda_i \in F$.
2. We claim that for each $k \ge 1$,
$$\prod_{i=1}^{k} (t - \lambda_i) = t^k - (\lambda_1 + \dots + \lambda_k)\, t^{k-1} + r_k,$$
   where $r_k$ is $0$ or a polynomial of [[degree|0DPF6WRZW6]] at most $k - 2$.
3. For $k = 1$ the claim holds with $r_1 = 0$.
4. Suppose that the claim holds for $k$.
   Write $s = \lambda_1 + \dots + \lambda_k$ and $c = \lambda_{k+1}$, and multiply both sides by $t - c$:
$$\big(t^k - s t^{k-1} + r_k\big)(t - c) = t^{k+1} - (s + c)\, t^k + r_{k+1}, \qquad r_{k+1} = c s\, t^{k-1} + t\, r_k - c\, r_k.$$
5. Each of the three terms of $r_{k+1}$ is $0$ or has degree at most $k - 1$, because $r_k$ has degree at most $k - 2$.
   So the claim holds for $k + 1$, and by induction it holds for every $k$.
6. With $k = n$, step 2 shows that the coefficient of $t^{n-1}$ in $p_A$ is $-(\lambda_1 + \dots + \lambda_n)$.
7. By the theorem on the [[coefficients of the characteristic polynomial|0FRYPZ6D0X]], the same coefficient is $-\operatorname{tr} A$.
8. Comparing steps 6 and 7 gives $\operatorname{tr} A = \lambda_1 + \dots + \lambda_n$.

*Part 2.*

9. Fix $k \ge 1$.
   Since $p_A$ splits over $F$, [[triangularization|0363JMQ42Y]] gives an invertible $P$ and an upper triangular $U$ with $A = P U P^{-1}$.
10. The matrices $U$ and $A$ are similar, so $p_U = p_A$, because the [[characteristic polynomial does not depend on the basis|0TYMASG33Y]].
11. The matrix $tI - U$ is upper triangular with the diagonal entries $t - u_{11}, \dots, t - u_{nn}$.
    By the [[determinant of a triangular matrix|0K1KKMFHYH]] over $F[t]$, $p_U = \prod_i (t - u_{ii})$.
12. Steps 1, 10 and 11 give $\prod_i (t - u_{ii}) = \prod_i (t - \lambda_i)$.
    Unique factorization in $F[t]$ shows that $u_{11}, \dots, u_{nn}$ is a reordering of $\lambda_1, \dots, \lambda_n$.
13. In $(P U P^{-1})^k$ each inner pair $P^{-1} P$ cancels, so $A^k = P U^k P^{-1}$.
14. A [[product of upper triangular matrices is upper triangular|45RET2Y995]], and its diagonal entries are the products of the diagonal entries.
    By induction on $k$, $U^k$ is upper triangular with the diagonal entries $u_{11}^k, \dots, u_{nn}^k$.
15. By the [[cyclic property of the trace|0Y4NF1DRKD]],
$$\operatorname{tr}(A^k) = \operatorname{tr}(P U^k P^{-1}) = \operatorname{tr}(U^k P^{-1} P) = \operatorname{tr}(U^k).$$
16. By steps 12, 14 and 15, $\operatorname{tr}(A^k) = \sum_i u_{ii}^k = \sum_i \lambda_i^k$.

## Idea

Multiply out $(t - \lambda_1) \cdots (t - \lambda_n)$ and only watch the second coefficient: it is minus the sum of the roots.
Expand $\det(tI - A)$ and watch the same coefficient: only the product of the diagonal entries reaches $t^{n-1}$, and it gives minus the trace.
So the two numbers agree.
For the powers, a triangular form puts the eigenvalues on the diagonal, and raising a triangular matrix to the power $k$ raises each diagonal entry to the power $k$.

## Variants

Part 1 is the case $k = 1$ of part 2, so the triangular argument alone proves both parts.
Part 2 also follows from part 1 applied to $A^k$, once we know that $p_{A^k} = \prod_i (t - \lambda_i^k)$; that product formula is itself proved by triangularization.
When $p_A$ does not split over $F$, we apply the theorem in a splitting field $E$ of $p_A$.
The trace and $p_A$ do not change when $A$ is viewed over $E$, so the roots of $p_A$ in $E$ add up to $\operatorname{tr} A$.
