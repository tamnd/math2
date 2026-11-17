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

Consider the argument:

- Premise 1: the integer $n$ is divisible by $2$ or $n$ is divisible by $3$.
- Premise 2: $n$ is divisible by $2$.
- Conclusion: so $n$ is not divisible by $3$.

Let $p$ be "$2 \mid n$" and $q$ be "$3 \mid n$".
The form of the argument is: from $p \lor q$ and $p$, conclude $\neg q$.
This form is called affirming a disjunct.
We show that it is not an instance of [[disjunctive syllogism|6EFJF9NAYX]] and that it is not valid.

1. Disjunctive syllogism needs the negation $\neg p$ of a disjunct as its second premise. Here the second premise is $p$ itself, so the argument does not have the form of the rule.
2. A form is valid only when every row of the [[truth table|05RSK4Q657]] that makes the premises true makes the conclusion true.
3. Take the row $p = \mathrm{T}$, $q = \mathrm{T}$. Then $p \lor q = \mathrm{T}$ by the table of the [[disjunction|0F72FK8EKB]], and $p = \mathrm{T}$, so both premises are true.
4. In the same row, $\neg q = \mathrm{F}$, so the conclusion is false.
5. So the form is not valid. The integer $n = 6$ realizes this row: $6 = 2 \cdot 3$, so both premises are true, and the conclusion "$3 \nmid 6$" is false.

## Remarks

The example shows that the inclusive "or" of mathematics allows both disjuncts to be true, so the truth of one disjunct says nothing about the other.

Two changes make a valid argument.

- Replace the first premise by the [[exclusive or|PTMR3P9J6C]] $p \oplus q$. The row $p = q = \mathrm{T}$ then makes the first premise false, and from $p \oplus q$ and $p$ the conclusion $\neg q$ follows.
- Replace the first premise by $\neg (p \land q)$, "$n$ is not divisible by both $2$ and $3$". From $\neg (p \land q)$ and $p$ the conclusion $\neg q$ follows.

Affirming a disjunct is a formal fallacy, like the forms on the page [[formal fallacies|T5BG7Y4J0T]].

## Explanations

### L1 human

"The café sells tea or coffee" is true when it sells both.
So the fact that it sells tea does not show that it does not sell coffee.
With numbers: $6$ is even or a multiple of $3$, and $6$ is even, but $6$ is also a multiple of $3$.
Knowing that one part of an "or" is true tells nothing about the other part.

### L2 human

We test two arguments with the premise "$x \ge 0$ or $x \le 0$" for a real number $x$.

1. Argument A: "$x \ge 0$, so $x \le 0$ is false", that is, "so $x > 0$". This affirms the disjunct $x \ge 0$. The number $x = 0$ makes both premises true and the conclusion $0 > 0$ false.
2. Argument B: "$x \ge 0$ is false, so $x \le 0$". This denies a disjunct, so it is disjunctive syllogism, and it is valid.

The typical use of this check is in the reading of a case analysis: a case that holds does not exclude the other cases unless the cases are disjoint.
A trap is the everyday reading of "or" as "one or the other but not both".
