---
tag: 0HV1SKWPMS
kind: statement
role: theorem
name: Rouché–Capelli theorem
aliases: [kronecker-capelli-theorem]
msc: [15A06]
uses: [0JTRMBQ1SA, 0YCDZ7N8VD, 0EWQEYRVA8]
sources:
  - url: https://en.wikipedia.org/wiki/Rouché–Capelli_theorem
    locator: lead section
same_as:
  wikidata: Q2071632
  wikipedia: Rouché–Capelli theorem
inventory: [CHV02TF7SA]
---

## Statement

Let $F$ be a field, let $A$ be an $m \times n$ matrix over $F$, and let $b \in F^m$.
The [[system|0GT4WWGWH2]] $Ax = b$ has a solution if and only if $\rank A = \rank [A \mid b]$, where $[A \mid b]$ is the [[augmented matrix|0T6MWGZSXA]] and $\rank$ is the [[rank of a matrix|0ZC9YTXZRY]].
If a solution exists, then the solution set is an affine subspace of $F^n$ of dimension $n - \rank A$.
In particular, the solution is unique if and only if $\rank A = n$.

## Remarks

The theorem is also called the Kronecker–Capelli theorem.
If $\rank [A \mid b] = \rank A + 1$, then the system is [[inconsistent|0X6V9B1V10]].
The dimension $n - \rank A$ is the number of free variables.

## Explanations

### L1 human

The theorem says that a system has a solution exactly when the right side adds no new independent information.
If adding the column $b$ raises the rank, then $b$ is not a combination of the columns of $A$, and no solution exists.
When solutions exist, each unknown without a pivot is free, and it adds one dimension to the solution set.
