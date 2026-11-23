---
tag: 8G1BXJ7ZJM
kind: example
name: Products of consecutive integers by the integrality of binomial coefficients
msc: ["00A35", "11A05"]
topics: [X1NSTVGDNQ]
audience: ug1
instance_of: [FVRKDXBJF6]
uses: [FVRKDXBJF6, 0GBZM0MT0F, 0YRG241HQQ]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_coefficient
    locator: lead section
---

## Example

We prove that $n(n + 1)(n + 2)(n + 3)$ is divisible by $24$ for every positive integer $n$.
Following the [[inventor's paradox|FVRKDXBJF6]], we prove a more ambitious statement and specialize.

1. We look at the direct attempt.
   Among four consecutive integers one is divisible by $4$, another is even, and one is divisible by $3$, so $4 \cdot 2 \cdot 3 = 24$ divides the product.
   The argument works, but it uses the factorization $24 = 2^3 \cdot 3$ and must be redone for each length.
2. We state the general claim.
   For all positive integers $n$ and $k$, the product of the $k$ consecutive integers $n, n + 1, \ldots, n + k - 1$ is divisible by $k!$, and for $k = 4$ we have $k! = 24$.
3. We rewrite the quotient as a [[binomial coefficient|0GBZM0MT0F]]:
   $$\frac{n(n + 1) \cdots (n + k - 1)}{k!} = \frac{(n + k - 1)!}{k! \, (n - 1)!} = \binom{n + k - 1}{k}.$$
4. So the general claim says that binomial coefficients are integers.
5. We prove that.
   Define $\binom{m}{j}$ by the factorial formula for $0 \le j \le m$.
   By [[Pascal's rule|0YRG241HQQ]], $\binom{m}{j} = \binom{m - 1}{j - 1} + \binom{m - 1}{j}$ for $0 < j < m$, and $\binom{m}{0} = \binom{m}{m} = 1$, so induction on $m$ shows that every $\binom{m}{j}$ is an integer.
6. We specialize to $k = 4$:
   $$n(n + 1)(n + 2)(n + 3) = 24 \binom{n + 3}{4},$$
   so $24$ divides the product.
7. We test: $n = 1$ gives $24 = 24 \cdot 1$, and $n = 2$ gives $120 = 24 \cdot 5$, with $\binom{5}{4} = 5$.

## Remarks

The general claim is stronger, since it covers every $k$ and the case $k = 4$ is one of infinitely many.
Its proof is still easier than a separate proof for each $k$, because binomial coefficients obey Pascal's rule, while a direct proof needs the prime factorization of $k!$.
The general claim also says what the quotient is: the number of ways to choose $k$ objects from $n + k - 1$.

The direct argument of step 1 is correct and short for $k = 4$.
For $k = 10$ it would need to count the factors $2$, $3$, $5$ and $7$ in
$$10! = 2^8 \cdot 3^4 \cdot 5^2 \cdot 7,$$
and the general argument needs no change.

## Explanations

### L1 human

Multiply four numbers in a row, like $5 \cdot 6 \cdot 7 \cdot 8 = 1680$.
The result always divides by $24 = 1 \cdot 2 \cdot 3 \cdot 4$, and here $1680 = 24 \cdot 70$.
The reason is that $\frac{5 \cdot 6 \cdot 7 \cdot 8}{1 \cdot 2 \cdot 3 \cdot 4}$ counts the ways to choose $4$ things out of $8$, and a count is a whole number.
The same reason works for any number of factors in a row, which is easier than checking each length.

### L2 human

We use the general claim for a new case: $720$ divides $n(n + 1)(n + 2)(n + 3)(n + 4)(n + 5)$ for every positive integer $n$.
The product has $k = 6$ consecutive factors, and $6! = 720$, so the quotient is $\binom{n + 5}{6}$, an integer.
Test with $n = 1$: the product is $720$ and $\binom{6}{6} = 1$.
Test with $n = 2$: the product is $5040 = 720 \cdot 7$, and $\binom{7}{6} = 7$.

This is the typical use: one general argument replaces a separate count of prime factors for each $k$.
Watch out: the claim is about consecutive integers, and the product $1 \cdot 3 \cdot 5 \cdot 7 = 105$ of four consecutive odd numbers is not divisible by $24$.
