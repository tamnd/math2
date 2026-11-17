---
tag: 0NNQ4KFEX7
kind: definition
name: Associativity
msc: [08A02]
topics: [BAZT8JJ70S]
audience: school
defines: 0K8F7PVDMX
uses: [0580ZJSA3Q]
formal:
  - system: lean4
    library: mathlib
    decl: Std.Associative
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Associative_property
    locator: Definition
  - book: isbn:9780471433347
    locator: Section 1.1
---

## Definition

Let $S$ be a set and let $\ast$ be a [[binary operation|0M418FE7BB]] on $S$.
The operation $\ast$ is associative when $(a \ast b) \ast c = a \ast (b \ast c)$ for all $a, b, c \in S$.

## Notation

For an associative operation, we write $a \ast b \ast c$, or $abc$, without parentheses.
In Mathlib, the class `Std.Associative op` states that the function `op` satisfies `op (op a b) c = op a (op b c)` for all `a`, `b`, `c`.

## Remarks

Addition and multiplication of real numbers are associative.
Subtraction of integers is not associative: $(1 - 1) - 1 = -1$, but $1 - (1 - 1) = 1$.
Composition of maps from a set to itself is associative.
For an associative operation, each way to put parentheses in $a_1 \ast a_2 \ast \cdots \ast a_n$ gives the same result, by [[general associativity|~d51940ae]].
The concept page [[associativity|0K8F7PVDMX]] gives more examples, the non-examples and the first properties.

## Explanations

### L1 human

Associativity says that you can do the operations in a chain in any grouping.
For example, $(2 + 3) + 4$ and $2 + (3 + 4)$ are both $9$.
Thus we can write $2 + 3 + 4$ without parentheses.
The order of the numbers must stay the same.

### L2 human

To check that an operation is associative, take three arbitrary elements $a, b, c$, compute $(a \ast b) \ast c$ and $a \ast (b \ast c)$, and show that the results are equal.
To show that an operation is not associative, one triple with different results is enough.
A trap is to test only triples with a special element, such as $0$ for subtraction, where the law can hold by chance.
