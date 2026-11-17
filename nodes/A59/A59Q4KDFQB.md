---
tag: A59Q4KDFQB
kind: example
name: A counterexample to Euler's sum of powers conjecture
msc: ["00A35", "11D41"]
topics: [958EF46EYJ]
audience: school
instance_of: [0ED72CTBNP]
uses: [0ED72CTBNP, E486QA4JS4]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_sum_of_powers_conjecture
    locator: Counterexamples
  - url: https://en.wikipedia.org/wiki/Counterexample
    locator: lead section
---

## Example

[[Euler's sum of powers conjecture|E486QA4JS4]] says: for integers $n > 1$ and $k > 1$, if a sum of $n$ $k$-th powers of positive integers is a $k$-th power, then $n \geq k$.
For $k = 5$ it says that no sum of four fifth powers of positive integers is a fifth power.
The numbers $27$, $84$, $110$, $133$ and $144$ form a [[counterexample|0ED72CTBNP]].

1. Hypothesis: $k = 5$ and $n = 4$, and $27$, $84$, $110$, $133$, $144$ are positive integers.
2. Compute the fifth powers: $27^5 = 14348907$, $84^5 = 4182119424$, $110^5 = 16105100000$, $133^5 = 41615795893$.
3. Their sum is $61917364224$.
4. Also $144^5 = 61917364224$. So $27^5 + 84^5 + 110^5 + 133^5 = 144^5$.
5. A sum of four fifth powers is a fifth power, and $4 < 5$. So the conjecture fails for $k = 5$.

Lander and Parkin found this example in 1966 by a computer search.

## Remarks

The single equation in step 4 settles the question for $k = 5$.
No argument about all integers was needed; a disproof needs only one instance.

The case $k = 4$ fell later.
In 1988 Noam Elkies found $2682440^4 + 15365639^4 + 18796760^4 = 20615673^4$, and Roger Frye then found the smallest such example, $95800^4 + 217519^4 + 414560^4 = 422481^4$.
For $k = 3$ the conjecture says that two positive cubes never add up to a cube, which is the exponent $3$ case of [[Fermat's last theorem|0Y5X3SDBCZ]] and is true.

## Explanations

### L1 human

Euler guessed that to make a fifth power by adding fifth powers, at least five of them are needed.
For a long time nobody could prove it or find an exception.
In 1966 a computer search found four fifth powers that add up to a fifth power.
Anyone with a calculator can check the sum.
One true equation was enough to show that the guess was wrong.

### L2 human

We check the last digits of the counterexample without a full computation.

1. A fifth power $a^5$ has the same last digit as $a$. For example $2^5 = 32$ and $3^5 = 243$.
2. So the last digits of $27^5$, $84^5$, $110^5$, $133^5$ are $7$, $4$, $0$, $3$.
3. Their sum ends in the last digit of $7 + 4 + 0 + 3 = 14$, that is, $4$.
4. And $144^5$ ends in $4$, as it should.

The typical use: a quick check modulo $10$ catches many errors in a claimed counterexample before the full computation.

A trap: such a check can only reject a claimed counterexample.
Agreement of the last digits does not prove the equation; the full computation in step 4 of the example does.
