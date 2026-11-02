---
tag: BWWZB1F0HY
kind: statement
role: theorem
name: Hardy's Tauberian theorem for Cesàro means
msc: ["40E05", "40G05"]
uses: [N8ZGG7EW6J, D6XWK1NRY1, 0RYTGBJAGN, 0CVVKY7GY2]
about: [N8ZGG7EW6J, D6XWK1NRY1]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_and_Tauberian_theorems
---

## Statement

Let $\sum_{n \ge 0} a_n$ be a series of complex numbers.
Assume that it is [[Cesàro summable|N8ZGG7EW6J]] to $s$.
Assume also that $a_n = O(1/n)$ in [[big O notation|0RYTGBJAGN]], that is, there is a constant $K$ with $n \abs{a_n} \le K$ for all $n \ge 1$.
Then $\sum_{n \ge 0} a_n$ [[converges|0CVVKY7GY2]] and its sum is $s$.

## Remarks

Let $s_n$ be the partial sums and $\sigma_n$ their Cesàro means.
For $m > n$ one has the identity
$$s_n = \frac{(m+1)\sigma_m - (n+1)\sigma_n}{m - n} - \frac{1}{m - n} \sum_{k=n+1}^{m} (s_k - s_n).$$
The first term tends to $s$ when $m \approx (1 + \varepsilon) n$ and $n \to \infty$.
The second term is at most $\max_{n < k \le m} \abs{s_k - s_n} \le K \frac{m - n}{n} \approx K\varepsilon$, so $\limsup \abs{s_n - s} \le K\varepsilon$ for every $\varepsilon > 0$.

The Tauberian condition cannot be dropped.
The series $1 - 1 + 1 - \cdots$ is Cesàro summable to $\frac12$ and diverges; here $n \abs{a_n} = n$ is unbounded.
For real $a_n$, the one-sided condition $n a_n \ge -K$ is already enough.

## Explanations

### L1 human

Averaging the partial sums can give a value to a series that diverges.
Hardy's theorem says this cannot happen when the terms shrink at least like $1/n$.
Then a Cesàro sum is an honest sum.

### L2 human

This is one of the first Tauberian theorems in which the condition $n a_n \to 0$ of [[Tauber's theorem|8SK3GQ4S0M]] is relaxed to $n a_n = O(1)$.
The analogous result for Abel summation is [[Littlewood's Tauberian theorem|Z35TD4ZZRD]], which is harder, because Abel summation is stronger than Cesàro summation.
Hardy's theorem is used to show that a Fourier series of a function of bounded variation converges wherever its Cesàro means do, since its coefficients are $O(1/n)$.
