---
tag: T7C1TEZBRD
kind: example
name: An integer is even if and only if its square is even
msc: ["00A35", "11A05"]
topics: [958EF46EYJ, PM1AYWABA7]
audience: school
instance_of: [TFQ1845T84, 0S6GMNJ62Y]
uses: [TFQ1845T84, 0NTF6DMVAP, 0BB5TPGQ1N, MKNWSR8WRN]
sources:
  - url: https://en.wikipedia.org/wiki/If_and_only_if
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.4
---

## Example

Statement: for every integer $n$, $n$ is even if and only if $n^2$ is even.
We [[prove the biconditional|TFQ1845T84]] by proving its two directions separately.

1. $(\Rightarrow)$ Assume $n$ is even. Then $n = 2k$ for an integer $k$.
2. So $n^2 = 4k^2 = 2(2k^2)$, and $2k^2$ is an integer. Hence $n^2$ is even. This direction is a [[direct proof|0NTF6DMVAP]].
3. $(\Leftarrow)$ Assume $n^2$ is even. We must show that $n$ is even.
4. This is the statement [[if n^2 is even, then n is even|MKNWSR8WRN]], which is proved by [[contrapositive|0BB5TPGQ1N]]: if $n$ is odd, say $n = 2k + 1$, then $n^2 = 2(2k^2 + 2k) + 1$ is odd.
5. Both directions hold, so $n$ is even if and only if $n^2$ is even.

## Remarks

The two directions need different methods.
The direction $(\Rightarrow)$ starts from a formula $n = 2k$ and computes.
The direction $(\Leftarrow)$ starts from "$n^2 = 2m$", and taking a square root of $2m$ gives no formula for $n$; the contrapositive turns it into a computation again.
This pattern is typical: one direction of an equivalence is often a short computation, and the other needs a different idea.

The same equivalence holds with $2$ replaced by any prime $p$: $p \mid n$ if and only if $p \mid n^2$.
The direction $(\Leftarrow)$ then follows from [[Euclid's lemma|051VYKA1EX]].
For a number that is not prime it fails: $4 \mid 6^2 = 36$, but $4 \nmid 6$.

## Explanations

### L1 human

Look at the squares of $1$ to $6$: $1, 4, 9, 16, 25, 36$.
The even numbers $2, 4, 6$ have the even squares $4, 16, 36$.
The odd numbers $1, 3, 5$ have the odd squares $1, 9, 25$.
The statement says this always happens, in both directions.
An even number has an even square, and an even square comes from an even number.

### L2 human

We use the equivalence in the proof that $\sqrt{2}$ is irrational.

1. Suppose $\sqrt{2} = \frac{a}{b}$ with integers $a$, $b$ that have no common factor greater than $1$.
2. Then $a^2 = 2b^2$, so $a^2$ is even. By direction $(\Leftarrow)$, $a$ is even, say $a = 2c$.
3. Then $4c^2 = 2b^2$, so $b^2 = 2c^2$ is even. By direction $(\Leftarrow)$ again, $b$ is even.
4. So $2$ divides both $a$ and $b$, which contradicts step 1.

The typical use: an equivalence is proved once and then used in either direction wherever it is needed.

A trap: step 2 uses the direction $(\Leftarrow)$, not $(\Rightarrow)$.
A proof that only established "even numbers have even squares" could not be used here.
