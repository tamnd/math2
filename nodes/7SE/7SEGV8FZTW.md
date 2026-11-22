---
tag: 7SEGV8FZTW
kind: proof
name: Proof of the diagonalizability test by multiplicities
msc: ["15A20", "15A18"]
topics: [Z6S6PWMJPH]
audience: ug1
proves: CDB8KCNNG9
methods: [0NTF6DMVAP, TFQ1845T84]
uses: [ENVF51H5S3, 056SW1E0AC, 0AYEPBQMAW, 0B5H4208Z9, 0S7A0EMPF4, 0K1KKMFHYH, 0TYMASG33Y, 053QVHF6N7]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Characterization
  - book: isbn:9780134860244
    locator: Section 5.2
---

## Proof

We prove the bound of part 1 with the block triangular form, and then both directions of part 2 with the characterization by eigenvectors.

*Part 1.*

1. Let $\lambda$ be an eigenvalue of $T$, let $E = \ker(T - \lambda \id_V)$, and let $g = \dim E$.
2. The space $E$ contains an [[eigenvector|0B5H4208Z9]], which is nonzero, so $g \ge 1$.
3. If $v \in E$, then $T(v) = \lambda v \in E$.
   So $E$ is $T$-invariant, and the restriction $T|_E$ is $\lambda \id_E$.
4. The matrix of $T|_E$ in any basis of $E$ is $\lambda I_g$, so $p_{T|_E} = (t - \lambda)^g$.
5. By the [[block triangular form|ENVF51H5S3]], $p_T = p_{T|_E} \cdot p_{\bar T} = (t - \lambda)^g \, p_{\bar T}$, where $\bar T$ is the map induced on $V / E$.
6. So $(t - \lambda)^g$ divides $p_T$, and $g \le m_\lambda$ by the definition of the [[algebraic multiplicity|0S7A0EMPF4]].
   This proves part 1.

*Part 2, the forward direction.*

7. Assume that $T$ is diagonalizable, and choose a basis $(v_1, \dots, v_n)$ with $T(v_j) = \mu_j v_j$.
8. The matrix of $T$ in this basis is $D = \operatorname{diag}(\mu_1, \dots, \mu_n)$.
9. The matrix $tI - D$ is diagonal, so the [[determinant of a triangular matrix|0K1KKMFHYH]] gives $p_D = \prod_j (t - \mu_j)$.
10. By [[similarity invariance|0TYMASG33Y]], $p_T = p_D$, so $p_T$ splits over $F$.
11. Fix an eigenvalue $\lambda_i$.
    By step 9, $m_i$ is the number of indices $j$ with $\mu_j = \lambda_i$.
12. These $m_i$ basis vectors lie in $E_{\lambda_i}$ and are independent, so $\dim E_{\lambda_i} \ge m_i$.
13. Part 1 gives $\dim E_{\lambda_i} \le m_i$, so $\dim E_{\lambda_i} = m_i$ for each $i$.

*Part 2, the backward direction.*

14. Assume that $p_T = \prod_{i=1}^k (t - \lambda_i)^{m_i}$ with distinct $\lambda_i \in F$, and that $\dim E_{\lambda_i} = m_i$ for each $i$.
15. The roots of $p_T$ in $F$ are the eigenvalues of $T$, because [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]].
    So $\lambda_1, \dots, \lambda_k$ are all the eigenvalues.
16. The polynomial $p_T$ has degree $n$, so comparing degrees in step 14 gives $m_1 + \cdots + m_k = n$.
17. So $\dim E_{\lambda_1} + \cdots + \dim E_{\lambda_k} = n$.
18. This is condition 4 of the [[characterization by eigenvectors|056SW1E0AC]], so $T$ is diagonalizable.
19. For a matrix $A$, apply steps 1 to 18 to the map $x \mapsto A x$, whose characteristic polynomial is $p_A$.

## Idea

An eigenspace is an invariant subspace on which $T$ acts as a scalar.
So it splits off a factor $(t - \lambda)^g$ of the characteristic polynomial, and $g$ cannot exceed the exponent of $t - \lambda$.
When the polynomial splits, the exponents add up to $n$.
Then equality for each eigenvalue says that the eigenspaces have total dimension $n$, which is the characterization by eigenvectors.

## Variants

Part 1 can also be proved without the quotient map.
Extend a basis of $E_\lambda$ to a basis of $V$, write the matrix of $T$ in this basis, and expand $\det(tI - [T])$ along the first $g$ columns, each of which has the single nonzero entry $t - \lambda$.

Part 2 also follows from the [[generalized eigenspaces|0AJ035ZTZE]].
If $p_T$ splits, then $V$ is the direct sum of the generalized eigenspaces, and the one for $\lambda_i$ has dimension $m_i$ by the [[dimension formula|PHZ684KGWS]].
It contains $E_{\lambda_i}$, so it equals $E_{\lambda_i}$ exactly when $\dim E_{\lambda_i} = m_i$.
The [[minimal polynomial criterion|0MPAJRB23T]] gives a third route.
