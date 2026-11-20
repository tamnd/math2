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

Let $T \colon F^n \to F^n$ be $T(v) = Av$, and let $\chi_A = \prod_{i=1}^p (x - \lambda_i)^{m_i}$ with distinct $\lambda_i \in F$.

1. Since $\chi_A$ splits, the [[decomposition into generalised eigenspaces|0Z3GDY89T5]] gives $F^n = V_1 \oplus \cdots \oplus V_p$, where $V_i$ is the [[generalised eigenspace|0AJ035ZTZE]] of $\lambda_i$. Each $V_i$ is $T$-invariant, $\dim V_i = m_i$, and $N_i = (T - \lambda_i)|_{V_i}$ is nilpotent.
2. By the [[normal form of nilpotent endomorphisms|Z2RTKWZZAZ]], $V_i$ has a basis $\mathcal{B}_i$ in which the matrix of $N_i$ is $J_{k_{i1}}(0) \oplus \cdots \oplus J_{k_{i s_i}}(0)$.
3. The [[restriction|0KN7EPH7Z0]] $T|_{V_i} = \lambda_i \operatorname{id} + N_i$ therefore has matrix $\lambda_i I + \bigoplus_j J_{k_{ij}}(0) = \bigoplus_j J_{k_{ij}}(\lambda_i)$ in $\mathcal{B}_i$.
4. The union $\mathcal{B} = \mathcal{B}_1 \cup \cdots \cup \mathcal{B}_p$ is a basis of $F^n$, since the sum in step 1 is direct. Each $V_i$ is $T$-invariant, so the matrix of $T$ in $\mathcal{B}$ is block diagonal with the blocks of step 3. Call it $J$.
5. Let $P$ be the [[change of basis matrix|0MKRHZB3WS]] with the vectors of $\mathcal{B}$ as columns. By the [[change of basis formula|0MQXVZEBMT]], $J = P^{-1} A P$. This proves part 1.
6. Uniqueness. Let $J' = \bigoplus_{b} J_{k_b}(\mu_b)$ be any Jordan matrix similar to $A$, and fix $\lambda \in F$. The rank of a block diagonal matrix is the sum of the ranks of its blocks, so $\operatorname{rank}(J' - \lambda I)^j = \sum_b \operatorname{rank}(J_{k_b}(\mu_b) - \lambda I)^j$.
7. If $\mu_b \ne \lambda$, then $J_{k_b}(\mu_b) - \lambda I$ is triangular with nonzero diagonal $\mu_b - \lambda$. Its [[determinant|0C3CFHDN6R]] is nonzero, so all its powers have rank $k_b$.
8. If $\mu_b = \lambda$, then $(J_{k_b}(\lambda) - \lambda I)^j = J_{k_b}(0)^j$ has rank $\max(k_b - j, 0)$, by part 1 of the lemma on Jordan blocks.
9. So $r_j = \operatorname{rank}(J' - \lambda I)^j = c + \sum_{b : \mu_b = \lambda} \max(k_b - j, 0)$, where $c$ does not depend on $j$.
10. For an integer $k \ge 1$, the number $\max(k - j + 1, 0) - 2 \max(k - j, 0) + \max(k - j - 1, 0)$ is $0$ if $k < j$, $1$ if $k = j$, $2 - 2 + 0 = 0$ if $k = j + 1$, and $(k - j + 1) - 2(k - j) + (k - j - 1) = 0$ if $k \ge j + 2$.
11. By steps 9 and 10, $r_{j-1} - 2 r_j + r_{j+1}$ is the number of blocks $J_j(\lambda)$ in $J'$; the constant $c$ cancels.
12. [[Similar matrices|191HBJ7PVZ]] have the same rank, and $(P^{-1} A P - \lambda I)^j = P^{-1} (A - \lambda I)^j P$. So $r_j = \operatorname{rank}(A - \lambda I)^j$ depends only on $A$.
13. By steps 11 and 12, the number of blocks of each size and each eigenvalue in $J'$ is fixed by $A$. So any two Jordan matrices similar to $A$ differ only in the order of the blocks. This proves part 2 and the formula there.
14. Part 3. Over an [[algebraically closed field|02SJG1HC32]], every nonconstant polynomial has a root $\lambda$, and $x - \lambda$ divides it. By induction on the degree, every polynomial splits, and in particular $\chi_A$ does.
15. Two matrices with split characteristic polynomials that have the same Jordan form $J$ are both similar to $J$, hence to each other. Conversely, similar matrices have the same ranks $r_j$ for every $\lambda$, hence the same Jordan form by step 13.

## Idea

Split the space into generalized eigenspaces, one for each eigenvalue.
On each piece, $A - \lambda I$ is nilpotent, and the chain basis for nilpotent maps gives the Jordan blocks.
The ranks of the powers of $A - \lambda I$ count the blocks, so the form is unique.

## Variants

The module proof applies the [[structure theorem for finitely generated modules over a principal ideal domain|TXMV0YDACG]] to $F^n$ as an $F[x]$-module, in its elementary divisor form $F^n \cong \bigoplus F[x]/((x - \lambda)^k)$.
Each summand has the basis $(x - \lambda)^{k-1}, \dots, x - \lambda, 1$, in which $x$ acts as $J_k(\lambda)$.
A third route goes through the [[rational canonical form|042JWAR3Q0]] in its primary version, splitting each companion matrix of $(x - \lambda)^k$ into a Jordan block.
