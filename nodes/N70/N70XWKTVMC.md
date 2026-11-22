---
tag: N70XWKTVMC
kind: example
name: The square of an integer leaves remainder 0 or 1 on division by 3
msc: ["00A35", "11A07"]
topics: [958EF46EYJ]
audience: school
instance_of: [0WCP0PVET6]
uses: [0WCP0PVET6, 0CHQKZFK5S]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_exhaustion
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Quadratic_residue
    locator: lead section
---

## Example

Statement: for every integer $n$, the remainder of $n^2$ on division by $3$ is $0$ or $1$.
In other words, $n^2 = 3m$ or $n^2 = 3m + 1$ for some integer $m$.
We give a [[proof by cases|0WCP0PVET6]], with one case for each remainder of $n$.

1. By the [[division algorithm|0CHQKZFK5S]], each integer $n$ equals $3k$, $3k + 1$ or $3k + 2$ for some integer $k$.
   So these three cases cover all integers.
2. Case $n = 3k$.
   Then $n^2 = 9k^2 = 3(3k^2)$, and the remainder is $0$.
3. Case $n = 3k + 1$.
   Then
   $$n^2 = 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1,$$
   and the remainder is $1$.
4. Case $n = 3k + 2$.
   Then
   $$n^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1,$$
   and the remainder is $1$.
5. In each case the remainder is $0$ or $1$.
   The cases cover all integers, so the statement holds for every integer $n$.

Check: $n = 7 = 3 \cdot 2 + 1$ gives $49 = 3 \cdot 16 + 1$, and $n = 8 = 3 \cdot 2 + 2$ gives $64 = 3 \cdot 21 + 1$.

## Remarks

The remainder $2$ never occurs.
So a number of the form $3m + 2$, such as $2$, $5$, $8$ or $11$, is never a perfect square.
This is already a small [[proof of impossibility|6F55216R53]], and the same fact shows that [[the equation x^2 - 3y^2 = 2 has no integer solution|1QT670FE82]]: modulo $3$ the equation says $x^2 \equiv 2$.

Change the modulus and the method stays the same, with one case for each remainder.
Modulo $4$, a square has remainder $0$ or $1$, because $(2k)^2 = 4k^2$ and $(2k + 1)^2 = 4(k^2 + k) + 1$.
So a sum of two squares never has remainder $3$ modulo $4$, and $7$, $11$ and $15$ are not sums of two squares.
Modulo $5$, the squares of $0, 1, 2, 3, 4$ are $0, 1, 4, 9, 16$, with remainders $0, 1, 4, 4, 1$, so a square has remainder $0$, $1$ or $4$.

## Explanations

### L1 human

Divide the squares $1, 4, 9, 16, 25, 36, 49$ by $3$.
The remainders are $1, 1, 0, 1, 1, 0, 1$.
The remainder $2$ never appears.
The proof explains why: every whole number is a multiple of $3$, one more, or two more, and in each of these three cases the square has remainder $0$ or $1$.
Three cases cover all numbers, so the remainder $2$ can never appear.

### L2 human

We use the result to show that if $3 \mid a^2 + b^2$, then $3 \mid a$ and $3 \mid b$.
By the example, $a^2$ and $b^2$ each have remainder $0$ or $1$ modulo $3$, so there are four combinations.
Their sums have the remainders
$$0 + 0 = 0, \quad 0 + 1 = 1, \quad 1 + 0 = 1, \quad 1 + 1 = 2.$$
Only the first combination gives remainder $0$, so $3 \mid a^2 + b^2$ forces both squares to have remainder $0$.
By the case analysis, $n^2$ has remainder $0$ only in the case $n = 3k$, so $3 \mid a$ and $3 \mid b$.
This is the typical use: list the possible remainders of each term, then combine them in a small table of cases.
Watch out: the case $n = 3k + 2$ is often forgotten because it can also be written $n = 3k - 1$.
Both forms describe the same integers, but one of them must be in the list.
