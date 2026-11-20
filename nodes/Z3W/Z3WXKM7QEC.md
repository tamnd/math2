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

We find a common eigenvector for a finite family, pass to any family, and then build the flag by induction on $n$ with quotients.

1. First let $W \ne 0$ be a subspace invariant under one $T \in \mathcal{F}$, with $p_T = (t - \lambda_1) \cdots (t - \lambda_n)$. We show that $T$ has an eigenvector in $W$.
2. By the [[Cayley-Hamilton theorem|0QEM68Y0DE]], $(T - \lambda_n) \cdots (T - \lambda_1) = p_T(T) = 0$. Choose $w \in W$ with $w \ne 0$.
3. Let $u_0 = w$ and $u_j = (T - \lambda_j) u_{j-1}$. Then $u_n = 0$, and each $u_j \in W$ since $W$ is $T$-invariant.
4. Let $j \ge 1$ be the least index with $u_j = 0$. Then $u_{j-1} \ne 0$ and $T u_{j-1} = \lambda_j u_{j-1}$. So $u_{j-1}$ is an eigenvector of $T$ in $W$.
5. Now let $T_1, \dots, T_r \in \mathcal{F}$. Let $W_0 = V$. Assume that $W_{i-1} \ne 0$ is invariant under every member of $\mathcal{F}$.
6. By steps 1 to 4, $T_i$ has an eigenvalue $\mu_i$ with an eigenvector in $W_{i-1}$. Let $W_i = W_{i-1} \cap \ker(T_i - \mu_i)$, so $W_i \ne 0$.
7. Each $S \in \mathcal{F}$ commutes with $T_i - \mu_i$. So $\ker(T_i - \mu_i)$ is $S$-invariant, by [[kernels of commuting maps are invariant|8YNE1HTZEP]].
8. An intersection of $S$-invariant subspaces is $S$-invariant. So $W_i$ is invariant under every $S \in \mathcal{F}$.
9. After $r$ steps, $W_r \ne 0$, and each nonzero $v \in W_r$ satisfies $T_i v = \mu_i v$ for $i = 1, \dots, r$.
10. For any $\mathcal{F}$, its span in $\operatorname{End}(V)$ is finite-dimensional. [[Every spanning set contains a basis|06MRNP4BNT]], so some finite $T_1, \dots, T_r \in \mathcal{F}$ span it.
11. Each $T \in \mathcal{F}$ is $\sum_i c_i T_i$. So $T v = \big(\sum_i c_i \mu_i\big) v$ for $v$ from step 9. This proves part 1.
12. For part 2, we use induction on $n$. For $n = 1$, the flag $0 \subset V$ works.
13. Let $n \ge 2$. Choose a common eigenvector $v$ by part 1, and let $U = F v$. Then $U$ is invariant under every $T \in \mathcal{F}$.
14. Each $T$ induces the [[quotient operator|0PFPWKBDTJ]] $\bar T$ on $V / U$, with $\bar T \pi = \pi T$ for the [[quotient map|0J0SK5FF4M]] $\pi$.
15. Since $\bar S \bar T \pi = \pi S T = \pi T S = \bar T \bar S \pi$ and $\pi$ is onto, the $\bar T$ commute pairwise.
16. By the [[block triangular form|ENVF51H5S3]], $p_T = (t - \alpha_T) p_{\bar T}$, where $T v = \alpha_T v$.
17. Write $p_T = \prod_i (t - \lambda_i)$. Evaluating at $\alpha_T$ gives $\alpha_T = \lambda_k$ for some $k$. Cancelling $t - \lambda_k$ in $F[t]$ gives $p_{\bar T} = \prod_{i \ne k} (t - \lambda_i)$, which splits.
18. $V / U$ has dimension $n - 1$. By the induction hypothesis, it has a common invariant flag $0 = W_0 \subset \cdots \subset W_{n-1} = V / U$.
19. Let $V_0 = 0$ and $V_i = \pi^{-1}(W_{i-1})$ for $1 \le i \le n$. Then $V_1 = U$ and $V_n = V$.
20. By [[rank-nullity|0W4FSW1TVB]] for $\pi$ restricted to $V_i$, with kernel $U$, $\dim V_i = \dim W_{i-1} + 1 = i$.
21. If $x \in V_i$, then $\pi(T x) = \bar T \pi(x) \in W_{i-1}$, since $W_{i-1}$ is $\bar T$-invariant. So $T x \in V_i$.
22. So $(V_i)$ is a common invariant flag of $V$, which proves part 2.
23. Part 3 follows from part 2, since a flag of invariant subspaces gives a triangular basis, by the [[triangularization theorem|0363JMQ42Y]].
24. Over $\C$, every characteristic polynomial splits, by the fundamental theorem of algebra. So the result applies to all commuting complex matrices.

## Idea

Commuting maps preserve each other's eigenspaces.
So one eigenspace of the first map contains an eigenvector of the second, and so on, which gives a common eigenvector.
The line it spans is invariant for the whole family.
Passing to the quotient by this line reduces the dimension by one, and induction builds the flag.

## Variants

One can instead restrict to a common eigenspace and induct on $\dim V$ there, but quotients are needed anyway to finish the flag.
Over $\C$ with an inner product, Gram-Schmidt applied to the common triangular basis gives a common unitary triangularization.
McCoy's theorem and [[Lie's theorem|11K6SVNXMH]] replace step 7, which uses commutativity, by weaker hypotheses with harder proofs.
