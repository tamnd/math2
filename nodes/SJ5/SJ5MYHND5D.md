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
We give a [[constructive proof|01XM7JEKHY]]: we write the $n$ numbers down and check each one.

1. Let $n \ge 1$, and let $N = (n + 1)!$, the [[factorial|0XWG0JGDFW]] $1 \cdot 2 \cdots (n + 1)$.
2. The witnesses are the $n$ consecutive integers $N + 2, N + 3, \dots, N + (n + 1)$.
3. Take one of them, $N + k$ with $2 \le k \le n + 1$.
   The number $k$ is one of the factors in the product $N$, so $k \mid N$.
4. Since $k \mid N$ and $k \mid k$, the number $k$ [[divides|096PW7Q014]] the sum $N + k$.
5. Also $1 < k < N + k$, because $k \ge 2$ and $N \ge 2$.
   So $N + k$ has a divisor strictly between $1$ and itself, and it is composite.
6. Step 5 holds for each $k$ from $2$ to $n + 1$, so all $n$ numbers are composite.

For $n = 4$ we get $N = 5! = 120$ and the four numbers
$$122 = 2 \cdot 61, \quad 123 = 3 \cdot 41, \quad 124 = 4 \cdot 31, \quad 125 = 5 \cdot 25.$$
Check: each factorization multiplies out, and the divisors are $2, 3, 4, 5$ in turn, as step 3 predicts.

## Remarks

The proof gives the numbers by a formula, so it is constructive, and anyone can compute the run for any $n$.
The formula is not the smallest choice.
The first run of four consecutive composite numbers is $24, 25, 26, 27$, far below $122$.
A constructive proof needs some witness, not the best one.

The result says that the gaps between consecutive primes can be as large as you like.
It does not contradict [[Euclid's theorem|0292EPPPT0]], which says that the primes never stop: they keep coming, but they can be far apart.

Why start at $N + 2$ and not at $N + 1$?
The divisor of $N + k$ in step 3 is $k$, and for $k = 1$ that divisor is $1$, which proves nothing.
In fact $N + 1$ can be prime: $2! + 1 = 3$ and $3! + 1 = 7$ are prime.

## Explanations

### L1 human

Can we find three whole numbers in a row with no prime among them?
The recipe says: take $4! = 1 \cdot 2 \cdot 3 \cdot 4 = 24$, and look at $26, 27, 28$.
$26$ is $2 \times 13$, $27$ is $3 \times 9$, and $28$ is $4 \times 7$.
The recipe works for any length: for ten numbers in a row, start from $11!$.
The proof does not just say that such numbers exist; it shows them.

### L2 human

We use the example to show that some two consecutive primes differ by at least $1000$.

1. Take $n = 999$ and $N = 1000!$.
   By the example, the $999$ numbers $N + 2, \dots, N + 1000$ are composite.
2. Let $p$ be the largest prime with $p \le N + 1$.
   It exists, because $2$ is a prime and $2 \le N + 1$.
3. Let $q$ be the smallest prime with $q > N + 1$.
   It exists by Euclid's theorem.
4. No prime lies strictly between $p$ and $q$, so they are consecutive primes.
5. By step 1, $q$ is not among $N + 2, \dots, N + 1000$, so $q \ge N + 1001$.
   Then
   $$q - p \ge (N + 1001) - (N + 1) = 1000.$$

The typical use of a constructive existence proof is visible here: it gives explicit bounds, in this case a place below $1000! + 1001$ where a gap of at least $1000$ must occur.
