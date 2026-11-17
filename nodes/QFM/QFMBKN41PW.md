---
tag: QFMBKN41PW
kind: example
name: A generic proof that the sum of three consecutive integers is divisible by 3
msc: ["97E50", "97F60"]
topics: [VHGA6J4NZK]
audience: school
instance_of: [SG9XA69J64]
uses: [SG9XA69J64, 0PG2H7WKGG]
sources:
  - url: https://doi.org/10.1007/BF00312078
    locator: pages 277-289
---

## Example

The claim is: the sum of any three consecutive integers is [[divisible|0PG2H7WKGG]] by $3$.
A student argues on one example.

> Take $7 + 8 + 9$.
> Write it as $(8 - 1) + 8 + (8 + 1)$.
> The $-1$ and the $+1$ cancel, so the sum is $8 + 8 + 8 = 3 \cdot 8$.
> The same happens for any three numbers in a row: the sum is three times the middle number.

We check that the argument is a [[generic proof|SG9XA69J64]].

1. Check the arithmetic: $7 + 8 + 9 = 24$ and $3 \cdot 8 = 24$.
2. Replace $8$ by an integer $m$: the three consecutive integers are $m - 1$, $m$, $m + 1$.
3. The step "the $-1$ and the $+1$ cancel" holds for each $m$: $(m - 1) + m + (m + 1) = 3m$.
4. The conclusion "three times the middle number" holds for each $m$, and $3m$ is divisible by $3$.
5. No step uses a special feature of $8$.

So the argument is a generic proof.

## Remarks

The key is the way the student writes the example: $(8 - 1) + 8 + (8 + 1)$, not $7 + 8 + 9$.
The rewriting makes the structure visible, and the last sentence states that the structure does not depend on $8$.
The same argument shows more: the sum is $3$ times the middle number, not only some multiple of $3$.
For four consecutive integers the analogue fails: $(m - 1) + m + (m + 1) + (m + 2) = 4m + 2$, which is never divisible by $4$.

## Explanations

### L1 human

The student takes one example, $7 + 8 + 9$, and sees that $7$ is one less than $8$ and $9$ is one more.
The one less and the one more cancel out, so the sum is three eights.
This works for any three numbers in a row, so the sum is always three times the middle one.

### L2 human

1. Write the example around the middle number.
2. Find the step that does the work: the cancellation of $-1$ and $+1$.
3. Check that the step works with a letter in place of the number.
4. State the general claim.

A trap is to skip step 1.
The bare computation $7 + 8 + 9 = 24$ does not show the reason, and it is only a check of one case.
