---
tag: 2VA8Q8BG5Y
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

The claim is: for all real numbers $a$ and $b$, $a^2 + b^2 \geq 2ab$.
A student writes this argument.

1. $a^2 + b^2 \geq 2ab$.
2. So $a^2 - 2ab + b^2 \geq 0$.
3. So $(a - b)^2 \geq 0$.
4. This is true, because the square of a real number is never negative.

The argument is not a [[direct proof|0NTF6DMVAP]] of the claim, and we can say which condition fails.
A direct proof must start from the hypotheses and from known facts, and it must end with the conclusion.
The student's line 1 is the conclusion itself, so the argument assumes what it wants to prove.
It ends with a true statement in line 4, so what it shows is "if $a^2 + b^2 \geq 2ab$, then $(a - b)^2 \geq 0$".
An implication whose conclusion is true holds whatever its hypothesis is, so line 4 tells us nothing about line 1.

## Remarks

In this case each step can be reversed, so a correct direct proof exists, and it is the student's chain read from the bottom up.

1. For all real $a$ and $b$, $(a - b)^2 \geq 0$, because the square of a real number is never negative.
2. Expand the square:
   $$a^2 - 2ab + b^2 \geq 0.$$
3. Add $2ab$ to both sides to get $a^2 + b^2 \geq 2ab$.

So the student's work is good scratch work that finds the proof, but the proof must be written in the reverse order.
The danger is real when a step cannot be reversed.
Start from the false claim $-1 = 1$ and square both sides.
You get $1 = 1$, which is true, so "start from the claim and reach a truth" can happen even when the claim is false.

## Explanations

### L1 human

An argument that starts from the claim can end with a true sentence even when the claim is false.
For example, start from the false claim $-1 = 1$ and square both sides.
The result is $1 = 1$, a true sentence.
So reaching a true sentence does not show that the starting claim is true.
A proof must start from facts and end with the claim, not the other way round.

### L2 human

Take the claim $x + \frac{1}{x} \geq 2$ for every real $x > 0$, and do the scratch work from the goal first.
Multiply by $x > 0$ and move every term to one side:
$$x + \frac{1}{x} \geq 2 \quad \text{becomes} \quad x^2 + 1 \geq 2x \quad \text{becomes} \quad (x - 1)^2 \geq 0.$$
Now check that each step runs backward.
From $(x - 1)^2 \geq 0$, expanding and adding $2x$ gives $x^2 + 1 \geq 2x$, and dividing by $x > 0$ gives $x + \frac{1}{x} \geq 2$.
The written proof follows this backward check, from $(x - 1)^2 \geq 0$ to the claim.
Working from the goal to find a proof is normal, and the [[forward-backward method|V8ZB838JY5]] makes it systematic.
Watch out: multiplying or dividing by $x$ keeps the direction of an inequality only when $x > 0$, and the claim fails without that hypothesis, since $x = -1$ gives $-1 + \frac{1}{-1} = -2$.
