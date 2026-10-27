---
tag: 0BKJT6WG96
kind: definition
name: Number of divisors
aliases: [divisor-counting-function, tau-function]
msc: [11A25]
defines: 0VV3ZMRF88
uses: [0YEW47VJ0J, 0FCWA16FZE]
sources:
  - url: https://en.wikipedia.org/wiki/Divisor_function
    locator: Definition
inventory: [8GDRG1CKD7]
---

## Definition

For a positive integer $n$, the number of divisors of $n$ is $d(n) = \sigma_0(n) = \# D(n)$.
Here $\sigma_0$ is the [[divisor function|0YEW47VJ0J]] with $k = 0$, and $D(n)$ is the [[set of divisors|0FCWA16FZE]] of $n$.

## Remarks

Other common notations are $\tau(n)$ and $\sigma_0(n)$.
If $n = p_1^{e_1} \cdots p_r^{e_r}$ with distinct primes $p_i$, then $d(n) = (e_1 + 1) \cdots (e_r + 1)$.
For example, $12 = 2^2 \cdot 3$, so $d(12) = 3 \cdot 2 = 6$.
The number $d(n)$ is odd if and only if $n$ is a perfect square.

## Explanations

### L1 human

The function $d(n)$ counts the divisors of $n$.
A divisor of $p^e q^f$ is $p^a q^b$ with $0 \le a \le e$ and $0 \le b \le f$. So there are $(e + 1)(f + 1)$ choices.
