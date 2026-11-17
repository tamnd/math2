---
tag: 1PYKFFYD3V
kind: example
name: Subtraction is not a binary operation on the natural numbers
msc: [08A02]
topics: [BAZT8JJ70S]
audience: school
not_instance_of:
  - target: 0M418FE7BB
    note: closure fails, because 1 - 2 is not a natural number
uses: [0MWKJ44V5A, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Binary_operation
    locator: lead section
---

## Example

Let $\mathbb{N} = \{0, 1, 2, \ldots\}$ be the set of [[natural numbers|0MWKJ44V5A]].
Consider the rule that takes $a, b \in \mathbb{N}$ to the difference $a - b$.
We show that this rule is not a [[binary operation|0M418FE7BB]] on $\mathbb{N}$.

1. A binary operation on $\mathbb{N}$ must give an element of $\mathbb{N}$ for each pair $(a, b)$ of natural numbers.
2. Take the pair $(1, 2)$. Then $1 - 2 = -1$.
3. Each natural number is $\geq 0$, and $-1 < 0$. Thus $-1 \notin \mathbb{N}$.

So closure fails for the pair $(1, 2)$, and subtraction is not a binary operation on $\mathbb{N}$.

## Remarks

The failure comes from the set, not from the rule.
On the [[integers|0C4JS9RF5M]] $\mathbb{Z}$, subtraction is a binary operation, because the difference of two integers is an integer.
On $\mathbb{N}$, the pairs $(a, b)$ with $a \geq b$ give a natural number $a - b$, and the pairs with $a < b$ do not.
So one bad pair is enough to show that closure fails.
A changed rule, the truncated difference $\max(a - b, 0)$, is a binary operation on $\mathbb{N}$, because its value is always $\geq 0$.

## Explanations

### L1 human

With the numbers $0, 1, 2, 3, \ldots$ we can always add, and the answer is again one of these numbers.
We cannot always take away: $1$ take away $2$ needs the number $-1$, and $-1$ is not in the list.
So take away does not stay inside the list, and it is not a binary operation on it.
When we allow negative numbers, take away always works.

### L2 human

To show that a rule is not a binary operation on a set, it is enough to find one pair whose value is not in the set.

1. The set is $\mathbb{N}$ and the rule is $a - b$.
2. For the pair $(3, 5)$, the value is $3 - 5 = -2$.
3. The value $-2$ is negative, so it is not a natural number.
4. Thus the rule does not map $\mathbb{N} \times \mathbb{N}$ to $\mathbb{N}$.

The same test shows that division is not a binary operation on the positive integers, because $1 / 2$ is not an integer.
The typical use is to explain why we pass from $\mathbb{N}$ to $\mathbb{Z}$: the integers are the natural numbers with the differences added.
A trap is to conclude from good pairs such as $(5, 3)$ that the rule is a binary operation; closure must hold for every pair.
