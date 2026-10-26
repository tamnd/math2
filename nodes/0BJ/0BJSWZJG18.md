---
tag: 0BJSWZJG18
kind: statement
role: theorem
name: Mertens' theorem on Cauchy products
msc: [40A05]
uses: [0B1K9PVWE9, 0W3K3QPEWT, 0CVVKY7GY2]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_product
    locator: Convergence and Mertens' theorem
---

## Statement

Let $\sum a_n$ be a real series that [[converges absolutely|0W3K3QPEWT]], with sum $A$.
Let $\sum b_n$ be a [[convergent|0CVVKY7GY2]] real series, with sum $B$.
Then their [[Cauchy product|0B1K9PVWE9]] converges, and its sum is $A B$.

## Remarks

Convergence of both series is not enough. Take $a_n = b_n = (-1)^n / \sqrt{n + 1}$. Both series converge, but $|c_n| \ge 1$ for all $n$, so the Cauchy product diverges.
Franz Mertens proved the theorem.

## Explanations

### L1 human

One series may converge only conditionally, if the other converges absolutely.
Then the product of the two series is still the sum of their Cauchy product.
