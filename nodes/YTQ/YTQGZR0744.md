---
tag: YTQGZR0744
kind: proof
name: Proof of Lucas's theorem by generating functions
msc: [11B65]
proves: 0RY4GGMEQG
uses: [0SN0MAEKYX, 0TPW25CBN6, 092GEF38YD, 0EHWPWGHB2, 0396VGFA78, 0Q9EZS90GY, 01N3AYAA6N, 0P7CH1CND5, 0CHQKZFK5S]
sources:
  - url: https://en.wikipedia.org/wiki/Lucas%27s_theorem
    locator: Proof based on generating functions
---

## Proof

1. Let $p$ be a [[prime number|0SN0MAEKYX]] and $m = \sum_{i=0}^{k} m_i p^i$, $n = \sum_{i=0}^{k} n_i p^i$ with digits $0 \le m_i, n_i < p$.
2. Let $R = (\mathbb{Z}/p\mathbb{Z})[x]$ be the [[polynomial ring|0Q9EZS90GY]] over the [[integers modulo p|01N3AYAA6N]]. It is a commutative ring. In $R$, the sum of $j$ copies of $1$ is the class of $j$, which is $0$ for $j = p$ and nonzero for $0 < j < p$.
3. So $R$ has [[characteristic|0P7CH1CND5]] $p$. By the [[freshman's dream|0396VGFA78]], $(1 + x)^p = 1 + x^p$ in $R$.
4. By induction on $i$, $(1 + x)^{p^i} = 1 + x^{p^i}$ in $R$. The case $i = 0$ is clear. If it holds for $i$, then $(1+x)^{p^{i+1}} = (1 + x^{p^i})^p = 1 + x^{p^{i+1}}$, by the freshman's dream applied to $1$ and $x^{p^i}$.
5. By the [[binomial theorem|0EHWPWGHB2]] in $R$, for each natural number $N$, $(1 + x)^N = \sum_{j=0}^{N} \overline{\binom{N}{j}} x^j$. Here the bar is the class modulo $p$ of the [[binomial coefficient|092GEF38YD]].
6. So the coefficient of $x^n$ in $(1+x)^m$ is the class of $\binom{m}{n}$. This also holds when $n > m$, since the coefficient is then $0$ and $\binom{m}{n} = 0$ by convention.
7. Since $m = \sum_i m_i p^i$, step 4 gives $(1 + x)^m = \prod_{i=0}^{k} \left((1+x)^{p^i}\right)^{m_i} = \prod_{i=0}^{k} (1 + x^{p^i})^{m_i}$.
8. By the binomial theorem, $(1 + x^{p^i})^{m_i} = \sum_{j=0}^{m_i} \overline{\binom{m_i}{j}} x^{j p^i}$.
9. Multiplying out, $(1 + x)^m$ is the sum, over all tuples $(j_0, \dots, j_k)$ with $0 \le j_i \le m_i$, of $\overline{\prod_i \binom{m_i}{j_i}} \, x^{\sum_i j_i p^i}$.
10. Base-$p$ digits are unique. If $\sum_i a_i p^i = \sum_i b_i p^i$ with digits in $\set{0, \dots, p-1}$, the [[division algorithm|0CHQKZFK5S]] by $p$ gives $a_0 = b_0$. Subtracting, dividing by $p$ and repeating gives $a_i = b_i$ for all $i$.
11. In step 9 each $j_i \le m_i < p$. So by step 10, $\sum_i j_i p^i = n$ holds exactly when $j_i = n_i$ for every $i$.
12. If $n_i \le m_i$ for all $i$, exactly one tuple contributes to $x^n$, and the coefficient of $x^n$ is the class of $\prod_i \binom{m_i}{n_i}$.
13. If $n_i > m_i$ for some $i$, no tuple contributes, and the coefficient of $x^n$ is $0$. In this case $\binom{m_i}{n_i} = 0$, so the coefficient is again the class of $\prod_i \binom{m_i}{n_i}$.
14. Two equal polynomials have equal coefficients. Comparing steps 6, 12 and 13 gives $\binom{m}{n} \equiv \prod_{i=0}^{k} \binom{m_i}{n_i} \pmod p$, a [[congruence modulo p|0TPW25CBN6]].

## Idea

Modulo $p$, raising to the power $p$ is additive, so $(1+x)^{p^i} \equiv 1 + x^{p^i}$. Writing $m$ in base $p$ factors $(1+x)^m$ into pieces, one for each digit. Uniqueness of base-$p$ digits means that $x^n$ arises from exactly one choice in each piece, namely the digit $n_i$.
