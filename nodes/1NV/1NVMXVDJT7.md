---
tag: 1NVMXVDJT7
kind: example
name: The ternary majority connective
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: ug1
instance_of: [QS0XVAN9BG]
uses: [QS0XVAN9BG, CA49F5KQGB, 025YZN3VJW, 0F72FK8EKB]
sources:
  - url: https://en.wikipedia.org/wiki/Majority_function
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Truth_function
    locator: lead section
---

## Example

A committee of three votes, and a motion passes when at least two members vote yes.
Let $p$, $q$, $r$ say that the first, second and third member votes yes, and define $\operatorname{maj}(p, q, r)$ to be true when at least two of $p$, $q$, $r$ are true.
We check that $\operatorname{maj}$ is a [[logical connective|QS0XVAN9BG]] of arity $3$, with the same truth table as
$$(p \land q) \lor (p \land r) \lor (q \land r).$$

1. The value of $\operatorname{maj}$ depends only on the number of true inputs, so it is a truth function of the three values.
   By the [[definition|CA49F5KQGB]], $\operatorname{maj}$ is a connective of arity $3$.
2. The table lists the $2^3 = 8$ rows, the number $k$ of true inputs, and both values.

| $p$ | $q$ | $r$ | $k$ | $\operatorname{maj}(p, q, r)$ | $(p \land q) \lor (p \land r) \lor (q \land r)$ |
|---|---|---|---|---|---|
| T | T | T | 3 | T | T |
| T | T | F | 2 | T | T |
| T | F | T | 2 | T | T |
| T | F | F | 1 | F | F |
| F | T | T | 2 | T | T |
| F | T | F | 1 | F | F |
| F | F | T | 1 | F | F |
| F | F | F | 0 | F | F |

3. If $k \ge 2$, then two of the inputs are true, so the [[conjunction|025YZN3VJW]] of these two is true, and the [[disjunction|0F72FK8EKB]] is true.
4. If $k \le 1$, then each of the three conjunctions contains a false input, so each is false, and the disjunction is false.
5. Steps 3 and 4 show that the two columns agree in all $8$ rows.

## Remarks

### A formula without negation

The formula is a [[disjunctive normal form|0GVDFAY4KW]] without negations.
This is possible because $\operatorname{maj}$ is monotone: making an input true never makes the value false.
A connective such as negation, which turns T into F, needs $\neg$ in every formula for it.

### Larger votes and circuits

The majority of $2m + 1$ inputs is true when at least $m + 1$ inputs are true.
For an even number of inputs a tie is possible, and the definition must say what happens in a tie.
In circuit design, $\operatorname{maj}(a, b, c)$ is the carry bit of the sum $a + b + c$ of three bits.

## Explanations

### L1 human

Three friends vote yes or no.
The group says yes when at least two friends say yes.
This rule takes three answers and gives one answer.
It looks only at the answers, so it is a connective with three inputs.

### L2 human

Use the majority connective to compute the carry of a binary addition.

1. Add the bits $a = 1$ and $b = 1$ and the incoming carry $c = 0$.
2. The sum is $1 + 1 + 0 = 2$, which is $10$ in binary.
3. So the new carry is $1$, and the sum bit is $0$.
4. With $1$ as T and $0$ as F, the majority gives $\operatorname{maj}(\mathrm{T}, \mathrm{T}, \mathrm{F}) = \mathrm{T}$, which is the carry $1$.

Ternary connectives such as this one appear in circuits and in coding, where one output depends on several inputs.
Watch out: $\operatorname{maj}(p, q, r)$ is not $p \land q \land r$.
The row TTF gives T for the majority and F for the conjunction.
