---
tag: 818MZC1FYJ
kind: example
name: Every integer greater than 1 is a product of primes, by strong induction
msc: ["00A35", "11A51"]
topics: [EEH2F76CYQ]
audience: school
illustrates: [0KMVFSHFGZ]
uses: [0KMVFSHFGZ, 01826KMG2H, 02EKEPPJ3R]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: "Example: prime factorization"
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Example

Claim: every integer $n \ge 2$ is a product of one or more [[prime numbers|01826KMG2H]], where a prime $p$ by itself counts as a product of one prime.
We prove the claim by [[strong induction|0KMVFSHFGZ]] from the base $2$.

1. Let $P(n)$ be the statement "$n$ is a product of one or more primes".
   Let $n \ge 2$, and assume $P(k)$ for every integer $k$ with $2 \le k < n$.
2. Case 1: $n$ is prime.
   Then $n$ is a product of one prime, and $P(n)$ holds.
3. Case 2: $n$ is not prime.
   Since $n \ge 2$, the definition of a prime gives $n = ab$ with integers $a, b$ and $1 < a < n$.
4. Then $b = n / a$, and $1 < a < n$ gives $1 < b < n$.
   So both $a$ and $b$ lie in the range $2 \le k < n$, and the hypothesis gives $P(a)$ and $P(b)$.
5. Write $a = p_1 \cdots p_r$ and $b = q_1 \cdots q_s$ with primes $p_i$ and $q_j$.
   Then $n = p_1 \cdots p_r \, q_1 \cdots q_s$ is a product of primes, and $P(n)$ holds.
6. Cases 1 and 2 cover every $n \ge 2$, so strong induction gives $P(n)$ for every $n \ge 2$.

Here is the proof run on $n = 360$.
It is not prime, and one split is $360 = 18 \cdot 20$.
The factors split again:
$$18 = 2 \cdot 9 = 2 \cdot 3 \cdot 3, \qquad 20 = 4 \cdot 5 = 2 \cdot 2 \cdot 5.$$
So $360 = 2 \cdot 3 \cdot 3 \cdot 2 \cdot 2 \cdot 5 = 2^3 \cdot 3^2 \cdot 5$.
Check: $8 \cdot 9 \cdot 5 = 72 \cdot 5 = 360$.

## Remarks

The example shows why the strong form is needed.
The factors $a$ and $b$ can be any numbers below $n$, so the proof must be allowed to use every earlier case.
Ordinary induction would offer only $P(n - 1)$, and the factorization of $359$ says nothing about $360$.

There is no separate base case, and the case $n = 2$ is still covered.
For $n = 2$ no integer satisfies $2 \le k < 2$, so the hypothesis is empty, and the proof must work alone; it does, because $2$ is prime and Case 1 applies.

The proof gives existence only.
Uniqueness of the factorization is the second half of the [[fundamental theorem of arithmetic|084HH1NDCB]], and it needs Euclid's lemma.
The same proof works whenever a size goes down under factoring, for example for polynomials over a field, with the degree as the size.

## Explanations

### L1 human

Take a number such as $60$.
If it is prime, we are done.
If not, it splits as a product of two smaller numbers, for example $6 \times 10$.
Each smaller number is prime or splits again: $6 = 2 \times 3$ and $10 = 2 \times 5$.
The numbers get smaller each time, so the splitting stops, and only primes are left: $60 = 2 \times 3 \times 2 \times 5$.

### L2 human

The same argument reads well as a [[minimal counterexample|JGRCNPKNGG]], and the comparison shows that the two forms are one idea.
Suppose some integer $n \ge 2$ is not a product of primes.
By the [[well-ordering principle|01BX15HSRR]] there is a least such $n$.
This $n$ is not prime, so $n = ab$ with $1 < a, b < n$.
Both $a$ and $b$ are below the least failure, so both are products of primes, and then so is $n$.
That contradicts the choice of $n$, so every $n \ge 2$ is a product of primes.

Strong induction is the usual tool for a recursive split of an object into smaller pieces of unknown size.
Watch out: the factor $a$ must lie strictly between $1$ and $n$.
The split $n = 1 \cdot n$ always exists, and it gives no smaller case.
