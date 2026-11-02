---
tag: PKYQY68PCB
kind: definition
name: Lauricella hypergeometric series
msc: [33C65, 33C70]
defines: 6YSVDFEM39
uses: [YZHM3HSM0F, QG9VDK1HN9, 0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Lauricella_hypergeometric_series
---

## Definition

Let $n \ge 1$ be an integer, let $x = (x_1, \dots, x_n) \in \C^n$, and let $a, a_i, b, b_i, c, c_i$ be complex numbers with every lower parameter $c, c_i$ outside $\set{0, -1, -2, \dots}$.
Write $(x)_k$ for the [[Pochhammer symbol|YZHM3HSM0F]], and for a multi-index $m = (m_1, \dots, m_n) \in \N^n$ write $\abs{m} = m_1 + \cdots + m_n$, $m! = m_1! \cdots m_n!$ and $x^m = x_1^{m_1} \cdots x_n^{m_n}$.
The four *Lauricella series* are:

1. $F_A^{(n)}(a; b_1, \dots, b_n; c_1, \dots, c_n; x) = \sum_{m} \frac{(a)_{\abs{m}} (b_1)_{m_1} \cdots (b_n)_{m_n}}{(c_1)_{m_1} \cdots (c_n)_{m_n}} \frac{x^m}{m!}$, convergent for $\abs{x_1} + \cdots + \abs{x_n} < 1$;
2. $F_B^{(n)}(a_1, \dots, a_n; b_1, \dots, b_n; c; x) = \sum_{m} \frac{(a_1)_{m_1} \cdots (a_n)_{m_n} (b_1)_{m_1} \cdots (b_n)_{m_n}}{(c)_{\abs{m}}} \frac{x^m}{m!}$, convergent for $\abs{x_i} < 1$ for all $i$;
3. $F_C^{(n)}(a; b; c_1, \dots, c_n; x) = \sum_{m} \frac{(a)_{\abs{m}} (b)_{\abs{m}}}{(c_1)_{m_1} \cdots (c_n)_{m_n}} \frac{x^m}{m!}$, convergent for $\sqrt{\abs{x_1}} + \cdots + \sqrt{\abs{x_n}} < 1$;
4. $F_D^{(n)}(a; b_1, \dots, b_n; c; x) = \sum_{m} \frac{(a)_{\abs{m}} (b_1)_{m_1} \cdots (b_n)_{m_n}}{(c)_{\abs{m}}} \frac{x^m}{m!}$, convergent for $\abs{x_i} < 1$ for all $i$.

Each sum runs over all $m \in \N^n$.

## Remarks

For $n = 2$ the four series are the [[Appell series|QG9VDK1HN9]]: $F_A = F_2$, $F_B = F_3$, $F_C = F_4$ and $F_D = F_1$.
Example: for $n = 1$ all four series reduce to $\sum_{k} \frac{(a)_k (b)_k}{(c)_k} \frac{x^k}{k!} = {}_2F_1(a, b; c; x)$, with $b = b_1$ and $c = c_1$ as needed; the check is a direct comparison of coefficients.
Non-example: the point $x_1 = x_2 = \frac12$ is outside the region of convergence of $F_A^{(2)}$; with $a = 1$ and $b_i = c_i$ the series is $\sum_{N \ge 0} (x_1 + x_2)^N$, which diverges there.
For $\operatorname{Re} c > \operatorname{Re} a > 0$, with $\Gamma$ the [[gamma function|0H5SYBSED9]], the series $F_D$ has the integral form
$$F_D^{(n)}(a; b_1, \dots, b_n; c; x) = \frac{\Gamma(c)}{\Gamma(a)\Gamma(c - a)} \int_0^1 t^{a - 1} (1 - t)^{c - a - 1} \prod_{i = 1}^{n} (1 - x_i t)^{-b_i}\, dt.$$
