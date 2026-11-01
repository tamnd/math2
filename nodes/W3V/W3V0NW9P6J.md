---
tag: W3V0NW9P6J
kind: definition
name: Matrix norm
msc: [15A60, 65F35]
defines: 54T6Y6DSY4
uses: [0V2WP9B1MF, 0VD9ZSWWJG, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_norm
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, let $m, n \ge 1$, and let $\mathbb{K}^{m \times n}$ be the vector space of $m \times n$ [[matrices|0VD9ZSWWJG]] over $\mathbb{K}$.
A *matrix norm* on $\mathbb{K}^{m \times n}$ is a map $\norm{\cdot} \colon \mathbb{K}^{m \times n} \to \R$ such that, for all $A, B \in \mathbb{K}^{m \times n}$ and $c \in \mathbb{K}$:

1. $\norm{A} \ge 0$, and $\norm{A} = 0$ only if $A = 0$.
2. $\norm{cA} = \abs{c} \norm{A}$.
3. $\norm{A + B} \le \norm{A} + \norm{B}$.

A matrix norm on $\mathbb{K}^{n \times n}$ is *submultiplicative* if moreover $\norm{AB} \le \norm{A} \norm{B}$ for all $A, B \in \mathbb{K}^{n \times n}$.

## Remarks

Clauses 1 to 3 say that $\norm{\cdot}$ is a [[norm|0V2WP9B1MF]] on $\mathbb{K}^{m \times n}$; many authors include submultiplicativity in the word "matrix norm".
Example: for a vector norm $\abs{\cdot}$ on $\mathbb{K}^n$, the [[operator norm|06EKW1AKXF]] $\norm{A} = \max_{\abs{x} = 1} \abs{Ax}$ is a submultiplicative matrix norm, since $\abs{ABx} \le \norm{A} \abs{Bx} \le \norm{A}\norm{B}\abs{x}$.
Non-example: $\norm{A}_{\max} = \max_{i,j} \abs{a_{ij}}$ is a norm but not submultiplicative.
For $A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ one has $A^2 = 2A$, so $\norm{A^2}_{\max} = 2 > 1 = \norm{A}_{\max}^2$.
All norms on $\mathbb{K}^{m \times n}$ are equivalent, because the space has finite dimension.
