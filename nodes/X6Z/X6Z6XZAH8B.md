---
tag: X6Z6XZAH8B
kind: example
name: The congruence p^2 = 1 mod 24 for primes p > 3, written for two readers
msc: ["00A35", "11A07"]
topics: [STSM6PR7TX]
audience: ug2
instance_of: [VYGBV5D8Y4]
uses: [VYGBV5D8Y4, 01826KMG2H, 0WAY5WX8NY, 051VYKA1EX]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: lead section
---

## Example

The statement is that for every [[prime|01826KMG2H]] $p > 3$, we have $p^2 \equiv 1 \pmod{24}$.
Here $x \equiv y \pmod n$ means that $n$ divides $x - y$, as in [[congruence modulo n|0WAY5WX8NY]].
First, a proof for a reader who knows elementary number theory:

> Since $p > 3$ is prime, $p$ is coprime to $6$.
> Every odd square is $1$ modulo $8$, and every square of an integer prime to $3$ is $1$ modulo $3$, so $p^2 \equiv 1 \pmod{24}$.
> $\square$

Second, a proof of the same idea for a first-year reader:

> (1) The only even prime is $2$ and $p > 3$, so $2 \nmid p$, and for the same reason $3 \nmid p$.
> (2) Since $p$ is odd, $p = 2k + 1$ for an integer $k$, and $p^2 - 1 = 4k^2 + 4k = 4k(k + 1)$.
> (3) One of the consecutive integers $k$ and $k + 1$ is even, so $k(k + 1) = 2j$ for an integer $j$, and $p^2 - 1 = 8j$.
> (4) Since $3 \nmid p$, division by $3$ gives $p = 3m + 1$ or $p = 3m + 2$ for an integer $m$.
> (5) In the first case $p - 1 = 3m$, and in the second $p + 1 = 3(m + 1)$, so $3$ divides $(p - 1)(p + 1) = p^2 - 1$ either way.
> (6) So $3 \mid 8j$, and since $3$ is prime and $3 \nmid 8$, [[Euclid's lemma|051VYKA1EX]] gives $3 \mid j$.
> (7) Writing $j = 3i$, we get $p^2 - 1 = 24i$, hence $p^2 \equiv 1 \pmod{24}$.
> $\square$

Both texts are complete proofs for their readers.
The short text leaves out steps (2) and (3), because "every odd square is $1$ modulo $8$" is a known fact to a number theorist.
It leaves out steps (4) and (5), because a square prime to $3$ is $1$ modulo $3$, as $1^2 = 1$ and $2^2 = 4 \equiv 1 \pmod 3$ show.
It leaves out steps (6) and (7), because combining "modulo $8$" and "modulo $3$" into "modulo $24$" uses only that $8$ and $3$ are coprime.
Each omitted step is true and needs no new idea, so the short text has no gap for its reader.
For a first-year reader the fact about odd squares is new, so the short text would have a gap, and the long text fills it.

Check: $5^2 - 1 = 24$, $7^2 - 1 = 48 = 24 \cdot 2$, $11^2 - 1 = 120 = 24 \cdot 5$ and $13^2 - 1 = 168 = 24 \cdot 7$.

## Remarks

The [[level of detail|VYGBV5D8Y4]] depends on the reader, not on the statement: both texts prove the same statement with the same idea.

The condition $p > 3$ is needed, since $2^2 - 1 = 3$ and $3^2 - 1 = 8$ are not divisible by $24$.
Step (1) uses the condition, and the short text uses it in the words "coprime to $6$".
In fact the proof uses only that $p$ is coprime to $6$, so the statement holds for every integer $n$ with $\gcd(n, 6) = 1$, for example $25^2 - 1 = 624 = 24 \cdot 26$.

A middle version for a second-year reader could keep steps (2), (3) and (5) and replace steps (6) and (7) by "since $\gcd(8, 3) = 1$".

## Explanations

### L1 human

The statement says that the square of a prime larger than $3$ is one more than a multiple of $24$.
For example, $7 \times 7 = 49 = 48 + 1$, and $48 = 2 \times 24$.
An expert can prove this in two lines, because the expert already knows two small facts.
A beginner needs those two facts proved as well.
So the same proof is written once short and once long, and both are correct for their readers.

### L2 human

We follow the long proof for $p = 13$.
Step (1) holds, since $13$ is odd and not divisible by $3$.
Step (2) gives $k = 6$ and $168 = 4 \cdot 6 \cdot 7$, and step (3) gives $6 \cdot 7 = 2 \cdot 21$, so $j = 21$ and $168 = 8 \cdot 21$.
Step (4) gives $13 = 3 \cdot 4 + 1$, and step (5) gives $p - 1 = 12$, so $3 \mid 168$.
Steps (6) and (7) give $3 \mid 21$, $i = 7$ and $168 = 24 \cdot 7$.

A textbook can give the short proof in the text and the long proof as an exercise.
Watch out: the short proof does not skip the hard part.
It skips only facts that its intended reader has proved before, and a reader who has not must prove them first.
