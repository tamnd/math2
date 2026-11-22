---
tag: MZXYW75TC3
kind: example
name: A direct induction on the bound 2 for the sum of 1/k²
msc: ["00A35", "40A05"]
topics: [EEH2F76CYQ]
audience: ug1
not_instance_of:
  - target: F94KJC2RXP
    note: the induction hypothesis is the claim itself, not a stronger statement, and the step cannot be completed from it
uses: [F94KJC2RXP, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Description
---

## Example

For $n \ge 1$, let $S_n = \sum_{k=1}^{n} 1/k^2$, and let $P(n)$ be the claim $S_n < 2$.
We try to prove $P(n)$ by plain [[induction|0ASJVEFA9J]], with $P(n)$ itself as the hypothesis, and we watch the step fail.

1. Base case.
   We have $S_1 = 1 < 2$, so $P(1)$ holds.
2. Step.
   Assume $S_n < 2$, and add the next term:
   $$S_{n+1} = S_n + \frac{1}{(n+1)^2} < 2 + \frac{1}{(n+1)^2}.$$
   This bound is larger than $2$, so it does not give $P(n + 1)$.
3. The hypothesis cannot do better, because it allows every value of $S_n$ below $2$.
   For example, it allows $S_n = 2 - \dfrac{1}{2(n+1)^2}$.
4. For that value the next sum would be
   $$2 - \frac{1}{2(n+1)^2} + \frac{1}{(n+1)^2} = 2 + \frac{1}{2(n+1)^2} > 2.$$
5. So no argument that uses only "$S_n < 2$" and the formula of step 2 can prove $S_{n+1} < 2$.
   The step is not proved, and the attempt is not a proof.

The claim itself is true.
The attempt fails because its hypothesis is the bare claim and not a [[stronger statement|F94KJC2RXP]], so it is not an instance of that method.

## Remarks

The value in step 3 is not a real value of $S_n$, since the true $S_n$ is at most $2 - \tfrac1n$.
The point is that the hypothesis cannot rule that value out, so the hypothesis carries too little information for the step.
The repair is the strengthened claim $S_n \le 2 - \tfrac1n$, worked out in [[the sum of $1/k^2$ is at most $2 - 1/n$|DFVCKA01PN]].

The same failure happens for every constant bound $S_n < c$, because each step adds a positive amount and the hypothesis says nothing about the distance to $c$.
A plain induction does work for a bound that grows with $n$, such as $S_n \le n$, since $S_{n+1} \le n + \tfrac{1}{(n+1)^2} \le n + 1$.
That bound is true and provable, but it is too weak to show that the series converges.

## Explanations

### L1 human

We want to show that a growing total stays below $2$.
Knowing only "the total so far is below $2$" does not help, because the total could be just a hair below $2$.
Then the next small piece could push it over.
To make the step work, we must know how far below $2$ the total is.
That is the idea of a stronger hypothesis.

### L2 human

We put numbers into the failed step for $n = 3$.
The hypothesis is $S_3 < 2$, while the true value is $S_3 = \tfrac{49}{36} \approx 1.361$.
The new term is $\tfrac{1}{16} = 0.0625$.
From the hypothesis alone, $S_3$ could be $1.99$, and then
$$1.99 + 0.0625 = 2.0525 > 2.$$
So the hypothesis does not decide whether $S_4 < 2$, even though the true value $S_4 = \tfrac{205}{144} \approx 1.424$ is below $2$.

You can recognize a stalled step of this kind by its shape: the hypothesis is an inequality with a constant bound, and each step adds a positive amount.
Watch out: "the new term is small" is not a proof of the step, because small is not the same as smaller than the remaining gap.
