---
tag: QAP2SBSK2G
kind: definition
name: Riesz mean
msc: ["40G99", "30B50"]
defines: AGXZ2G4MFM
uses: [8X25Q4XYMN, 0JH4MN4K1C, 0NB643K60Q]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_mean
---

## Definition

Let $(\lambda_n)_{n \ge 0}$ be a strictly increasing sequence of real numbers with $\lambda_0 \ge 0$ and $\lambda_n \to \infty$, and let $\delta > 0$.
Let $\sum_{n \ge 0} a_n$ be a [[series|0JH4MN4K1C]] of complex numbers.
For real $\omega > 0$, the *Riesz mean* of type $\lambda$ and order $\delta$ is the finite sum
$$R^{\delta}_{\lambda}(\omega) = \sum_{n \,:\, \lambda_n < \omega} \left(1 - \frac{\lambda_n}{\omega}\right)^{\delta} a_n.$$
The series is $(R, \lambda, \delta)$ summable to $s$ if $R^{\delta}_{\lambda}(\omega) \to s$ as $\omega \to \infty$.

## Remarks

Example: take $\lambda_n = n$, $\delta = 1$ and an integer cut-off $\omega = N + 1$.
Then
$$R^1_{\lambda}(N + 1) = \sum_{n=0}^{N} \frac{N + 1 - n}{N + 1} a_n = \frac{s_0 + s_1 + \cdots + s_N}{N + 1},$$
where $s_j$ are the [[partial sums|0NB643K60Q]], because $a_n$ occurs in exactly the $N + 1 - n$ partial sums $s_n, \dots, s_N$.
So these Riesz means are the Cesàro means of the partial sums.

Non-example: if $\lambda_n = 1 - 2^{-n}$, the sequence is increasing but bounded, so the condition $\lambda_n \to \infty$ fails.
Then for $\omega > 1$ every term enters $R^{\delta}_{\lambda}(\omega)$, which is not a finite sum, and the definition does not apply.

For Dirichlet series $\sum a_n n^{-s}$ one usually takes $\lambda_n = \ln n$ for $n \ge 1$.
