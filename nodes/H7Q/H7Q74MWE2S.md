---
tag: H7Q74MWE2S
kind: example
name: A finite check of Goldbach from 4 to 100
msc: ["11P32", "00A35"]
topics: [DME0TPC348]
audience: ug1
not_instance_of:
  - target: JFD3QWCX8Z
    note: the check covers every case of a finite statement, so it is a proof of that statement and not evidence for unchecked cases
uses: [JFD3QWCX8Z, 063JNBSMJ0, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Goldbach%27s_conjecture
    locator: Computational results
  - url: https://en.wikipedia.org/wiki/Proof_by_exhaustion
    locator: lead section
---

## Example

The number $98$ is a sum of two primes, $98 = 19 + 79$, and no smaller first prime works for it.
Checks like this one, done for every even number from $4$ to $100$, prove a finite statement completely.
Let $G_{100}$ be the statement "every even $n$ with $4 \le n \le 100$ is a sum of two primes".
We prove $G_{100}$ by checking all its cases, and we compare the check with [[numerical evidence|JFD3QWCX8Z]].

1. We count the cases: the even numbers from $4$ to $100$ are $\tfrac{100 - 4}{2} + 1 = 49$ numbers.
2. For each $n$ we find the least prime $p$ such that $n - p$ is also prime, and we group the numbers by that $p$:
$$\begin{array}{ll} p = 2: & 4 \\ p = 3: & 6, 8, 10, 14, 16, 20, 22, 26, 32, 34, 40, 44, 46, 50, 56, 62, 64, 70, 74, 76, 82, 86, 92, 100 \\ p = 5: & 12, 18, 24, 28, 36, 42, 48, 52, 58, 66, 72, 78, 84, 88, 94 \\ p = 7: & 30, 38, 54, 60, 68, 80, 90, 96 \\ p = 19: & 98 \end{array}$$
3. We count the groups:
$$1 + 24 + 15 + 8 + 1 = 49,$$
   so every case of step 1 appears exactly once.
4. Each case has a partition into two primes, so $G_{100}$ is proved.
   The argument is a [[proof|0B94TKFQJX]] by exhaustion, and it is complete.

The check is not numerical evidence in the sense of the concept.
Numerical evidence supports a statement about cases that were not checked, and here no case is left unchecked.

## Remarks

### The same computation in two roles

The same $49$ checks are also numerical evidence for the full [[Goldbach's conjecture|063JNBSMJ0]], which speaks about every even number from $4$ on.
So the role of a computation depends on the statement it is attached to.
For $G_{100}$ it is a proof, and for the conjecture it is only evidence, because the conjecture has infinitely many cases beyond $100$.
A pattern that holds in $49$ cases, or in $10^{18}$ cases, is not a proof of a statement with infinitely many.

### The hardest case

The case $n = 98$ is the only one up to $100$ that needs a prime as large as $19$.
Every smaller odd prime leaves a composite partner, as the L2 explanation shows.
[[Goldbach's conjecture for small even numbers|51WEX891JK]] does the same kind of check for the even numbers up to $30$.

### Watch out

A proof by exhaustion must cover every case, and step 3 is there to confirm that.
A list that skips one even number proves nothing about that number, however long the list is.

### Try it

Find two primes that add up to $68$.
The least choice is $7 + 61$, and $31 + 37$ also works.

## Explanations

### L1 human

The claim is only about the even numbers from $4$ to $100$.
There are $49$ of them, and we can check each one, for example $30 = 7 + 23$ and $98 = 19 + 79$.
After all $49$ checks, the claim is proved.
Nothing is left to guess, so this is a proof and not just evidence.
The famous Goldbach conjecture is about all even numbers, and no list of checks can finish it.

### L2 human

We check the hardest case, $n = 98$, by subtracting each odd prime in turn:
$$98 - 3 = 95 = 5 \cdot 19, \qquad 98 - 5 = 93 = 3 \cdot 31, \qquad 98 - 7 = 91 = 7 \cdot 13,$$
$$98 - 11 = 87 = 3 \cdot 29, \qquad 98 - 13 = 85 = 5 \cdot 17, \qquad 98 - 17 = 81 = 3^4.$$
All six partners are composite.
The next prime works, since $98 - 19 = 79$ and $79$ is prime.
The typical use: a statement about finitely many cases can be proved by a complete check, by hand or by computer.
Watch out: the check of $98$ proves nothing about $102$, which needs its own check.
