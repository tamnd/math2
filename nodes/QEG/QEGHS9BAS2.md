---
tag: QEGHS9BAS2
kind: example
name: A case split that misses the interval 0 < x < 1
msc: ["00A35", "26D05"]
topics: [958EF46EYJ]
audience: school
not_instance_of:
  - target: 0WCP0PVET6
    note: the cases x >= 1 and x <= 0 do not cover all real numbers, and the claim fails in the missing interval
uses: [0WCP0PVET6, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_exhaustion
    locator: lead section
---

## Example

Claim: for every real number $x$, $x^2 \ge x$.
A student writes this argument.

1. Case $x \ge 1$: multiply both sides of $x \ge 1$ by the positive number $x$, which gives $x^2 \ge x$.
2. Case $x \le 0$: then $x^2 \ge 0 \ge x$.
3. So $x^2 \ge x$ in all cases.

This is not a valid [[proof by cases|0WCP0PVET6]].
We check the condition that fails.

1. A proof by cases needs cases that together cover every possibility.
   Here the possibilities are all real numbers.
2. The cases $x \ge 1$ and $x \le 0$ cover $(-\infty, 0] \cup [1, \infty)$.
   The numbers with $0 < x < 1$ are in neither case.
3. Each of the two cases is proved correctly.
   The error is only in line 3, the words "in all cases".
4. In the missing interval the claim is false.
   For $x = \tfrac{1}{2}$ we get $x^2 = \tfrac{1}{4} < \tfrac{1}{2} = x$, so $x = \tfrac{1}{2}$ is a [[counterexample|0ED72CTBNP]].

## Remarks

The true statement is that $x^2 \ge x$ exactly when $x \le 0$ or $x \ge 1$.
To prove it, factor:
$$x^2 - x = x(x - 1).$$
A product of two real numbers is at least $0$ exactly when one factor is $0$ or both have the same sign, and that happens exactly when $x \le 0$ or $x \ge 1$.
So the student's two cases are precisely the set where the claim holds, and the gap is precisely the set where it fails.

Here the missing case is a whole interval.
A missing case can also be a single point.
The argument "$x / |x|$ is $1$ or $-1$ for every real $x$, by the cases $x > 0$ and $x < 0$" misses $x = 0$, where the expression is not defined at all.

## Explanations

### L1 human

A number times itself is often bigger than the number: $3 \times 3 = 9$ is bigger than $3$.
For negative numbers it is also true, because the square is positive.
But for numbers between $0$ and $1$ it is false.
Half of a half is a quarter, and a quarter is less than a half.
The student checked the big numbers and the negative numbers and forgot the numbers in between.

### L2 human

Before you use a case split, test it for coverage.
Take the claim $|x - 1| + |x + 1| \ge 2$ for every real $x$.
The expressions inside the absolute values change sign at $x = 1$ and $x = -1$, so the natural cases are $x \le -1$, $-1 < x < 1$ and $x \ge 1$.
These three sets together are the whole real line, and each real number lies in exactly one of them.
Now each case is a short computation:
$$x \le -1: \ (1 - x) + (-x - 1) = -2x \ge 2, \qquad -1 < x < 1: \ (1 - x) + (x + 1) = 2, \qquad x \ge 1: \ (x - 1) + (x + 1) = 2x \ge 2.$$
Check: at $x = 0$ the sum is $1 + 1 = 2$, and at $x = 3$ it is $2 + 4 = 6$.
The typical use is to list the points where the formula changes and to check that every interval between them is a case.
Watch out: the middle interval is the one most often forgotten, exactly as in the student's argument.
