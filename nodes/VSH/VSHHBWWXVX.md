---
tag: VSHHBWWXVX
kind: example
name: Every integer at least 2 has a prime divisor
msc: ["00A35", "11A41"]
topics: [EEH2F76CYQ]
audience: ug1
instance_of: [JGRCNPKNGG]
uses: [JGRCNPKNGG, 01BX15HSRR, 01826KMG2H, 0PG2H7WKGG]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_infinite_descent
    locator: Number theory
  - url: https://en.wikipedia.org/wiki/Minimal_counterexample
    locator: Examples
---

## Example

We prove that every integer $n \ge 2$ has a prime divisor.
A [[prime number|01826KMG2H]] is an integer $p \ge 2$ whose only positive divisors are $1$ and $p$.
So an integer $n \ge 2$ that is not prime has a divisor $a$ with $1 < a < n$.
The proof is a [[minimal counterexample|JGRCNPKNGG]] argument.

1. Suppose that the claim is false.
   Then the set $C$ of integers $n \ge 2$ with no prime divisor is not empty.
2. By the [[well-ordering principle|01BX15HSRR]], $C$ has a least element $m$.
3. The number $m$ is not prime, because a prime $m$ divides itself and so has the prime divisor $m$.
4. So $m$ has a divisor $a$ with $1 < a < m$, and $m = ab$ for an integer $b$.
5. Since $2 \le a < m$ and $m$ is the least element of $C$, the number $a$ is not in $C$.
6. So $a$ has a prime divisor $p$, and $a = pc$ for an integer $c$.
7. Then $m = ab = p(cb)$, so $p$ [[divides|0PG2H7WKGG]] $m$.
8. So $m$ has a prime divisor, and $m$ is not in $C$.
   This contradicts step 2.
9. Therefore $C$ is empty, and every integer $n \ge 2$ has a prime divisor.

For example, $91$ is not prime, because $91 = 7 \cdot 13$.
The proof passes to the smaller factor $7$, which is prime, and $7$ divides $91$.

## Remarks

Steps 5 to 8 also hide a descent.
If $m$ had no prime divisor, then the smaller number $a$ would have none either, so a counterexample would give a smaller counterexample.
The same claim has a proof by [[strong induction|0KMVFSHFGZ]] with exactly the same steps, written forward.

A small change gives more.
Let $d$ be the least divisor of $n$ with $d > 1$.
Then $d$ is prime, because a divisor of $d$ strictly between $1$ and $d$ would be a smaller divisor of $n$.
So the least divisor above $1$ is always a prime, and for $91$ it is $7$.

The hypothesis $n \ge 2$ is needed, because $1$ has no prime divisor.
The proof uses it in step 4, where a non-prime $m \ge 2$ has a divisor strictly between $1$ and $m$.
The claim is the first step of the [[fundamental theorem of arithmetic|084HH1NDCB]], and of [[Euclid's theorem|0292EPPPT0]] that there are infinitely many primes.

## Explanations

### L1 human

Take any whole number from $2$ on, for example $91$.
Either it is prime, or it splits as a product of two smaller numbers, here $7$ times $13$.
If a number had no prime divisor, then its smaller factor would have none either.
So we could go down and down, but whole numbers cannot go down forever.
Hence every number from $2$ on has a prime divisor.

### L2 human

We follow the descent for $n = 360$.
The number $360$ is not prime, because $360 = 12 \cdot 30$.
The factor $12$ is not prime either, because $12 = 4 \cdot 3$, and $4 = 2 \cdot 2$.
The chain of factors is
$$360 > 12 > 4 > 2,$$
and it stops at the prime $2$ after finitely many steps, because it is a decreasing chain of positive integers.
Divisibility passes up the chain: $2$ divides $4$, $4$ divides $12$, and $12$ divides $360$, so $2$ divides $360$.

Check: $360 = 2 \cdot 180$.
The typical use of the argument is the first step of each proof about prime factorizations.
Watch out: the factorization $m = 1 \cdot m$ gives no smaller number, so the proof must use a factor strictly between $1$ and $m$.
