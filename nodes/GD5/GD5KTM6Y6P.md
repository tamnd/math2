---
tag: GD5KTM6Y6P
kind: example
name: Which primes are sums of two squares
msc: ["11E25", "11A41"]
topics: [DME0TPC348]
audience: ug1
instance_of: [R2T42N5XGK]
uses: [R2T42N5XGK, 0SN0MAEKYX, 043B3ENSTY]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat%27s_theorem_on_sums_of_two_squares
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Conjecture
    locator: lead section
---

## Example

The prime $13$ is $2^2 + 3^2$, and the prime $7$ is not a sum of two squares, since $7 - 0$, $7 - 1$ and $7 - 4$ are not squares.
Which [[primes|0SN0MAEKYX]] $p$ can be written as $p = a^2 + b^2$ with integers $a$ and $b$?
We [[form a conjecture|R2T42N5XGK]] from a table, test it, and prove the half that is easy.

1. We list the primes up to $113$ that are sums of two squares:
$$\begin{gathered} 2 = 1^2 + 1^2, \quad 5 = 1^2 + 2^2, \quad 13 = 2^2 + 3^2, \quad 17 = 1^2 + 4^2, \quad 29 = 2^2 + 5^2, \\ 37 = 1^2 + 6^2, \quad 41 = 4^2 + 5^2, \quad 53 = 2^2 + 7^2, \quad 61 = 5^2 + 6^2, \quad 73 = 3^2 + 8^2, \\ 89 = 5^2 + 8^2, \quad 97 = 4^2 + 9^2, \quad 101 = 1^2 + 10^2, \quad 109 = 3^2 + 10^2, \quad 113 = 7^2 + 8^2. \end{gathered}$$
2. We list the primes up to $113$ that are not:
$$3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103, 107.$$
3. We look for a feature that separates the lists.
   The last digit fails, because $13$ is in the first list and $23$ is in the second.
   The remainder on division by $4$ works: every odd prime in step 1 leaves remainder $1$, and every prime in step 2 leaves remainder $3$.
4. We state the conjecture precisely: an odd prime $p$ is a sum of two squares if and only if $p \equiv 1 \pmod 4$.
5. We test it on primes outside the table.
   The prime $1009$ leaves remainder $1$, and $1009 = 15^2 + 28^2 = 225 + 784$.
   The prime $1019$ leaves remainder $3$, and a search finds no representation.
6. We prove one direction.
   A square is $0$ or $1$ modulo $4$, because $(2m)^2 = 4m^2$ and $(2m+1)^2 = 4(m^2 + m) + 1$.
   So a sum of two squares is $0$, $1$ or $2$ modulo $4$, and a prime $p \equiv 3 \pmod 4$ is never a sum of two squares.
7. The other direction is [[Fermat's theorem on sums of two squares|043B3ENSTY]], and its proof is harder.

## Remarks

### How the pattern was found

Step 3 tried a feature that failed, the last digit, before a feature that worked, the remainder modulo $4$.
Trying several simple features of the data, one after another, is a standard way to find a pattern.
Step 6 then explains why the remainder modulo $4$ was the right feature: squares themselves have only two remainders modulo $4$.

### What the table does and does not show

The table supports the conjecture in $29$ cases, the odd primes up to $113$, and the test adds two more.
None of these cases proves the direction "$p \equiv 1 \pmod 4$ implies $p$ is a sum of two squares" for the primes beyond the table.
A pattern that holds for every prime we checked is not a proof, so that direction needed Fermat's theorem.
Fermat stated the full result in a letter of 1640 without a proof, and Euler published the first known proof.

### Watch out

The pattern is about primes, and it does not extend to all integers.
The number $21$ leaves remainder $1$ modulo $4$, but it is not a sum of two squares, since $21 - 0$, $21 - 1$, $21 - 4$ and $21 - 16$ are not squares.
The theorem for general integers depends on the prime factors $p \equiv 3 \pmod 4$ and their exponents.

### Try it

Write $41$ and $61$ as sums of two squares.
They are $41 = 16 + 25$ and $61 = 25 + 36$.

Is $2027$ a sum of two squares?
It is not, because $2027 = 4 \cdot 506 + 3$, and step 6 excludes every number that leaves remainder $3$ modulo $4$.

## Explanations

### L1 human

Some primes are sums of two square numbers, like $13 = 4 + 9$, and some are not, like $7$.
Make two lists and look at them closely.
After you divide by $4$, the odd primes in the first list leave remainder $1$, and the primes in the second list leave remainder $3$.
That is the guess, and half of it has a two-line proof.
The other half is a famous theorem of Fermat, and a longer list would never have been enough to prove it.

### L2 human

We check by search that $1019$ is not a sum of two squares.
If $1019 = a^2 + b^2$ with $0 \le a \le b$, then $2a^2 \le 1019$, so $a^2 \le 509$ and $a \le 22$.
For $a = 0, 1, \dots, 22$ we compute
$$1019 - a^2 = 1019, 1018, 1015, 1010, \dots, 535,$$
and none of these $23$ numbers is a perfect square.
Step 6 gives the same result at once, because
$$1019 = 4 \cdot 254 + 3.$$
The typical use: a search confirms single cases, and a congruence argument explains all of them together.
Watch out: a search can only confirm the cases it reaches, while the congruence covers every case.
