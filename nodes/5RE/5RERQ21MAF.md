---
tag: 5RERQ21MAF
kind: example
name: The expression 2 + 3 · 4 has one value under every convention
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
not_instance_of:
  - target: CSFEP56A7D
    note: every standard convention gives multiplication precedence over addition, so the value 14 does not depend on the source
uses: [CSFEP56A7D, QKEX4PD029]
sources:
  - url: https://en.wikipedia.org/wiki/Order_of_operations
    locator: lead section
---

## Example

A puzzle online asks "what is $2 + 3 \cdot 4$?" and claims that people disagree.
We evaluate the expression and show that no standard convention gives a second value.

1. The shared rule of precedence is that multiplication binds more strongly than addition.
2. So
   $$2 + 3 \cdot 4 = 2 + (3 \cdot 4) = 2 + 12 = 14.$$
3. The other bracketing, $(2 + 3) \cdot 4 = 20$, is not the reading of any standard textbook, scientific calculator or programming language.
4. So the expression has one meaning, and it is not an instance of a [[conflicting convention|CSFEP56A7D]].

Now compare the expression $6 / 2(1 + 2)$.

5. If multiplication by juxtaposition binds more strongly than the slash, the expression is
   $$\frac{6}{2(1 + 2)} = \frac{6}{6} = 1.$$
6. If the slash and juxtaposition have equal precedence and are read from left to right, the expression is
   $$\frac{6}{2} \cdot (1 + 2) = 3 \cdot 3 = 9.$$
7. Both readings occur in published texts, so this expression is a real conflict, and careful authors add brackets.

## Remarks

The example separates a fixed rule from a conflict.
The precedence of $\cdot$ over $+$ is shared by all standard sources, so it is part of [[mathematical notation|QKEX4PD029]] and not a choice.
The precedence of juxtaposition over the slash is not shared, so an expression such as $6 / 2(1 + 2)$ needs brackets.
In displayed formulas the fraction bar removes the problem, because the layout shows the numerator and the denominator.

## Explanations

### L1 human

In $2 + 3 \cdot 4$ we multiply first, so we get $2 + 12 = 14$.
Every book and every scientific calculator agrees on this rule.
So this expression has only one answer.

### L2 human

Evaluate $1 - 2 \cdot 3 + 4$ with the shared rules.
Multiplication comes first, so $2 \cdot 3 = 6$ and the expression becomes $1 - 6 + 4$.
Addition and subtraction have equal precedence and go from left to right:
$$1 - 6 + 4 = (1 - 6) + 4 = -5 + 4 = -1.$$
The reading $1 - (6 + 4) = -9$ breaks the left-to-right rule, and no standard source uses it.
The left-to-right rule matters exactly for subtraction and division, which are not associative.
Watch out: $8 - 3 - 2 = (8 - 3) - 2 = 3$, but $8 - (3 - 2) = 7$.
