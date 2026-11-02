---
tag: R8MZAZ6GCR
kind: statement
role: theorem
name: Frobenius theorem on Cesàro and Abel summability
msc: ["40D25", "40G05", "40G10"]
uses: [N8ZGG7EW6J, EZXPY4A19C, 0VP56B4EMX]
about: [N8ZGG7EW6J, EZXPY4A19C]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_and_Tauberian_theorems
---

## Statement

Let $\sum_{n \ge 0} a_n$ be a series of complex numbers that is [[Cesàro summable|N8ZGG7EW6J]] to $s$, that is, $\sigma_n = \frac{s_0 + \cdots + s_n}{n + 1} \to s$, where $s_n = a_0 + \cdots + a_n$.
Then the [[power series|0VP56B4EMX]] $f(x) = \sum_{n \ge 0} a_n x^n$ converges for $\abs{x} < 1$, and $f(x) \to s$ as $x \to 1^-$.
So the series is [[Abel summable|EZXPY4A19C]] to $s$.

## Remarks

The sequence $(\sigma_n)$ converges, so it is bounded, and then $s_n = (n+1)\sigma_n - n\sigma_{n-1}$ and $a_n = s_n - s_{n-1}$ are $O(n)$; hence the power series converges for $\abs{x} < 1$.
Multiplying by $\frac{1}{1-x}$ twice gives, for $\abs{x} < 1$,
$$f(x) = (1 - x)^2 \sum_{n \ge 0} (n + 1) \sigma_n x^n.$$
Since $(1 - x)^2 \sum_{n \ge 0} (n+1) x^n = 1$, one gets $f(x) - s = (1 - x)^2 \sum_{n \ge 0} (n + 1)(\sigma_n - s) x^n$.
Splitting the sum at a large $N$ where $\abs{\sigma_n - s} < \varepsilon$ for $n > N$ shows that this tends to $0$ as $x \to 1^-$.

Example: $1 - 1 + 1 - \cdots$ is Cesàro summable to $\frac12$, and indeed $\sum (-1)^n x^n = \frac{1}{1+x} \to \frac12$.

The converse fails: $1 - 2 + 3 - 4 + \cdots$ is Abel summable to $\frac14$, since $\sum (-1)^n (n+1) x^n = \frac{1}{(1+x)^2}$, but it is not Cesàro summable of order $1$.

## Explanations

### L1 human

Cesàro summation averages the partial sums; Abel summation damps the terms by powers of $x$ and lets $x \to 1$.
The theorem says that the second method is at least as strong as the first and gives the same answer.
Every series that averaging can sum, damping can sum too, to the same value.

### L2 human

This is an Abelian theorem in the sense of summability: it compares two methods and shows an inclusion with consistency.
It is a strengthening of [[Abel's theorem|0S4EMDQS2F]], because every convergent series is Cesàro summable to its sum.
The same argument shows that Cesàro summability of any order $k$ implies Abel summability to the same value.
