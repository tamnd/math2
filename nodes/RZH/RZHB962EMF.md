---
tag: RZHB962EMF
kind: definition
name: Contingency table
msc: [62H17]
defines: PANSMHE0SW
uses: [08QMKTWF9T, 0PNRKMRC55]
sources:
  - url: https://en.wikipedia.org/wiki/Contingency_table
---

## Definition

Let $X$ and $Y$ be categorical [[variables|0PNRKMRC55]] with values in $\set{1, \ldots, r}$ and $\set{1, \ldots, c}$, observed on $n$ units.
The $r \times c$ *contingency table* of the sample is the matrix $N = (n_{ij})$, where $n_{ij}$ is the number of units with $X = i$ and $Y = j$.
The row totals are $n_{i+} = \sum_j n_{ij}$, the column totals are $n_{+j} = \sum_i n_{ij}$, and $\sum_{i,j} n_{ij} = n$.
A contingency table of $m \ge 3$ variables is defined in the same way as an $m$-way array of counts.

## Remarks

The cells correspond to a [[partition|08QMKTWF9T]] of the sample: each unit is counted in exactly one cell.
Example: among $100$ people, $10$ smoke and exercise, $20$ smoke and do not exercise, $40$ do not smoke and exercise, and $30$ do neither.
The table is $\begin{pmatrix} 10 & 20 \\ 40 & 30 \end{pmatrix}$, with row totals $30, 70$, column totals $50, 50$, and grand total $100$.
Non-example: in a survey where people may tick several sports, a table of persons by sport counts some people more than once.
Then the cells do not partition the sample, and the entries need not add up to $n$.
To test independence, the expected counts are $E_{ij} = n_{i+} n_{+j} / n$, and Pearson's statistic is $\sum_{i,j} (n_{ij} - E_{ij})^2 / E_{ij}$.
Under independence and for large $n$, it is approximately chi-squared with $(r - 1)(c - 1)$ degrees of freedom.
