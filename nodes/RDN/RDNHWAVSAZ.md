---
tag: RDNHWAVSAZ
kind: example
name: Squaring the goal produces a goal that does not imply it
msc: ["00A35", "26D05"]
topics: [958EF46EYJ]
audience: school
not_instance_of:
  - target: V8ZB838JY5
    note: the backward step replaces the goal x + 1 >= 0 by (x + 1)^2 >= 0, which does not imply it, so the chain does not reach the goal
uses: [V8ZB838JY5]
sources:
  - url: https://en.wikipedia.org/wiki/Necessity_and_sufficiency
    locator: lead section
---

## Example

The claim is: for every real number $x$ with $x^2 \leq 1$, $x + 1 \geq 0$.
A student plans the proof backward.

1. The goal is $x + 1 \geq 0$.
2. "It suffices to show $(x + 1)^2 \geq 0$."
3. "A square is never negative, so $(x + 1)^2 \geq 0$, and we are done."

The claim is true, but the plan is not a valid use of the [[forward-backward method|V8ZB838JY5]], and we can locate the failure.
A backward step must replace the goal $B$ by a statement $B'$ with $B' \Rightarrow B$.
Here $B$ is $x + 1 \geq 0$ and $B'$ is $(x + 1)^2 \geq 0$.
But $B'$ does not imply $B$: for $x = -2$,
$$(x + 1)^2 = 1 \geq 0, \qquad \text{but} \qquad x + 1 = -1 < 0.$$
The implication holds the other way, $B \Rightarrow B'$, so $B'$ is a necessary condition for $B$ and not a sufficient one.
A warning sign is that the argument never uses the hypothesis $x^2 \leq 1$, so it would also "prove" $x + 1 \geq 0$ for $x = -2$, where it is false.

## Remarks

A correct plan uses the hypothesis.
Backward, $x + 1 \geq 0$ means $x \geq -1$.
Forward, $x^2 \leq 1$ gives $|x| \leq 1$, because $|x|$ and $1$ are nonnegative and $|x|^2 = x^2 \le 1^2$.
Then $|x| \leq 1$ gives $-1 \leq x \leq 1$, and the chains meet at $x \geq -1$.

Squaring is a safe backward step only when both sides are known to be at least $0$.
In that case $u \leq v$ and $u^2 \leq v^2$ are equivalent, and the step can be used in both directions.

## Explanations

### L1 human

To show that a number is not negative, the student showed that its square is not negative.
But every square is not negative, even the square of $-1$.
So the student's step would work for any number at all, also for numbers that are negative.
A step that would "prove" a false claim as well cannot prove the true one.

### L2 human

How do you test a proposed backward step "to show $B$, it suffices to show $B'$"?
Ask whether $B'$ implies $B$, and look for a value that makes $B'$ true and $B$ false.
Take $B$ to be $x > 2$ and $B'$ to be $x^2 > 4$.
The value $x = -3$ makes $B'$ true and $B$ false, so the step is not valid.
Now swap them, with $B$ the inequality $x^2 > 4$ and $B'$ the inequality $x > 2$.
Every $x > 2$ has $x^2 > 4$, so this step is valid.
One test value is enough to reject a backward step.
Watch out: a valid backward step can still lead to a false goal.
To show $x^2 > 4$ for $x = -3$, the valid step "it suffices to show $x > 2$" leads to the false goal $-3 > 2$, so a dead end means you should back up, not that the claim is false.
