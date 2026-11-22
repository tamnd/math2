---
tag: Z3WXKM7QEC
kind: proof
name: Proof of simultaneous triangularization by a common eigenvector
msc: ["15A21", "15A27"]
topics: [Z6S6PWMJPH]
audience: grad
proves: 42PG67Q5YN
methods: [0ASJVEFA9J, B2D8PTFNN1]
uses: [0QEM68Y0DE, 8YNE1HTZEP, ENVF51H5S3, 0PFPWKBDTJ, 0J0SK5FF4M, 0W4FSW1TVB, 0363JMQ42Y, 06MRNP4BNT, 0EP59ESQ94]
sources:
  - book: isbn:9780135367971
    locator: Section 6.5
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Triangularisability
---

## Proof

We first find an eigenvector of one map inside any invariant subspace, then a common eigenvector of a finite family, and then of any family.
After that we build the common flag by induction on $n$, passing to the quotient by the line of a common eigenvector.

*An eigenvector inside an invariant subspace.*

1. Let $T \in \mathcal{F}$ with $p_T = (t - \lambda_1) \cdots (t - \lambda_n)$, and let $W \ne 0$ be a $T$-invariant subspace.
   We show that $T$ has an eigenvector in $W$.
2. By the [[Cayley-Hamilton theorem|0QEM68Y0DE]], $(T - \lambda_n) \cdots (T - \lambda_1) = p_T(T) = 0$, where the factors commute because they are polynomials in $T$.
3. Choose $w \in W$ with $w \ne 0$.
   Put $u_0 = w$ and $u_j = (T - \lambda_j) u_{j-1}$ for $j = 1, \dots, n$.
   Each $u_j$ lies in $W$ because $W$ is $T$-invariant, and $u_n = p_T(T) w = 0$ by step 2.
4. Let $j \ge 1$ be the least index with $u_j = 0$, which exists because $u_0 \ne 0$ and $u_n = 0$.
   Then $u_{j-1} \ne 0$ and $(T - \lambda_j) u_{j-1} = 0$, so $u_{j-1}$ is an eigenvector of $T$ in $W$.

*A common eigenvector of finitely many members.*

5. Let $T_1, \dots, T_r \in \mathcal{F}$, and put $W_0 = V$.
   Suppose that $W_{i-1} \ne 0$ is invariant under every member of $\mathcal{F}$.
6. By steps 1 to 4, $T_i$ has an eigenvalue $\mu_i$ with an eigenvector in $W_{i-1}$.
   Put $W_i = W_{i-1} \cap \ker(T_i - \mu_i)$, so $W_i \ne 0$.
7. Each $S \in \mathcal{F}$ commutes with $T_i$, hence with $T_i - \mu_i$.
   So $\ker(T_i - \mu_i)$ is $S$-invariant, by the result that [[kernels of commuting maps are invariant|8YNE1HTZEP]].
8. An intersection of $S$-invariant subspaces is $S$-invariant, so $W_i$ is invariant under every $S \in \mathcal{F}$.
   This allows the next step of the construction.
9. After $r$ steps, $W_r \ne 0$, and every nonzero $v \in W_r$ satisfies $T_i v = \mu_i v$ for $i = 1, \dots, r$.

*A common eigenvector of the whole family.*

10. The span of $\mathcal{F}$ in $\operatorname{End}(V)$ has dimension at most $n^2$.
    [[Every spanning set contains a basis|06MRNP4BNT]], so finitely many members $T_1, \dots, T_r$ span it.
11. Each $T \in \mathcal{F}$ is a combination $\sum_i c_i T_i$, so for $v$ as in step 9
    $$T v = \sum_i c_i T_i v = \Big(\sum_i c_i \mu_i\Big) v.$$
    This proves part 1.

*The common flag.*

12. We prove part 2 by induction on $n$.
    For $n = 1$, the flag $0 \subset V$ works.
13. Let $n \ge 2$.
    By part 1 there is a common eigenvector $v$, and $U = F v$ is invariant under every $T \in \mathcal{F}$.
14. Each $T$ induces the [[quotient operator|0PFPWKBDTJ]] $\bar T$ on $V / U$, with $\bar T \pi = \pi T$ for the [[quotient map|0J0SK5FF4M]] $\pi \colon V \to V / U$.
15. The maps $\bar T$ commute pairwise.
    Indeed $\bar S \bar T \pi = \pi S T = \pi T S = \bar T \bar S \pi$, and $\pi$ is onto.
16. Write $T v = \alpha_T v$.
    By the [[block triangular form|ENVF51H5S3]], $p_T = (t - \alpha_T) \, p_{\bar T}$.
17. Write $p_T = \prod_i (t - \lambda_i)$.
    Putting $t = \alpha_T$ gives $\prod_i (\alpha_T - \lambda_i) = 0$, so $\alpha_T = \lambda_k$ for some $k$.
    Cancelling $t - \lambda_k$ in the integral domain $F[t]$ gives $p_{\bar T} = \prod_{i \ne k} (t - \lambda_i)$, which splits.
18. The space $V / U$ has dimension $n - 1$, so by steps 15 and 17 and the induction hypothesis it has a common invariant flag $0 = W_0 \subset \dots \subset W_{n-1} = V / U$.
19. Put $V_0 = 0$ and $V_i = \pi^{-1}(W_{i-1})$ for $1 \le i \le n$.
    Then $V_1 = \pi^{-1}(0) = U$ and $V_n = V$.
20. The map $\pi$ restricted to $V_i$ is onto $W_{i-1}$ with kernel $U$, so [[rank-nullity|0W4FSW1TVB]] gives $\dim V_i = \dim W_{i-1} + 1 = i$.
21. If $x \in V_i$, then $\pi(T x) = \bar T \pi(x) \in W_{i-1}$, because $W_{i-1}$ is $\bar T$-invariant.
    So $T x \in V_i$, and $(V_i)$ is a common invariant flag of $V$, which proves part 2.

*Triangular matrices.*

22. A flag of invariant subspaces gives a triangular basis, by the equivalence of conditions 1 and 2 in the [[triangularization theorem|0363JMQ42Y]].
    The basis built there from the common flag works for every member at once, which proves part 3.
23. Over $\C$, every characteristic polynomial splits, by the fundamental theorem of algebra, so the result applies to every commuting family of complex matrices.

## Idea

Commuting maps preserve each other's eigenspaces.
So an eigenspace of the first map is invariant under the second, and it contains an eigenvector of the second, and so on through the family.
This gives a common eigenvector, and the line it spans is invariant for the whole family.
Passing to the quotient by this line keeps the maps commuting and their characteristic polynomials split, and it lowers the dimension by one, so induction builds the flag.

## Variants

One can work inside a common eigenspace instead of the quotient, but the flag still has to be completed outside it, so quotients or complements appear anyway.
Over $\C$ with an inner product, the Gram-Schmidt process applied to the common triangular basis gives one unitary matrix that triangularizes the whole family.
McCoy's theorem and [[Lie's theorem|11K6SVNXMH]] replace commutativity, which steps 7 and 15 use, by weaker hypotheses with harder proofs.
