---
tag: 61PMPT3QQZ
kind: example
name: Paraphrase without checking does not catch a false step
msc: ["00A35", "97E50"]
topics: [STSM6PR7TX]
audience: ug1
not_instance_of:
  - target: 40GCSM2G56
    note: the reader restates each line in other words but never asks for the reason of a line and never tests a line on an example
uses: [40GCSM2G56, 0FFXKTKKQC]
sources:
  - doi: 10.5951/jresematheduc.45.1.0062
    locator: pages 62-101
  - url: https://en.wikipedia.org/wiki/Square_root
    locator: lead section
---

## Example

The claimed statement is that for every real number $x$, if $x^2 > 4$, then $x > 2$.
The proof in the text, which is flawed, reads as follows.

> Suppose that $x^2 > 4$.
> Taking square roots of both sides, we get $x > 2$.

A reader paraphrases it as "we start from $x^2 > 4$ and take roots, so $x$ is more than $2$", finds each line plausible, and accepts the proof.
We check this reading against the method of [[reading proofs|40GCSM2G56]].

The method asks for the reason of each line, and the paraphrase gives none for "taking square roots": it only repeats the step.
Written out, the reason is that the square root is increasing on $[0, \infty)$, so $x^2 > 4$ gives $\sqrt{x^2} > \sqrt{4} = 2$.
But $\sqrt{x^2} = \lvert x \rvert$, the [[absolute value|0FFXKTKKQC]] of $x$, and not $x$.
So the step correctly gives only $\lvert x \rvert > 2$.

The method also asks for a test on an example.
Take $x = -3$: then $x^2 = 9 > 4$, so the hypothesis holds, but $x > 2$ is false.
The claimed statement is false, and the flaw is the step $\sqrt{x^2} = x$.
The paraphrase did neither check, so it is not active reading, and it accepted a false proof.

## Remarks

The correct statement is that if $x^2 > 4$, then $x > 2$ or $x < -2$.
The written-out reason above gives $\lvert x \rvert > 2$, which says exactly this.

The identity $\sqrt{x^2} = x$ holds only for $x \ge 0$, so with the extra hypothesis $x \ge 0$ the original proof becomes correct.
The same false step runs the other way when a proof squares both sides of an inequality or an equation, as [[squaring both sides does not prove an identity|FGS7ZJJYRK]] shows.
[[Fallacies and errors in proofs|T6QQ749DM5]] collects other errors of this kind.

## Explanations

### L1 human

A proof says: "the square of $x$ is more than $4$, so $x$ is more than $2$".
This sounds right, and a reader who just repeats it in other words will accept it.
But try $x = -3$: its square is $9$, which is more than $4$, and yet $-3$ is less than $2$.
So the proof is wrong.
Only a reader who tests the claim, or who asks why the step holds, finds the error.

### L2 human

We contrast two readings of the single step "taking square roots of both sides".
The paraphrase, "we take roots of both sides", repeats the step and checks nothing.
The explanation, "the square root is increasing on $[0, \infty)$, and both $x^2$ and $4$ lie there, so $\sqrt{x^2} > 2$", names a result and checks its hypotheses.
The explanation then needs $\sqrt{x^2}$ in terms of $x$, and the definition of the square root gives $\lvert x \rvert$, which is where the error shows.

In training, a student learns to replace each paraphrase with a sentence that names a reason.
Watch out: tests with positive numbers such as $x = 3$ or $x = 5$ all pass, and only a negative test value shows the error.
