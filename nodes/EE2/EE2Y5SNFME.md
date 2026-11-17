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

Claim: for each integer $n \ge 1$,
$$1 + 3 + 5 + \cdots + (2n - 1) = n^2.$$
The picture is an $n \times n$ square of cells, cut into $n$ L-shaped layers.
The first layer is the corner cell, and each next layer wraps around the previous square on two sides.
We turn the picture into a [[proof without words|V6ESFEFKJC]] by stating what the eye sees.

1. Give each cell of the square the coordinates $(i, j)$, with $1 \le i \le n$ for the row and $1 \le j \le n$ for the column.
2. For $k = 1, \ldots, n$, let layer $k$ be the set of cells with $\max(i, j) = k$. This is the L-shape of the picture: the cells of row $k$ and of column $k$ inside the first $k$ rows and columns.
3. Each cell lies in exactly one layer, because $\max(i, j)$ is one number between $1$ and $n$. So the layers cover the square, with no overlap.
4. Layer $k$ has the $k$ cells $(k, 1), \ldots, (k, k)$ of row $k$, and the $k - 1$ cells $(1, k), \ldots, (k - 1, k)$ of column $k$ above the corner. So layer $k$ has $k + (k - 1) = 2k - 1$ cells.
5. We count the cells of the square in two ways. By rows and columns there are $n^2$ cells. By layers there are $1 + 3 + \cdots + (2n - 1)$ cells, by steps 3 and 4.
6. The two counts are equal, so $1 + 3 + \cdots + (2n - 1) = n^2$.
7. Check for $n = 5$: $1 + 3 + 5 + 7 + 9 = 25 = 5^2$.

## Remarks

The example shows how a picture becomes a proof.
Step 2 states the rule that makes the picture work for every $n$, and step 4 is the one count that the eye does.
Steps 5 and 6 are a [[double counting|0F8YBHF2W3]] argument, and the layer rule shows why the [[square numbers|HCGCPW8ZFE]] appear.

The same picture changes in a simple way when we change the shape.
Take an $n \times (n + 1)$ rectangle, and let layer $k$ be the part of the $k \times (k + 1)$ rectangle outside the $(k - 1) \times k$ rectangle.
Layer $k$ has $k(k + 1) - (k - 1)k = 2k$ cells, so $2 + 4 + \cdots + 2n = n(n + 1)$.

The page [[three kinds of reasoning on the sum of the first odd numbers|5W8G4689R2]] uses the same picture as the explanation of a guess, and then proves the guess by a telescoping sum.
The page [[the sum of the first n odd numbers by induction|QSWRESJAZ4]] gives the proof by induction.
The picture and the induction proof prove the same identity, but only the picture shows where the squares come from.

## Explanations

### L1 human

Put one coin on a table.
Add $3$ coins around it to make a $2 \times 2$ square.
Add $5$ more coins along two sides to make a $3 \times 3$ square.
Each time we add the next odd number of coins, and each time we get the next square.
So $1 + 3 + 5 + 7$ is the number of coins in a $4 \times 4$ square, which is $16$.

### L2 human

We check the layers for $n = 3$.

1. Layer $1$ is the cell $(1, 1)$. It has $1$ cell, and $2 \cdot 1 - 1 = 1$.
2. Layer $2$ is the cells $(2, 1)$, $(2, 2)$ and $(1, 2)$. It has $3$ cells, and $2 \cdot 2 - 1 = 3$.
3. Layer $3$ is the cells $(3, 1)$, $(3, 2)$, $(3, 3)$, $(1, 3)$ and $(2, 3)$. It has $5$ cells, and $2 \cdot 3 - 1 = 5$.
4. The three layers hold $1 + 3 + 5 = 9$ cells, and the square has $3^2 = 9$ cells.

The typical use of this picture is to explain the identity before or after a proof by induction.
A trap is to count the corner cell of a layer twice: row $k$ and column $k$ share the cell $(k, k)$, so the layer has $2k - 1$ cells and not $2k$.
