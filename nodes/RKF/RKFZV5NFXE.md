---
tag: RKFZV5NFXE
kind: example
name: Goldbach partitions grow with n
msc: ["11P32", "11Y16"]
topics: [DME0TPC348]
audience: ug2
instance_of: [JFD3QWCX8Z]
uses: [JFD3QWCX8Z, 063JNBSMJ0, 110ATC90X5, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Goldbach%27s_conjecture
    locator: Heuristic justification
  - url: https://en.wikipedia.org/wiki/Goldbach%27s_comet
    locator: lead section
---

## Example

The number $100$ is a sum of two primes in $6$ ways, from $3 + 97$ to $47 + 53$, and the number $1000000$ is a sum of two primes in $5402$ ways.
[[Goldbach's conjecture|063JNBSMJ0]] asks only for one way, so these counts carry more information than the conjecture needs.
Let $g(n)$ be the number of ways to write an even number $n$ as $n = p + q$ with [[primes|0SN0MAEKYX]] $p \le q$.
The conjecture says that $g(n) \ge 1$ for every even $n \ge 4$.
We look at the size of $g(n)$, which gives stronger [[numerical evidence|JFD3QWCX8Z]] than the bare statement.

1. A sieve of the primes up to $10^6$ gives these counts:

| $n$ | $10$ | $10^2$ | $10^3$ | $10^4$ | $10^5$ | $10^6$ |
|---|---|---|---|---|---|---|
| $g(n)$ | $2$ | $6$ | $28$ | $127$ | $810$ | $5402$ |

2. The counts grow roughly like $n/(\ln n)^2$.
   A failure at a large $n$ would need $g(n)$ to drop from thousands of partitions to none.
3. The heuristic of Hardy and Littlewood predicts
$$g(n) \approx C_2 \prod_{p \mid n, \ p > 2} \frac{p-1}{p-2} \int_2^{n-2} \frac{dt}{\ln t \, \ln(n-t)}, \qquad C_2 = 0.6601618\ldots$$
4. We test the prediction.
   For $n = 10^5$ the only odd prime factor is $5$, the product is $\tfrac43$, and the prediction is about $810.3$, against $g(n) = 810$.
   For $n = 10^6$ the prediction is about $5417$, against $g(n) = 5402$.
5. We test how the prediction depends on the factors of $n$.
   The neighbor $999998 = 2 \cdot 31 \cdot 127^2$ has the product $\tfrac{30}{29} \cdot \tfrac{126}{125} \approx 1.043$, smaller than $\tfrac43$.
   The prediction drops to about $4237$, and indeed $g(999998) = 4206$.
6. Steps 4 and 5 test a quantitative prediction, including its dependence on the prime factors of $n$.
   That is evidence of a different kind from "the next case works".

## Remarks

### What the agreement shows and what it does not

The prediction of step 3 is itself a [[heuristic argument|VCQQNJ3SEZ]], not a theorem.
So the agreement in steps 4 and 5 supports both the heuristic and the conjecture, and it proves neither.
Goldbach's conjecture has been checked for all even $n$ up to $4 \cdot 10^{18}$, and it is still open.
A pattern that holds for every case computed, even with the right sizes, is not a proof.

### The comet

The plot of $g(n)$ against $n$ is [[Goldbach's comet|110ATC90X5]].
Its separate bands come from the factor $\prod (p-1)/(p-2)$ of step 3.
For example, multiples of $3$ get the extra factor $2$, so they lie on a band about twice as high as their neighbors.

### Watch out

The agreement is with a heuristic formula, so it does not rule out rare exceptions that the formula ignores.
At small $n$ the agreement is rough: for $n = 10^4$ the prediction is about $134.8$, against $g(n) = 127$.

### Try it

Is $g(102)$ likely to be larger or smaller than $g(100)$?
Larger, because $102 = 2 \cdot 3 \cdot 17$ has the factor $3$, which doubles the product; in fact $g(102) = 8$ while $g(100) = 6$.

## Explanations

### L1 human

Every even number we try can be written as a sum of two primes.
More than that, large even numbers can be written so in thousands of ways.
For example, $1000000$ has $5402$ such ways.
It would be very strange if, far out, the number of ways suddenly dropped to zero.
That is why mathematicians believe the conjecture, but a belief backed by many cases is still not a proof.

### L2 human

We count $g(100)$ by hand.
For each prime $p \le 50$ we test whether $100 - p$ is prime.
Six primes work:
$$100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53.$$
The other primes up to $50$ give composite partners, for example $100 - 7 = 93 = 3 \cdot 31$ and $100 - 13 = 87 = 3 \cdot 29$.
So $g(100) = 6$.
The typical use: counting all partitions, not only finding one, tests the conjecture against a precise prediction.
Watch out: the hand count is easy to get wrong by one, so check that the partner of each prime is prime and that no pair is counted twice.
