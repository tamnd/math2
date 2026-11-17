---
tag: 9WSEMZ8BWN
kind: example
name: Sums of the first odd numbers
msc: ["00A35", "11B83"]
topics: [DME0TPC348]
audience: ug1
not_instance_of:
  - target: 8AFXPXCE3N
    note: the pattern seen in small cases holds for every n, so small numbers did not mislead and the law has nothing to warn about
uses: [8AFXPXCE3N, 0ASJVEFA9J, 5W8G4689R2]
sources:
  - url: https://en.wikipedia.org/wiki/Square_number
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Strong_law_of_small_numbers
    locator: lead section
---

## Example

We look at the sums $s_n = 1 + 3 + 5 + \cdots + (2n - 1)$ of the first $n$ odd numbers.

1. The data. $s_1 = 1$, $s_2 = 4$, $s_3 = 9$, $s_4 = 16$, $s_5 = 25$ and $s_6 = 36$.
2. The guess. The values are the squares $1^2, 2^2, \ldots, 6^2$, which suggests $s_n = n^2$ for all $n \geq 1$.
3. The proof. $s_1 = 1 = 1^2$. If $s_n = n^2$, then $s_{n+1} = n^2 + (2n + 1) = (n+1)^2$. By [[mathematical induction|0ASJVEFA9J]], $s_n = n^2$ for all $n$.

The guess of step 2 came from six small cases, as in the examples of the [[strong law of small numbers|8AFXPXCE3N]].
Here the pattern is true for every $n$, so the small numbers did not deceive.
This is the reason the example is a non-example: the law warns about coincidences, and there is no coincidence here.

## Remarks

The law does not say that small patterns are usually false.
It says that small cases alone cannot tell a true pattern from a coincidence.
In this example the induction step of step 3 explains the pattern: adding the odd number $2n + 1$ adds a border of $2n + 1$ unit squares to an $n \times n$ square.
The page [[three kinds of reasoning on the sum of the first odd numbers|5W8G4689R2]] compares this guess with its proofs in more detail.

## Explanations

### L1 human

Add the odd numbers: $1 = 1$, $1 + 3 = 4$, $1 + 3 + 5 = 9$, $1 + 3 + 5 + 7 = 16$.
The answers are the square numbers.
Here the pattern is real: a square of side $n$ grows into a square of side $n + 1$ by adding an L-shaped border of $2n + 1$ small squares.
So this pattern never breaks, unlike the patterns in the strong law of small numbers.

### L2 human

We check the step from $n = 3$ to $n = 4$ with the picture.

1. A $3 \times 3$ square has $9$ unit squares, which is $s_3$.
2. A border along the right side and the top has $3 + 3 + 1 = 7$ unit squares.
3. The square with the border is a $4 \times 4$ square with $16$ unit squares.
4. So $s_4 = s_3 + 7 = 16$, and the same picture works for every $n$.

The typical use: a pattern found in small cases becomes a theorem once a mechanism, such as an induction step, explains it.
A trap: the same six data points would also fit other rules, so the data alone did not settle the question; the proof did.
