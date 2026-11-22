---
tag: D6G69GNKPC
kind: example
name: Two proofs of the formula for 1 + 2 + ... + n
msc: ["00A35", "97E50"]
topics: [N4P3E53HM0]
audience: school
instance_of: [ENY0GKRJS8]
uses: [ENY0GKRJS8, 01QZNHQWYD, 0ASJVEFA9J, WHN4CBYZXD]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_number
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Examples
---

## Example

The [[sum of the first n natural numbers|01QZNHQWYD]] has a closed formula: for each integer $n \geq 1$,
$$1 + 2 + \cdots + n = \frac{n(n + 1)}{2}.$$
We give two complete proofs and compare their [[functions|ENY0GKRJS8]].

Proof A, by [[mathematical induction|0ASJVEFA9J]].

1. Base case $n = 1$: the left side is $1$, and the right side is $\frac{1 \cdot 2}{2} = 1$.
2. Induction step: assume the formula for some $n \geq 1$, and add $n + 1$ to both sides.
   $$1 + 2 + \cdots + n + (n + 1) = \frac{n(n + 1)}{2} + (n + 1) = \frac{n(n + 1) + 2(n + 1)}{2} = \frac{(n + 1)(n + 2)}{2}.$$
3. The right side is the formula for $n + 1$, so by induction the formula holds for each $n \geq 1$.

Proof B, by pairing.

4. Let $S = 1 + 2 + \cdots + n$, and write the sum forwards and backwards.
   $$\begin{aligned} S &= 1 + 2 + \cdots + n, \\ S &= n + (n - 1) + \cdots + 1. \end{aligned}$$
5. Add the two lines term by term.
   The $k$th terms are $k$ and $n + 1 - k$, and their sum is $n + 1$.
6. There are $n$ such columns, so $2S = n(n + 1)$, and dividing by $2$ gives $S = \frac{n(n + 1)}{2}$.

## Remarks

Both proofs verify the formula for every $n$.
Proof A needs the answer in advance: it checks a given formula, but it does not say where the formula comes from.
Proof B produces the answer, and it shows that the sum is $n$ copies of the average term $\frac{n + 1}{2}$.
So Proof B serves explanation, while Proof A serves mainly verification.

Proof B also serves discovery.
The same pairing works for any arithmetic progression, because the $k$th term from the front and the $k$th from the back always have the same sum:
$$a + (a + d) + \cdots + (a + (n - 1)d) = \frac{n\bigl(2a + (n - 1)d\bigr)}{2}.$$
Proof A is the better tool when the answer is known and only needs checking.
For example, $1^2 + 2^2 + \cdots + n^2 = \frac{n(n + 1)(2n + 1)}{6}$ yields to induction at once, while the pairing of Proof B does not apply to it directly.
The numbers $\frac{n(n + 1)}{2}$ are the [[triangular numbers|WHN4CBYZXD]] $1, 3, 6, 10, 15, \ldots$.

## Explanations

### L1 human

To add $1 + 2 + \cdots + 10$, write the numbers in a row, and write them again backwards under the first row.
Each column adds to $11$: $1 + 10$, $2 + 9$, and so on.
There are $10$ columns, so the two rows together make $110$.
One row is half of that, so the sum is $55$.
This shows why the answer is what it is, not only that it is right.

### L2 human

Here are both proofs run on the case $n = 6$.
The direct sum and the formula agree:
$$1 + 2 + 3 + 4 + 5 + 6 = 21 = \frac{6 \cdot 7}{2}.$$
Proof A reaches $n = 6$ from $n = 5$: the formula gives $\frac{5 \cdot 6}{2} = 15$, and $15 + 6 = 21$.
Proof B pairs the row with its reverse: the columns $1 + 6$, $2 + 5$, $3 + 4$, $4 + 3$, $5 + 2$, $6 + 1$ each give $7$, and $6 \cdot 7 = 42 = 2 \cdot 21$.
Watch out: pairing the first term with the last inside one row needs a separate step for the middle term when $n$ is odd.
Pairing the row with its reverse, as in step 5, avoids this and works for every $n$.
