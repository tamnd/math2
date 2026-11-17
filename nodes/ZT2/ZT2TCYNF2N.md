---
tag: ZT2TCYNF2N
kind: example
name: The sum of the maximum and the minimum of two numbers
msc: ["00A35", "26A03"]
topics: [958EF46EYJ]
audience: school
instance_of: [Y7NE0E6PCV]
uses: [Y7NE0E6PCV, 5X1YMSR204]
sources:
  - url: https://en.wikipedia.org/wiki/Without_loss_of_generality
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Maximum_and_minimum
    locator: lead section
---

## Example

Statement: for all real numbers $a$ and $b$, $\max(a, b) + \min(a, b) = a + b$.
Here $\max(a, b)$ is the larger and $\min(a, b)$ the smaller of the two numbers; see [[maximum and minimum|5X1YMSR204]].
We use [[without loss of generality|Y7NE0E6PCV]].

1. Symmetry: exchanging $a$ and $b$ does not change $\max(a, b)$, $\min(a, b)$ or $a + b$. So the statement for $(a, b)$ is the same as the statement for $(b, a)$.
2. For any two real numbers, $a \leq b$ or $b \leq a$. In the second case, exchanging the names gives the first case. So wlog $a \leq b$.
3. If $a \leq b$, then $\max(a, b) = b$ and $\min(a, b) = a$.
4. So $\max(a, b) + \min(a, b) = b + a = a + b$.

## Remarks

Without the wlog step, the proof has two cases, $a \leq b$ and $b < a$.
The second case repeats steps 3 and 4 with $a$ and $b$ exchanged.
Step 1 is the reason why this repetition can be skipped.

The same method proves the companion identity $\max(a, b) - \min(a, b) = |a - b|$.
Wlog $a \leq b$, since $|a - b| = |b - a|$; then the left side is $b - a = |a - b|$.
Together the two identities give $\max(a, b) = \frac{a + b + |a - b|}{2}$ and $\min(a, b) = \frac{a + b - |a - b|}{2}$.

## Explanations

### L1 human

Take the numbers $3$ and $8$.
The larger is $8$ and the smaller is $3$, and $8 + 3 = 11 = 3 + 8$.
Adding the larger and the smaller gives back the sum of the two numbers.
It does not matter which number is called the first one, so we may name them so that the first one is the smaller.

### L2 human

We use the identity to compute $\max(x, 1 - x) + \min(x, 1 - x)$ for real $x$.

1. Apply the statement with $a = x$ and $b = 1 - x$.
2. The sum is $x + (1 - x) = 1$, for every $x$.
3. Check at $x = 3$: $\max(3, -2) + \min(3, -2) = 3 + (-2) = 1$.

The typical use: an expression that is symmetric in two variables can be computed with the variables in a chosen order.

A trap: the symmetry in step 1 of the example concerns the whole statement.
For $\max(a, b) - a$, exchanging $a$ and $b$ gives $\max(a, b) - b$, which is a different number, so "wlog $a \leq b$" is not allowed for that expression.
