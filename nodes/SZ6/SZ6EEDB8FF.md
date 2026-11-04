---
tag: SZ6EEDB8FF
kind: proof
name: Proof that the exponential function is its own derivative, by term-by-term differentiation
msc: [33B10, 26A24]
proves: 0EX9GFJ0B3
uses: [0RMVS7RXZX, 0VP56B4EMX, 0PVJRACB9H, 002X7EK91H, 0WFCGVMRRC]
sources:
  - url: https://proofwiki.org/wiki/Derivative_of_Exponential_Function
    locator: Proof 4
---

## Proof

We differentiate the power series term by term.

1. By definition, the [[exponential function|0RMVS7RXZX]] is the [[power series|0VP56B4EMX]] $\exp(x) = \sum_{n=0}^{\infty} a_n x^n$ with center $0$ and $a_n = \frac{1}{n!}$.
2. Its radius of convergence is $R = \infty$, by [[the exponential series has infinite radius of convergence|0PVJRACB9H]]. So the interval $(0 - R, 0 + R)$ is all of $\R$.
3. By the theorem that [[power series are differentiable inside the radius of convergence|002X7EK91H]], $\exp$ is differentiable on $\R$. For every real $x$, $\exp'(x) = \sum_{n=1}^{\infty} n a_n x^{n-1}$.
4. For $n \ge 1$, the definition of the [[factorial|0WFCGVMRRC]] gives $n! = n \cdot (n-1)!$. So $n a_n = \frac{n}{n!} = \frac{1}{(n-1)!}$.
5. By steps 3 and 4, and the index change $m = n - 1$, $\exp'(x) = \sum_{n=1}^{\infty} \frac{x^{n-1}}{(n-1)!} = \sum_{m=0}^{\infty} \frac{x^m}{m!} = \exp(x)$.

## Idea

Differentiating $x^n/n!$ gives $x^{n-1}/(n-1)!$, the previous term of the same series. So differentiating the whole series shifts it by one place and returns the same series. The infinite radius of convergence makes term-by-term differentiation valid everywhere.
