---
tag: ~f5eefa58
kind: example
name: Every integer at least 2 has a prime divisor
msc: ["00A35", "11A41"]
topics: [EEH2F76CYQ]
audience: ug1
instance_of: [~f8c099da]
uses: [~f8c099da, 01BX15HSRR, 01826KMG2H, 0PG2H7WKGG]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_infinite_descent
    locator: Number theory
  - url: https://en.wikipedia.org/wiki/Minimal_counterexample
    locator: Examples
---

## Example

Claim: every integer $n \ge 2$ has a prime divisor.
A [[prime number|01826KMG2H]] is an integer $p \ge 2$ whose only positive divisors are $1$ and $p$.
An integer $n \ge 2$ that is not prime has a divisor $a$ with $1 < a < n$.
We prove the claim with a [[minimal counterexample|~f8c099da]].

1. Suppose that the claim is false. Then the set $C$ of integers $n \ge 2$ with no prime divisor is not empty.
2. By the [[well-ordering principle|01BX15HSRR]], $C$ has a least element $m$.
3. The number $m$ is not prime: a prime $m$ divides itself, so it would have the prime divisor $m$.
4. So $m$ has a divisor $a$ with $1 < a < m$. Write $m = a b$ with an integer $b$.
5. Since $2 \le a < m$ and $m$ is the least element of $C$, the number $a$ is not in $C$.
6. So $a$ has a prime divisor $p$. Then $a = p c$ for an integer $c$.
7. Then $m = a b = p (c b)$, so $p$ [[divides|0PG2H7WKGG]] $m$.
8. So $m$ has a prime divisor, and $m$ is not in $C$. This contradicts step 2.
9. Therefore $C$ is empty, and every integer $n \ge 2$ has a prime divisor.

For example, take $n = 91$.
It is not prime, because $91 = 7 \cdot 13$.
The smaller factor $7$ is prime, and it divides $91$.

## Remarks

1. Steps 5 to 8 show the descent form of the argument: if $m$ has no prime divisor, then the smaller number $a$ has no prime divisor either. So a counterexample gives a smaller counterexample.
2. The same argument with the least divisor gives more: the least divisor $d > 1$ of $n$ is prime, because a divisor of $d$ between $1$ and $d$ would be a smaller divisor of $n$.
3. The claim is the first step of the [[fundamental theorem of arithmetic|084HH1NDCB]], and of [[Euclid's theorem|0292EPPPT0]] that there are infinitely many primes.
4. The claim fails if we drop the condition $n \ge 2$: the integer $1$ has no prime divisor. In the proof, the condition is used in step 4, where a non-prime $m \ge 2$ has a divisor strictly between $1$ and $m$.

## Explanations

### L1 human

Take any whole number from $2$ on, for example $91$.
Either it is prime, or it splits as a product of two smaller numbers, here $7$ times $13$.
If a number had no prime divisor, then its smaller factor would also have none.
So we could go down and down, but whole numbers cannot go down forever.
Hence every number from $2$ on has a prime divisor.

### L2 human

We follow the descent for the number $n = 360$.

1. $360$ is not prime, because $360 = 2 \cdot 180$.
2. Its smallest divisor greater than $1$ is $2$, and $2$ is prime.
3. A longer chain also works: $360 = 12 \cdot 30$, then $12 = 4 \cdot 3$, then $4 = 2 \cdot 2$.
4. The chain $360 > 12 > 4 > 2$ is decreasing, so it stops after finitely many steps, at the prime $2$.
5. The prime $2$ divides $4$, $4$ divides $12$ and $12$ divides $360$, so $2$ divides $360$.

The typical use of this argument is the first step of each proof about prime factorizations.
A trap is to forget that a non-prime number $m \ge 2$ must be written with a factor strictly between $1$ and $m$; the factorization $m = 1 \cdot m$ gives no smaller number.
