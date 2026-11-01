---
tag: MC9HE0M2RG
kind: definition
name: Chebyshev functions
msc: [11N05, 11A41]
defines: B8AKSVBE5Z
uses: [01826KMG2H, 04DXAFN2ES, 0NK8JTE1NN]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev_function
---

## Definition

Let $x$ be a real number.
The *first Chebyshev function* is
$$\vartheta(x) = \sum_{p \le x} \log p,$$
where $p$ runs over the [[prime numbers|01826KMG2H]] at most $x$ and $\log$ is the [[natural logarithm|04DXAFN2ES]].
The *second Chebyshev function* is
$$\psi(x) = \sum_{\substack{p, k \\ p^k \le x}} \log p = \sum_{1 \le n \le x} \Lambda(n).$$
Here the first sum runs over the pairs of a prime $p$ and an integer $k \ge 1$.
The symbol $\Lambda$ denotes the [[von Mangoldt function|0NK8JTE1NN]].

## Remarks

Example: $\vartheta(10) = \log 2 + \log 3 + \log 5 + \log 7 = \log 210$.
The prime powers up to $10$ are $2, 4, 8, 3, 9, 5, 7$, so $\psi(10) = \log(2^3 \cdot 3^2 \cdot 5 \cdot 7) = \log 2520$.
In general $\psi(x) = \log \operatorname{lcm}(1, 2, \dots, \floor{x})$ for $x \ge 1$.
Non-example: $\sum_{n \le 10} \log n = \log 10!$ is not $\psi(10)$, since it also has terms such as $\log 6$ for $n$ that are not prime powers.
The two functions are related by $\psi(x) = \sum_{k \ge 1} \vartheta(x^{1/k})$, and $\psi(x) - \vartheta(x) = O(\sqrt{x} \log x)$.
Both are $0$ for $x < 2$.
