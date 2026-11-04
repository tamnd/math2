---
tag: T4HQMF76W8
kind: proof
name: Proof of the power series of the exponential function
msc: [33B10]
proves: 06JZGMYTYD
uses: [0RMVS7RXZX, 0PVJRACB9H, 0EX9GFJ0B3, 07ZMX4ANJS, 084NGSTWM7, 06SKCHDQT5, 0BE3QDH73A, 043SJ5RF59, 0BWXV7GADW, 08FPABDQ4C]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Power series
---

## Proof

We check the three claims in turn: the identity, the Maclaurin coefficients and the uniform convergence.

1. By the definition of the [[exponential function|0RMVS7RXZX]], $e^x = \exp(x) = \sum_{n=0}^{\infty} \frac{x^n}{n!}$ for every real $x$. The series converges for every $x$, since its [[radius of convergence is infinite|0PVJRACB9H]].
2. By [[the derivative of exp|0EX9GFJ0B3]], $\exp$ is differentiable on $\R$ and $\exp' = \exp$.
3. We show by induction on $n$ that the [[higher derivative|084NGSTWM7]] $\exp^{(n)}$ exists on $\R$ and equals $\exp$. For $n = 0$ this is the definition $\exp^{(0)} = \exp$.
4. If $\exp^{(n)} = \exp$, then $\exp^{(n)}$ is differentiable by step 2, and $\exp^{(n+1)} = \exp' = \exp$. This completes the induction.
5. Each $\exp^{(n)} = \exp$ is differentiable, hence [[continuous|07ZMX4ANJS]]. So $\exp$ is of [[class $C^k$|06SKCHDQT5]] on $\R$ for each $k$, that is, [[smooth|0BE3QDH73A]].
6. At $0$, every term of the series with $n \ge 1$ is $0$, and the term with $n = 0$ is $1$. So $\exp^{(n)}(0) = \exp(0) = 1$ for every $n$.
7. By step 6, the [[Maclaurin series|043SJ5RF59]] of $\exp$ is $\sum_{n=0}^{\infty} \frac{\exp^{(n)}(0)}{n!} x^n = \sum_{n=0}^{\infty} \frac{x^n}{n!}$. This is the given series.
8. Let $J$ be a bounded interval. Then $J \subseteq [-r, r]$ for some real $r > 0$.
9. The radius of convergence is $\infty > r$. By the result on [[uniform convergence inside the radius|0BWXV7GADW]], the partial sums converge [[uniformly|08FPABDQ4C]] on $[-r, r]$ to $\exp$.
10. For each $\varepsilon > 0$, the index $N$ given by step 9 for $[-r, r]$ also works for every point of $J$. So the partial sums converge to $\exp$ uniformly on $J$.

## Idea

The exponential function is defined by this series, so the identity holds by definition. Because $\exp$ is its own derivative, all its derivatives at $0$ equal $1$, which gives the coefficients $1/n!$. An infinite radius of convergence gives uniform convergence on every bounded interval.
