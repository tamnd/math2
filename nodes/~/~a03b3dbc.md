---
tag: ~a03b3dbc
kind: proof
name: Proof of the diagonalizability test by multiplicities
msc: ["15A20", "15A18"]
topics: [Z6S6PWMJPH]
audience: ug1
proves: ~1ac265ba
methods: [0NTF6DMVAP, TFQ1845T84]
uses: [~955c2a39, 056SW1E0AC, 0AYEPBQMAW, 0B5H4208Z9, 0S7A0EMPF4, 0K1KKMFHYH, 0TYMASG33Y, 053QVHF6N7]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Characterization
  - book: isbn:9780134860244
    locator: Section 5.2
---

## Proof

We prove the bound of part 1 with the block triangular form, and then both directions of part 2.

1. Let $\lambda$ be an eigenvalue of $T$, and let $E = \ker(T - \lambda \id_V)$ with $g = \dim E$.
2. $E$ contains an [[eigenvector|0B5H4208Z9]], which is nonzero. So $g \ge 1$.
3. If $v \in E$, then $T(v) = \lambda v \in E$. So $E$ is $T$-invariant, and $T|_E = \lambda \id_E$.
4. The matrix of $T|_E$ in any basis of $E$ is $\lambda I_g$. So $p_{T|_E} = (t - \lambda)^g$.
5. By the [[block triangular form|~955c2a39]], $p_T = p_{T|_E} \cdot p_{\bar T} = (t - \lambda)^g \, p_{\bar T}$.
6. So $(t - \lambda)^g$ divides $p_T$. By the definition of the [[algebraic multiplicity|0S7A0EMPF4]], $g \le m_\lambda$. This proves part 1.
7. For part 2, assume that $T$ is diagonalizable. Choose a basis $(v_1, \dots, v_n)$ with $T(v_j) = \mu_j v_j$.
8. The matrix of $T$ in this basis is $D = \operatorname{diag}(\mu_1, \dots, \mu_n)$.
9. $tI - D$ is diagonal. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $p_D = \prod_j (t - \mu_j)$.
10. By [[similarity invariance|0TYMASG33Y]], $p_T = p_D$. So $p_T$ splits over $F$.
11. Fix an eigenvalue $\lambda_i$. By step 9, $m_i$ is the number of indices $j$ with $\mu_j = \lambda_i$.
12. These $m_i$ basis vectors lie in $E_{\lambda_i}$ and are independent. So $\dim E_{\lambda_i} \ge m_i$.
13. Part 1 gives $\dim E_{\lambda_i} \le m_i$. So $\dim E_{\lambda_i} = m_i$ for each $i$.
14. Conversely, assume that $p_T = \prod_{i=1}^k (t - \lambda_i)^{m_i}$ with distinct $\lambda_i \in F$, and $\dim E_{\lambda_i} = m_i$.
15. The roots of $p_T$ in $F$ are the eigenvalues of $T$, by [[eigenvalues are roots|053QVHF6N7]]. So the $\lambda_i$ are all the eigenvalues.
16. The polynomial $p_T$ has degree $n$. Comparing degrees in step 14 gives $m_1 + \cdots + m_k = n$.
17. So $\dim E_{\lambda_1} + \cdots + \dim E_{\lambda_k} = n$.
18. This is condition 4 of the [[characterization by eigenvectors|056SW1E0AC]]. So $T$ is diagonalizable.
19. For a matrix $A$, apply steps 1 to 18 to $x \mapsto A x$, whose characteristic polynomial is $p_A$.

## Idea

An eigenspace is an invariant subspace on which $T$ is a scalar.
So it contributes a factor $(t - \lambda)^g$ to the characteristic polynomial, and $g$ cannot exceed the exponent.
If the polynomial splits, the exponents add up to $n$.
Then equality for each eigenvalue means that the eigenspaces fill $V$.

## Variants

Part 1 can also be proved by extending a basis of $E_\lambda$ to a basis of $V$ and expanding the determinant directly, without the quotient operator.
Another proof of part 2 uses the [[minimal polynomial criterion|0MPAJRB23T]].
If $p_T$ splits and $\dim E_{\lambda_i} = m_i$, then $V$ is the sum of the [[generalized eigenspaces|0AJ035ZTZE]], and each of them equals the eigenspace by the [[dimension formula|~b8d53cf6]].
