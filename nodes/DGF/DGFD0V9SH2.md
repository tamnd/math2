---
tag: DGFD0V9SH2
kind: example
name: Two readings of "x plus y squared"
msc: ["97E40", "97H20"]
topics: [WMY13MXY3W]
audience: school
instance_of: [8BZPKYF912]
uses: [8BZPKYF912]
sources:
  - url: https://en.wikipedia.org/wiki/Order_of_operations
    locator: lead section
---

## Example

A teacher says aloud: "$x$ plus $y$ squared".
Spoken words have no parentheses, so the phrase has two readings, an instance of [[ambiguity in mathematical language|8BZPKYF912]].
We write both and show that they differ.

1. Reading 1: the sum is squared, $(x + y)^2$.
2. Reading 2: only $y$ is squared, $x + y^2$.
3. For $x = 1$ and $y = 2$, reading 1 gives $(1 + 2)^2 = 9$.
4. For the same values, reading 2 gives $1 + 2^2 = 5$.
5. The values differ, so the two readings are different expressions. The phrase alone does not say which one is meant.

## Remarks

The written order of operations settles the written form: $x + y^2$ means $x + (y^2)$, because powers come before sums.
Speech has no such rule, so speakers mark the grouping.
"The quantity $x$ plus $y$, squared" or "the square of $x + y$" gives reading 1, and "$x$ plus the square of $y$" gives reading 2.
A pause after "$x$ plus $y$" often signals reading 1, but a listener can miss it.

The same problem arises in writing with a minus sign.
By the order of operations, $-3^2 = -(3^2) = -9$, and $(-3)^2 = 9$.
The phrase "minus three squared" can mean either one.

## Explanations

### L1 human

"Two plus three times four" can be worked out in two ways.
Add first: $2 + 3 = 5$, then $5 \times 4 = 20$.
Multiply first: $3 \times 4 = 12$, then $2 + 12 = 14$.
Written as $2 + 3 \times 4$, the rule "multiply before add" gives $14$.
To mean $20$, we write $(2 + 3) \times 4$.

### L2 human

We find all readings of "the square root of $x$ plus $1$" and test them at $x = 8$.

1. Reading 1: the root of the sum, $\sqrt{x + 1}$. At $x = 8$, this is $\sqrt{9} = 3$.
2. Reading 2: the root plus one, $\sqrt{x} + 1$. At $x = 8$, this is $2\sqrt{2} + 1 \approx 3.83$.
3. The values differ, so the phrase is ambiguous. The written forms $\sqrt{x + 1}$ and $\sqrt{x} + 1$ are not, because the bar of the root sign shows its scope.

The typical use of this test is in dictated or spoken mathematics: one trial value shows whether two readings differ.

A trap: if the two readings agree for the trial value, the test proves nothing.
For $x = 0$ and $y = 0$, both readings of "$x$ plus $y$ squared" give $0$.
