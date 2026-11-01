---
tag: NQGAM8PDG7
kind: definition
name: Infinitely divisible distribution
msc: ["60E07"]
defines: BX3V3NYM1Y
uses: [0DVDCMA2DK, 00MRN0FARV, 0F8GDKM0A7, 0V5B6D6BQH]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite_divisibility_(probability)
---

## Definition

Let $\mu$ be a [[probability distribution|0DVDCMA2DK]] on $\R$.
$\mu$ is *infinitely divisible* if for every integer $n \ge 1$ there are [[independent and identically distributed|00MRN0FARV]] random variables $Y_{n,1}, \dots, Y_{n,n}$ such that $Y_{n,1} + \dots + Y_{n,n}$ has law $\mu$.
A real random variable is infinitely divisible if its law is.

## Remarks

Equivalently, for every $n \ge 1$ there is a probability measure $\mu_n$ whose $n$-fold [[convolution|0F8GDKM0A7]] power is $\mu$; or, in terms of [[characteristic functions|0V5B6D6BQH]], $\varphi = \varphi_n^n$ for some characteristic function $\varphi_n$.
The same definition applies to laws on $\R^d$.
Example: the Poisson law with mean $\lambda$ is the law of a sum of $n$ independent Poisson variables with mean $\lambda / n$, since $e^{\lambda(e^{it} - 1)} = \left(e^{(\lambda/n)(e^{it} - 1)}\right)^n$.
Example: the normal law with mean $m$ and variance $\sigma^2$ is the law of a sum of $n$ independent normal variables with mean $m/n$ and variance $\sigma^2/n$.
Non-example: a [[Bernoulli|0386Y0Z7Y7]] law with parameter $p \in (0, 1)$.
Suppose $Y_1 + Y_2$ has this law, with $Y_1, Y_2$ i.i.d.
If $s < s'$ were two points of the support of $Y_1$, then $2s < s + s' < 2s'$ would be three values in $\set{0, 1}$.
So $Y_1$ is constant, and then $Y_1 + Y_2$ is constant, a contradiction.
The characteristic function of an infinitely divisible law has no zeros.
