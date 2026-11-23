---
tag: FGS7ZJJYRK
kind: example
name: Squaring both sides does not prove an identity
msc: ["00A35", "97H30"]
topics: [MEKKHHQTKB]
audience: school
not_instance_of:
  - target: XP5SDYKJX0
    note: the argument starts from the claim and uses the squaring step, which cannot be reversed, so it proves nothing about the claim
uses: [XP5SDYKJX0, 0F7FQS6XY6, 0FFXKTKKQC]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Extraneous_and_missing_solutions
    locator: lead section
---

## Example

A student claims that $\sqrt{x^2} = x$ for every real $x$, where $\sqrt{\ }$ is the non-negative [[square root|0F7FQS6XY6]].
The argument: start from $\sqrt{x^2} = x$, square both sides to get $\big(\sqrt{x^2}\big)^2 = x^2$, simplify the left side to $x^2$, and reach $x^2 = x^2$, which is true.
We check why this is not a [[proof of an identity|XP5SDYKJX0]].

1. The argument starts from the claim, so it shows only that the claim implies the true equation $x^2 = x^2$.
2. A false statement can imply a true one.
   From $-1 = 1$, squaring gives $1 = 1$.
3. The squaring step cannot be reversed.
   From $u^2 = v^2$ we get only $u = v$ or $u = -v$.
4. The claim is in fact false: at $x = -1$ the left side is $\sqrt{1} = 1$ and the right side is $-1$.
5. The correct identity is $\sqrt{x^2} = \lvert x \rvert$, with the [[absolute value|0FFXKTKKQC]].

## Remarks

Read the student's chain upward and the problem shows: each "$A$ implies $B$" becomes "$B$ implies $A$", and the squaring step fails in that direction.
A valid proof needs each step to hold in the direction from the known fact to the claim.

The correct identity has a proof by two cases.
If $x \ge 0$, then $x$ is a non-negative number whose square is $x^2$, so $\sqrt{x^2} = x = \lvert x \rvert$.
If $x < 0$, then $-x > 0$ and $(-x)^2 = x^2$, so $\sqrt{x^2} = -x = \lvert x \rvert$.

Squaring is allowed when you solve an equation, because it can only add solutions, and you then check each candidate; the added ones are the extraneous solutions.
Multiplying by an expression that can be $0$ fails in the same way.
From the claim $\frac{x^2 - 1}{x - 1} = x + 1$ for all real $x$, multiplying by $x - 1$ gives $x^2 - 1 = (x + 1)(x - 1)$, which is true everywhere, yet the claim fails at $x = 1$, where the left side is undefined.

## Explanations

### L1 human

Suppose someone claims that $-1$ equals $1$.
Square both numbers and you get $1$ and $1$, which are equal.
That does not make $-1$ equal to $1$.
Squaring can make two different numbers look the same, so it cannot show that two numbers were the same.
The claim "$\sqrt{x^2}$ is always $x$" fails in exactly this way, at every negative $x$.

### L2 human

We turn a backward argument into a forward proof of $(x + 1)^2 - x^2 = 2x + 1$ for every real $x$.

1. A backward argument would start from the claim and reach $2x + 1 = 2x + 1$.
   Its steps are expansions and additions, which are reversible, but the reader has to check that.
2. A forward proof avoids the question.
   Let $x$ be real, and expand:
   $$(x + 1)^2 - x^2 = x^2 + 2x + 1 - x^2 = 2x + 1.$$
3. This chain starts at the left side and ends at the right side, so it proves the identity.

Scratch work may run backward, but the written proof should run forward.
Watch out for the phrase "and since $1 = 1$, the identity holds": it signals a backward argument, and every step then needs a reversibility check.
