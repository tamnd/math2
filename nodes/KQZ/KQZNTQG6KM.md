---
tag: KQZNTQG6KM
kind: example
name: The sum 1 + 2 + ... + n at two levels of rigor
aliases: [the-sum-1-2-n-at-two-levels-of-rigour]
msc: ["00A35", "11B25"]
topics: [1BTHSHST4M]
audience: school
instance_of: [E1PE9R8DBB]
uses: [E1PE9R8DBB, 0ASJVEFA9J, AM4GQQMZ3C, WHN4CBYZXD]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_number
    locator: Formula
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Sum of consecutive natural numbers
---

## Example

The claim is that for each integer $n \ge 1$ the sum $S(n) = 1 + 2 + \dots + n$ equals $n(n + 1)/2$.
We give two proofs of it.
The first is [[rigorous|E1PE9R8DBB]] for a school reader, and the second answers a reader who asks what the dots mean.

The first proof pairs the terms.

1. Write the sum forward and backward: $S(n) = 1 + 2 + \dots + n$ and $S(n) = n + (n - 1) + \dots + 1$.
2. Add the two rows term by term. The $k$-th pair is $k + (n + 1 - k) = n + 1$.
3. There are $n$ pairs, so $2 S(n) = n(n + 1)$.
4. Divide by $2$ to get $S(n) = n(n + 1)/2$.

The second proof defines the sum first and then uses induction.

1. We define the sum without dots by a [[recursive definition|AM4GQQMZ3C]]: $S(1) = 1$, and $S(m + 1) = S(m) + (m + 1)$ for each $m \ge 1$.
2. Let $P(n)$ be the statement $S(n) = n(n + 1)/2$. We prove $P(n)$ for all $n \ge 1$ by [[mathematical induction|0ASJVEFA9J]].
3. Base case: $S(1) = 1$ by the definition, and $1 \cdot 2 / 2 = 1$, so $P(1)$ holds.
4. Induction step: let $m \ge 1$ and assume $P(m)$, that is, $S(m) = m(m + 1)/2$.
5. By the definition, $S(m + 1) = S(m) + (m + 1)$.
6. By the assumption of step 4, this equals $m(m + 1)/2 + (m + 1)$.
7. Over the common denominator $2$ this is $\big(m(m + 1) + 2(m + 1)\big)/2 = (m + 1)(m + 2)/2$, which is $P(m + 1)$.
8. By induction, $P(n)$ holds for every $n \ge 1$.

Check for $n = 4$: $1 + 2 + 3 + 4 = 10$, and $4 \cdot 5 / 2 = 10$.

## Remarks

Both proofs are correct, and they differ in what they take as known.
The pairing proof assumes that a sum with dots has a meaning, and that we may reverse its terms and add two such sums term by term.
For a school reader these facts are routine, so the pairing proof is rigorous for that reader.
The induction proof defines the sum and then uses only the definition, algebra and the principle of induction.
So a reader who asks what the dots mean gets an answer from the second proof and not from the first.

The pairing proof can also be made exact without changing its idea, with sigma notation.
The change of index $j = n + 1 - k$ maps $\{1, \dots, n\}$ onto itself, so
$$\sum_{k = 1}^{n} k = \sum_{k = 1}^{n} (n + 1 - k).$$
Adding the two sums gives $\sum_{k = 1}^{n} (n + 1) = n(n + 1)$.
The fact that a change of index does not change a finite sum is itself a lemma, proved by induction on $n$, so the dots are paid for in the end.

The same two levels exist for many identities.
For the sum of the first $n$ odd numbers, the [[picture of nested squares|EE2Y5SNFME]] is a proof at the first level, and an induction on $n$ is a proof at the second.

## Explanations

### L1 human

To add $1 + 2 + 3 + 4 + 5$, write the numbers forward in one row and backward in a second row.
Each column adds to $6$: $1 + 5$, $2 + 4$, $3 + 3$, $4 + 2$ and $5 + 1$.
There are $5$ columns, so the two rows together give $5 \times 6 = 30$.
One row is half of this, so the sum is $15$.
The same idea works for any number of terms: multiply the last number by the next one, and halve.

### L2 human

We use the recursive definition to check the formula at $n = 100$ and $n = 101$.
The formula gives
$$S(100) = \frac{100 \cdot 101}{2} = 5050.$$
The definition then gives $S(101) = S(100) + 101 = 5151$, and the formula gives $101 \cdot 102 / 2 = 5151$.
The two values agree, which is step 7 of the induction proof with $m = 100$.

The typical use of the two levels is in teaching: first the idea that convinces, then the version that a doubtful reader can check line by line.
Watch out for the view that the pairing proof is wrong because it uses dots.
It is a correct proof for its reader, and it has a gap only for a reader who does not accept the meaning of the dots.
