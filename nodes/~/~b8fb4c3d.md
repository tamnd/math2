---
tag: ~b8fb4c3d
kind: example
name: A brute force check of the values of n^2 + n + 41
msc: ["00A35", "11A41"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [~1ac18cfd]
uses: [01826KMG2H, 0ED72CTBNP, ~1ac18cfd]
sources:
  - url: https://en.wikipedia.org/wiki/Lucky_numbers_of_Euler
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof techniques
---

## Example

Let $f(n) = n^2 + n + 41$.
We prove by [[brute force|~1ac18cfd]] that $f(n)$ is [[prime|01826KMG2H]] for $n = 0, 1, \dots, 39$, and we find where this stops.

1. Compute the $40$ values. They begin $41, 43, 47, 53, 61, 71$, and they end with $f(39) = 1601$.
2. Test each value for primality. A number $m$ is prime if no prime $p \le \sqrt{m}$ divides it, and $\sqrt{1601} < 41$, so it is enough to test the primes up to $37$.
3. Every one of the $40$ tests finds no divisor. So $f(n)$ is prime for $0 \le n \le 39$.
4. At $n = 40$, $f(40) = 40^2 + 40 + 41 = 40 \cdot 41 + 41 = 41^2 = 1681$, which is not prime.
5. At $n = 41$, $f(41) = 41^2 + 41 + 41 = 41 \cdot 43 = 1763$, which is not prime.

So the claim "$f(n)$ is prime for every $n \ge 0$" is false, and $n = 40$ is the least [[counterexample|0ED72CTBNP]].

## Remarks

Steps 1 to 3 are a complete proof of a finite statement, but they give no reason why the values are prime.
Steps 4 and 5 are not brute force: they use the factor $41$ that appears in the formula.
A brute force check of finitely many cases never proves a statement about all $n$; the example shows that $40$ correct cases can precede a failure.
The discriminant of $n^2 + n + 41$ is $1 - 4 \cdot 41 = -163$, and the explanation of the $40$ primes is a deep fact about the number $163$.

## Explanations

### L1 human

Euler noticed that $n^2 + n + 41$ gives a prime for $n = 0, 1, 2, \dots$ for a long time.
The values are $41, 43, 47, 53, 61, \dots$.
To check this, we compute each value and test it for divisors.
This is brute force: we check case after case, without a general idea.
At $n = 40$ the value is $1681 = 41 \cdot 41$, so the pattern breaks.

### L2 human

A brute force proof has a fixed shape.

1. State the finite list of cases: here $n = 0, 1, \dots, 39$.
2. Give the test for one case: here, trial division by the primes up to $37$.
3. Report that every case passes.

The typical use is for finite statements, often with a computer, when no general argument is known.
A trap: the check proves only the cases that it tests, so a pattern in $40$ cases is evidence, not a proof, for the other cases.
