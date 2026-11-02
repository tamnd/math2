---
tag: 7DMEGGFD0J
kind: definition
name: Optimal truncation
msc: [41A60, 40A05]
defines: 1YR53GZEPT
uses: [BJQTEPEZ9G]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_expansion
---

## Definition

Let $f(x) \sim \sum_{n \ge 0} a_n \varphi_n(x)$ be an [[asymptotic expansion|BJQTEPEZ9G]] of $f$ as $x \to x_0$, and fix a value of $x$ near $x_0$.
Assume that the sequence $\abs{a_n \varphi_n(x)}$, $n \ge 0$, attains a minimum, and let $N(x)$ be the smallest index $n$ at which it does.
The *optimally truncated* sum at $x$ is
$$S_{\mathrm{opt}}(x) = \sum_{n=0}^{N(x) - 1} a_n \varphi_n(x),$$
the partial sum that stops just before the smallest term.
*Optimal truncation* is the approximation of $f(x)$ by $S_{\mathrm{opt}}(x)$.

## Remarks

Some authors include the smallest term, or half of it; these choices change the error only by a fraction of the smallest term.
The index $N(x)$ depends on $x$ and usually tends to infinity as $x \to x_0$.

Example: $F(x) = \int_0^\infty \frac{e^{-t}}{1 + xt}\,dt \sim \sum_{n \ge 0} (-1)^n n!\, x^n$ as $x \to 0^+$.
For $x = 0.1$ the terms $n!\, (0.1)^n$ decrease while $n + 1 < 10$, the terms with $n = 9$ and $n = 10$ are equal, and then they increase.
So $N(0.1) = 9$, and the error of the optimally truncated sum is at most the first omitted term $9!\, (0.1)^9 \approx 3.6 \cdot 10^{-4}$, since the remainder after $N$ terms is bounded by the next term.

Non-example: for a convergent series such as $\frac{1}{1 - x} = \sum x^n$ at $x = \frac12$ the terms decrease forever, no minimum is attained, and optimal truncation is not defined; one simply sums the series.
