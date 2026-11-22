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

Let $P(n)$ be the statement "$2^n > n^3$" for a natural number $n$.
We show that $P(n)$ holds [[for all sufficiently large|FEQ7WATMHF]] $n$, with threshold $N = 10$, and that no smaller threshold works.

1. Compute the small values.
   For $n = 0$ and $n = 1$ the statement is true, since $1 > 0$ and $2 > 1$.
2. For $n = 2$ to $n = 9$ the statement is false.
   The pairs $(2^n, n^3)$ are
   $$(4, 8), \ (8, 27), \ (16, 64), \ (32, 125), \ (64, 216), \ (128, 343), \ (256, 512), \ (512, 729).$$
3. For $n = 10$ the statement is true: $2^{10} = 1024$ and $10^3 = 1000$.
4. Induction step.
   Let $n \ge 10$ and suppose $2^n > n^3$.
   Then $2^{n+1} = 2 \cdot 2^n > 2n^3$.
5. Compare $2n^3$ with $(n + 1)^3$.
   For $n \ge 10$ we have
   $$(n + 1)^3 = n^3 \left( 1 + \frac{1}{n} \right)^3 \le 1.1^3 \, n^3 = 1.331 \, n^3 < 2n^3 < 2^{n+1}.$$
6. By [[mathematical induction|0ASJVEFA9J]] from $n = 10$, the statement $2^n > n^3$ is true for every $n \ge 10$.
7. No smaller threshold works.
   A threshold $N \le 9$ would need $P(9)$, and step 2 shows that $P(9)$ is false.

## Remarks

The statement is true at $n = 0$ and $n = 1$, false from $n = 2$ to $n = 9$, and true from $n = 10$ on.
So the first values alone give a wrong picture, and the eventual behavior needs a proof.

The same method shows that $2^n > n^k$ eventually for every fixed $k$, but the threshold grows with $k$.
The step needs $(1 + 1/n)^k < 2$, and that holds only once $n$ is large compared with $k$.

## Explanations

### L1 human

The number $2^n$ doubles at each step, while $n^3$ grows more slowly once $n$ is large.
At first $n^3$ is ahead: for $n = 9$ we have $2^9 = 512$ and $9^3 = 729$.
At $n = 10$ the doubling catches up, with $1024$ against $1000$, and after that it stays ahead forever.
This is what "eventually" means: from some point on, and at every later step.

### L2 human

Find the least threshold for $2^n > n^2$ by the same method.
The small values are
$$2^2 = 4 = 2^2, \qquad 2^3 = 8 < 9 = 3^2, \qquad 2^4 = 16 = 4^2, \qquad 2^5 = 32 > 25 = 5^2.$$
So the statement is true at $n = 0$ and $n = 1$, false at $n = 2, 3, 4$, and true at $n = 5$.
For the step with $n \ge 5$:
$$(n + 1)^2 = n^2 \left( 1 + \frac{1}{n} \right)^2 \le 1.44 \, n^2 < 2n^2 < 2^{n+1}.$$
So $2^n > n^2$ for all $n \ge 5$, and $5$ is the least threshold, because the statement fails at $n = 4$.

Watch out: the equality $2^4 = 4^2$ shows that a strict inequality can fail without the reverse inequality being true.
