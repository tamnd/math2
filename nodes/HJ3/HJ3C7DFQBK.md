---
tag: HJ3C7DFQBK
kind: example
name: Perron's paradox on the largest positive integer
msc: ["00A35", "06A05"]
topics: [GB14W4SYPK]
audience: school
not_instance_of:
  - target: MD3MRG90W4
    note: the largest positive integer does not exist, so the extremal object that the argument starts from is not available
uses: [MD3MRG90W4, 01BX15HSRR]
sources:
  - url: https://en.wikipedia.org/wiki/Oskar_Perron
    locator: lead section
---

## Example

Perron's paradox is the following false argument.

> Let $N$ be the largest positive integer.
> If $N > 1$, then $N^2 > N$, which contradicts the choice of $N$.
> So $N = 1$.

We find the step that fails.

1. Each step after the first is correct. If $N > 1$, then $N^2 - N = N(N - 1) > 0$, so $N^2 > N$, and $N^2$ is a positive integer.
2. The conclusion is false: $1$ is not the largest positive integer, since $2 > 1$.
3. So a premise is false. The only premise is the first sentence, that a largest positive integer $N$ exists.
4. This premise is indeed false. For every positive integer $N$, the number $N + 1$ is a positive integer larger than $N$.
5. So the argument proves only a conditional statement: if a largest positive integer existed, it would be $1$. Since none exists, the statement says nothing.

## Remarks

The example shows the trap of the [[extremal principle|MD3MRG90W4]]: the extremal object must exist before the argument uses it.
The steps after the choice of $N$ are of the usual form, a better object against the choice.
The defect sits only in the existence part.

The paradox disappears when the question changes.
For the smallest positive integer, the [[well-ordering principle|01BX15HSRR]] says that it exists, and an argument about it is valid.
For the finite set $\{1, 2, \ldots, 10\}$, a largest element $N = 10$ exists, and the argument fails at another step: $N^2 = 100$ is not in the set, so it does not contradict the choice of $N$.
So an extremal proof needs both parts: the extremum exists, and the improved object lies in the same family.

## Explanations

### L1 human

Pretend that there is a biggest whole number, and call it $N$.
If $N$ were bigger than $1$, then $N$ times $N$ would be even bigger, which cannot be.
So the biggest whole number would be $1$, which is absurd.
The mistake is the first step: there is no biggest whole number, because adding $1$ always gives a bigger one.
An argument that starts from "the biggest" or "the smallest" must first check that such an object exists.

### L2 human

We compare Perron's argument with a valid argument of the same shape.

1. Claim: there is no smallest positive real number.
2. Suppose $x$ is the smallest positive real number.
3. Then $x / 2$ is a positive real number, and $x / 2 < x$, which contradicts the choice of $x$.
4. So the assumption of step 2 is false, and the claim is proved.

This argument is valid because it ends by rejecting the assumption that the extremum exists.
Perron's argument keeps that assumption and draws a conclusion from it.
The typical use of the example is as a warning before any extremal proof in an infinite family.
The trap is to read "take the largest" as a harmless phrase, when it is a claim that needs a proof.
