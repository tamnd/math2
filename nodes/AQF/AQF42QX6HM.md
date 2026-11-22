---
tag: AQF42QX6HM
kind: proof
name: Proof of the theorem on the eigenvalues of a polynomial in an endomorphism
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: F2S8WGVARA
methods: [0NTF6DMVAP, MKHVRNW68H, 0WCP0PVET6]
uses: [0BNEXSKNRV, 0ZND7NQ970, 08CJB2NQ92, 02SJG1HC32, 0K3MWA7DMC]
sources:
  - book: isbn:9783031410253
    locator: Chapter 5
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: Additional properties
---

## Proof

For part 1 we apply $p(T)$ to an eigenvector term by term; for part 2 we factor $p(x) - \mu$ into linear factors and find one factor with a kernel; for part 3 we apply $T^{-1}$ to the eigenvalue equation.

*Part 1.*

1. Let $Tv = \lambda v$ with $v \ne 0$.
   Then $T^0 v = v$, and if $T^{k-1} v = \lambda^{k-1} v$, then
$$T^k v = T(T^{k-1}v) = T(\lambda^{k-1}v) = \lambda^{k-1}\, Tv = \lambda^k v,$$
   so $T^k v = \lambda^k v$ for all $k \ge 0$ by induction.
2. Write $p = c_0 + c_1 x + \dots + c_d x^d$.
   By the definition of the [[value of a polynomial at an endomorphism|0BNEXSKNRV]] and step 1,
$$p(T)v = \sum_{k=0}^{d} c_k T^k v = \sum_{k=0}^{d} c_k \lambda^k v = p(\lambda)\, v.$$
3. Since $v \ne 0$, step 2 shows that $p(\lambda)$ is an [[eigenvalue|0ZND7NQ970]] of $p(T)$.
   This proves $p(\sigma(T)) \subseteq \sigma(p(T))$.

*Part 2.* Let $F$ be algebraically closed and $V$ finite-dimensional.
By part 1, it remains to prove $\sigma(p(T)) \subseteq p(\sigma(T))$.

4. If $V = 0$, there is no nonzero vector, so $\sigma(p(T)) = \emptyset$ and the inclusion holds.
5. If $V \ne 0$ and $p = c$ is constant, then $p(T) = cI$ and $\sigma(p(T)) = \{c\}$.
   By the [[existence of an eigenvalue over an algebraically closed field|08CJB2NQ92]], $T$ has an eigenvalue $\lambda$, and $p(\lambda) = c$, so $\{c\} \subseteq p(\sigma(T))$.
6. Now let $\deg p = d \ge 1$ and let $\mu \in \sigma(p(T))$.
   The polynomial $p - \mu$ also has degree $d \ge 1$.
7. Since $F$ is [[algebraically closed|02SJG1HC32]], repeated use of the [[factor theorem|0K3MWA7DMC]] gives
$$p(x) - \mu = c\,(x - r_1) \cdots (x - r_d)$$
   with $c \ne 0$ and $r_1, \dots, r_d \in F$.
8. Evaluation at $T$ keeps sums and products, by the remarks on the [[value of a polynomial at an endomorphism|0BNEXSKNRV]], so
$$p(T) - \mu I = c\,(T - r_1 I) \cdots (T - r_d I).$$
9. Since $\mu$ is an eigenvalue of $p(T)$, the map $p(T) - \mu I$ has a nonzero kernel, so it is not injective.
10. A composite of injective maps is injective, and multiplication by $c \ne 0$ is injective.
    So by step 8, some factor $T - r_j I$ is not injective.
11. So there is $w \ne 0$ with $Tw = r_j w$, and $r_j \in \sigma(T)$.
12. Since $r_j$ is a root of $p - \mu$, we have $p(r_j) = \mu$, so $\mu \in p(\sigma(T))$.

*Part 3.* Let $T$ be invertible.

13. If $Tv = 0$, then $v = T^{-1}(Tv) = 0$.
    So $0$ is not an eigenvalue of $T$, and in the same way, with $T$ in place of $T^{-1}$, $0$ is not an eigenvalue of $T^{-1}$.
14. Let $Tv = \lambda v$ with $v \ne 0$, so $\lambda \ne 0$ by step 13.
    Applying $T^{-1}$ gives $v = \lambda\, T^{-1}v$, so $T^{-1}v = \lambda^{-1}v$.
15. Conversely, let $T^{-1}v = \nu v$ with $v \ne 0$.
    Then $\nu \ne 0$ by step 13, and applying $T$ gives $v = \nu\, Tv$, so $Tv = \nu^{-1} v$.
16. Steps 14 and 15 show that $v$ is an eigenvector of $T$ for $\lambda$ exactly when it is an eigenvector of $T^{-1}$ for $1/\lambda$, which proves part 3.

## Idea

An eigenvector of $T$ is an eigenvector of every power of $T$, so it is an eigenvector of every polynomial in $T$, with the eigenvalue $p(\lambda)$.
The reverse inclusion is the real content.
If $p(T) - \mu I$ kills a nonzero vector, factor $p(x) - \mu$ into linear factors $x - r$.
Then $p(T) - \mu I$ is a product of maps $T - rI$, and a product with a nonzero kernel must have a factor with a nonzero kernel.
That factor gives an eigenvalue $r$ of $T$ with $p(r) = \mu$.

For example, let $T$ have the eigenvalues $1$ and $3$, and take $p(x) = x^2 - 4x$ and $\mu = -3$.
Then $p(x) + 3 = (x - 1)(x - 3)$, and the kernel of $p(T) + 3I$ comes from the factors $T - I$ and $T - 3I$, which both have a kernel.

## Variants

[[Triangularization|0363JMQ42Y]] gives a second proof of part 2 that also counts multiplicities.
If $A = SUS^{-1}$ with $U$ upper triangular, then $p(A) = S\,p(U)\,S^{-1}$, and $p(U)$ is upper triangular with the diagonal entries $p(u_{ii})$.
So the eigenvalues of $p(A)$, with multiplicity, are the numbers $p(u_{ii})$.

For part 3 in finite dimension, $T^{-1}$ is a polynomial in $T$ by the [[Cayley-Hamilton theorem|0F765KFC2J]], so part 1 already gives one direction.
The direct argument above is shorter and works in every dimension.
