---
tag: ~c6caae36
kind: proof
name: Proof of the theorem on the eigenvalues of a polynomial in an endomorphism
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: ~ceb4bf0e
methods: [0NTF6DMVAP, MKHVRNW68H, 0WCP0PVET6]
uses: [0BNEXSKNRV, 0ZND7NQ970, 08CJB2NQ92, 02SJG1HC32, 0K3MWA7DMC]
sources:
  - book: isbn:9783031410253
    locator: Chapter 5
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Additional properties
---

## Proof

Part 1.

1. Let $Tv = \lambda v$ with $v \ne 0$. By induction on $k$, $T^k v = T(T^{k-1}v) = T(\lambda^{k-1}v) = \lambda^k v$, with $T^0 v = v$.
2. Write $p = c_0 + c_1 x + \cdots + c_d x^d$. By the definition of the [[value of a polynomial at an endomorphism|0BNEXSKNRV]], $p(T)v = \sum_k c_k T^k v = \sum_k c_k \lambda^k v = p(\lambda)v$.
3. Since $v \ne 0$, $p(\lambda)$ is an [[eigenvalue|0ZND7NQ970]] of $p(T)$. This proves $p(\sigma(T)) \subseteq \sigma(p(T))$.

Part 2.
Let $F$ be algebraically closed and $V$ finite-dimensional.
By part 1 it remains to prove $\sigma(p(T)) \subseteq p(\sigma(T))$.

4. Case $V = 0$. There is no nonzero vector, so $\sigma(p(T)) = \emptyset$, and the inclusion holds.
5. Case $V \ne 0$ and $p = c$ constant. Then $p(T) = cI$, so $\sigma(p(T)) = \{c\}$. By the [[existence of an eigenvalue over an algebraically closed field|08CJB2NQ92]], $T$ has an eigenvalue $\lambda$, and $p(\lambda) = c$. So $\{c\} \subseteq p(\sigma(T))$.
6. Case $\deg p = d \ge 1$. Let $\mu \in \sigma(p(T))$. The polynomial $p - \mu$ also has degree $d \ge 1$.
7. Since $F$ is [[algebraically closed|02SJG1HC32]], repeated use of the [[factor theorem|0K3MWA7DMC]] gives $p(x) - \mu = c(x - r_1) \cdots (x - r_d)$ with $c \ne 0$ and $r_j \in F$.
8. Evaluation at $T$ preserves sums and products, by the remarks on the [[value of a polynomial at an endomorphism|0BNEXSKNRV]]. So $p(T) - \mu I = c(T - r_1 I) \cdots (T - r_d I)$.
9. Since $\mu$ is an eigenvalue of $p(T)$, the map $p(T) - \mu I$ is not injective.
10. A composite of injective maps is injective, and $c \ne 0$. So some factor $T - r_j I$ is not injective.
11. So there is $w \ne 0$ with $Tw = r_j w$, and $r_j \in \sigma(T)$.
12. Since $r_j$ is a root of $p - \mu$, $p(r_j) = \mu$. So $\mu \in p(\sigma(T))$.

Part 3.
Let $T$ be invertible.

13. If $Tv = 0$, then $v = T^{-1}Tv = 0$. So $0$ is not an eigenvalue of $T$, and in the same way $0$ is not an eigenvalue of $T^{-1}$.
14. Let $Tv = \lambda v$ with $v \ne 0$, so $\lambda \ne 0$ by step 13. Apply $T^{-1}$: $v = \lambda T^{-1}v$, so $T^{-1}v = \lambda^{-1}v$.
15. Conversely, let $T^{-1}v = \nu v$ with $v \ne 0$. Then $\nu \ne 0$, and applying $T$ gives $v = \nu Tv$, so $Tv = \nu^{-1} v$.
16. Steps 14 and 15 show that $v$ is an eigenvector of $T$ for $\lambda$ if and only if it is an eigenvector of $T^{-1}$ for $1/\lambda$.

## Idea

An eigenvector of $T$ is an eigenvector of every power of $T$, so it is an eigenvector of $p(T)$.
For the reverse inclusion, factor $p(x) - \mu$ into linear factors.
If $p(T) - \mu I$ kills a vector, then one linear factor $T - rI$ kills a nonzero vector, and then $p(r) = \mu$.

## Variants

- With [[triangularisation|0363JMQ42Y]]: if $A = SUS^{-1}$ with $U$ upper triangular, then $p(A) = S\,p(U)\,S^{-1}$, and $p(U)$ is upper triangular with diagonal entries $p(u_{ii})$. This also gives the algebraic multiplicities.
- For part 3, $T^{-1}$ is a polynomial in $T$ in finite dimension, by the [[Cayley-Hamilton theorem|0F765KFC2J]]. But the direct argument above is shorter and needs no finite dimension.
