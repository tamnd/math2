---
tag: HWSPS1M53G
kind: proof
name: Proof of quadratic reciprocity for the Jacobi symbol
msc: [11A15]
proves: 0YY06KP3ZQ
uses: [0XDB5AW7M1, 01J8AMV9RS, 085MJS6907, 0NW1JP7TBR, 084HH1NDCB]
sources:
  - url: https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Elementary_Number_Theory_(Raji)/05%3A_Primitive_Roots_and_Quadratic_Residues/5.07%3A_Jacobi_Symbol
---

## Proof

1. Let $m$ and $n$ be coprime positive odd integers. For an odd integer $r$, put $\delta(r) = (r - 1)/2$, an integer.
2. Claim: for odd $r$ and $s$, $\delta(rs) \equiv \delta(r) + \delta(s) \pmod 2$. Indeed $(rs - 1) - (r - 1) - (s - 1) = (r-1)(s-1)$. Both factors are even, so this is divisible by $4$, and $\delta(rs) - \delta(r) - \delta(s)$ is even.
3. By induction on $t$, $\delta(r_1 \cdots r_t) \equiv \sum_{i=1}^{t} \delta(r_i) \pmod 2$ for odd $r_1, \dots, r_t$. For $t = 0$, both sides are $\delta(1) = 0$.
4. By the [[fundamental theorem of arithmetic|084HH1NDCB]], write $m = p_1 \cdots p_s$ and $n = q_1 \cdots q_t$ as products of primes, listed with repetition. All of them are odd, and $p_i \ne q_j$ for all $i, j$ because $\gcd(m, n) = 1$.
5. By the definition of the [[Jacobi symbol|0XDB5AW7M1]], $\left(\frac{m}{n}\right) = \prod_{j=1}^{t} \left(\frac{m}{q_j}\right)$, with [[Legendre symbols|01J8AMV9RS]] on the right.
6. By the [[multiplicativity of the Legendre symbol|0NW1JP7TBR]], $\left(\frac{m}{q_j}\right) = \prod_{i=1}^{s} \left(\frac{p_i}{q_j}\right)$. So $\left(\frac{m}{n}\right) = \prod_{i, j} \left(\frac{p_i}{q_j}\right)$.
7. In the same way, $\left(\frac{n}{m}\right) = \prod_{i, j} \left(\frac{q_j}{p_i}\right)$.
8. For each pair $(i, j)$, the [[law of quadratic reciprocity|085MJS6907]] gives $\left(\frac{p_i}{q_j}\right) \left(\frac{q_j}{p_i}\right) = (-1)^{\delta(p_i) \delta(q_j)}$.
9. Multiplying over all pairs, $\left(\frac{m}{n}\right) \left(\frac{n}{m}\right) = (-1)^{\sum_{i,j} \delta(p_i) \delta(q_j)} = (-1)^{A B}$, where $A = \sum_i \delta(p_i)$ and $B = \sum_j \delta(q_j)$.
10. By step 3, $A \equiv \delta(m)$ and $B \equiv \delta(n) \pmod 2$. So $AB \equiv \delta(m) \delta(n) \pmod 2$.
11. Hence $\left(\frac{m}{n}\right) \left(\frac{n}{m}\right) = (-1)^{\frac{m-1}{2} \cdot \frac{n-1}{2}}$.

## Idea

Both Jacobi symbols break into Legendre symbols over pairs of prime factors, one from $m$ and one from $n$. Quadratic reciprocity handles each pair. The signs combine correctly because $(r-1)/2$ is additive modulo $2$ under multiplication of odd numbers.
