---
tag: 2KKPFMRRWR
kind: proof
name: Proof of the characterizations of nilpotent endomorphisms
msc: ["15A04", "15A18"]
topics: [Z6S6PWMJPH]
audience: ug2
proves: FSKECQK1GW
methods: [0NTF6DMVAP, TFQ1845T84]
uses: [0K1KKMFHYH, 0TYMASG33Y, 0QEM68Y0DE, 053QVHF6N7]
sources:
  - book: isbn:9783031410253
    locator: Chapter 8
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Characterization
---

## Proof

We prove the cycle $1 \Rightarrow 2 \Rightarrow 3 \Rightarrow 4 \Rightarrow 1$, and then the claims on eigenvalues.
Write $K_j = \ker T^j$ for $j \ge 0$, so that $K_0 = 0$ and $K_j \subseteq K_{j+1}$ for each $j$.

*From 1 to 2.*

1. Assume condition 1, with $T^k = 0$.
   Then $K_k = V$.
2. Assume that $K_j = K_{j+1}$ for some $j$, and let $T^{j+2} v = 0$.
   Then $T v \in K_{j+1} = K_j$, so $T^{j+1} v = 0$.
   Hence $K_{j+2} = K_{j+1}$.
3. By step 2 and induction, once two consecutive terms of the chain are equal, all later terms are equal.
4. Let $m$ be the first index with $K_m = K_{m+1}$, which exists since all $K_j$ lie in $V$ of dimension $n$.
   The dimensions strictly increase from $K_0$ to $K_m$, so $m \le \dim K_m \le n$.
5. By steps 3 and 4, $K_n = K_{\max(k, n)}$, and this contains $K_k = V$ by step 1.
   So $T^n = 0$, which is condition 2.

*From 2 to 3.*

6. Assume condition 2.
   Then $0 = K_0 \subseteq K_1 \subseteq \cdots \subseteq K_n = V$.
7. Choose a basis of $K_1$, extend it to a basis of $K_2$, and continue up to a basis of $K_n = V$.
8. If $T^j v = 0$, then $T^{j-1}(T v) = 0$, so $T(K_j) \subseteq K_{j-1}$ for each $j \ge 1$.
9. Let $b$ be a basis vector added at level $j$, that is, $b \in K_j$ but $b$ was not in the basis of $K_{j-1}$.
   By step 8, $T b \in K_{j-1}$, and $K_{j-1}$ is spanned by the basis vectors that come before $b$.
10. So the column of $b$ has nonzero entries only above the diagonal.
    This holds for every basis vector, so the matrix of $T$ is strictly upper triangular, which is condition 3.

*From 3 to 4 and from 4 to 1.*

11. Assume condition 3, with a strictly upper triangular matrix $A$ of $T$.
    Then $t I - A$ is upper triangular with every diagonal entry equal to $t$.
12. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $\det(t I - A) = t^n$.
    By [[basis independence of the characteristic polynomial|0TYMASG33Y]], $p_T = t^n$, which is condition 4.
13. Assume condition 4.
    By the [[Cayley-Hamilton theorem|0QEM68Y0DE]], $T^n = p_T(T) = 0$, so $T$ is nilpotent, which is condition 1.

*The eigenvalues.*

14. Assume the conditions hold.
    By condition 4 and [[the roots of the characteristic polynomial|053QVHF6N7]], the eigenvalues of $T$ in $F$ are the roots of $t^n$ in $F$.
15. Since $n \ge 1$, the only root of $t^n$ is $0$.
    So $0$ is an eigenvalue of $T$, and it is the only one.
16. Now let $F$ be algebraically closed, and assume condition 5.
    Then $p_T$ splits as $(t - \mu_1) \cdots (t - \mu_n)$ with all $\mu_i \in F$.
17. Each $\mu_i$ is a root of $p_T$, so it is an eigenvalue of $T$ by step 14, and condition 5 gives $\mu_i = 0$.
    So $p_T = t^n$, which is condition 4.
18. Conversely, condition 4 gives condition 5 by step 15, so condition 5 is equivalent to the others.

## Idea

The kernels of the powers of $T$ grow by at least one dimension at each step until they stop, so they reach $V$ by step $n$.
A basis adapted to these kernels makes $T$ strictly upper triangular, because $T$ moves each kernel into the one before it.
The triangular determinant then gives $p_T = t^n$, and Cayley-Hamilton closes the cycle.

## Variants

Without Cayley-Hamilton, $4 \Rightarrow 1$ follows from [[triangularization|0363JMQ42Y]] over an algebraic closure of $F$.
There the diagonal entries are the roots of $p_T = t^n$, so the triangular matrix is strictly triangular, and it is nilpotent by the [[triangular power argument|AW5RBMW7RK]].
The powers of a matrix do not depend on the field we view it over, so $T$ is nilpotent over $F$ as well.

For $1 \Rightarrow 2$, one can also use the minimal polynomial.
It divides $t^k$, so it equals $t^j$ for some $j$, and it divides $p_T$, which has degree $n$, so $j \le n$ and $T^n = 0$.
