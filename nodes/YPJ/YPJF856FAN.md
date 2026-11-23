---
tag: YPJF856FAN
kind: example
name: A counterfactual conditional is not a material implication
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 0NMG7W7Q11
    note: the truth of a counterfactual is not a function of the truth values of its antecedent and consequent
uses: [0NMG7W7Q11, 0ZNX6DQ3EJ, QS0XVAN9BG]
sources:
  - url: https://en.wikipedia.org/wiki/Counterfactual_conditional
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Material_conditional
    locator: lead section
---

## Example

A counterfactual conditional has the form "if $A$ were the case, then $B$ would be the case", where $A$ is in fact false.
Compare two counterfactuals about the number $9$.
$C_1$ is "if $9$ were even, then $9$ would be divisible by $2$".
$C_2$ is "if $9$ were even, then $9$ would be divisible by $5$".
We show that "if ... were, then ... would" is not the [[material implication|0NMG7W7Q11]], because its value is not a function of the truth values of its parts.

1. The antecedent "$9$ is even" is false in both, because $9 = 2 \cdot 4 + 1$.
2. The consequent "$9$ is divisible by $2$" of $C_1$ is false, by step 1.
3. The consequent "$9$ is divisible by $5$" of $C_2$ is false, because $9 = 5 \cdot 1 + 4$.
4. So $C_1$ and $C_2$ have the same values of the parts, antecedent F and consequent F.
   The material implication gives T in the row FF of its [[truth table|0ZNX6DQ3EJ]] for both.
5. A competent speaker accepts $C_1$, because "even" means "divisible by $2$".
   The same speaker rejects $C_2$, because being even gives no divisor $5$.
6. The verdicts on $C_1$ and $C_2$ differ, although the values of the parts are the same.
   So no truth function of the two parts gives the meaning of a counterfactual, and a counterfactual is not a material implication.

## Remarks

### Many kinds of "if"

English "if" covers more than one connective.
Material implication is a [[logical connective|QS0XVAN9BG]] in the strict sense: its value depends only on the values of its parts.
A counterfactual depends on what would follow if the facts were different, and that is not a truth value.
Logics of counterfactuals use possible worlds, as in [[modal logic|C3RZY20ETK]].

### The indicative version

Replace the counterfactuals by "if $9$ is even, then $9$ is divisible by $2$" and "if $9$ is even, then $9$ is divisible by $5$".
Both are material implications with a false antecedent, so both are true, as step 4 computes.
So the difference between $C_1$ and $C_2$ lies in the word "would", not in the truth values.

## Explanations

### L1 human

"If a cat were a bird, it could fly" and "if a cat were a bird, it could speak French" both start with something false.
Both end with something false about cats.
Most people accept the first sentence and reject the second.
So the truth of such a sentence is not decided by the truth of its parts alone.
The "if, then" of logic is decided by its parts alone, so it is a different thing.

### L2 human

Test whether a phrase defines a truth-functional connective.

1. Find two sentences of that form whose parts have the same values.
   Here the parts of $C_1$ and $C_2$ are F and F.
2. Compare the values of the two whole sentences.
   Here $C_1$ is accepted and $C_2$ is rejected.
3. The values in step 2 differ, so the phrase is not truth-functional.

This test decides whether a [[truth table|05RSK4Q657]] can analyze a sentence.
Watch out: the test can only show that a phrase is not truth-functional.
Equal values in step 2 for one pair prove nothing about all pairs.
