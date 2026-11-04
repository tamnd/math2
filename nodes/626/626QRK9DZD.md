---
tag: 626QRK9DZD
kind: proof
name: Proof of the sum of a finite geometric series
msc: [40A05]
proves: 05APWSX53S
uses: [0MNM54WB99]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_series
---

## Proof

We multiply the sum by $1 - r$ and observe that the result telescopes.

1. Let $S_n = \sum_{k=0}^{n-1} r^k$, the sum of the first $n$ terms of the [[geometric sequence|0MNM54WB99]] $1, r, r^2, \dots$. For $n = 0$ the sum is empty, so $S_0 = 0$.
2. Multiply by $r$: $r S_n = \sum_{k=0}^{n-1} r^{k+1} = \sum_{k=1}^{n} r^k$.
3. Subtract step 2 from the definition of $S_n$. Every power $r^k$ with $1 \le k \le n-1$ appears once with each sign and cancels.
4. What remains is $S_n - r S_n = r^0 - r^n = 1 - r^n$. This also holds for $n = 0$, since both sides are $0$.
5. So $(1 - r) S_n = 1 - r^n$.
6. Since $r \ne 1$, the number $1 - r$ is not zero. Dividing step 5 by $1 - r$ gives
$$\sum_{k=0}^{n-1} r^k = \frac{1 - r^n}{1 - r}.$$

## Idea

Multiplying by $r$ shifts every term one place to the right. So the sum and $r$ times the sum share all terms but the first and the last. Subtracting leaves only $1 - r^n$.
