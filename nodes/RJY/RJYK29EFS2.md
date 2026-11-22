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

We prove the two directions of part 1 separately, using only the definition of $m_T$ and the factor theorem, and then we deduce part 2 from the characteristic polynomial.
Let $m_T$ be the [[minimal polynomial|0V58FPM3EQ]] of $T$, and write $\mathrm{id}$ for the identity map of $V$.

*Every eigenvalue is a root of $m_T$.*

1. Let $\lambda$ be an [[eigenvalue|0ZND7NQ970]] of $T$.
   So there is a vector $v \ne 0$ with $T(v) = \lambda v$.
2. We show $T^k(v) = \lambda^k v$ for all $k \ge 0$ by induction on $k$.
   For $k = 0$ both sides are $v$, and if it holds for $k$, then $T^{k+1}(v) = T(\lambda^k v) = \lambda^k T(v) = \lambda^{k+1} v$, by linearity of $T$.
3. Write $m_T(x) = c_0 + c_1 x + \dots + c_d x^d$.
   By the definition of the [[value at T|0BNEXSKNRV]] and step 2,
$$m_T(T)(v) = \sum_{k=0}^{d} c_k T^k(v) = \sum_{k=0}^{d} c_k \lambda^k v = m_T(\lambda)\, v.$$
4. The left side is $0$, because $m_T(T) = 0$.
   So $m_T(\lambda)\, v = 0$, and since $v \ne 0$, the scalar $m_T(\lambda)$ is $0$.

*Every root of $m_T$ is an eigenvalue.*

5. Let $\lambda \in F$ with $m_T(\lambda) = 0$.
   By the [[factor theorem|0K3MWA7DMC]], $m_T = (x - \lambda)\, q$ for some $q \in F[x]$.
6. The polynomial $q$ is monic, because $m_T$ and $x - \lambda$ are monic, and its [[degree|0DPF6WRZW6]] is $\deg m_T - 1$.
   Since no monic polynomial of degree less than $\deg m_T$ annihilates $T$, we have $q(T) \ne 0$.
7. So there is a vector $w \in V$ with $u = q(T)(w) \ne 0$.
8. Evaluation at $T$ respects products, so
$$(T - \lambda\, \mathrm{id})(u) = (T - \lambda\, \mathrm{id})\big(q(T)(w)\big) = \big((x - \lambda)\, q\big)(T)(w) = m_T(T)(w) = 0.$$
9. So $T(u) = \lambda u$ with $u \ne 0$, and $\lambda$ is an eigenvalue of $T$.

*Conclusion.*

10. Steps 4 and 9 show that $\lambda$ is an eigenvalue of $T$ if and only if $m_T(\lambda) = 0$, which is part 1.
11. By the theorem that the [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]], $\lambda$ is an eigenvalue of $T$ if and only if $p_T(\lambda) = 0$.
12. Steps 10 and 11 together give $m_T(\lambda) = 0$ if and only if $p_T(\lambda) = 0$, which is part 2.

No step uses the Cayley-Hamilton theorem.

## Idea

On an eigenvector, the map $T$ acts as the number $\lambda$, so every polynomial in $T$ acts as the same polynomial evaluated at $\lambda$.
Since $m_T(T)$ is the zero map, $m_T(\lambda)$ must be $0$.
For the other direction, split off the factor $x - \lambda$ and look at the other factor $q$.
Its degree is too small for it to kill $T$, so it sends some vector to $u \ne 0$, and then $T - \lambda\, \mathrm{id}$ kills $u$, which makes $u$ an eigenvector.

## Variants

With the Cayley-Hamilton theorem, one half of part 2 is immediate: $m_T$ divides $p_T$, so every root of $m_T$ is a root of $p_T$.
The proof above avoids this, so that the result can be used before the Cayley-Hamilton theorem and in a course that, like Axler's, puts determinants late.
[[Axler's proof of the existence of an eigenvalue|6TPH8WGRJJ]] uses the same idea: a product of linear factors kills a nonzero vector, so one of the factors is not injective.
