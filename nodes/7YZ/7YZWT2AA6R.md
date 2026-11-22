---
tag: 7YZWT2AA6R
kind: example
name: A false minimal counterexample argument over the positive rationals
msc: ["00A35", "97E50"]
topics: [EEH2F76CYQ]
audience: ug1
not_instance_of:
  - target: JGRCNPKNGG
    note: the set of counterexamples is a set of positive rationals with no least element, so a least counterexample does not exist
uses: [JGRCNPKNGG, 01BX15HSRR, 0NCJ5WXN6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_counterexample
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Well-ordering_principle
    locator: lead section
---

## Example

Consider the false claim that every positive [[rational number|0NCJ5WXN6Z]] $q$ satisfies $q \ge 1$.
Here is an argument that looks like a [[minimal counterexample|JGRCNPKNGG]] proof of it.

> Suppose that some positive rational is less than $1$, and let $q$ be the least positive rational with $q < 1$.
> Then $q/2$ is a positive rational, and $q/2 < q < 1$.
> So $q/2$ is a smaller counterexample, which contradicts the choice of $q$.

The argument seems to show that no positive rational is less than $1$, which is absurd.
We find the step that fails.

1. The claim is false, because $q = \tfrac12$ is a positive rational with $q < 1$.
2. So the set of counterexamples
   $$C = \{ q \in \mathbb{Q} : 0 < q < 1 \}$$
   is not empty.
3. The set $C$ has no least element.
   For each $q \in C$, the number $q/2$ is in $C$, and $q/2 < q$.
4. So the sentence "let $q$ be the least counterexample" names an object that does not exist.
5. The [[well-ordering principle|01BX15HSRR]] gives least elements only to nonempty sets of natural numbers, and $C$ is not such a set.
6. The method needs a size with values in $\mathbb{N}$.
   Here the size is $q$ itself, and its values are positive rationals.

So the argument is not an instance of the method: its first step has no justification.

## Remarks

The argument does prove something true, namely that $C$ has no least element.
Steps 3 and 4 are that proof, and the contradiction in the quoted text is exactly the statement that the assumed least element cannot exist.

The same failure occurs over the integers.
The false claim "every integer is at least $0$" has the counterexamples $-1, -2, -3, \ldots$, and this set has no least element either.

The argument becomes valid once the size lies in $\mathbb{N}$.
For example, every nonempty set of fractions $a/b$ with positive integers $a$ and $b$ has a member with the least denominator $b$, and the proof of the [[irrationality of the square root of 2|0DZGSDHD92]] uses this.
So every correct minimal counterexample proof must say why a least counterexample exists, and over $\mathbb{N}$ the reason is the well-ordering principle.

## Explanations

### L1 human

Among the whole numbers there is always a smallest one with a given property, as long as at least one has it.
Among the fractions there is not.
The fractions between $0$ and $1$ go down as $\tfrac12$, $\tfrac14$, $\tfrac18$, and they never reach a smallest one.
So "take the smallest fraction below $1$" is not allowed, and the argument proves nothing.

### L2 human

We compare a valid and an invalid use of a least element.
The set $\{ n \in \mathbb{N} : n^2 > 50 \}$ is a nonempty set of natural numbers, and its least element is $8$, because $7^2 = 49$ and $8^2 = 64$.
The set $\{ q \in \mathbb{Q} : q > 0, \ q^2 > 2 \}$ is a nonempty set of positive rationals, and it has no least element.

To see this, take $q$ in the set and move down by the Newton step:
$$r = q - \frac{q^2 - 2}{2q} = \frac{q^2 + 2}{2q}.$$
The number $r$ is rational and positive, and $r < q$ because $q^2 - 2 > 0$.
Write $d = (q^2 - 2)/(2q)$, so that $r = q - d$, and expand:
$$r^2 = q^2 - 2qd + d^2 = q^2 - (q^2 - 2) + d^2 = 2 + d^2 > 2.$$
So $r$ is a smaller member of the set.

Check with $q = 2$: then $r = 6/4 = 3/2$, and $(3/2)^2 = 9/4 > 2$.
The typical use of this non-example is a test for each minimal counterexample proof: name the set in which the least element is taken.
Watch out: a set that is bounded below need not have a least element, and here the greatest lower bound $\sqrt{2}$ is not even rational.
