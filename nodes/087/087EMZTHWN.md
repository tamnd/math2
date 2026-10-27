---
tag: 087EMZTHWN
kind: definition
name: von Mangoldt function
msc: [11A25]
defines: 0NK8JTE1NN
uses: [0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Mangoldt_function
    locator: Definition
inventory: [GCDRWN4XQZ]
---

## Definition

The von Mangoldt function $\Lambda$ is the arithmetic function given, for each positive integer $n$, by
$$\Lambda(n) = \begin{cases} \log p & \text{if } n = p^k \text{ for a prime } p \text{ and an integer } k \ge 1, \\ 0 & \text{otherwise}. \end{cases}$$
Here $\log$ is the natural logarithm. The word prime has the meaning of the [[definition of a prime number|0SN0MAEKYX]].

## Remarks

For example, $\Lambda(8) = \log 2$, $\Lambda(7) = \log 7$, and $\Lambda(1) = \Lambda(6) = 0$.
For each positive integer $n$, $\sum_{d \mid n} \Lambda(d) = \log n$.
The function $\Lambda$ is not multiplicative. It is named after Hans von Mangoldt.
The sum $\psi(x) = \sum_{n \le x} \Lambda(n)$ is the second Chebyshev function. The [[prime number theorem|0EHBY5Y84N]] is equivalent to $\psi(x) \sim x$.

## Explanations

### L1 human

The von Mangoldt function puts the weight $\log p$ on each prime power $p^k$, and $0$ on all other numbers.
With these weights, the divisor sums give exactly $\log n$, which makes the function useful in the study of primes.
