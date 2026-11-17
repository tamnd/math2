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
In other words, $n^2$ has the form $3m$ or $3m + 1$ for an integer $m$.
We give a [[proof by cases|0WCP0PVET6]].

1. By the [[division algorithm|0CHQKZFK5S]], each integer $n$ is $3k$, $3k + 1$ or $3k + 2$ for an integer $k$. These three cases cover all integers.
2. Case $n = 3k$: $n^2 = 9k^2 = 3(3k^2)$. The remainder is $0$.
3. Case $n = 3k + 1$: $n^2 = 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1$. The remainder is $1$.
4. Case $n = 3k + 2$: $n^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1$. The remainder is $1$.
5. In each case the remainder is $0$ or $1$. Since the cases cover all integers, the statement holds for every integer $n$.

## Remarks

The remainder $2$ never occurs.
So an integer of the form $3m + 2$, such as $2$, $5$, $8$ or $11$, is never a perfect square.
The example also gives a [[proof of impossibility|6F55216R53]]: [[the equation x^2 - 3y^2 = 2 has no integer solution|1QT670FE82]], because $x^2$ would have remainder $2$.

The same method works for other moduli, with one case for each remainder.
Modulo $4$, a square has remainder $0$ or $1$: $(2k)^2 = 4k^2$ and $(2k + 1)^2 = 4(k^2 + k) + 1$.
So a sum of two squares never has remainder $3$ modulo $4$, and $7$, $11$ and $15$ are not sums of two squares.
Modulo $5$, the squares of $0, 1, 2, 3, 4$ are $0, 1, 4, 9, 16$, with remainders $0, 1, 4, 4, 1$; so a square has remainder $0$, $1$ or $4$.

## Explanations

### L1 human

Divide the squares $1, 4, 9, 16, 25, 36, 49$ by $3$.
The remainders are $1, 1, 0, 1, 1, 0, 1$.
The remainder $2$ never appears.
The proof explains why: every whole number is a multiple of $3$, one more, or two more, and in each of these three cases the square has remainder $0$ or $1$.
Three cases cover all numbers, so the remainder $2$ can never appear.

### L2 human

We use the result to show that $3$ divides $a$ and $b$ whenever $3 \mid a^2 + b^2$.

1. By the example, $a^2$ and $b^2$ each have remainder $0$ or $1$ modulo $3$.
2. The four combinations give $a^2 + b^2$ the remainders $0 + 0 = 0$, $0 + 1 = 1$, $1 + 0 = 1$ and $1 + 1 = 2$.
3. Only the first combination gives remainder $0$. So $3 \mid a^2 + b^2$ forces $a^2$ and $b^2$ to have remainder $0$.
4. By step 2 of the example, $n^2$ has remainder $0$ only in the case $n = 3k$. So $3 \mid a$ and $3 \mid b$.

The typical use: list the possible remainders of each term, then combine them in a small table of cases.

A trap: case 4 of the example is often forgotten, because $n = 3k + 2$ "looks like" $n = 3k - 1$.
Both forms describe the same integers, but one of them must appear in the list.
