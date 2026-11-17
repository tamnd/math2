---
tag: ~d73ceca2
kind: example
name: An argument that starts from the conclusion a^2 + b^2 >= 2ab
msc: ["00A35", "26D05"]
topics: [958EF46EYJ]
audience: school
not_instance_of:
  - target: 0NTF6DMVAP
    note: the chain starts from the conclusion and ends with a true statement, so it does not derive the conclusion from the hypotheses
uses: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_proof
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.1
---

## Example

Statement: for all real numbers $a$ and $b$, $a^2 + b^2 \geq 2ab$.
A student writes this argument.

1. $a^2 + b^2 \geq 2ab$.
2. So $a^2 - 2ab + b^2 \geq 0$.
3. So $(a - b)^2 \geq 0$.
4. This is true, because a square of a real number is never negative.

The argument is not a [[direct proof|0NTF6DMVAP]] of the statement.
We check the condition that fails.

1. A direct proof must start from the hypotheses and known facts, and it must end with the conclusion.
2. The argument starts with the conclusion in its line 1. So it assumes what it wants to prove.
3. It ends with a true statement in line 4. So it shows only "if $a^2 + b^2 \geq 2ab$, then $(a - b)^2 \geq 0$".
4. An implication with a true conclusion is true whatever its hypothesis is. So line 4 gives no information about line 1.

## Remarks

Here the steps can be reversed, so a correct direct proof exists.

1. For all real $a$ and $b$, $(a - b)^2 \geq 0$, because a square of a real number is never negative.
2. Expand: $a^2 - 2ab + b^2 \geq 0$.
3. Add $2ab$ to both sides: $a^2 + b^2 \geq 2ab$.

The reversed chain is the proof, and the student's chain is only the scratch work that finds it.
The danger shows when a step cannot be reversed.
From the false claim $-1 = 1$, squaring gives $1 = 1$, which is true.
So "starting from the claim and reaching a truth" can also happen for a false claim.

## Explanations

### L1 human

An argument that starts from the claim can end with a true sentence even when the claim is false.
For example, start from the false claim $-1 = 1$ and square both sides.
The result is $1 = 1$, a true sentence.
So reaching a true sentence does not show that the starting claim is true.
A proof must start from facts and end with the claim, not the other way.

### L2 human

We compare the two directions for the claim $x + \frac{1}{x} \geq 2$ for real $x > 0$.

1. Scratch work, from the goal: $x + \frac{1}{x} \geq 2$, so $x^2 + 1 \geq 2x$ (multiply by $x > 0$), so $(x - 1)^2 \geq 0$.
2. Check each step backward: from $(x - 1)^2 \geq 0$ we get $x^2 + 1 \geq 2x$ by expanding and adding $2x$. Dividing by $x > 0$ gives $x + \frac{1}{x} \geq 2$.
3. Write the proof in the order of step 2.

The typical use of scratch work from the goal is to find the proof; the [[forward-backward method|~f8b8bc06]] makes this systematic.

A trap: multiplying an inequality by $x$ keeps its direction only when $x > 0$.
Without the hypothesis $x > 0$, the claim fails: $x = -1$ gives $-1 + \frac{1}{-1} = -2$.
