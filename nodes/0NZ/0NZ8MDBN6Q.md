---
tag: 0NZ8MDBN6Q
kind: definition
name: Adjacency matrix
msc: [05C50]
defines: 08B9CX109G
uses: [0JD5C82QMB]
sources:
  - url: https://en.wikipedia.org/wiki/Adjacency_matrix
    locator: Definition
---

## Definition

Let $G$ be a finite [[graph|0JD5C82QMB]] with vertex set $\{v_1, \dots, v_n\}$.
The adjacency matrix of $G$ is the $n \times n$ matrix $A = (a_{ij})$ with
$$a_{ij} = \begin{cases} 1 & \text{if } v_i \sim v_j, \\ 0 & \text{otherwise.} \end{cases}$$

## Remarks

The matrix $A$ is symmetric and has zeros on the diagonal. The sum of row $i$ is the [[degree|0T0F6CCS9W]] of $v_i$.
The entry $(A^k)_{ij}$ is the number of [[walks|0VJZM0F9YM]] of length $k$ from $v_i$ to $v_j$.
Another order of the vertices gives the matrix $P^{T} A P$ for a permutation matrix $P$.

## Explanations

### L1 human

The adjacency matrix is a table of zeros and ones. A $1$ in row $i$ and column $j$ means that vertices $i$ and $j$ are joined.
For a triangle, every entry off the diagonal is $1$.
