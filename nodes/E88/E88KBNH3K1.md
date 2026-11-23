---
tag: E88KBNH3K1
kind: example
name: An omitted symmetric case in max(a, b) + min(a, b) = a + b
msc: ["00A35", "26A06"]
topics: [STSM6PR7TX]
audience: ug2
instance_of: [VYGBV5D8Y4]
uses: [VYGBV5D8Y4, 5X1YMSR204, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof terminology
  - url: https://en.wikipedia.org/wiki/Without_loss_of_generality
    locator: lead section
---

## Example

The statement is that for all real numbers $a$ and $b$, $\max(a, b) + \min(a, b) = a + b$.
Here $\max(a, b)$ is the larger and $\min(a, b)$ the smaller of the two numbers, as in [[maximum and minimum|5X1YMSR204]].
The proof as written handles one case and omits the other.

> We consider two cases.
> If $a \ge b$, then $\max(a, b) = a$ and $\min(a, b) = b$, so the sum is $a + b$.
> The case $b \ge a$ is the same with $a$ and $b$ exchanged.
> $\square$

We check that the omission is acceptable for the [[level of detail|VYGBV5D8Y4]] of a second-year reader.
The statement is symmetric in $a$ and $b$, since $\max(a, b) = \max(b, a)$, $\min(a, b) = \min(b, a)$ and $a + b = b + a$.
The case $b \ge a$ is the written case applied to the pair $(b, a)$, which gives $\max(b, a) + \min(b, a) = b + a$, and by symmetry this is the statement for $(a, b)$.
Written in full, the omitted case reads: if $b \ge a$, then $\max(a, b) = b$ and $\min(a, b) = a$, so the sum is $b + a = a + b$.
The two cases cover all pairs, because $a \ge b$ or $b \ge a$ for real numbers, and when $a = b$ both cases apply and agree.

So the omitted step is true, it needs no new idea, and any reader who follows the first case can write the second.

## Remarks

A case that follows from a written case by renaming is the most common acceptable omission in a [[proof by cases|0WCP0PVET6]].
The test for it is the symmetry of the statement.
"Without loss of generality, $a \ge b$" makes the same omission at the start of a proof, and the same symmetry justifies it.

The shortcut is wrong for a statement that is not symmetric.
The claim $\max(a, b) - \min(a, b) = a - b$ holds when $a \ge b$, but for $a = 1$ and $b = 3$ the left side is $2$ and the right side is $-2$.
The correct statement, $\max(a, b) - \min(a, b) = \lvert a - b \rvert$, is symmetric, because $\lvert a - b \rvert = \lvert b - a \rvert$.

## Explanations

### L1 human

Take two numbers, for example $3$ and $8$.
The larger is $8$, the smaller is $3$, and $8 + 3 = 11$, which is $3 + 8$.
The proof first handles the case where the first number is the larger.
For the other case it says "the same, with the names swapped".
This shortcut is fair, because swapping the two numbers does not change the question.

### L2 human

We test the shortcut on a statement where it fails and on one where it works.
For $\max(a, b) - \min(a, b) = a - b$, the case $a \ge b$ holds, since the left side is $a - b$.
Exchanging the names gives $\max(b, a) - \min(b, a) = b - a$, which is a different claim unless $a = b$, so the case $b > a$ does not follow by renaming.
For $\max(a, b) \cdot \min(a, b) = ab$, the case $a \ge b$ also holds, and exchanging the names gives $\max(b, a) \cdot \min(b, a) = ba$, which is the same claim because $ba = ab$.
So for the product the omitted case is acceptable, and for the difference it is not.

The shortcut suits proofs about two or more objects that play the same role.
Watch out: before writing "similarly" or "by symmetry", exchange the names in the statement and check that it does not change.
