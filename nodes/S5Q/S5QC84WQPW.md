---
tag: S5QC84WQPW
kind: proof
name: Proof of the exponential of a sum by the Cauchy product
msc: [33B10]
proves: 0E8HNVBCSP
uses: [0RMVS7RXZX, 0PVJRACB9H, 0B1K9PVWE9, 0AN28XQ45Z, 0EHWPWGHB2, 033KTKKRV6]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_product
    locator: Examples
---

## Proof

We multiply the two series by the Cauchy product and use the binomial theorem.

1. Let $x, y$ be real. Let $a_k = \frac{x^k}{k!}$ and $b_k = \frac{y^k}{k!}$ for $k \ge 0$. By the definition of the [[exponential function|0RMVS7RXZX]], $\sum a_k = \exp(x)$ and $\sum b_k = \exp(y)$.
2. Both series converge absolutely, since the [[exponential series has infinite radius of convergence|0PVJRACB9H]].
3. The [[Cauchy product|0B1K9PVWE9]] of the two series has the terms $c_n = \sum_{k=0}^{n} a_k b_{n-k} = \sum_{k=0}^{n} \frac{x^k y^{n-k}}{k! \, (n-k)!}$.
4. By the [[factorial formula for binomial coefficients|033KTKKRV6]], $\frac{1}{k! \, (n-k)!} = \frac{1}{n!} \binom{n}{k}$ for $0 \le k \le n$.
5. By step 4 and the [[binomial theorem|0EHWPWGHB2]] in $\R$, $c_n = \frac{1}{n!} \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k} = \frac{(x + y)^n}{n!}$.
6. By step 2 and the theorem on the [[Cauchy product of absolutely convergent series|0AN28XQ45Z]], $\sum c_n$ converges, and its sum is $\exp(x) \exp(y)$.
7. By step 5 and the definition of $\exp$, $\sum_{n=0}^{\infty} c_n = \sum_{n=0}^{\infty} \frac{(x+y)^n}{n!} = \exp(x + y)$.
8. Comparing steps 6 and 7 gives $\exp(x + y) = \exp(x) \exp(y)$.

## Idea

Multiplying the two series and collecting the terms of total degree $n$ gives exactly the binomial expansion of $(x + y)^n$, divided by $n!$. Absolute convergence makes this rearrangement legitimate.
