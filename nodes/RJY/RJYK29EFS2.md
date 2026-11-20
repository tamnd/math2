---
tag: RJYK29EFS2
kind: proof
name: Proof that the eigenvalues are the roots of the minimal polynomial
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: 0QF4ZEFG52
methods: [TFQ1845T84, 0NTF6DMVAP, 0J0XBKG64S]
uses: [0V58FPM3EQ, 0ZND7NQ970, 0BNEXSKNRV, 0K3MWA7DMC, 0DPF6WRZW6, 053QVHF6N7]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/minpolyandappns.pdf
    locator: Theorem 4.7
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Proof

We prove the two implications separately.

1. Let $m_T$ be the [[minimal polynomial|0V58FPM3EQ]] of $T$, and write $\id = \id_V$.
2. First let $\lambda$ be an [[eigenvalue|0ZND7NQ970]] of $T$. So there is $v \in V$ with $v \ne 0$ and $T(v) = \lambda v$.
3. By induction on $k$, $T^k(v) = \lambda^k v$ for all $k \ge 0$: the case $k = 0$ is $\id(v) = v$, and $T^{k+1}(v) = T(\lambda^k v) = \lambda^{k+1} v$.
4. Write $m_T(x) = \sum_{k=0}^{d} c_k x^k$. By the definition of the [[value at $T$|0BNEXSKNRV]] and step 3, $m_T(T)(v) = \sum_k c_k \lambda^k v = m_T(\lambda) v$.
5. Since $m_T(T) = 0$, step 4 gives $m_T(\lambda) v = 0$. As $v \ne 0$, we get $m_T(\lambda) = 0$.
6. Conversely, let $m_T(\lambda) = 0$. By the [[factor theorem|0K3MWA7DMC]], $m_T = (x - \lambda) q$ for some $q \in F[x]$.
7. The polynomial $q$ is monic, and its [[degree|0DPF6WRZW6]] is $\deg m_T - 1$. By the minimality of $\deg m_T$, $q(T) \ne 0$.
8. So there is $w \in V$ with $u = q(T)(w) \ne 0$.
9. Evaluation at $T$ respects products, so $(T - \lambda \id)(u) = \big((x - \lambda) q\big)(T)(w) = m_T(T)(w) = 0$.
10. Hence $T(u) = \lambda u$ with $u \ne 0$, and $\lambda$ is an eigenvalue of $T$.
11. Steps 5 and 10 show that $\lambda$ is an eigenvalue of $T$ if and only if $m_T(\lambda) = 0$. This proves part 1.
12. By the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]], $\lambda$ is an eigenvalue of $T$ if and only if $p_T(\lambda) = 0$.
13. By steps 11 and 12, $m_T(\lambda) = 0$ if and only if $p_T(\lambda) = 0$. This proves part 2.

No step uses the Cayley-Hamilton theorem.

## Idea

On an eigenvector, a polynomial in $T$ acts as the same polynomial evaluated at $\lambda$.
So $m_T(T) = 0$ forces $m_T(\lambda) = 0$.
Conversely, if $x - \lambda$ is a factor of $m_T$, the other factor $q$ does not kill $T$, by minimality.
Any nonzero vector in the image of $q(T)$ is then an eigenvector for $\lambda$.

## Variants

- With the Cayley-Hamilton theorem, one direction of part 2 is immediate: $m_T$ divides $p_T$, so every root of $m_T$ is a root of $p_T$. The proof above avoids this, so that the theorem can be used before the Cayley-Hamilton theorem.
- [[Axler's proof of the existence of an eigenvalue|6TPH8WGRJJ]] uses the same idea of a factor that is not injective.
