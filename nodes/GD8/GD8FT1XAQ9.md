---
tag: GD8FT1XAQ9
kind: example
name: A two-column proof is not a structured proof
msc: ["00A35", "11A05"]
topics: [STSM6PR7TX]
audience: research
not_instance_of:
  - target: H2W8D7BMSW
    note: the table is one flat list with no levels, so the case assumptions have no scope and no step has its own sub-proof
uses: [H2W8D7BMSW, P8PCGFASP8, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Two-column proof
  - doi: 10.1080/00029890.1995.12004627
    locator: pages 600-608
---

## Example

*Statement.* For every integer $n$, the number $n^2 + n$ is even.

A student writes this [[two-column proof|P8PCGFASP8]] and calls it a structured proof.

| # | Statements | Reasons |
|---|---|---|
| 1 | $n$ is an integer | given |
| 2 | $n$ is even or $n$ is odd | every integer is even or odd |
| 3 | $n = 2k$ for an integer $k$ | $n$ is even |
| 4 | $n^2 + n = 4k^2 + 2k = 2(2k^2 + k)$ | algebra (3) |
| 5 | $n = 2k + 1$ for an integer $k$ | $n$ is odd |
| 6 | $n^2 + n = (2k + 1)(2k + 2) = 2(2k + 1)(k + 1)$ | algebra (5) |
| 7 | $n^2 + n$ is even | rows 4 and 6 |

The mathematics is correct, and the table is a reasonable proof by cases for a school reader.
It is not a [[structured proof|H2W8D7BMSW]], and we check which features are missing.

1. There are no levels. Rows 3 and 5 are case assumptions, but they stand at the same level as the given fact in row 1.
2. The scope of each assumption is not shown. Read as a flat list, rows 3 and 5 together say $2k = 2k + 1$, which is false.
3. The letter $k$ has two different meanings, in row 3 and in row 5. In a flat list the second use clashes with the first.
4. Row 7 cites rows 4 and 6, but each of them holds only in its own case. The table does not say that row 2 is the reason why the two cases cover all integers.
5. No step has its own sub-proof. Each row is a leaf, so the format cannot show that rows 3 and 4 together prove one case.

The structured proof of the same statement is:

- `<1>1.` CASE: $n$ is even.
    - `<2>1.` PICK an integer $k$ with $n = 2k$. PROOF: by the case assumption.
    - `<2>2.` Q.E.D. PROOF: $n^2 + n = 2(2k^2 + k)$ by `<2>1`.
- `<1>2.` CASE: $n$ is odd.
    - `<2>1.` PICK an integer $k$ with $n = 2k + 1$. PROOF: by the case assumption.
    - `<2>2.` Q.E.D. PROOF: $n^2 + n = 2(2k + 1)(k + 1)$ by `<2>1`.
- `<1>3.` Q.E.D. PROOF: by `<1>1` and `<1>2`, since every integer is even or odd.

Here each case is a sub-proof, and its letter $k$ and its assumption end with it.

## Remarks

1. The example shows the trap named in the writing notes of this topic: a two-column proof and a structured proof are different formats. Both number their steps, but only the structured proof has levels.
2. A Fitch-style table with indentation for each case would come close to a structured proof. The indentation plays the role of the levels.
3. The algebra in row 6 holds because $(2k + 1)^2 + (2k + 1) = (2k + 1)\bigl((2k + 1) + 1\bigr) = (2k + 1)(2k + 2)$.
4. A shorter proof avoids cases: $n^2 + n = n(n + 1)$, and one of two consecutive integers is even. Its structured form has one level.

## Explanations

### L1 human

Two ways to write a proof can both use numbered lines and still differ.
A two-column proof is one long list, like a shopping list.
A structured proof is like a folder with sub-folders: each case has its own sub-folder.
In the list above, "$n$ is even" and "$n$ is odd" sit next to each other, as if both were true.
In the structured proof, each of them lives in its own sub-folder, so they never meet.

### L2 human

We check the structured proof for $n = 6$ and $n = 7$.

1. For $n = 6$, case `<1>1` applies with $k = 3$. Then $n^2 + n = 42 = 2(2 \cdot 9 + 3) = 2 \cdot 21$.
2. For $n = 7$, case `<1>2` applies with $k = 3$. Then $n^2 + n = 56 = 2 \cdot 7 \cdot 4$.
3. The letter $k$ is $3$ in both cases, but the two values belong to different sub-proofs, so no clash arises.

The typical use of this contrast is to choose a format.
A flat table suits a short chain of facts, and levels suit cases and assumptions.
A trap is to number the rows of a table as $1.1$, $1.2$, $2.1$ and to call that hierarchical.
The numbers alone are not enough: each level must be the proof of the step above it, with its own assumptions.
