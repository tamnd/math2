---
tag: 0YEW47VJ0J
kind: definition
name: Divisor function
msc: [11A25]
defines: 04J4Z73J5B
uses: [0FCWA16FZE, 0H2EPRZC0D]
sources:
  - url: https://en.wikipedia.org/wiki/Divisor_function
    locator: Definition
---

## Definition

Let $k$ be a natural number.
The divisor function $\sigma_k$ is the [[arithmetic function|0H2EPRZC0D]] given by
$$\sigma_k(n) = \sum_{d \mid n} d^k,$$
where the sum runs over the [[positive divisors|0FCWA16FZE]] $d$ of $n$.

## Remarks

The case $k = 0$ is the [[number of divisors|0BKJT6WG96]], and the case $k = 1$ is the [[sum of divisors|009QCP5T3Z]].
For example, $\sigma_2(6) = 1 + 4 + 9 + 36 = 50$.
The same formula defines $\sigma_k$ for each real or complex number $k$.
The function $\sigma_k$ is [[multiplicative|04WC36XKV6]].

## Explanations

### L1 human

To compute $\sigma_k(n)$, list the divisors of $n$, raise each one to the power $k$, and add the results.
