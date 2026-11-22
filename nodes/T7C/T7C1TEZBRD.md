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

1. $(\Rightarrow)$ Assume that $n$ is even, so $n = 2k$ for some integer $k$.
   Then $n^2 = 4k^2 = 2(2k^2)$, and $2k^2$ is an integer, so $n^2$ is even.
   This direction is a [[direct proof|0NTF6DMVAP]].
2. $(\Leftarrow)$ Assume that $n^2$ is even; we must show that $n$ is even.
   This is the statement [[if n^2 is even, then n is even|MKNWSR8WRN]], and we prove its [[contrapositive|0BB5TPGQ1N]].
3. Suppose $n$ is odd, say $n = 2k + 1$.
   Then
   $$n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1,$$
   so $n^2$ is odd.
   This proves "if $n$ is odd, then $n^2$ is odd", which is equivalent to the direction $(\Leftarrow)$.
4. Both directions hold, so $n$ is even if and only if $n^2$ is even.

## Remarks

The two directions need different methods.
The direction $(\Rightarrow)$ starts from the formula $n = 2k$ and computes.
The direction $(\Leftarrow)$ starts from $n^2 = 2m$, and that gives no formula for $n$ of the form $2k$.
The contrapositive turns it back into a computation.
This pattern is common: one direction of an equivalence is a short computation, and the other needs a different idea.

The equivalence stays true with $2$ replaced by any prime $p$: $p \mid n$ if and only if $p \mid n^2$.
The direction $(\Leftarrow)$ then follows from [[Euclid's lemma|051VYKA1EX]], since $p \mid n \cdot n$ gives $p \mid n$.
For a number that is not prime the direction $(\Leftarrow)$ fails: $4 \mid 6^2 = 36$, but $4 \nmid 6$.

## Explanations

### L1 human

Look at the squares of $1$ to $6$: $1, 4, 9, 16, 25, 36$.
The even numbers $2, 4, 6$ have the even squares $4, 16, 36$.
The odd numbers $1, 3, 5$ have the odd squares $1, 9, 25$.
The statement says that this always happens, in both directions.
An even number has an even square, and an even square comes from an even number.

### L2 human

The equivalence is the main step in the proof that [[the square root of 2 is irrational|0DZGSDHD92]].
Suppose $\sqrt{2} = a / b$ with integers $a$ and $b$ that have no common factor greater than $1$.
Squaring gives
$$a^2 = 2b^2,$$
so $a^2$ is even, and the direction $(\Leftarrow)$ makes $a$ even, say $a = 2c$.
Then $4c^2 = 2b^2$, so $b^2 = 2c^2$ is even, and the direction $(\Leftarrow)$ makes $b$ even too.
Now $2$ divides both $a$ and $b$, which contradicts the choice of $a$ and $b$.
The problem shows the typical use: an equivalence is proved once and then used in whichever direction is needed.
Watch out: both uses here are of the direction $(\Leftarrow)$, so a proof that only established "even numbers have even squares" would not help.
