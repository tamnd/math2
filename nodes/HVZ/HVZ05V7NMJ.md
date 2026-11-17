---
tag: HVZ05V7NMJ
kind: example
name: The inequality 2^n > n^3 holds for all sufficiently large n
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [FEQ7WATMHF]
uses: [FEQ7WATMHF, 0ASJVEFA9J, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Eventually_(mathematics)
    locator: lead section
---

## Example

We show that the statement $P(n)$: "$2^n > n^3$" holds [[for all sufficiently large|FEQ7WATMHF]] natural numbers $n$, with threshold $N = 10$.
We also show that $N = 10$ is the least threshold.

1. We compute the small values. For $n = 0$ and $n = 1$, the statement is true: $1 > 0$ and $2 > 1$.
2. For $n = 2$ to $n = 9$, the statement is false. The pairs $(2^n, n^3)$ are $(4, 8)$, $(8, 27)$, $(16, 64)$, $(32, 125)$, $(64, 216)$, $(128, 343)$, $(256, 512)$ and $(512, 729)$.
3. For $n = 10$, the statement is true: $2^{10} = 1024$ and $10^3 = 1000$.
4. Induction step. Let $n \geq 10$ and suppose $2^n > n^3$. Then $2^{n+1} = 2 \cdot 2^n > 2n^3$.
5. We compare $2n^3$ with $(n + 1)^3$. We have $(n + 1)^3 = n^3 (1 + 1/n)^3$, and for $n \geq 10$ we have $(1 + 1/n)^3 \leq 1.1^3 = 1.331 < 2$. So $(n + 1)^3 < 2n^3 < 2^{n+1}$.
6. By [[mathematical induction|0ASJVEFA9J]] from $n = 10$, the statement $2^n > n^3$ is true for every $n \geq 10$.
7. No smaller threshold works. A threshold $N \leq 9$ would need $P(9)$, and step 2 shows that $P(9)$ is false.

## Remarks

The statement is true at $n = 0$ and $n = 1$, false from $n = 2$ to $n = 9$, and true from $n = 10$ on.
So a check of the first values alone gives a wrong picture, and the eventual behaviour needs a proof.
The same method shows that $2^n > n^k$ eventually for each fixed $k$, but the threshold grows with $k$.
The inequality $(1 + 1/n)^k < 2$ is the key step, and it holds for all $n$ larger than some bound that depends on $k$.

## Explanations

### L1 human

The number $2^n$ doubles at each step, while $n^3$ grows more slowly once $n$ is large.
At first $n^3$ is ahead: for $n = 9$ we have $2^9 = 512$ and $9^3 = 729$.
At $n = 10$ the doubling catches up, with $1024$ against $1000$, and after that it stays ahead forever.
This is what "eventually" means: from some point on, and at every later step.

### L2 human

We find the least threshold for $2^n > n^2$ with the same method.

1. Small values: the statement is true for $n = 0$ and $n = 1$, false for $n = 2$ ($4 = 4$), $n = 3$ ($8 < 9$) and $n = 4$ ($16 = 16$), and true for $n = 5$ ($32 > 25$).
2. Induction step for $n \geq 5$: $(n + 1)^2 = n^2 (1 + 1/n)^2 \leq 1.44 n^2 < 2n^2 < 2^{n+1}$.
3. So $2^n > n^2$ holds for all $n \geq 5$, and the threshold $5$ is the least one, because the statement fails at $n = 4$.

A trap: the equality case $2^4 = 4^2$ shows that a strict inequality can fail without the reverse inequality being true.
