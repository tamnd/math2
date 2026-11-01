---
tag: HC3BQBQECH
kind: definition
name: Boolean matrix
msc: [15B34, 05C50]
defines: AS4WVMYEDZ
uses: [0VD9ZSWWJG, 05AVARPXA2, 0PYSR20HGF]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_matrix
---

## Definition

Let $m, n \ge 1$ be integers.
A *Boolean matrix* of size $m \times n$ is an $m \times n$ [[matrix|0VD9ZSWWJG]] $A = (a_{ij})$ with every entry $a_{ij} \in \set{0, 1}$.
Let $A$ be a Boolean matrix of size $m \times n$ and $B$ one of size $n \times p$.
Their *Boolean product* $A \odot B$ is the $m \times p$ Boolean matrix with entries
$$(A \odot B)_{ik} = \max_{1 \le j \le n} \min(a_{ij}, b_{jk}),$$
that is, $(A \odot B)_{ik} = 1$ exactly when there is some $j$ with $a_{ij} = b_{jk} = 1$.

## Remarks

Equivalently, the entries are computed in the Boolean semiring $\set{0, 1}$ with $1 + 1 = 1$.
For finite sets $X = \set{x_1, \ldots, x_m}$ and $Y = \set{y_1, \ldots, y_n}$, a [[relation|05AVARPXA2]] $R \subseteq X \times Y$ has the Boolean matrix with $a_{ij} = 1$ exactly when $(x_i, y_j) \in R$.
If $S \subseteq Y \times Z$ has matrix $B$, then the [[composite relation|0PYSR20HGF]] "first $R$, then $S$" has matrix $A \odot B$.
Example: for $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $A \odot A = A$, since the entry $(1,2)$ is $\max(\min(1,1), \min(1,1)) = 1$ and the entry $(2,1)$ is $\max(\min(0,1), \min(1,0)) = 0$; the ordinary product would give the entry $2$ at $(1,2)$.
Non-example: $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ is not a Boolean matrix, because the entry $2$ is not in $\set{0, 1}$.
