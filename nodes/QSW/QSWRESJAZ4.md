---
tag: QSWRESJAZ4
kind: example
name: The sum of the first n odd numbers by induction
msc: ["00A35", "11B83"]
topics: [EEH2F76CYQ]
audience: school
instance_of: [0ASJVEFA9J]
illustrates: [9PESCNHE7Q]
uses: [0ASJVEFA9J, 9PESCNHE7Q]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: History
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Example

Add the odd numbers in order and look at the running totals: $1$, then $1 + 3 = 4$, then $4 + 5 = 9$, then $9 + 7 = 16$.
Every total is a perfect square, and the table shows the pattern for six values.

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $1 + 3 + \dots + (2n - 1)$ | 1 | 4 | 9 | 16 | 25 | 36 |

A table checks six cases, and we want all of them.
So we prove the [[sum of the first $n$ odd positive integers|9PESCNHE7Q]] by [[mathematical induction|0ASJVEFA9J]]:
$$1 + 3 + 5 + \dots + (2n - 1) = n^2 \quad \text{for every integer } n \ge 1.$$

1. Let $P(n)$ be the statement $\sum_{i=1}^{n} (2i - 1) = n^2$.
   The claim starts at $n = 1$, so the base case is $n = 1$.
2. Base case.
   For $n = 1$ the sum has the one term $2 \cdot 1 - 1 = 1$, and $1^2 = 1$, so $P(1)$ holds.
3. Induction step.
   Let $n \ge 1$ be an arbitrary integer, and assume $P(n)$, that is, $\sum_{i=1}^{n} (2i - 1) = n^2$.
4. The sum for $n + 1$ is the sum for $n$ plus the term with $i = n + 1$, and that term is $2(n + 1) - 1 = 2n + 1$.
5. Replace the old sum by $n^2$, which the induction hypothesis of step 3 allows:
   $$\sum_{i=1}^{n+1} (2i - 1) = n^2 + (2n + 1) = (n + 1)^2.$$
   So $P(n + 1)$ holds.
6. Steps 3 to 5 prove that $P(n)$ implies $P(n + 1)$ for every $n \ge 1$.
   With the base case of step 2, the principle of induction gives $P(n)$ for every $n \ge 1$.

Check: for $n = 6$ the formula gives $36$, and $1 + 3 + 5 + 7 + 9 + 11 = 36$.

## Remarks

The example has the shape of almost every induction for a sum.
The sum for $n + 1$ is the sum for $n$ plus one new term, so the induction hypothesis replaces the old sum by a closed form, and only algebra is left.
The hypothesis does real work in step 5: without it, we have no value for the old sum.

The start of the range can move.
If we allow $n = 0$, the sum is empty and equals $0 = 0^2$, so the base case is $n = 0$ and the step does not change.
The same plan proves $\sum_{i=1}^{n} i^3 = \left(\tfrac{n(n+1)}{2}\right)^2$, with the new term $(n + 1)^3$ and longer algebra in the step.

A proof without induction also exists.
Write the sum forward and backward and add the two copies term by term: each pair is $(2i - 1) + (2(n + 1 - i) - 1) = 2n$.
There are $n$ pairs, so twice the sum is $n \cdot 2n$, and the sum is $n^2$.

Francesco Maurolico proved this identity in 1575 with an argument that passes from each case to the next, one of the first recorded uses of the method.

## Explanations

### L1 human

Put dots in squares: one dot, then a $2$ by $2$ square, then a $3$ by $3$ square.
To grow a square of side $n$ into a square of side $n + 1$, add one new row and one new column that share a corner.
That adds $n + n + 1 = 2n + 1$ dots, which is the next odd number.
So the odd numbers $1, 3, 5, \ldots$ add up to the squares $1, 4, 9, \ldots$, and the growth rule works at every size.
The induction step is this picture written in algebra.

### L2 human

We use the same plan for the sum of the first $n$ even numbers, $2 + 4 + \dots + 2n = n(n + 1)$.
For the base case $n = 1$, the left side is $2$ and the right side is $1 \cdot 2 = 2$.
For the step, assume the formula for some $n \ge 1$ and add the next even number $2(n + 1)$:
$$n(n + 1) + 2(n + 1) = (n + 1)(n + 2).$$
That is the formula for $n + 1$, so induction proves it for every $n \ge 1$.
Check: for $n = 4$, $2 + 4 + 6 + 8 = 20 = 4 \cdot 5$.

The method fits every closed formula for a finite sum that a table of small cases suggests.
Watch out for the new term: it is the term with index $n + 1$, which for the odd numbers is $2n + 1$ and not $2n - 1$.
A wrong new term gives an algebra error that looks like a failure of the formula.
