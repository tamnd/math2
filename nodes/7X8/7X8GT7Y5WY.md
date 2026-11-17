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

1. The number $\sqrt{2}$ is irrational; see [[irrationality of the square root of 2|0DZGSDHD92]].
2. Consider the real number $c = \sqrt{2}^{\sqrt{2}}$. By the [[law of excluded middle|0RYYK8PG4S]], $c$ is rational or $c$ is irrational.
3. Case $c$ is rational: take $a = \sqrt{2}$ and $b = \sqrt{2}$. Both are irrational, and $a^b = c$ is rational.
4. Case $c$ is irrational: take $a = c$ and $b = \sqrt{2}$. Both are irrational, and $a^b = \sqrt{2}^{\sqrt{2} \cdot \sqrt{2}} = \sqrt{2}^{2} = 2$ is rational.
5. In both cases a pair exists. So the statement holds.

## Remarks

The proof is correct in classical mathematics, but it does not say which pair works.
It is not a [[constructive proof|01XM7JEKHY]], since step 2 splits on a question that the proof does not answer.

The question has an answer.
The [[Gelfond-Schneider theorem|RN58Z2NWAC]] of 1934 implies that $\sqrt{2}^{\sqrt{2}}$ is [[transcendental|0VTQXTCR2G]], and so irrational.
So the second case is the true one.
That fact is much deeper than the statement, and the proof above does not need it.

A constructive proof with a named pair is [[irrational a and b with a to the power b rational, by construction|H7X4FMAHC8]].

## Explanations

### L1 human

Here is a puzzle with two doors.
Behind one of the two doors there is a prize, and we can prove it.
But the proof does not say which door.
In this example, the first door is the pair $\sqrt{2}, \sqrt{2}$, and the second door is the pair $\sqrt{2}^{\sqrt{2}}, \sqrt{2}$.
One of them works for sure, and the short proof stops there.

### L2 human

We check the computation in step 4.

1. For $x > 0$ and real $r$, $s$, the rule $(x^r)^s = x^{rs}$ holds.
2. With $x = \sqrt{2}$, $r = \sqrt{2}$ and $s = \sqrt{2}$: $\left(\sqrt{2}^{\sqrt{2}}\right)^{\sqrt{2}} = \sqrt{2}^{\sqrt{2} \cdot \sqrt{2}}$.
3. $\sqrt{2} \cdot \sqrt{2} = 2$, so this is $\sqrt{2}^2 = 2$.

The typical use: a case split on an unknown property, with a witness ready in each case, gives a short existence proof.

A trap: the proof does not show that $\sqrt{2}^{\sqrt{2}}$ is rational, nor that it is irrational.
Quoting this proof for either fact is a mistake.
