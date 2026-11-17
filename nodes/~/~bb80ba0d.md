---
tag: ~bb80ba0d
kind: example
name: The sum 1 + 2 + ... + n at two levels of rigour
msc: ["00A35", "11B25"]
topics: [1BTHSHST4M]
audience: school
instance_of: [~cc99a1f7]
uses: [~cc99a1f7, 0ASJVEFA9J, AM4GQQMZ3C, WHN4CBYZXD]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_number
    locator: Formula
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Sum of consecutive natural numbers
---

## Example

Claim: for each integer $n \ge 1$, the sum $S(n) = 1 + 2 + \cdots + n$ equals $\dfrac{n(n+1)}{2}$.
We give a proof that is [[rigorous|~cc99a1f7]] for a school reader, and then a proof that answers the question "what do the dots mean?".

Level 1, the pairing argument.

1. Write the sum forwards and backwards: $S(n) = 1 + 2 + \cdots + n$ and $S(n) = n + (n - 1) + \cdots + 1$.
2. Add the two lines term by term. The $k$-th pair is $k + (n + 1 - k) = n + 1$.
3. There are $n$ pairs, so $2S(n) = n(n + 1)$.
4. Divide by $2$: $S(n) = n(n + 1)/2$.

Level 2, a proof by induction from a definition of the sum.

1. We define the sum without dots, by a [[recursive definition|AM4GQQMZ3C]]: $S(1) = 1$, and $S(m + 1) = S(m) + (m + 1)$ for each $m \ge 1$.
2. Let $P(n)$ be the statement $S(n) = n(n + 1)/2$. We prove $P(n)$ for all $n \ge 1$ by [[mathematical induction|0ASJVEFA9J]].
3. Base case: $S(1) = 1$ by the definition, and $1 \cdot 2 / 2 = 1$. So $P(1)$ holds.
4. Induction step: let $m \ge 1$ and assume $P(m)$, that is, $S(m) = m(m + 1)/2$.
5. By the definition, $S(m + 1) = S(m) + (m + 1)$.
6. By the hypothesis of step 4, this equals $m(m + 1)/2 + (m + 1)$.
7. We compute: $m(m + 1)/2 + 2(m + 1)/2 = (m + 1)(m + 2)/2$. This is $P(m + 1)$.
8. By induction, $P(n)$ holds for every $n \ge 1$.

Check for $n = 4$: $1 + 2 + 3 + 4 = 10$, and $4 \cdot 5 / 2 = 10$.

## Remarks

Both proofs are correct, and they differ in what they take as known.
Level 1 assumes that a sum with dots has a meaning and that we may add two sums term by term and reorder the terms.
For a school reader these facts are routine, so Level 1 is rigorous for that reader.
Level 2 defines the sum, and it uses only the definition, algebra and the principle of induction.
A reader who asks what the dots mean gets an answer from Level 2 and not from Level 1.

Level 1 can also be made rigorous without induction, with the sigma notation.
The change of index $j = n + 1 - k$ maps $\{1, \dots, n\}$ onto itself, so $\sum_{k=1}^{n} k = \sum_{k=1}^{n} (n + 1 - k)$.
Adding the two sums gives $\sum_{k=1}^{n} (n + 1) = n(n + 1)$.
The step "a change of index does not change a finite sum" is itself a lemma, proved by induction on $n$.

The same two levels exist for many identities.
For the sum of the first $n$ odd numbers, the picture of nested squares is a Level 1 proof, and an induction on $n$ is a Level 2 proof.

## Explanations

### L1 human

To add $1 + 2 + 3 + 4 + 5$, write the numbers forwards and backwards in two rows.
Each column adds to $6$: $1 + 5$, $2 + 4$, $3 + 3$, $4 + 2$, $5 + 1$.
There are $5$ columns, so both rows together give $5 \times 6 = 30$.
One row is half of this, so the sum is $15$.
The same idea works for any number of terms, and it gives the rule "multiply the last number by the next one, and halve".

### L2 human

We use Level 2 to find $S(100)$ and to check one step by hand.

1. The formula gives $S(100) = 100 \cdot 101 / 2 = 5050$.
2. The definition gives $S(101) = S(100) + 101 = 5151$.
3. The formula gives $101 \cdot 102 / 2 = 5151$, so the two values agree, as step 7 of Level 2 predicts.

The typical use of the two levels is in teaching: first the idea, then the version that a sceptical reader can check line by line.
A trap is to think that Level 1 is wrong because it uses dots.
It is a correct proof for its reader; it becomes a gap only for a reader who does not accept the meaning of the dots.
