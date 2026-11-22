---
tag: NKHRMEB65A
kind: proof
name: Proof of the Jordan-Chevalley decomposition in the split case
msc: ["15A21", "15A20"]
topics: [Z6S6PWMJPH]
audience: grad
proves: 011K11VPJN
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0Z3GDY89T5, 0FK17N4DKA, DS9TS6AFMW, FSKECQK1GW, 0Q9PGXD9E4]
sources:
  - book: isbn:9780135367971
    locator: Section 6.8
  - url: https://en.wikipedia.org/wiki/Jordan%E2%80%93Chevalley_decomposition
    locator: Decomposition of a linear operator
---

## Proof

We build $S$ from the projections onto the generalized eigenspaces, which are polynomials in $T$, and then prove uniqueness with simultaneous diagonalization.

*Existence.*

1. Since $p_T$ splits, we can write $p_T = (t - \lambda_1)^{m_1} \cdots (t - \lambda_k)^{m_k}$ with distinct $\lambda_1, \dots, \lambda_k \in F$.
2. By the [[decomposition into generalized eigenspaces|0Z3GDY89T5]], $V = V_1 \oplus \cdots \oplus V_k$ with $V_i = \ker (T - \lambda_i)^{m_i}$, and the projections $\pi_i$ of $V$ onto $V_i$ along the other summands are polynomials in $T$.
3. Define
$$S = \lambda_1 \pi_1 + \cdots + \lambda_k \pi_k, \qquad N = T - S.$$
4. The map $S$ acts on $V_i$ as multiplication by $\lambda_i$, because $\pi_i$ is the identity on $V_i$ and $\pi_j$ is $0$ on $V_i$ for $j \ne i$.
   A basis of $V$ made of bases of the $V_i$ is therefore a basis of eigenvectors of $S$, so $S$ is diagonalizable.
5. On $V_i$ the map $N$ equals $T - \lambda_i$, by step 4, and $(T - \lambda_i)^{m_i}$ is $0$ on $V_i$ by the definition of $V_i$.
   Each $V_i$ is $T$-invariant, so $N^m$ is $0$ on every $V_i$ for $m = \max_i m_i$, hence $N^m = 0$ and $N$ is nilpotent.
6. The map $S$ is a polynomial in $T$ by steps 2 and 3, and then $N = T - S$ is one too.
   Two polynomials in $T$ commute, so $S N = N S$.

*Uniqueness.*

7. Let $T = S' + N'$ be a second decomposition, with $S'$ diagonalizable, $N'$ nilpotent and $S' N' = N' S'$.
8. The map $S'$ commutes with itself and with $N'$, so it commutes with $T = S' + N'$; in the same way $N'$ commutes with $T$.
9. By step 6, $S$ and $N$ are polynomials in $T$, so $S'$ and $N'$ commute with $S$ and with $N$.
10. The maps $S$ and $S'$ are diagonalizable and commute, so by [[simultaneous diagonalization|0FK17N4DKA]] there is one basis in which both are [[diagonal|0Q9PGXD9E4]].
    In that basis $S - S'$ is diagonal, so $S - S'$ is diagonalizable.
11. By the [[characterizations of nilpotent maps|FSKECQK1GW]], $N^n = 0$ and $N'^n = 0$ with $n = \dim V$.
12. The maps $N$ and $N'$ commute, so the [[binomial theorem for commuting matrices|DS9TS6AFMW]] writes $(N' - N)^{2n}$ as a sum of multiples of $N'^a N^b$ with $a + b = 2n$.
    In each term $a \ge n$ or $b \ge n$, so each term is $0$, and $N' - N$ is nilpotent.
13. From $S + N = T = S' + N'$ we get $D := S - S' = N' - N$, so $D$ is diagonalizable by step 10 and nilpotent by step 12.
14. Write $D = Q \operatorname{diag}(\mu_1, \dots, \mu_n) Q^{-1}$.
    Then $0 = D^{2n} = Q \operatorname{diag}(\mu_1^{2n}, \dots, \mu_n^{2n}) Q^{-1}$, so each $\mu_j^{2n} = 0$, and each $\mu_j = 0$ because $F$ is a field.
15. So $D = 0$, which gives $S' = S$ and $N' = N$.

This proves existence, uniqueness, and that $S$ and $N$ are polynomials in $T$.

## Idea

On each generalized eigenspace, $T$ is "the eigenvalue plus something nilpotent".
So we let $S$ be the eigenvalue on each piece and let $N$ be the rest.
The projections onto the pieces are polynomials in $T$, so $S$ and $N$ are too, and that is what makes them commute.
For uniqueness, any other pair commutes with $T$ and hence with $S$ and $N$.
Then $S - S'$ is at the same time diagonalizable and nilpotent, and the only such map is $0$.

## Variants

One can construct $S = g(T)$ directly: by the Chinese remainder theorem there is a polynomial $g$ with $g \equiv \lambda_i \bmod (t - \lambda_i)^{m_i}$ for each $i$, and then $g(T)$ acts as $\lambda_i$ on $V_i$.
The [[3 × 3 worked example|4P9QZRCJND]] finds the projections of step 2 with Bézout's identity, and the resulting $S$ is such a polynomial $g(A)$.

Over a perfect field, the same uniqueness argument works with "semisimple" in place of "diagonalizable", because there a sum of two commuting semisimple maps is semisimple.
Existence over a perfect field follows by passing to an algebraic closure and showing that $S$ is fixed by the field automorphisms, or by a Newton iteration on the squarefree part of $m_T$.
