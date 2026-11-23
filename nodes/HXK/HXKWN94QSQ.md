---
tag: HXKWN94QSQ
kind: example
name: Citing a theorem with its statement is not proof by authority
msc: ["00A35", "26A15"]
topics: [T6QQ749DM5]
audience: ug1
not_instance_of:
  - target: D8A1K052XV
    note: the step names the theorem, states it and checks its hypotheses, so the reader can verify the step
uses: [D8A1K052XV, 00KAFBR32E, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: Theorem
  - url: https://en.wikipedia.org/wiki/Argument_from_authority
    locator: lead section
---

## Example

This proof leans on a famous theorem; decide whether that is a fair reason or [[proof by authority|D8A1K052XV]].

> Claim: $x^3 + x - 1 = 0$ has a real solution in $[0, 1]$.
> Let $f(x) = x^3 + x - 1$, a polynomial, so $f$ is [[continuous|0X3WGX95FE]] on $[0, 1]$, with $f(0) = -1 < 0$ and $f(1) = 1 > 0$.
> The [[intermediate value theorem|00KAFBR32E]] says that a continuous $g$ on $[a, b]$ takes every value between $g(a)$ and $g(b)$ somewhere in $[a, b]$.
> Its hypotheses hold for $g = f$ on $[0, 1]$ with the value $0$, so $f(c) = 0$ for some $c \in [0, 1]$.

It is a fair reason, and the proof is complete.

1. The proof names the result and states it in full, so the reader can look up its proof in any analysis textbook.
2. It checks each hypothesis for the given function and interval.
3. So the conclusion follows from a stated result and verified hypotheses, and it does not depend on who wrote it.

## Remarks

The difference is between an appeal to a result and an appeal to a person.
"By a theorem of Bolzano, $f$ has a root", with no statement and no check, would be close to proof by authority, because the reader cannot tell which theorem is meant or whether it applies.
On the interval $[1, 2]$, the values $f(1) = 1$ and $f(2) = 9$ have the same sign, so the hypothesis about the value $0$ fails, and the same citation gives nothing.

## Explanations

### L1 human

"My teacher says it is true" is not a reason in mathematics.
"This follows from a known rule, here is the rule, and here is why it applies" is a reason.
For example, an unbroken curve that goes from below zero to above zero must cross zero.
If we say which rule we use and check that it fits, anyone can follow the step.

### L2 human

We repair a citation that hides a failed hypothesis.
A student writes: "By the intermediate value theorem, $h(x) = \frac{1}{x}$ takes the value $0$ on $[-1, 1]$, since $h(-1) = -1$ and $h(1) = 1$."
Stating the theorem shows what it needs: $h$ continuous on the whole of $[-1, 1]$.
But $h$ is not defined at $0$, so the hypothesis fails.
The conclusion is false too, since $\frac{1}{x} \neq 0$ for every $x \neq 0$.

The typical use of this check is to write out the hypotheses of each cited theorem and verify them one by one.
Watch out for citing a famous theorem by name and skipping the check, which turns a correct citation into proof by authority.
