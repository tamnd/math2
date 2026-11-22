---
tag: 3ENDPQZA6V
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

Statement: for all real numbers $a$ and $b$, if $a + b \ge 100$, then $a \ge 50$ or $b \ge 50$.
We give a [[proof by contrapositive|0BB5TPGQ1N]].

1. The conclusion is "$a \ge 50$ or $b \ge 50$".
   By [[De Morgan's laws|09PKJKA6J0]], its negation is "$a < 50$ and $b < 50$".
2. The negation of the hypothesis $a + b \ge 100$ is $a + b < 100$.
3. So the contrapositive is: if $a < 50$ and $b < 50$, then $a + b < 100$.
4. Assume $a < 50$ and $b < 50$, and add the two inequalities:
   $$a + b < 50 + 50 = 100.$$
5. This proves the contrapositive, and therefore the statement.

## Remarks

The conclusion is an "or", so a direct proof would have to decide which of $a$ and $b$ is the large one.
The negated conclusion is an "and", which hands us two facts at once.
This is one of the most common reasons to choose the contrapositive.

The constant $50$ is the best possible.
The stronger claim "if $a + b \ge 100$, then $a \ge 51$ or $b \ge 51$" fails for $a = b = 50$.
For $n$ real numbers the same proof gives: if $a_1 + \dots + a_n \ge S$, then $a_i \ge S / n$ for some $i$.
If every $a_i$ were less than $S / n$, the sum would be less than $n \cdot S / n = S$.
This averaging idea is behind the [[pigeonhole principle|0HGVCWQGY3]].

## Explanations

### L1 human

Two friends together have at least $100$ coins.
Then at least one of them has at least $50$ coins.
Why: if both had fewer than $50$, together they would have fewer than $100$.
That last sentence is the contrapositive, and it is the whole proof.
For example, $49$ coins and $49$ coins make only $98$.

### L2 human

The same idea works for three numbers: if $a + b + c \ge 30$, then at least one of $a$, $b$, $c$ is at least $10$.
Negate the conclusion to get "$a < 10$ and $b < 10$ and $c < 10$", and assume these three inequalities.
Adding them gives
$$a + b + c < 10 + 10 + 10 = 30,$$
which is the negated hypothesis, so the contrapositive holds.
The typical use is the one shown: a claim "some part is large" is proved by assuming "every part is small" and adding.
Watch out: the negation "$a < 10$ or $b < 10$ or $c < 10$" keeps the "or", and with only one inequality known the sum cannot be bounded.
