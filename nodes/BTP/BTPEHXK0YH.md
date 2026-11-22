---
tag: BTPEHXK0YH
kind: example
name: Being prime holds frequently but not eventually
msc: ["00A35", "11A41"]
topics: [Z2WNQ1DNTX]
audience: ug1
not_instance_of:
  - target: FEQ7WATMHF
    note: Primality holds for infinitely many n, but it fails for arbitrarily large n, so it does not hold for all sufficiently large n.
uses: [FEQ7WATMHF, 01826KMG2H, 0292EPPPT0, 0XWG0JGDFW]
sources:
  - url: https://en.wikipedia.org/wiki/Eventually_(mathematics)
    locator: lead section
---

## Example

Let $P(n)$ be the statement "$n$ is a [[prime number|01826KMG2H]]".
We show that $P(n)$ holds frequently, but that it does not hold [[for all sufficiently large|FEQ7WATMHF]] $n$.

1. By [[Euclid's theorem|0292EPPPT0]], there are infinitely many primes.
2. Let $N$ be given.
   Only finitely many natural numbers are less than $N$, so some prime $p$ satisfies $p \ge N$.
   So $P(n)$ holds frequently.
3. Suppose that $P(n)$ holds eventually, with some threshold $N$.
4. Put $n = 2N + 4$.
   Then $n \ge N$, and $n$ is even with $n \ge 4$, so $2$ divides $n$ and $2 < n$.
   Therefore $n$ is not prime.
5. This contradicts step 3, so $P(n)$ does not hold eventually.
6. In the language of negation, step 4 shows that "$n$ is not prime" holds frequently, which is the same as "$P(n)$ does not hold eventually".

## Remarks

The example separates the two words.
"Frequently" needs the good cases to go on forever, and "eventually" needs the bad cases to stop.
The primes go on forever, and the non-primes never stop.

The gaps between primes even grow without bound.
For $m \ge 2$, the $m - 1$ numbers $m! + 2, m! + 3, \ldots, m! + m$ are all composite, because $k$ divides $m! + k$ for $2 \le k \le m$; here $m!$ is the [[factorial|0XWG0JGDFW]] of $m$.
For $m = 4$ this gives $26$, $27$ and $28$, which are divisible by $2$, $3$ and $4$.
So both "prime" and "not prime" hold frequently, and neither holds eventually.

## Explanations

### L1 human

The primes never stop: there is always another prime further along the number line.
So "being prime" happens again and again, which is what "frequently" means.
But the primes do not take over from some point on.
After any point there are still even numbers such as $100$, $1000$ and $10000$, and they are not prime.
So "being prime" does not happen "eventually".

### L2 human

Take the threshold $N = 100$ and find both kinds of number past it.
The number $101$ is prime: it is not divisible by $2$, $3$, $5$ or $7$, and
$$11^2 = 121 > 101,$$
so no larger prime factor needs testing.
The number $2 \cdot 100 + 4 = 204$ is even, so it is not prime.
Both kinds appear after $100$, and steps 2 and 4 show the same after every threshold.

Watch out: "infinitely many $n$ have property $P$" does not give "all large $n$ have property $P$".
