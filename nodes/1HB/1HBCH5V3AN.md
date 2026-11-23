---
tag: 1HBCH5V3AN
kind: example
name: The primes 31, 331, 3331 and their end
msc: ["11A41", "00A08"]
topics: [DME0TPC348]
audience: ug1
instance_of: [8AFXPXCE3N]
uses: [8AFXPXCE3N, 0SN0MAEKYX, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Strong_law_of_small_numbers
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Formula_for_primes
    locator: lead section
---

## Example

Check that $31$, $331$ and $3331$ are [[prime|0SN0MAEKYX]].
For $331$, trial division by $2, 3, 5, 7, 11, 13, 17$ leaves a remainder each time, and $19^2 = 361 > 331$, so $331$ is prime.
Write a $3$ in front again and again, and ask whether the result stays prime.

Let $a_m = 33\ldots31$ be the number with $m - 1$ digits $3$ followed by a digit $1$, so $a_m = (10^m - 7)/3$.

1. The data.
   The numbers $a_2 = 31$, $a_3 = 331$, $a_4 = 3331$, $a_5 = 33331$, $a_6 = 333331$, $a_7 = 3333331$ and $a_8 = 33333331$ are all prime.
2. The guess.
   Seven primes in a row suggest the conjecture "every $a_m$ with $m \geq 2$ is prime".
3. The failure.
   The next number factors: $a_9 = 333333331 = 17 \cdot 19607843$.
4. More failures.
   Also $a_{10} = 3333333331 = 673 \cdot 4952947$ and $a_{11} = 33333333331 = 307 \cdot 108577633$.

So the conjecture of step 2 is false, and $m = 9$ is a [[counterexample|0ED72CTBNP]].
The seven primes were evidence of a weak kind, and they were not a proof, as the [[strong law of small numbers|8AFXPXCE3N]] warns.

## Remarks

### Why the run is long

The run of primes has a reason, and the reason is not a law that makes every $a_m$ prime.
No $a_m$ is divisible by $2$ or $5$, because it ends in $1$.
No $a_m$ is divisible by $3$, because its digit sum $3(m-1) + 1$ is not.
A prime $p \geq 7$ divides $a_m$ exactly when $10^m \equiv 7 \pmod p$, because $3$ is invertible modulo $p$.
For $p = 7$ this is impossible, since $7$ does not divide $10^m$.
The powers of $10$ modulo $11$ are $10, 1, 10, 1, \ldots$, and modulo $13$ they are $10, 9, 12, 3, 4, 1$ and then repeat, so neither list contains $7$.
So the smallest prime that can divide some $a_m$ is $17$.
Numbers without small factors are prime more often than numbers of the same size chosen at random, and that explains the long run.

### Watch out

A long run of primes does not show that the terms are always prime.
It often shows only that small primes cannot divide them, and a larger prime eventually does.

### Try it

Find the first $m$ with $17 \mid a_m$.
The powers of $10$ modulo $17$ are
$$10, \ 15, \ 14, \ 4, \ 6, \ 9, \ 5, \ 16, \ 7$$
for $m = 1, \ldots, 9$, so the first one equal to $7$ is $10^9$, and $17$ divides $a_9$.
They repeat with period $16$, so $17$ also divides $a_{25}$, $a_{41}$ and so on, and infinitely many $a_m$ are not prime.

## Explanations

### L1 human

The numbers $31$, $331$, $3331$, $33331$, $333331$, $3333331$ and $33333331$ are all prime.
It is tempting to believe that adding another $3$ in front always gives a prime.
But $333333331$ is $17 \times 19607843$, so the pattern breaks.
Seven good cases were a coincidence helped by the absence of small factors, not a rule.

### L2 human

We check the factorization of $a_9$ by multiplying.
First $19607843 \cdot 10 = 196078430$ and $19607843 \cdot 7 = 137254901$.
Their sum is $196078430 + 137254901 = 333333331$, so $17 \cdot 19607843 = a_9$.
The typical use: to explain a run of primes, find the primes that can never divide the terms, and then the first prime that can.
