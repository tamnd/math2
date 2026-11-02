---
tag: PW313WB7HE
kind: definition
name: Wilf–Zeilberger pair
msc: [33F10, 05A19, 68W30]
defines: WC0QNABPZ4
uses: [0XDK9CGYKJ, 0GBZM0MT0F, 0GXKM1R7E4]
sources:
  - url: https://en.wikipedia.org/wiki/Wilf%E2%80%93Zeilberger_pair
---

## Definition

A function $F(n, k)$ of two integer variables is a *hypergeometric term* if the ratios $F(n + 1, k)/F(n, k)$ and $F(n, k + 1)/F(n, k)$ are [[rational functions|0XDK9CGYKJ]] of $n$ and $k$.
A *Wilf–Zeilberger pair* (WZ pair) is a pair of hypergeometric terms $F$ and $G$ such that

1. $F(n + 1, k) - F(n, k) = G(n, k + 1) - G(n, k)$ for all integers $n, k$;
2. $G(n, k) = R(n, k)\,F(n, k)$ for a rational function $R$, called the *WZ certificate*.

## Remarks

Consequence: suppose that for each $n$ the sum $\sum_k F(n, k)$ converges and $G(n, k) \to 0$ as $k \to \pm\infty$.
Then summing clause 1 over $k$ gives a [[telescoping sum|0GXKM1R7E4]] on the right.
So $\sum_k F(n + 1, k) = \sum_k F(n, k)$, and the sum is constant in $n$.

Example: let $F(n, k) = \binom{n}{k}/2^n$ and $G(n, k) = -\binom{n}{k - 1}/2^{n + 1}$, with [[binomial coefficients|0GBZM0MT0F]] that vanish outside $0 \le k \le n$.
Pascal's rule gives $F(n + 1, k) - F(n, k) = \big(\binom{n}{k - 1} - \binom{n}{k}\big)/2^{n + 1}$, which is $G(n, k + 1) - G(n, k)$.
The certificate is $R(n, k) = -k/(2(n - k + 1))$.
So $\sum_k \binom{n}{k}/2^n$ is constant, and its value $1$ at $n = 0$ proves $\sum_k \binom{n}{k} = 2^n$.

Non-example: the same $F$ with $G = 0$ is not a WZ pair, since clause 1 would need $F(n + 1, k) = F(n, k)$, which fails for $n = 0$, $k = 0$: $F(1, 0) = 1/2$ but $F(0, 0) = 1$.
