---
tag: AE08JXN7CA
kind: definition
name: Birkhoff interpolation
msc: [41A05, 65D05]
defines: FT1YKVBFC9
uses: [SS1YMS2NPC, 9Z50M2WPTP, 0V1EJCT8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Birkhoff_interpolation
---

## Definition

Let $m \ge 1$ and $n \ge 0$, and let $x_1, \dots, x_m \in \R$ be pairwise distinct.
An *incidence matrix* is an $m \times (n + 1)$ matrix $E = (e_{ij})$, with $1 \le i \le m$ and $0 \le j \le n$.
Its entries are $0$ or $1$, and exactly $n + 1$ of them are equal to $1$.
Given real numbers $y_{ij}$ for the pairs with $e_{ij} = 1$, the *Birkhoff interpolation problem* asks for a polynomial $p$ with real coefficients such that:

1. $p = 0$ or $\deg p \le n$;
2. $p^{(j)}(x_i) = y_{ij}$ for every pair $(i, j)$ with $e_{ij} = 1$, where $p^{(j)}$ is the $j$-th [[derivative|0V1EJCT8G6]].

The pair of $E$ and the nodes is *poised* if this problem has exactly one solution for every choice of the data $y_{ij}$.

## Remarks

The conditions form a square linear system in the $n + 1$ coefficients of $p$, so poisedness means that its determinant is nonzero.
If in each row of $E$ the ones form an initial block $e_{i0} = \cdots = e_{i,k_i - 1} = 1$, the problem is [[Hermite interpolation|9Z50M2WPTP]], which is always poised.
If moreover each row has a single one in column $0$, it is [[polynomial interpolation|SS1YMS2NPC]].

Example: nodes $x_1 = 0$, $x_2 = 1$, $n = 1$, conditions $p(0) = a$ and $p'(1) = b$.
For $p = c_0 + c_1 x$ these give $c_0 = a$ and $c_1 = b$, so the problem is poised.

Non-example: nodes $-1, 0, 1$, $n = 2$, conditions $p(-1) = a$, $p'(0) = b$, $p(1) = c$.
For $p = c_0 + c_1 x + c_2 x^2$ the system has the matrix with rows $(1, -1, 1)$, $(0, 1, 0)$, $(1, 1, 1)$, whose determinant is $0$.
For instance $p = x^2 - 1$ is a nonzero solution with zero data, so the problem is not poised.
