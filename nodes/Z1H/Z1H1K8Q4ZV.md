---
tag: Z1H1K8Q4ZV
kind: definition
name: Abel summation
msc: ["40G10"]
defines: EZXPY4A19C
uses: [8X25Q4XYMN, 0JH4MN4K1C, 0VP56B4EMX, 0909PWZR62]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_and_Tauberian_theorems
---

## Definition

Let $\sum_{n \ge 0} a_n$ be a [[series|0JH4MN4K1C]] of complex numbers.
The series is *Abel summable* to $s$ if the following two conditions hold.

1. The [[power series|0VP56B4EMX]] $f(x) = \sum_{n \ge 0} a_n x^n$ converges for every real $x$ with $0 \le x < 1$.
2. The [[one-sided limit|0909PWZR62]] $\lim_{x \to 1^-} f(x)$ exists and equals $s$.

## Remarks

Example: for $a_n = (-1)^n (n + 1)$, that is $1 - 2 + 3 - 4 + \cdots$, one has $f(x) = \sum_{n \ge 0} (-1)^n (n+1) x^n = \frac{1}{(1 + x)^2}$ for $0 \le x < 1$.
This tends to $\frac14$ as $x \to 1^-$, so the series is Abel summable to $1/4$.

Non-example: for $1 + 1 + 1 + \cdots$, condition 1 holds with $f(x) = \frac{1}{1 - x}$.
But $f(x) \to +\infty$ as $x \to 1^-$, so condition 2 fails and the series is not Abel summable.

If $\sum a_n$ converges to $s$, then it is Abel summable to $s$; this is Abel's theorem on power series.
In the notation of summability, one writes $A\text{-}\sum a_n = s$.
