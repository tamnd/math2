---
tag: 6TPH8WGRJJ
kind: proof
name: Proof without determinants of the existence of an eigenvalue
aliases: [axlers-proof-of-the-existence-of-an-eigenvalue]
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: 08CJB2NQ92
methods: [01XM7JEKHY, 0J0XBKG64S]
uses: [08ZDRN6H41, 0BNEXSKNRV, 02SJG1HC32, 0K3MWA7DMC, 0ZND7NQ970]
sources:
  - book: isbn:9783031410253
    locator: Chapter 5
  - url: https://linear.axler.net/
    locator: Chapter 5
---

## Proof

We find a nonzero polynomial that kills one vector, split it into linear factors, and show that one factor has a nonzero kernel.
Let $n = \dim V$; since $V \ne 0$, we have $n \ge 1$.

*A polynomial that kills one vector.*

1. Choose $v \in V$ with $v \ne 0$, which is possible because $V \ne 0$.
2. The list $v, Tv, T^2 v, \dots, T^n v$ has $n + 1$ vectors.
   By the [[Steinitz exchange lemma|08ZDRN6H41]], an independent list in $V$ has at most $n$ vectors, so this list is dependent.
3. So there are scalars $a_0, a_1, \dots, a_n \in F$, not all zero, with
$$a_0 v + a_1 Tv + \dots + a_n T^n v = 0.$$
4. Let $p(x) = a_0 + a_1 x + \dots + a_n x^n$.
   Then $p \ne 0$, and $p(T)v = 0$ by the definition of the [[value of a polynomial at an endomorphism|0BNEXSKNRV]].
5. The polynomial $p$ is not constant.
   Otherwise $a_1 = \dots = a_n = 0$, so $a_0 \ne 0$ by step 3, and $a_0 v = 0$ gives $v = 0$, against step 1.
6. Let $m = \deg p$, so $m \ge 1$ by step 5.

*Splitting into linear factors.*

7. We claim that $p = c(x - r_1)(x - r_2) \cdots (x - r_m)$ for some $c \ne 0$ and some $r_1, \dots, r_m \in F$.
   We prove this for every nonzero polynomial, by induction on the degree $m$.
8. If $m = 0$, then $p = c$ is a nonzero constant, and the claim holds with the empty product.
9. If $m \ge 1$, then $p$ has a root $r_m \in F$, because $F$ is [[algebraically closed|02SJG1HC32]].
10. By the [[factor theorem|0K3MWA7DMC]], $p = (x - r_m) q$ for a polynomial $q$ of degree $m - 1$.
    The induction hypothesis for $q$ then gives the claim for $p$.

*One factor is not injective.*

11. Evaluation at $T$ keeps sums and products, by the remarks on the [[value of a polynomial at an endomorphism|0BNEXSKNRV]].
    So step 7 gives
$$p(T) = c\,(T - r_1 I)(T - r_2 I) \cdots (T - r_m I).$$
12. Suppose, for a contradiction, that every map $T - r_j I$ is injective.
13. A composite of injective maps is injective, and multiplication by $c \ne 0$ is injective.
    So $p(T)$ is injective, by step 11.
14. But $p(T)v = 0 = p(T)0$ with $v \ne 0$, by steps 1 and 4, so $p(T)$ is not injective.
    This contradicts step 13.
15. So some $T - r_j I$ is not injective, and there is $w \ne 0$ with $(T - r_j I) w = 0$, that is, $Tw = r_j w$.
16. By the definition of an [[eigenvalue|0ZND7NQ970]], $r_j$ is an eigenvalue of $T$, with the eigenvector $w$.

## Idea

Apply $T$ again and again to one nonzero vector.
In a space of dimension $n$, the vectors $v, Tv, \dots, T^n v$ cannot all be independent, and the dependence is a polynomial $p$ with $p(T)v = 0$.
Over an algebraically closed field, $p$ is a product of linear factors, so $p(T)$ is a product of the maps $T - r_j I$.
A product that kills a nonzero vector must have a factor that kills a nonzero vector, and that factor gives the eigenvalue.
Nothing in the argument uses a determinant.

For a small case, take the rotation $T(x, y) = (-y, x)$ of $\mathbb{C}^2$ and $v = (1, 0)$.
Then $Tv = (0, 1)$ and $T^2 v = (-1, 0) = -v$, so $p(x) = x^2 + 1 = (x - i)(x + i)$ kills $v$.
The vector $w = (T + iI)v = (i, 1)$ is not zero, and $(T - iI)w = p(T)v = 0$, so $i$ is an eigenvalue with the eigenvector $(i, 1)$.

## Variants

The [[proof by the characteristic polynomial|JZQEV913ZV]] finds a root of $\det(tI - A)$, and it is shorter once determinants are known.
The same argument with the [[minimal polynomial|03NDVCSHSB]] in place of $p$ shows that every root of the minimal polynomial is an eigenvalue, which is one half of the theorem that the [[eigenvalues are the roots of the minimal polynomial|0QF4ZEFG52]].
Over $\mathbb{R}$, the polynomial $p$ splits into factors of degree $1$ and $2$, and the same argument gives an [[invariant subspace of dimension 1 or 2|KAV44BRV77]].
