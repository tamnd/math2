---
tag: EE2Y5SNFME
kind: example
name: The sum of the first n odd numbers as a picture
msc: ["00A35", "11B83"]
topics: [1BTHSHST4M]
audience: school
instance_of: [V6ESFEFKJC]
uses: [V6ESFEFKJC, HCGCPW8ZFE, 0F8YBHF2W3]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_without_words
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Square_number
    locator: Properties
---

## Example

The statement is: for every integer $n \ge 1$,
$$1 + 3 + 5 + \dots + (2n - 1) = n^2.$$
The picture is an $n \times n$ square of cells, cut into $n$ L-shaped layers.
The first layer is the corner cell, and each later layer wraps around the square before it on two sides.
For $n = 4$, label each cell with its layer:
$$\begin{array}{cccc} 1 & 2 & 3 & 4 \\ 2 & 2 & 3 & 4 \\ 3 & 3 & 3 & 4 \\ 4 & 4 & 4 & 4 \end{array}$$
The picture shows the case $n = 4$ only.
What it leaves out is the rule that makes every $n$ work, and the steps below supply that rule, so that the picture becomes a [[proof without words|V6ESFEFKJC]] with the words written out.

1. Give each cell the position $(i, j)$, with row $i$ and column $j$ between $1$ and $n$.
2. For $k = 1, \dots, n$, let layer $k$ be the set of cells with $\max(i, j) = k$.
   This is the L-shape of the picture: the cells of row $k$ and of column $k$ inside the first $k$ rows and columns.
3. Each cell lies in exactly one layer, because $\max(i, j)$ is one number between $1$ and $n$.
   So the layers cover the square with no overlap.
4. Layer $k$ has the $k$ cells $(k, 1), \dots, (k, k)$ of row $k$ and the $k - 1$ cells $(1, k), \dots, (k - 1, k)$ of column $k$ above the corner.
   So it has $k + (k - 1) = 2k - 1$ cells.
5. Count the cells of the square in two ways.
   By rows there are $n^2$ cells, and by layers there are $1 + 3 + \dots + (2n - 1)$ cells, by steps 3 and 4.
6. The two counts agree, so $1 + 3 + \dots + (2n - 1) = n^2$.
7. Check for $n = 5$: $1 + 3 + 5 + 7 + 9 = 25 = 5^2$.

## Remarks

The example shows how a picture becomes a proof.
Step 2 states the rule that the eye applies without saying it, and step 4 is the one count that the eye does.
Steps 5 and 6 are a [[double counting|0F8YBHF2W3]] argument, and the layer rule explains why the [[square numbers|HCGCPW8ZFE]] appear: each odd number is the border that grows one square into the next.

Change the shape and the same idea gives a new identity.
In an $n \times (n + 1)$ rectangle, let layer $k$ be the part of the $k \times (k + 1)$ rectangle outside the $(k - 1) \times k$ rectangle.
That layer has
$$k(k + 1) - (k - 1)k = 2k$$
cells, so the same count gives $2 + 4 + \dots + 2n = n(n + 1)$.

[[Three kinds of reasoning on the sum of the first odd numbers|5W8G4689R2]] uses the same picture to explain a guess, and then proves the guess with a telescoping sum.
[[The sum of the first n odd numbers by induction|QSWRESJAZ4]] gives the induction proof.
Both prove the same identity, but only the picture shows where the squares come from.

## Explanations

### L1 human

Put one coin on a table.
Add $3$ coins around it to make a $2 \times 2$ square.
Add $5$ more coins along two sides to make a $3 \times 3$ square.
Each time you add the next odd number of coins, you get the next square.
So $1 + 3 + 5 + 7$ is the number of coins in a $4 \times 4$ square, which is $16$.

### L2 human

We check the layers for $n = 3$ cell by cell.
Layer $1$ is the cell $(1, 1)$, so it has $1 = 2 \cdot 1 - 1$ cell.
Layer $2$ is the cells $(2, 1)$, $(2, 2)$ and $(1, 2)$, so it has $3 = 2 \cdot 2 - 1$ cells.
Layer $3$ is the cells $(3, 1)$, $(3, 2)$, $(3, 3)$, $(1, 3)$ and $(2, 3)$, so it has $5 = 2 \cdot 3 - 1$ cells.
Together the layers hold
$$1 + 3 + 5 = 9 = 3^2$$
cells, which is the whole square.
The typical use of the picture is to explain the identity before or after a proof by induction.
Watch out for the corner cell: row $k$ and column $k$ share the cell $(k, k)$, so a layer has $2k - 1$ cells and not $2k$.
