---
tag: FTCN4TA67H
kind: example
name: Almost all primes are odd
msc: ["00A35", "11A41"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [N1XSAXCQY3]
uses: [N1XSAXCQY3, 01826KMG2H, 0292EPPPT0, 0PG2H7WKGG]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_all
    locator: Meaning in number theory
---

## Example

Let $\mathbb{P}$ be the set of [[prime numbers|01826KMG2H]].
We show that almost all primes are odd, in the cofinite sense of [[almost all|N1XSAXCQY3]]: the set of primes that are not odd is finite.

1. Let $p$ be a prime that is not odd.
   Then $p$ is even, so $2$ [[divides|0PG2H7WKGG]] $p$.
2. A prime has exactly two positive divisors, $1$ and itself.
   Since $2$ is a positive divisor of $p$ and $2 \neq 1$, we get $2 = p$.
3. The number $2$ is prime and even, so the set of exceptions is exactly $\{2\}$.
4. The set $\{2\}$ has one element, so it is finite.
5. The set $\mathbb{P}$ is infinite, by [[Euclid's theorem|0292EPPPT0]].
   So the claim is about an infinite set, where "all but finitely many" has content.
6. Therefore all primes except finitely many are odd, which is the claim.

## Remarks

The example shows the simplest sense of "almost all": all but finitely many.
A finite set of exceptions in an infinite set also has density zero, so the claim holds in the density sense among the primes as well.

Step 5 matters.
On a finite set every property holds for all but finitely many elements, so the cofinite sense says nothing there.

Change the property and watch the answer change.
"Almost all primes are at least $1000$" is still true in the cofinite sense, with the $168$ primes below $1000$ as the exceptions.
"Almost all primes have the form $4k + 1$" is false, because the primes of the form $4k + 3$, such as $3, 7, 11, 19$, are infinite by [[Dirichlet's theorem on arithmetic progressions|0GNVN3CA2P]].

## Explanations

### L1 human

The prime numbers are $2, 3, 5, 7, 11, 13, \ldots$, and only the first one is even.
Every other even number has $2$ as a factor, so it is not prime.
So the list of primes contains exactly one even number and infinitely many odd ones.
Mathematicians say that almost all primes are odd: you can count the exceptions on one finger.

### L2 human

Here is the fact at work in a short problem: which primes $p$ and $q$ have an odd sum $p + q$?
If both were odd, the sum would be even.
So one of them is even, and by steps 1 to 3 that one equals $2$.
For example, $p + q = 15$ forces $\{p, q\} = \{2, 13\}$.
The sum $p + q = 27$ has no solution, because $27 - 2 = 25 = 5^2$ is not prime.

The typical use of the fact is the phrase "let $p$ be an odd prime", which sets the single exception aside at the start of a proof.
Watch out: "almost all primes are odd" is not a reason to ignore $p = 2$ in a proof about all primes, and the case $p = 2$ must be checked on its own.
