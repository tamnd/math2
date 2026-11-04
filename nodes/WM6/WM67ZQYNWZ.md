---
tag: WM67ZQYNWZ
kind: proof
name: Proof that the Dirichlet convolution of multiplicative functions is multiplicative
msc: [11A25]
proves: 0PR88XHDMB
uses: [0AP80TT660, 0KH1N66QWW, 0FCWA16FZE, 0GFKP8F8AG, 084HH1NDCB, 04VCPS30ZE, 0850JJMJYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplicative_function
    locator: Convolution
---

## Proof

1. Let $f$ and $g$ be [[multiplicative functions|0AP80TT660]], and let $h = f * g$ be their [[Dirichlet convolution|0KH1N66QWW]].
2. First, $1$ is the only [[positive divisor|0FCWA16FZE]] of $1$, so $h(1) = f(1) g(1) = 1 \cdot 1 = 1$.
3. Now let $m$ and $n$ be [[coprime|0GFKP8F8AG]] positive integers. We show $h(mn) = h(m) h(n)$.
4. Since $\gcd(m, n) = 1$, no prime divides both $m$ and $n$. For a prime $p$, let $\nu_p$ be the [[p-adic valuation|04VCPS30ZE]].
5. Let $P$ be the set of pairs $(d_1, d_2)$ with $d_1 \mid m$ and $d_2 \mid n$. Define $\Phi(d_1, d_2) = d_1 d_2$. Then $d_1 d_2$ divides $mn$, so $\Phi$ maps $P$ to the divisors of $mn$.
6. $\Phi$ is onto. Let $d \mid mn$. Put $d_1 = \prod_{p \mid m} p^{\nu_p(d)}$ and $d_2 = \prod_{p \mid n} p^{\nu_p(d)}$, products over primes.
7. Every prime factor $p$ of $d$ divides $mn$, hence $m$ or $n$, but not both. So $d = d_1 d_2$ by the [[fundamental theorem of arithmetic|084HH1NDCB]].
8. For $p \mid m$ we have $\nu_p(d) \le \nu_p(mn) = \nu_p(m) + \nu_p(n) = \nu_p(m)$, by the [[valuation of a product|0850JJMJYZ]]. Hence $d_1 \mid m$, and in the same way $d_2 \mid n$.
9. $\Phi$ is one-to-one. Let $d = d_1 d_2$ with $(d_1, d_2) \in P$, and let $p \mid m$. Then $p \nmid d_2$, since $d_2 \mid n$. So $\nu_p(d_1) = \nu_p(d)$.
10. All prime factors of $d_1$ divide $m$. So step 9 gives $d_1 = \prod_{p \mid m} p^{\nu_p(d)}$, which depends only on $d$. Similarly $d_2$ depends only on $d$.
11. For $(d_1, d_2) \in P$, a common divisor of $d_1$ and $d_2$ divides $m$ and $n$, hence divides $1$. So $d_1$ and $d_2$ are coprime.
12. In the same way $m / d_1$ divides $m$ and $n / d_2$ divides $n$, so they are coprime. Also $mn / (d_1 d_2) = (m/d_1)(n/d_2)$.
13. By steps 5 to 10, we can sum over $P$ instead of over the divisors of $mn$:
$$h(mn) = \sum_{(d_1, d_2) \in P} f(d_1 d_2) \, g\!\left(\frac{m}{d_1} \cdot \frac{n}{d_2}\right).$$
14. By steps 11 and 12 and the multiplicativity of $f$ and $g$, each term equals $f(d_1) g(m/d_1) \cdot f(d_2) g(n/d_2)$.
15. The sum over $P$ of these products splits as a product of two sums:
$$h(mn) = \Bigl(\sum_{d_1 \mid m} f(d_1) g(m/d_1)\Bigr) \Bigl(\sum_{d_2 \mid n} f(d_2) g(n/d_2)\Bigr) = h(m) h(n).$$
16. With step 2, this shows that $f * g$ is multiplicative.

## Idea

When $m$ and $n$ are coprime, each divisor of $mn$ splits in exactly one way into a divisor of $m$ times a divisor of $n$. The two pieces are coprime, so $f$ and $g$ split over them. The double sum then factors into the product of the two convolutions.
