---
tag: 6GSKMHQTD1
kind: proof
name: Proof of the Jordan normal form by generalized eigenspaces and chains
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
proves: 085HQ5G5TE
methods: [0NTF6DMVAP]
uses: [0Z3GDY89T5, 0AJ035ZTZE, Z2RTKWZZAZ, 0KN7EPH7Z0, 0MKRHZB3WS, 0MQXVZEBMT, 191HBJ7PVZ, 02SJG1HC32, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_normal_form
    locator: Generalized eigenvectors
  - url: https://en.wikipedia.org/wiki/Jordan_normal_form
    locator: Uniqueness
  - book: isbn:9780135367971
    locator: Section 7.3
---

## Proof

We split $F^n$ into generalized eigenspaces, put each nilpotent part into its chain form, and then count the blocks with ranks to get uniqueness.
Let $T \colon F^n \to F^n$ be the map $T(v) = Av$, and let $\chi_A = \prod_{i=1}^p (x - \lambda_i)^{m_i}$ with distinct $\lambda_i \in F$.

1. Since $\chi_A$ splits, the [[decomposition into generalized eigenspaces|0Z3GDY89T5]] gives $F^n = V_1 \oplus \dots \oplus V_p$, where $V_i$ is the [[generalized eigenspace|0AJ035ZTZE]] of $\lambda_i$. Each $V_i$ is $T$-invariant, $\dim V_i = m_i$, and $N_i = (T - \lambda_i \operatorname{id})|_{V_i}$ is nilpotent.
2. By the [[normal form of nilpotent endomorphisms|Z2RTKWZZAZ]], each $V_i$ has a basis $\mathcal{B}_i$ in which the matrix of $N_i$ is $J_{k_{i1}}(0) \oplus \dots \oplus J_{k_{i s_i}}(0)$.
3. The [[restriction|0KN7EPH7Z0]] $T|_{V_i} = \lambda_i \operatorname{id} + N_i$ has the matrix $\lambda_i I + \bigoplus_j J_{k_{ij}}(0) = \bigoplus_j J_{k_{ij}}(\lambda_i)$ in $\mathcal{B}_i$.
4. The union $\mathcal{B} = \mathcal{B}_1 \cup \dots \cup \mathcal{B}_p$ is a basis of $F^n$, since the sum in step 1 is direct. Each $V_i$ is $T$-invariant, so the matrix $J$ of $T$ in $\mathcal{B}$ is block diagonal with the blocks of step 3.
5. Let $P$ be the [[change of basis matrix|0MKRHZB3WS]] whose columns are the vectors of $\mathcal{B}$. By the [[change of basis formula|0MQXVZEBMT]], $J = P^{-1} A P$. This proves existence.
6. For uniqueness, let $J' = \bigoplus_b J_{k_b}(\mu_b)$ be any Jordan matrix similar to $A$, and fix $\lambda \in F$. The rank of a block diagonal matrix is the sum of the ranks of its blocks, so $\operatorname{rank}(J' - \lambda I)^j = \sum_b \operatorname{rank}(J_{k_b}(\mu_b) - \lambda I)^j$.
7. If $\mu_b \ne \lambda$, then $J_{k_b}(\mu_b) - \lambda I$ is triangular with every diagonal entry equal to $\mu_b - \lambda \ne 0$. Its [[determinant|0C3CFHDN6R]] is nonzero, so it is invertible and all its powers have rank $k_b$.
8. If $\mu_b = \lambda$, then $(J_{k_b}(\lambda) - \lambda I)^j = J_{k_b}(0)^j$ has rank $\max(k_b - j, 0)$, by part 1 of the [[lemma on powers of a Jordan block|B9CHNGJV5K]].
9. So, with a constant $c$ that does not depend on $j$,
$$r_j = \operatorname{rank}(J' - \lambda I)^j = c + \sum_{b \colon \mu_b = \lambda} \max(k_b - j, 0).$$
10. For integers $k, j \ge 1$, let $g(k) = \max(k - j + 1, 0) - 2 \max(k - j, 0) + \max(k - j - 1, 0)$. Then $g(k) = 0$ for $k < j$, $g(j) = 1$, $g(j + 1) = 2 - 2 + 0 = 0$, and $g(k) = (k - j + 1) - 2(k - j) + (k - j - 1) = 0$ for $k \ge j + 2$.
11. By steps 9 and 10, $r_{j-1} - 2 r_j + r_{j+1} = \sum_{b \colon \mu_b = \lambda} g(k_b)$, since the constant $c$ cancels. This is the number of blocks $J_j(\lambda)$ in $J'$.
12. [[Similar matrices|191HBJ7PVZ]] have the same rank, and $(P^{-1} A P - \lambda I)^j = P^{-1} (A - \lambda I)^j P$. So $r_j = \operatorname{rank}(A - \lambda I)^j$ depends only on $A$.
13. By steps 11 and 12, the number of blocks of each size and each eigenvalue in $J'$ is fixed by $A$. So any two Jordan matrices similar to $A$ differ only in the order of the blocks, and the count is the formula of part 2.
14. Over an [[algebraically closed field|02SJG1HC32]], every nonconstant polynomial has a root $\lambda$, and then $x - \lambda$ divides it. By induction on the degree every polynomial splits, and in particular $\chi_A$ does. This proves part 3.
15. Finally, two matrices with split characteristic polynomials and the same Jordan form $J$ are both similar to $J$, hence to each other. Conversely, similar matrices have the same ranks $r_j$ for every $\lambda$, hence the same Jordan form by step 13.

## Idea

Cut the space into generalized eigenspaces, one for each eigenvalue.
On each piece, $A - \lambda I$ is nilpotent, and the chain basis of a nilpotent map turns it into Jordan blocks with eigenvalue $0$, so $A$ itself becomes blocks with eigenvalue $\lambda$.
For uniqueness, the ranks of the powers of $A - \lambda I$ do not depend on the basis, and the second difference of these ranks counts the blocks of each size.

## Variants

The module proof applies the [[structure theorem for finitely generated modules over a principal ideal domain|TXMV0YDACG]] to $F^n$ as an $F[x]$-module, in its elementary divisor form $F^n \cong \bigoplus F[x]/((x - \lambda)^k)$.
Each summand has the basis $(x - \lambda)^{k-1}, \dots, x - \lambda, 1$, in which $x$ acts as $J_k(\lambda)$, and uniqueness comes from the uniqueness of the elementary divisors.
A third route starts from the [[rational canonical form|042JWAR3Q0]] in its primary version and replaces each companion matrix of $(x - \lambda)^k$ by the Jordan block to which it is similar.
