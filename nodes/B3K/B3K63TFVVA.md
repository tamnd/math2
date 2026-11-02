---
tag: B3K63TFVVA
kind: definition
name: Krawtchouk polynomials
msc: [33C45, 94B25]
defines: CJGKW80KBR
uses: [YZHM3HSM0F, 0WCWA1KT3M]
sources:
  - url: https://en.wikipedia.org/wiki/Kravchuk_polynomials
---

## Definition

Let $N \ge 0$ be an integer, let $0 < p < 1$, and let $n$ be an integer with $0 \le n \le N$.
Write $(a)_k$ for the [[Pochhammer symbol|YZHM3HSM0F]].
The *Krawtchouk polynomial* of degree $n$ is
$$K_n(x; p, N) = \sum_{k=0}^{n} \frac{(-n)_k \, (-x)_k}{(-N)_k \, k!} \, p^{-k},$$
that is, $K_n(x; p, N) = {}_2F_1\left( -n, -x; -N; \frac{1}{p} \right)$.

## Remarks

The denominators $(-N)_k$ are nonzero because $k \le n \le N$.
They are orthogonal for the [[binomial distribution|0WCWA1KT3M]]:
$$\sum_{x=0}^{N} \binom{N}{x} p^x (1 - p)^{N - x} K_m(x; p, N) K_n(x; p, N) = \frac{\delta_{mn}}{\binom{N}{n}} \left( \frac{1 - p}{p} \right)^n.$$
Example: $K_1(x; p, N) = 1 - \frac{x}{Np}$.
Check: if $X$ is binomial with mean $Np$ and variance $Np(1 - p)$, then $E[K_1(X)] = 0$ and $E[K_1(X)^2] = \frac{Np(1 - p)}{N^2 p^2} = \frac{1}{N} \cdot \frac{1 - p}{p}$.
Non-example: the clause $n \le N$ matters; for $n > N$ the formula breaks down at $k = N + 1$, where $(-N)_k = 0$.
In coding theory one often uses the version $\mathcal{K}_k(x) = \sum_{j=0}^{k} (-1)^j (q - 1)^{k - j} \binom{x}{j} \binom{N - x}{k - j}$ for an alphabet of size $q$, which is a constant multiple of $K_k(x; 1 - 1/q, N)$.
