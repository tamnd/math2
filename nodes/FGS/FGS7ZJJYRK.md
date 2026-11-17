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

A student claims that $\sqrt{x^2} = x$ for every real number $x$, where $\sqrt{\ }$ is the non-negative [[square root|0F7FQS6XY6]].
The student writes the following argument.

1. Start from the claim $\sqrt{x^2} = x$.
2. Square both sides: $\left(\sqrt{x^2}\right)^2 = x^2$.
3. The left side is $x^2$, by the definition of the square root. So the equation becomes $x^2 = x^2$.
4. This is true for every real $x$, so the claim is "proved".

We check why this is not a [[proof of an identity|XP5SDYKJX0]].

1. The argument starts from the claim. It shows only that the claim implies the true equation $x^2 = x^2$.
2. A true conclusion does not make the starting point true. A false statement can imply a true one: from $-1 = 1$, squaring gives $1 = 1$.
3. Step 2 of the student is not reversible. From $u^2 = v^2$ we get only $u = v$ or $u = -v$, not $u = v$.
4. The claim is false. At $x = -1$, the left side is $\sqrt{(-1)^2} = \sqrt{1} = 1$, and the right side is $-1$.
5. The correct identity is $\sqrt{x^2} = \lvert x \rvert$, with the [[absolute value|0FFXKTKKQC]].

## Remarks

1. The same chain of steps can be read backward. A step "$A \Rightarrow B$" in the chain then becomes "$B \Rightarrow A$", and the squaring step fails in that direction. A legal proof needs each step to hold in the direction from the known to the claim.
2. A correct proof of $\sqrt{x^2} = \lvert x \rvert$ has two cases. If $x \ge 0$, then $x$ is a non-negative number whose square is $x^2$, so $\sqrt{x^2} = x = \lvert x \rvert$. If $x < 0$, then $-x > 0$ and $(-x)^2 = x^2$, so $\sqrt{x^2} = -x = \lvert x \rvert$.
3. When we solve an equation, squaring is allowed, because it can only add solutions. We then check each candidate in the original equation. These added solutions are the extraneous solutions.
4. Multiplication of both sides by $0$, or by an expression that can be $0$, fails in the same way. From the false claim $2x = x$, multiplication by $0$ gives the true equation $0 = 0$.
5. From the claim $\frac{x^2 - 1}{x - 1} = x + 1$ for all real $x$, multiplication by $x - 1$ gives $x^2 - 1 = (x + 1)(x - 1)$, which is true for all real $x$. But the claim fails at $x = 1$, where the left side is not defined.

## Explanations

### L1 human

Suppose someone claims that $-1$ equals $1$.
If we square both numbers, we get $1$ and $1$, which are equal.
That does not make $-1$ equal to $1$.
Squaring can make two different numbers look the same, so it cannot show that two numbers were the same.
The claim "$\sqrt{x^2}$ is always $x$" fails in exactly this way, for each negative $x$.

### L2 human

We repair a backward argument and make it a valid proof.
The claim is $(x + 1)^2 - x^2 = 2x + 1$ for every real $x$.

1. A backward argument would start from the claim and reach $2x + 1 = 2x + 1$. Its steps are additions and expansions, which are reversible, but the reader must check that.
2. A forward proof avoids the question. Let $x$ be an arbitrary real number.
3. By expanding, $(x + 1)^2 = x^2 + 2x + 1$.
4. So $(x + 1)^2 - x^2 = x^2 + 2x + 1 - x^2 = 2x + 1$.
5. This is a chain of equalities that starts at the left side and ends at the right side.

The typical use of this repair is in the writing of a proof: the scratch work may go backward, but the final proof goes forward.
A trap is the phrase "and since $1 = 1$, the identity is true", which signals a backward argument.
The reader must then check each step for reversibility.
