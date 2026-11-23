---
tag: 7FW2WDYPVR
kind: example
name: One proof written for two readers
msc: ["00A35", "11A05"]
topics: [STSM6PR7TX]
audience: ug1
instance_of: [8JQHJK94RZ]
uses: [8JQHJK94RZ, BV6E0ZG3YN, 0WCP0PVET6, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
  - url: https://en.wikipedia.org/wiki/Parity_(mathematics)
    locator: lead section
---

## Example

The claim is that for every [[integer|0C4JS9RF5M]] $n$, the number $n^2 - n$ is even.
We write one proof for a first-year course and one for a reader who knows elementary number theory.
Both are instances of [[writing proofs|8JQHJK94RZ]], because each fits a stated reader.

The proof for a first-year course reads as follows.

> Let $n$ be an integer.
> We have $n^2 - n = n(n - 1)$.
> Every integer is even or odd, so we consider two cases.
> Case 1: $n$ is even.
> Then $n = 2k$ for an integer $k$, by the [[definition of an even integer|BV6E0ZG3YN]].
> So $n(n - 1) = 2 \cdot k(n - 1)$, and $k(n - 1)$ is an integer.
> Hence $n(n - 1)$ is even.
> Case 2: $n$ is odd.
> Then $n = 2k + 1$ for an integer $k$, so $n - 1 = 2k$.
> So $n(n - 1) = 2 \cdot k(2k + 1)$, and $k(2k + 1)$ is an integer.
> Hence $n(n - 1)$ is even.
> In both cases $n^2 - n$ is even.
> $\square$

The proof for a reader who knows elementary number theory is one sentence.

> Since $n^2 - n = n(n - 1)$ is a product of two consecutive integers, one factor is even, and so is the product.
> $\square$

We check that each text fits its reader.

1. The first proof states each fact that a first-year student may lack: the factorization, the split into even and odd, and the definition in each case.
2. The first proof is a [[proof by cases|0WCP0PVET6]], and it says why the two cases cover all integers.
3. The second proof quotes "of two consecutive integers, one is even" without proof.
   For its reader this fact is standard, and the first proof in fact contains its proof.
4. Both proofs are correct, and they differ only in the steps that they leave to the reader.

Check: for $n = 5$ we get $25 - 5 = 20 = 2 \cdot 10$, and for $n = -3$ we get $9 + 3 = 12 = 2 \cdot 6$.

## Remarks

The choice of reader decides which steps are written, and [[level of detail in proofs|VYGBV5D8Y4]] treats this choice in general.
In a first-year exercise whose task is to prove the fact about consecutive integers, the short proof would be a gap.
In a research paper the long proof would waste the reader's time, because the reader expects the short form.

The same two styles work for $n^3 - n = (n - 1)n(n + 1)$, which is divisible by $3$.
The long proof then has three cases, by the remainder of $n$ on division by $3$, and the short proof says that one of three consecutive integers is a multiple of $3$.

## Explanations

### L1 human

A teacher explains a fact one way to a beginner and another way to a colleague, and a proof works the same way.
The fact here is that $n^2 - n$ is always even: for $n = 4$ it is $12$, and for $n = 7$ it is $42$.
For a beginner, we treat even and odd $n$ one at a time and show each calculation.
For an expert, one sentence is enough: $n^2 - n = n(n - 1)$, and of two neighboring whole numbers one is even.

### L2 human

We write both versions for the claim that $3$ divides $n^3 - n$ for every integer $n$.
First we factor:
$$n^3 - n = n(n^2 - 1) = (n - 1)n(n + 1).$$
For the long version, division with remainder gives $n = 3q$, $n = 3q + 1$ or $n = 3q + 2$ for an integer $q$.
If $n = 3q$, the factor $n$ is a multiple of $3$.
If $n = 3q + 1$, the factor $n - 1 = 3q$ is a multiple of $3$.
If $n = 3q + 2$, the factor $n + 1 = 3(q + 1)$ is a multiple of $3$.
In each case one factor is a multiple of $3$, so the product is.
The short version reads: "Of three consecutive integers, one is divisible by $3$."

Check: $4^3 - 4 = 60 = 3 \cdot 20$.
Decide who the reader is before you write.
Watch out for a mixed style: a proof that checks the easy cases in full and skips the hard case fits no reader.
