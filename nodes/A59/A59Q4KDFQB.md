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

1. The hypothesis holds: we take $k = 5$ and $n = 4$, and $27$, $84$, $110$, $133$ and $144$ are positive integers.
2. Compute the four fifth powers on the left:
   $$27^5 = 14348907, \quad 84^5 = 4182119424, \quad 110^5 = 16105100000, \quad 133^5 = 41615795893.$$
3. Add them:
   $$14348907 + 4182119424 + 16105100000 + 41615795893 = 61917364224.$$
4. Compute the right side, $144^5 = 61917364224$.
   So $27^5 + 84^5 + 110^5 + 133^5 = 144^5$.
5. A sum of four fifth powers is a fifth power, and $4 < 5$, so the conjecture fails for $k = 5$.

Lander and Parkin found this example in 1966 by a computer search.

## Remarks

The single equation of step 4 settles the question for $k = 5$.
No argument about all integers is needed, because a disproof needs only one instance.

The case $k = 4$ fell later.
In 1988 Noam Elkies found
$$2682440^4 + 15365639^4 + 18796760^4 = 20615673^4,$$
and Roger Frye then found the smallest such example, $95800^4 + 217519^4 + 414560^4 = 422481^4$.
For $k = 3$ the conjecture says that two positive cubes never add up to a cube, which is the exponent $3$ case of [[Fermat's last theorem|0Y5X3SDBCZ]] and is true.

## Explanations

### L1 human

Euler guessed that to make a fifth power by adding fifth powers, you need at least five of them.
For a long time nobody could prove it or find an exception.
In 1966 a computer search found four fifth powers that add up to a fifth power.
Anyone with a calculator can check the sum.
One true equation was enough to show that the guess was wrong.

### L2 human

Can we test the equation quickly before doing the full arithmetic?
Look at last digits.
A fifth power $a^5$ always ends in the same digit as $a$, for example $2^5 = 32$ and $3^5 = 243$, because $a^5 - a$ is divisible by $10$.
So the four fifth powers on the left end in $7$, $4$, $0$ and $3$, and
$$7 + 4 + 0 + 3 = 14$$
tells us that their sum ends in $4$.
The right side $144^5$ also ends in $4$, as it should.
A check modulo $10$ like this catches many errors in a claimed counterexample in a few seconds.
Watch out: the check can only reject a claim, because agreement of the last digits does not prove the equation, and only the full computation of steps 2 to 4 does.
