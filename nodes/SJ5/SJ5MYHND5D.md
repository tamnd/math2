---
tag: SJ5MYHND5D
kind: example
name: There are n consecutive composite numbers
msc: ["00A35", "11A41"]
topics: [958EF46EYJ]
audience: school
instance_of: [01XM7JEKHY]
uses: [01XM7JEKHY, 0XWG0JGDFW, 008BH74D7R, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_gap
    locator: Simple observations
  - url: https://en.wikipedia.org/wiki/Constructive_proof
    locator: lead section
---

## Example

Statement: for every positive integer $n$, there are $n$ consecutive integers that are all [[composite|008BH74D7R]].
We give a [[constructive proof|01XM7JEKHY]]: we write the $n$ numbers down.

1. Let $n \geq 1$, and let $N = (n + 1)!$, the [[factorial|0XWG0JGDFW]] $1 \cdot 2 \cdots (n + 1)$.
2. The witnesses are the $n$ consecutive integers $N + 2, N + 3, \ldots, N + (n + 1)$.
3. Take one of them, $N + k$ with $2 \leq k \leq n + 1$. The number $k$ is one of the factors of $N$, so $k \mid N$.
4. Since $k \mid N$ and $k \mid k$, it follows that $k \mid N + k$.
5. Also $1 < k < N + k$. So $N + k$ has a divisor strictly between $1$ and itself, and it is composite.
6. This holds for each $k$ from $2$ to $n + 1$, so all $n$ numbers are composite.

For $n = 4$: $N = 5! = 120$, and the numbers are $122, 123, 124, 125$.
They are divisible by $2, 3, 4, 5$ in turn.

## Remarks

The proof gives the numbers by a formula, so it is constructive.
The formula is not the smallest choice.
The first run of four consecutive composite numbers is $24, 25, 26, 27$, far below $122$.
A constructive proof only needs some witness, not the best one.

The statement says that the gaps between consecutive primes can be as large as one wishes.
It contrasts with [[Euclid's theorem|0292EPPPT0]], which says that primes never stop.

## Explanations

### L1 human

Can we find three whole numbers in a row with no prime among them?
The recipe says: take $4! = 1 \cdot 2 \cdot 3 \cdot 4 = 24$, and look at $26, 27, 28$.
$26$ is $2 \times 13$, $27$ is $3 \times 9$, and $28$ is $4 \times 7$.
The recipe works for any length: for ten numbers in a row, start from $11!$.
The proof does not just say that such numbers exist; it shows them.

### L2 human

We use the example to find two consecutive primes that differ by at least $1000$.

1. Take $n = 999$ and $N = 1000!$. The $999$ numbers $N + 2, \ldots, N + 1000$ are composite.
2. Let $p$ be the largest prime with $p \leq N + 1$. It exists, since $2 \leq N + 1$ is prime.
3. Let $q$ be the smallest prime with $q > N + 1$. It exists by Euclid's theorem.
4. Then $q > N + 1000$ by step 1, so $q - p \geq (N + 1001) - (N + 1) = 1000$.

The typical use: a constructive existence proof gives explicit bounds, here on where the large gap lies.

A trap: the argument starts at $N + 2$, not at $N + 1$.
The number $N + 1$ need not be composite; for example $2! + 1 = 3$ and $3! + 1 = 7$ are prime.
