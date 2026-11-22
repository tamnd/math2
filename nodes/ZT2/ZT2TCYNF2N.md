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
Here $\max(a, b)$ is the larger and $\min(a, b)$ the smaller of the two numbers, as in [[maximum and minimum|5X1YMSR204]].
We use [[without loss of generality|Y7NE0E6PCV]].

1. Exchanging $a$ and $b$ changes none of $\max(a, b)$, $\min(a, b)$ and $a + b$.
   So the statement for the pair $(a, b)$ says the same as the statement for $(b, a)$.
2. For any two real numbers, $a \le b$ or $b \le a$.
   In the second case, exchanging the names gives the first case, so we may assume $a \le b$.
3. If $a \le b$, then $\max(a, b) = b$ and $\min(a, b) = a$.
4. So $\max(a, b) + \min(a, b) = b + a = a + b$.

Check: $a = 8$ and $b = 3$ fall in the skipped case, and $8 + 3 = 11 = 8 + 3$ as the exchange predicts.

## Remarks

Without the wlog step, the proof has two cases, $a \le b$ and $b < a$, and the second repeats steps 3 and 4 with the letters exchanged.
Step 1 is the reason why that repetition can be skipped.

The same method proves the companion identity $\max(a, b) - \min(a, b) = |a - b|$.
Since $|a - b| = |b - a|$, the statement is again symmetric, so we may assume $a \le b$, and then the left side is $b - a = |a - b|$.
Adding and subtracting the two identities gives
$$\max(a, b) = \frac{a + b + |a - b|}{2}, \qquad \min(a, b) = \frac{a + b - |a - b|}{2}.$$

## Explanations

### L1 human

Take the numbers $3$ and $8$.
The larger is $8$ and the smaller is $3$, and $8 + 3 = 11 = 3 + 8$.
Adding the larger and the smaller gives back the sum of the two numbers.
It does not matter which number we call the first one, so we may name them so that the first one is the smaller.

### L2 human

Let us use the identity to compute $\max(x, 1 - x) + \min(x, 1 - x)$ for real $x$.
Apply the statement with $a = x$ and $b = 1 - x$:
$$\max(x, 1 - x) + \min(x, 1 - x) = x + (1 - x) = 1.$$
So the sum is $1$ for every $x$, with no need to know which of the two numbers is larger.
Check: at $x = 3$ we get $\max(3, -2) + \min(3, -2) = 3 + (-2) = 1$.
The typical use is that an expression symmetric in two variables can be computed with the variables in any order you like.
Watch out: the symmetry must hold for the whole expression, and $\max(a, b) - a$ becomes $\max(a, b) - b$ under the exchange, so "wlog $a \le b$" is not allowed for it.
