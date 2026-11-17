---
tag: ZHMHBFQ2E4
kind: example
name: Taking the converse of Fermat's little theorem as true
msc: ["00A35", "11A51"]
topics: [X1NSTVGDNQ]
audience: ug1
not_instance_of:
  - target: KT5SASGTQ5
    note: the converse is a variation that raises a new question, but accepting it without proof is not a use of the heuristic, and the converse is false, since 2^340 ≡ 1 mod 341 with 341 = 11 · 31
uses: [KT5SASGTQ5, 0M25PRN3WQ, 0RVYE75E2M, 0W93FJAC8F, 060ZX7C32T]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat_pseudoprime
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Carmichael_number
    locator: lead section
---

## Example

[[Fermat's little theorem|0M25PRN3WQ]] says: if $p$ is prime and $p \nmid a$, then $a^{p-1} \equiv 1 \pmod p$.
A natural variation of a theorem is its [[converse|0RVYE75E2M]], with hypothesis and conclusion exchanged.
For the base $a = 2$, the converse reads: if $n > 2$ and $2^{n-1} \equiv 1 \pmod n$, then $n$ is prime.
A student checks it for $n = 3, 5, 7, 11, 13$, finds it true each time, and uses it as a primality test.
We show that this use is wrong.

1. Take $n = 341 = 11 \cdot 31$, which is composite.
2. Compute $2^{10} = 1024 = 3 \cdot 341 + 1$, so $2^{10} \equiv 1 \pmod{341}$.
3. Then $2^{340} = (2^{10})^{34} \equiv 1^{34} = 1 \pmod{341}$.
4. So $n = 341$ satisfies the hypothesis of the converse but is not prime, and the converse is false.

The number $341$ is the least composite $n$ with $2^{n-1} \equiv 1 \pmod n$, the least [[Fermat pseudoprime|0W93FJAC8F]] to base $2$.
A computer search over the composite numbers below $2000$ lists $341, 561, 645, 1105, 1387$ as the first such numbers.

## Remarks

Forming the converse is a sound way to vary a problem: it produces a new question.
The mistake here is to treat the new question as answered.
A variation needs its own proof or its own counterexample, and checks on small cases are neither.

The repair is to vary the converse again.
Changing the base helps for $341$: $3^{340} \equiv 56 \pmod{341}$, so the base $3$ shows that $341$ is composite.
But the [[Carmichael number|060ZX7C32T]] $561 = 3 \cdot 11 \cdot 17$ satisfies $a^{560} \equiv 1 \pmod{561}$ for every $a$ coprime to $561$.
So no choice of base coprime to $561$ repairs the converse, and stronger tests, such as the Miller-Rabin test, are used instead.

## Explanations

### L1 human

Fermat's little theorem says that prime numbers pass a certain test.
It is tempting to turn this around and say that every number that passes the test is prime.
That turned-around statement is a new claim, and it needs its own proof.
Here it is false: $341 = 11 \cdot 31$ is not prime, but it passes the test.
A theorem and its converse are different statements, and one can be true while the other is false.

### L2 human

We check $2^{340} \equiv 1 \pmod{341}$ by working modulo the two prime factors.

1. Modulo $11$: Fermat's little theorem gives $2^{10} \equiv 1$, and $340 = 34 \cdot 10$, so $2^{340} \equiv 1 \pmod{11}$.
2. Modulo $31$: $2^5 = 32 \equiv 1$, and $340 = 68 \cdot 5$, so $2^{340} \equiv 1 \pmod{31}$.
3. Since $11$ and $31$ are coprime and both divide $2^{340} - 1$, so does $341 = 11 \cdot 31$.

The typical use: before accepting a variation of a theorem, search for a counterexample among numbers where the original proof breaks down.

A trap: the first cases $3, 5, 7, 11, 13$ are all prime, so they cannot refute the converse; only composite numbers can.
