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

For $n \ge 1$, let $S_n = \sum_{k=1}^{n} 1/k^2$.
Claim $P(n)$: $S_n < 2$.
We try to prove $P(n)$ by plain [[induction|0ASJVEFA9J]], with the hypothesis $P(n)$ itself, and we see the step fail.

1. Base case: $S_1 = 1 < 2$. So $P(1)$ holds.
2. Step: assume $S_n < 2$. Then $S_{n+1} = S_n + \dfrac{1}{(n+1)^2}$.
3. The hypothesis gives only $S_{n+1} < 2 + \dfrac{1}{(n+1)^2}$. This bound is larger than $2$.
4. The hypothesis allows every value of $S_n$ below $2$. For example, it allows $S_n = 2 - \dfrac{1}{2(n+1)^2}$.
5. For that value, $S_n + \dfrac{1}{(n+1)^2} = 2 + \dfrac{1}{2(n+1)^2} > 2$.
6. So no argument that uses only "$S_n < 2$" and the formula of step 2 can prove $S_{n+1} < 2$.
7. The step is not proved, and the attempt is not a proof.

The claim itself is true.
The attempt fails because it does not use a [[stronger induction hypothesis|F94KJC2RXP]], so it is not an instance of that method.

## Remarks

1. The value in step 4 is not a real value of $S_n$. The point is that the hypothesis cannot rule it out, so the hypothesis carries too little information.
2. The repair is the strengthened claim $S_n \le 2 - \tfrac1n$, on the page [[The sum of 1/k² is at most 2 − 1/n|DFVCKA01PN]].
3. A plain induction does work for a bound that grows with $n$, such as $S_n \le n$. Such a bound is too weak to be of use here.
4. The same failure happens for each bound $S_n < c$ with a constant $c$, because the terms $1/(n+1)^2$ are positive.

## Explanations

### L1 human

We want to show that a growing total stays below $2$.
Knowing only "the total so far is below $2$" does not help, because the total could be just a hair below $2$.
Then the next small piece could push it over.
To make the step work, we must know how far below $2$ the total is.
That is the idea of a stronger hypothesis.

### L2 human

We put numbers into the failed step for $n = 3$.

1. The hypothesis is $S_3 < 2$. The true value is $S_3 = \tfrac{49}{36} \approx 1.361$.
2. The new term is $\tfrac{1}{16} = 0.0625$.
3. From the hypothesis alone, $S_3$ could be $1.99$, and then $1.99 + 0.0625 = 2.0525 > 2$.
4. So the hypothesis does not decide whether $S_4 < 2$, even though the true value $S_4 = \tfrac{205}{144} \approx 1.424$ is below $2$.

The typical use of this non-example is to recognise a stalled step: the hypothesis is an inequality with a constant bound, and each step adds a positive amount.
A trap is to "prove" the step by saying that the new term is small; small is not the same as smaller than the remaining gap.
