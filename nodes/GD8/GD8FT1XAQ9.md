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

The statement is that for every integer $n$, the number $n^2 + n$ is even.
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

The mathematics is correct, and for a school reader the table is a fair [[proof by cases|0WCP0PVET6]].
It is not a [[structured proof|H2W8D7BMSW]], and the missing feature is levels.
Rows 3 and 5 are case assumptions, yet they stand at the same level as the given fact in row 1, so their scope is not shown.
Read as one flat list, rows 3 and 5 together say $2k = 2k + 1$, and the letter $k$ has two meanings.
Row 7 cites rows 4 and 6, each of which holds only in its own case, and it does not cite row 2, the reason why the two cases cover every integer.
No row has its own sub-proof, so the table cannot say that rows 3 and 4 together settle one case.

Here is the structured proof of the same statement.

- `<1>1.` CASE: $n$ is even.
    - `<2>1.` PICK an integer $k$ with $n = 2k$.
      PROOF: by the case assumption.
    - `<2>2.` Q.E.D.
      PROOF: $n^2 + n = 2(2k^2 + k)$ by `<2>1`.
- `<1>2.` CASE: $n$ is odd.
    - `<2>1.` PICK an integer $k$ with $n = 2k + 1$.
      PROOF: by the case assumption.
    - `<2>2.` Q.E.D.
      PROOF: $n^2 + n = 2(2k + 1)(k + 1)$ by `<2>1`.
- `<1>3.` Q.E.D.
  PROOF: by `<1>1` and `<1>2`, since every integer is even or odd.

Each case is now a sub-proof, and its letter $k$ and its assumption end with it.

## Remarks

Both formats number their steps, which is why students mix them up, but only the structured proof has levels.
A table in the style of Fitch, with each case indented, would come close to a structured proof, because the indentation plays the role of the levels.

The algebra in row 6 holds because $(2k + 1)^2 + (2k + 1) = (2k + 1)\bigl((2k + 1) + 1\bigr) = (2k + 1)(2k + 2)$.
A shorter proof avoids cases altogether: $n^2 + n = n(n + 1)$, and one of two consecutive integers is even.
Its structured form has a single level.

## Explanations

### L1 human

Two ways of writing a proof can both use numbered lines and still differ.
A two-column proof is one long list, like a shopping list.
A structured proof is like a folder with sub-folders, where each case has its own sub-folder.
In the table above, "$n$ is even" and "$n$ is odd" sit next to each other, as if both were true.
In the structured proof, each lives in its own sub-folder, so they never meet.

### L2 human

We check the structured proof for $n = 6$ and $n = 7$.
For $n = 6$, case `<1>1` applies with $k = 3$, and $n^2 + n = 42 = 2 \cdot 21$, where $21 = 2 \cdot 9 + 3$.
For $n = 7$, case `<1>2` applies with $k = 3$, and $n^2 + n = 56 = 2 \cdot 7 \cdot 4$.
The letter $k$ is $3$ both times, but the two values belong to different sub-proofs, so no clash arises.

A flat table suits a short chain of facts, and levels suit cases and assumptions.
Watch out: numbering the rows of a table as $1.1$, $1.2$ and $2.1$ does not make it hierarchical.
Each level must be the proof of the step above it, with its own assumptions.
