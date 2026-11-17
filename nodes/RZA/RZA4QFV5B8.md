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
We prove the [[negation|029JBBF693]] $\neg p$ with the rule of negation introduction: we assume $p$ and derive a contradiction.

1. Assume $p$. Then $\sqrt{2} = a/b$ for positive integers $a$ and $b$.
2. Cancel common factors, so that $a$ and $b$ have no common factor greater than $1$.
3. Square both sides: $2 = a^2/b^2$, so $a^2 = 2b^2$. So $a^2$ is even.
4. If $a$ were odd, $a = 2k + 1$, then $a^2 = 4k^2 + 4k + 1$ would be odd. So $a$ is even, $a = 2c$ for an integer $c$.
5. Then $4c^2 = 2b^2$, so $b^2 = 2c^2$ is even, and by the argument of step 4, $b$ is even.
6. Steps 4 and 5 show that $2$ divides both $a$ and $b$. This contradicts step 2.
7. The assumption $p$ led to a contradiction. By negation introduction, we conclude $\neg p$: $\sqrt{2}$ is not rational.

## Remarks

The example shows the meaning of $\neg p$ as "$p$ leads to a contradiction", which is the reading of Mathlib's definition `Not a := a → False`.
Steps 1 to 6 build a function from the assumption $p$ to a contradiction, and step 7 records that function as a proof of $\neg p$.
The general result is the [[irrationality of the square root of a prime|0YHFMXJJAZ]].

This proof is often called a proof by contradiction, but its last step is negation introduction: it proves a negation, $\neg p$.
A proof by contradiction in the strict sense proves a positive claim $q$ by refuting $\neg q$, and it needs the classical step $\neg\neg q \to q$.
The proof here uses no such step at the end.

If we replace $2$ by $4$, step 4 fails to give a contradiction, because $\sqrt{4} = 2/1$ is rational; the negation "$\sqrt{4}$ is not rational" is false.

## Explanations

### L1 human

To show that something is impossible, we can pretend it is possible and watch what goes wrong.
Pretend that $\sqrt{2}$ is a fraction in lowest terms.
A short calculation shows that the top and the bottom of the fraction are both even.
But a fraction in lowest terms cannot have both parts even.
So the pretence was wrong, and $\sqrt{2}$ is not a fraction.

### L2 human

We prove $\neg q$, where $q$ is "there is a largest even integer", with the same rule.

1. Assume $q$: let $m$ be an even integer with $m \geq n$ for every even integer $n$.
2. The integer $m + 2$ is even, because $m + 2 = 2(k + 1)$ when $m = 2k$.
3. By step 1, $m \geq m + 2$, so $0 \geq 2$, which is false.
4. The assumption $q$ led to a contradiction, so $\neg q$ holds.

The typical use of negation introduction is to prove that an object with some property does not exist.

A trap: the conclusion is the negation of the assumption, not some other statement.
From step 3 we may conclude $\neg q$, but not, for example, "every integer is odd".
