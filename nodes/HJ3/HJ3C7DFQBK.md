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

Perron's paradox is the following argument, which looks like a correct use of the [[extremal principle|MD3MRG90W4]].

> Let $N$ be the largest positive integer.
> If $N > 1$, then $N^2 > N$, which contradicts the choice of $N$.
> So $N = 1$.

The conclusion is false, so some step is wrong, and we find it.

1. The steps after the first are correct.
   If $N > 1$, then
   $$N^2 - N = N(N - 1) > 0,$$
   so $N^2 > N$, and $N^2$ is again a positive integer.
2. The conclusion is false: $1$ is not the largest positive integer, since $2 > 1$.
3. A valid argument with a false conclusion must have a false premise.
   The only premise is the first sentence, that a largest positive integer $N$ exists.
4. This premise is false indeed.
   For every positive integer $N$, the number $N + 1$ is a positive integer larger than $N$.
5. So the argument proves only a conditional statement: if a largest positive integer existed, it would be $1$.
   Since none exists, the statement gives no information.

## Remarks

The paradox isolates the trap of the extremal principle: the extreme object must exist before the argument uses it.
The steps after the choice of $N$ have the usual shape, a better object against the choice, and they are correct.
The defect sits only in the existence part.

Change the question and the picture changes.
For the smallest positive integer, the [[well-ordering principle|01BX15HSRR]] says that it exists, so an argument that starts from it is valid.
For the finite set $\{1, 2, \ldots, 10\}$, a largest element $N = 10$ exists, and now the argument fails at another step.
The number $N^2 = 100$ is not in the set, so it does not contradict the choice of $N$.
So an extremal proof needs two things: the extreme object exists, and the improved object lies in the same family.

The same error hides in real proofs.
"Take the curve of least length joining two points" assumes a minimizer, and in some families none exists.
Perron used his paradox to make exactly this point about problems of optimization.

## Explanations

### L1 human

Pretend that there is a biggest whole number, and call it $N$.
If $N$ were bigger than $1$, then $N$ times $N$ would be even bigger, which cannot be.
So the biggest whole number would be $1$, which is absurd.
The mistake is in the first step: there is no biggest whole number, because adding $1$ always gives a bigger one.
An argument that starts from "the biggest" or "the smallest" must first check that such an object exists.

### L2 human

Compare Perron's argument with a valid argument of the same shape.
The claim is that no positive real number is the smallest.
Suppose that $x$ is the smallest positive real number.
Then $x/2$ is a positive real number, and
$$\frac{x}{2} < x,$$
which contradicts the choice of $x$.
So the assumption is false, and the claim is proved.

The two arguments use the same moves, and the difference is what each one does with the contradiction.
The valid argument rejects the assumption that the extreme object exists.
Perron's argument keeps that assumption and draws a conclusion from it.
Watch out for the phrase "take the largest": it is a claim that needs a proof, and in an infinite family the proof may fail.
