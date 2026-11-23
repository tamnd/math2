---
tag: RZA4QFV5B8
kind: example
name: Proving "the square root of 2 is not rational" by negation introduction
msc: ["03B05", "11J72"]
topics: [PM1AYWABA7]
audience: school
instance_of: [029JBBF693]
uses: [029JBBF693, 0YHFMXJJAZ]
sources:
  - url: https://en.wikipedia.org/wiki/Negation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Square_root_of_2
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.2
---

## Example

Let $p$ be the proposition "$\sqrt{2}$ is rational".
We prove its [[negation|029JBBF693]] $\neg p$ by negation introduction: we assume $p$ and derive a contradiction.

1. Assume $p$.
   Then $\sqrt{2} = a/b$ for positive integers $a$ and $b$, and after cancelling we may take $a$ and $b$ with no common factor greater than $1$.
2. Squaring gives $2 = a^2 / b^2$, so
   $$a^2 = 2b^2,$$
   and $a^2$ is even.
3. If $a$ were odd, say $a = 2k + 1$, then $a^2 = 4k^2 + 4k + 1$ would be odd.
   So $a$ is even, and $a = 2c$ for an integer $c$.
4. Then $4c^2 = 2b^2$, so $b^2 = 2c^2$ is even, and the argument of step 3 shows that $b$ is even.
5. So $2$ divides both $a$ and $b$, which contradicts the choice in step 1.
6. The assumption $p$ led to a contradiction, so negation introduction gives $\neg p$: $\sqrt{2}$ is not rational.

## Remarks

The example shows the meaning of $\neg p$ as "$p$ leads to a contradiction", which is the reading of Mathlib's definition `Not a := a → False`.
Steps 1 to 5 build a way to turn the assumption $p$ into a contradiction, and step 6 records that as a proof of $\neg p$.
The general result is the [[irrationality of the square root of a prime|0YHFMXJJAZ]].

Many books call this a proof by contradiction, but its last step proves a negation.
A proof by contradiction in the strict sense proves a positive claim $q$ by refuting $\neg q$, and it needs the classical step $\neg\neg q \to q$.
This proof needs no such step, so it is valid in intuitionistic logic too.

Replace $2$ by $4$ and the argument breaks at step 4.
From $a^2 = 4b^2$ and $a = 2c$ we get only $c^2 = b^2$, which says nothing about the parity of $b$, and indeed $\sqrt{4} = 2/1$ is rational.

## Explanations

### L1 human

To show that something is impossible, pretend it is possible and watch what goes wrong.
Pretend that $\sqrt{2}$ is a fraction in lowest terms.
A short calculation shows that its top and its bottom are both even.
A fraction in lowest terms cannot have both parts even.
So the pretence was wrong, and $\sqrt{2}$ is not a fraction.

### L2 human

Prove $\neg q$, where $q$ is "there is a largest even integer", by the same rule.
Assume $q$, and let $m$ be an even integer with $m \ge n$ for every even integer $n$.
Write $m = 2k$; then $m + 2 = 2(k + 1)$ is even, so the assumption gives $m \ge m + 2$, that is, $0 \ge 2$, which is false.
The assumption $q$ led to a contradiction, so $\neg q$ holds.
Negation introduction is the usual way to prove that an object with some property does not exist.
Watch out: the conclusion is the negation of the assumption and nothing else, so from $0 \ge 2$ here you may conclude $\neg q$, but not an unrelated claim such as "every integer is odd".
