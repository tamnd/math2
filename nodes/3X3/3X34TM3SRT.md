---
tag: 3X34TM3SRT
kind: example
name: Affirming a disjunct is not disjunctive syllogism
msc: ["03B05", "97E30"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 6EFJF9NAYX
    note: the second premise affirms a disjunct instead of denying it, and the form is not valid for the inclusive "or"
uses: [6EFJF9NAYX, 0F72FK8EKB, 05RSK4Q657, T5BG7Y4J0T]
sources:
  - url: https://en.wikipedia.org/wiki/Affirming_a_disjunct
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Disjunctive_syllogism
    locator: lead section
---

## Example

Consider this argument about an integer $n$.
"The number $n$ is divisible by $2$ or by $3$.
It is divisible by $2$.
So it is not divisible by $3$."
Let $p$ be "$2 \mid n$" and $q$ be "$3 \mid n$".
The form is: from $p \lor q$ and $p$, conclude $\neg q$.
This form is called affirming a disjunct, and we show that it is neither [[disjunctive syllogism|6EFJF9NAYX]] nor valid.

1. Disjunctive syllogism needs the negation $\neg p$ of a disjunct as its second premise.
   Here the second premise is $p$ itself, so the argument does not have the form of the rule.
2. A form is valid only when every row of the [[truth table|05RSK4Q657]] that makes the premises true also makes the conclusion true.
3. Take the row $p = \mathrm{T}$, $q = \mathrm{T}$.
   By the table of the [[disjunction|0F72FK8EKB]], $p \lor q = \mathrm{T}$, and $p = \mathrm{T}$, so both premises are true.
4. In the same row $\neg q = \mathrm{F}$, so the conclusion is false.
5. So the form is not valid.
   The integer $n = 6 = 2 \cdot 3$ realizes this row: both premises are true, and the conclusion "$3 \nmid 6$" is false.

## Remarks

The example shows that the inclusive "or" of mathematics allows both disjuncts to be true, so the truth of one disjunct says nothing about the other.

Two changes to the first premise give a valid argument.
If the first premise is the [[exclusive or|PTMR3P9J6C]] $p \oplus q$, the row $p = q = \mathrm{T}$ makes it false, and from $p \oplus q$ and $p$ the conclusion $\neg q$ does follow.
If the first premise is $\neg (p \land q)$, "$n$ is not divisible by both $2$ and $3$", then $p$ again gives $\neg q$.
Affirming a disjunct sits beside the other invalid forms on the page [[formal fallacies|T5BG7Y4J0T]].

## Explanations

### L1 human

"The cafe sells tea or coffee" is true when it sells both.
So the fact that it sells tea does not show that it has no coffee.
With numbers: $6$ is even or a multiple of $3$, and $6$ is even, but $6$ is also a multiple of $3$.
Knowing that one part of an "or" is true tells you nothing about the other part.

### L2 human

Test two arguments that both start from "$x \ge 0$ or $x \le 0$" for a real number $x$.
Argument A says "$x \ge 0$, so $x \le 0$ is false", that is, "so $x > 0$".
It affirms the disjunct $x \ge 0$, and $x = 0$ makes both premises true and the conclusion $0 > 0$ false.
Argument B says "$x \ge 0$ is false, so $x \le 0$".
It denies a disjunct, so it is disjunctive syllogism, and it is valid.
When you read a case analysis, remember that a case that holds excludes the other cases only when the cases are disjoint.
Watch out for the everyday reading of "or" as "one or the other but not both", which makes argument A feel correct.
