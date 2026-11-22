---
tag: 6EHQD2M1PS
kind: example
name: A brute force check of the values of n^2 + n + 41
msc: ["00A35", "11A41"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [STHWD1K9AN]
uses: [01826KMG2H, 0ED72CTBNP, STHWD1K9AN]
sources:
  - url: https://en.wikipedia.org/wiki/Lucky_numbers_of_Euler
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof techniques
---

## Example

Let $f(n) = n^2 + n + 41$.
We prove by [[brute force|STHWD1K9AN]] that $f(n)$ is [[prime|01826KMG2H]] for $n = 0, 1, \dots, 39$, and we find where the pattern stops.

1. We compute the $40$ values.
   They begin $41, 43, 47, 53, 61, 71$, and they end with
   $$f(39) = 1521 + 39 + 41 = 1601.$$
2. We fix the test for one value.
   A number $m \ge 2$ is prime if no prime $p \le \sqrt{m}$ divides it.
   Since $40^2 = 1600$ and $41^2 = 1681$, every value is below $41^2$, so it is enough to test the primes up to $37$.
3. We run the test on all $40$ values.
   No test finds a divisor, so $f(n)$ is prime for $0 \le n \le 39$.
4. At $n = 40$ the pattern breaks:
   $$f(40) = 40^2 + 40 + 41 = 40 \cdot 41 + 41 = 41^2 = 1681.$$
5. At $n = 41$ it breaks again:
   $$f(41) = 41^2 + 41 + 41 = 41 \cdot 43 = 1763.$$

So the claim "$f(n)$ is prime for every $n \ge 0$" is false, and $n = 40$ is the least [[counterexample|0ED72CTBNP]].

## Remarks

Steps 1 to 3 are a complete proof of a finite statement, but they give no reason why the values are prime.
Steps 4 and 5 are not brute force: they use the factor $41$ that the formula itself contains.

A brute force check of finitely many cases never proves a statement about all $n$.
The forty passing cases are evidence for the larger claim, and the larger claim is false.

The explanation of the forty primes is a deep fact.
The discriminant of $n^2 + n + 41$ is $1 - 4 \cdot 41 = -163$, and the long run of primes is tied to arithmetic properties of the number $163$ in the theory of quadratic fields.
If you change $41$ to $17$, the same check works for $n = 0, \dots, 15$ and fails at $n = 16$, where $f(16) = 16 \cdot 17 + 17 = 17^2 = 289$.

## Explanations

### L1 human

Euler noticed that $n^2 + n + 41$ gives a prime for $n = 0, 1, 2, \dots$ for a long time.
The values are $41, 43, 47, 53, 61, \dots$.
To check this, we compute each value and test it for divisors.
This is brute force: we check case after case, without a general idea.
At $n = 40$ the value is $1681 = 41 \cdot 41$, so the pattern breaks.

### L2 human

A brute force proof has a fixed shape: a finite list of cases, a test for one case, and a report that every case passes.
Here the list is $n = 0, 1, \dots, 39$, and the test is trial division by the primes up to $37$.
Check one case by hand, $n = 10$:
$$f(10) = 100 + 10 + 41 = 151,$$
and $151$ is not divisible by $2, 3, 5, 7$ or $11$, while $13^2 = 169 > 151$, so $151$ is prime.
The method fits finite statements, often with a computer, when no general argument is known.
It proves only the cases it tests, so a pattern in forty cases says nothing certain about the forty-first.
