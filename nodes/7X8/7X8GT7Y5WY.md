---
tag: 7X8GT7Y5WY
kind: example
name: The proof by cases that some irrational power is rational
msc: ["00A35", "03F65"]
topics: [958EF46EYJ]
audience: ug1
instance_of: [JZQVJ9XT63]
not_instance_of:
  - target: 01XM7JEKHY
    note: the proof shows that one of two pairs works but does not say which, so it gives no witness
uses: [JZQVJ9XT63, 0WCP0PVET6, 0DZGSDHD92, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Constructive_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Gelfond%E2%80%93Schneider_theorem
    locator: lead section
---

## Example

Statement: there are irrational numbers $a$ and $b$ such that $a^b$ is rational.
We give a [[non-constructive existence proof|JZQVJ9XT63]], by [[cases|0WCP0PVET6]].

1. The number $\sqrt{2}$ is irrational, by the [[irrationality of the square root of 2|0DZGSDHD92]].
2. Consider the real number $c = \sqrt{2}^{\sqrt{2}}$.
   By the [[law of excluded middle|0RYYK8PG4S]], $c$ is rational or $c$ is irrational.
3. Case 1, $c$ is rational.
   Take $a = \sqrt{2}$ and $b = \sqrt{2}$.
   Both are irrational by step 1, and $a^b = c$ is rational.
4. Case 2, $c$ is irrational.
   Take $a = c$ and $b = \sqrt{2}$.
   Both are irrational, and the rule $(x^r)^s = x^{rs}$ for $x > 0$ gives
   $$a^b = \left(\sqrt{2}^{\sqrt{2}}\right)^{\sqrt{2}} = \sqrt{2}^{\sqrt{2} \cdot \sqrt{2}} = \sqrt{2}^{2} = 2,$$
   which is rational.
5. The two cases cover all possibilities, and each gives a pair.
   So the statement holds.

## Remarks

The proof is correct in classical mathematics, but it does not say which pair works.
It is not a [[constructive proof|01XM7JEKHY]], because step 2 splits on a question that the proof leaves open.

The question does have an answer.
The [[Gelfond-Schneider theorem|RN58Z2NWAC]] of 1934 implies that $\sqrt{2}^{\sqrt{2}}$ is [[transcendental|0VTQXTCR2G]], and a transcendental number is irrational.
So Case 2 is the true one, and the pair $\left(\sqrt{2}^{\sqrt{2}}, \sqrt{2}\right)$ is a witness.
That fact is much deeper than the statement, and the proof above does not need it.

Notice what each case used.
Case 1 needs only that $\sqrt{2}$ is irrational.
Case 2 needs that and the exponent rule, and it uses the case assumption to know that $a = c$ is irrational.
A constructive proof with a named pair is [[irrational a and b with a to the power b rational, by construction|H7X4FMAHC8]], and it needs the extra fact that $\log_2 3$ is irrational.

## Explanations

### L1 human

Here is a puzzle with two doors.
We can prove that a prize is behind one of the two doors.
But the proof does not say which door.
In this example the first door is the pair $\sqrt{2}, \sqrt{2}$, and the second door is the pair $\sqrt{2}^{\sqrt{2}}, \sqrt{2}$.
One of them works for sure, and the short proof stops there.
A much harder theorem, proved in 1934, opens the doors: the prize is behind the second one.

### L2 human

We check the computation in Case 2 slowly.
For $x > 0$ and real $r$ and $s$, the rule $(x^r)^s = x^{rs}$ holds.
With $x = \sqrt{2}$, $r = \sqrt{2}$ and $s = \sqrt{2}$, it gives
$$\left(\sqrt{2}^{\sqrt{2}}\right)^{\sqrt{2}} = \sqrt{2}^{\sqrt{2} \cdot \sqrt{2}} = \sqrt{2}^{2} = 2.$$
The base $\sqrt{2}$ is positive, so the rule applies.

The typical use: a case split on a property that you cannot decide, with a witness ready in each case, gives a short existence proof.
Watch out: the proof shows neither that $\sqrt{2}^{\sqrt{2}}$ is rational nor that it is irrational.
Quoting the proof for either fact is a mistake.
