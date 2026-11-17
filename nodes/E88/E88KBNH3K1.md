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

*Statement.* For all real numbers $a$ and $b$, $\max(a, b) + \min(a, b) = a + b$.
Here $\max(a, b)$ is the larger and $\min(a, b)$ is the smaller of the two numbers, as on the page [[maximum and minimum|5X1YMSR204]].

*Proof as written.*
We consider two cases.
If $a \ge b$, then $\max(a, b) = a$ and $\min(a, b) = b$, so the sum is $a + b$.
The case $b \ge a$ is the same with $a$ and $b$ exchanged.
$\square$

We check that the omitted case is an acceptable omission.

1. The statement is symmetric in $a$ and $b$: $\max(a, b) = \max(b, a)$, $\min(a, b) = \min(b, a)$, and $a + b = b + a$. So exchanging the names gives the same statement.
2. The case $b \ge a$ is the case "first number $\ge$ second number" for the pair $(b, a)$. The written case, applied to this pair, gives $\max(b, a) + \min(b, a) = b + a$.
3. By step 1, this equation is the statement for $(a, b)$.
4. Written in full, the omitted case reads: if $b \ge a$, then $\max(a, b) = b$ and $\min(a, b) = a$, so the sum is $b + a = a + b$.
5. The two cases cover all pairs, because for real numbers $a \ge b$ or $b \ge a$. When $a = b$ both cases apply, and they give the same result.

So the omission is true, it needs no new idea, and any reader who follows the first case can write the second one.

## Remarks

1. The example shows a typical acceptable omission in a [[proof by cases|0WCP0PVET6]]: a case that follows from a written case by renaming. The test for it is the symmetry of the statement, step 1 above.
2. The same omission is wrong for a statement that is not symmetric. The claim $\max(a, b) - \min(a, b) = a - b$ holds in the case $a \ge b$, but for $a = 1$ and $b = 3$ the left side is $2$ and the right side is $-2$.
3. The correct statement for the difference is $\max(a, b) - \min(a, b) = \lvert a - b \rvert$, which is symmetric, because $\lvert a - b \rvert = \lvert b - a \rvert$.
4. The phrase "without loss of generality, $a \ge b$" makes the same omission at the start of the proof. It is justified by the same symmetry.

## Explanations

### L1 human

Take two numbers, for example $3$ and $8$.
The larger is $8$, the smaller is $3$, and $8 + 3 = 11$, which is $3 + 8$.
The proof first handles the case where the first number is the larger.
For the other case it says "the same, with the names swapped".
This shortcut is fair, because swapping the two numbers does not change the question.

### L2 human

We test the shortcut on a statement where it fails, and on one where it works.

1. The claim $\max(a, b) - \min(a, b) = a - b$: for $a \ge b$, the left side is $a - b$. So the written case holds.
2. Exchange $a$ and $b$: the claim becomes $\max(b, a) - \min(b, a) = b - a$, which is a different claim, because $b - a \ne a - b$ unless $a = b$.
3. So the case $b > a$ does not follow by renaming. For $a = 1$, $b = 3$ the claim fails, since $3 - 1 = 2$ and $1 - 3 = -2$.
4. The claim $\max(a, b) \cdot \min(a, b) = ab$: for $a \ge b$, the left side is $ab$. Exchanging the names gives $\max(b, a) \cdot \min(b, a) = ba$, which is the same claim, because $ba = ab$.
5. So for the product the omitted case is acceptable.

The typical use of the shortcut is in proofs about two or more objects that play the same role.
A trap is to write "similarly" or "by symmetry" for a statement that changes under the exchange, as in step 2.
