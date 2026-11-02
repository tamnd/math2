---
tag: SVSVMWA9NQ
kind: statement
role: theorem
name: Pairwise summation
msc: [65G50, 65B10]
uses: [RTKRSC3KPH, JA3QXVF2B8, CPN6SD3BTV]
about: [CPN6SD3BTV]
sources:
  - url: https://en.wikipedia.org/wiki/Pairwise_summation
same_as:
  wikidata: Q17104961
  wikipedia: Pairwise summation
---

## Statement

Let $x_1, \ldots, x_n$ be [[floating-point|RTKRSC3KPH]] numbers in a system with unit roundoff $u$ (see [[machine epsilon|JA3QXVF2B8]]), with no overflow or underflow, and let $\gamma_k = ku/(1 - ku)$ for $ku < 1$.
*Pairwise summation* computes $\hat s$ recursively, with $\hat s = x_1$ if $n = 1$.
If $n \ge 2$, let $m = \floor{n/2}$; it computes $\hat s_1$ for $x_1, \ldots, x_m$ and $\hat s_2$ for $x_{m+1}, \ldots, x_n$ in the same way.
Then it sets $\hat s = \mathrm{fl}(\hat s_1 + \hat s_2)$.
If $\lceil \log_2 n \rceil u < 1$, then
$$\Bigl| \hat s - \sum_{i=1}^{n} x_i \Bigr| \le \gamma_{\lceil \log_2 n \rceil} \sum_{i=1}^{n} \abs{x_i}.$$

## Remarks

The recursion has depth $\lceil \log_2 n \rceil$, and each term $x_i$ takes part in at most $\lceil \log_2 n \rceil$ floating-point additions.
Each addition multiplies the term by a factor $1 + \delta$ with $\abs{\delta} \le u$, so $\hat s = \sum x_i (1 + \theta_i)$ with $\abs{\theta_i} \le \gamma_{\lceil \log_2 n \rceil}$, which gives the bound.
For $n = 10^6$ terms in double precision, the bound is about $20u \sum \abs{x_i}$, against about $10^6 u \sum \abs{x_i}$ for plain recursive summation.
The cost is the same $n - 1$ additions as recursive summation.
In practice the recursion stops at blocks of moderate size that are summed in a simple loop, which gives a bound of order $(B + \log_2 n) u \sum \abs{x_i}$ for blocks of size $B$.

## Explanations

### L1 human

When one adds a long list of numbers one by one, the running total gets large and each new small term is rounded against it.
Pairwise summation adds the numbers in pairs, then the pair sums in pairs, and so on, like a sports tournament bracket.
Each number then passes through only about $\log_2 n$ additions instead of up to $n$, so the rounding errors grow much more slowly.

### L2 human

The error bound grows like $u \log_2 n$, against $u n$ for recursive summation.
The [[Kahan summation algorithm|4JAEKN22Y5]] does better still, with a leading term $2u$ independent of $n$, at about four times the cost.
Pairwise summation is the default in several numerical libraries because it costs no extra arithmetic.
The same divide-and-conquer pattern appears in the fast Fourier transform, whose rounding errors also grow only logarithmically.
For random rounding errors the typical error is even smaller, of order $u \sqrt{\log n}$ in a statistical model.
