---
tag: ~fced09ad
kind: example
name: If a + b >= 100, then a >= 50 or b >= 50
msc: ["00A35", "26D05"]
topics: [958EF46EYJ]
audience: school
instance_of: [0BB5TPGQ1N]
uses: [0BB5TPGQ1N, K930V33BSC, 09PKJKA6J0]
sources:
  - url: https://en.wikipedia.org/wiki/Contraposition
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.2
---

## Example

Statement: for all real numbers $a$ and $b$, if $a + b \geq 100$, then $a \geq 50$ or $b \geq 50$.
We give a [[proof by contrapositive|0BB5TPGQ1N]].

1. The conclusion is "$a \geq 50$ or $b \geq 50$". By [[De Morgan's laws|09PKJKA6J0]], its negation is "$a < 50$ and $b < 50$".
2. The negation of the hypothesis $a + b \geq 100$ is $a + b < 100$.
3. So the contrapositive is: if $a < 50$ and $b < 50$, then $a + b < 100$.
4. Assume $a < 50$ and $b < 50$.
5. Add the two inequalities: $a + b < 50 + 50 = 100$.
6. This proves the contrapositive, and therefore the statement.

## Remarks

The conclusion of the statement is an "or", and a direct proof would have to decide which of $a$ and $b$ is large.
The negated conclusion is an "and", which gives two facts to use at once.
This is a common reason to choose the contrapositive.

The constant $50$ is the largest that works.
The statement "if $a + b \geq 100$, then $a \geq 51$ or $b \geq 51$" is false for $a = b = 50$.
For $n$ real numbers, the same proof gives: if $a_1 + \cdots + a_n \geq S$, then $a_i \geq S / n$ for some $i$.
This is the averaging idea behind the [[pigeonhole principle|0HGVCWQGY3]].

## Explanations

### L1 human

Two friends together have at least $100$ coins.
Then at least one of them has at least $50$ coins.
Why: if both had fewer than $50$, together they would have fewer than $100$.
That last sentence is the contrapositive, and it is the whole proof.
For example, $49$ coins and $49$ coins make only $98$.

### L2 human

We use the same idea on three numbers: if $a + b + c \geq 30$, then at least one of $a$, $b$, $c$ is at least $10$.

1. Negate the conclusion: "$a < 10$ and $b < 10$ and $c < 10$".
2. Assume these three inequalities.
3. Add them: $a + b + c < 30$.
4. This proves the contrapositive.

The typical use: a statement "some part is large" is proved by assuming "all parts are small" and adding.

A trap: negating "$a \geq 10$ or $b \geq 10$ or $c \geq 10$" as "$a < 10$ or $b < 10$ or $c < 10$".
This keeps the "or", and the proof in step 3 then fails, because only one inequality is known.
