---
tag: 8JMZDBJNZR
kind: definition
name: Additive energy
msc: [11B30, 11P70]
defines: MAQKH72P6V
uses: [082GHNPJ53, XNBN31HQWB]
sources:
  - url: https://en.wikipedia.org/wiki/Additive_combinatorics
---

## Definition

Let $G$ be an [[abelian group|082GHNPJ53]], and let $A$ and $B$ be finite subsets of $G$.
The *additive energy* of $A$ and $B$ is the number
$$E(A, B) = \abs{\set{(a_1, a_2, b_1, b_2) \in A \times A \times B \times B : a_1 + b_1 = a_2 + b_2}}.$$
One writes $E(A) = E(A, A)$.

## Remarks

Let $r(x)$ be the number of pairs $(a, b) \in A \times B$ with $a + b = x$.
Then $E(A, B) = \sum_{x} r(x)^2$, summed over the [[sumset|XNBN31HQWB]] $A + B$.
For $A = \set{0, 1, 2}$ in $\Z$, the values of $r$ on $0, 1, 2, 3, 4$ are $1, 2, 3, 2, 1$, so $E(A) = 1 + 4 + 9 + 4 + 1 = 19$.
A quadruple with $a_1 + b_1 \ne a_2 + b_2$ is not counted; for example $(0, 1, 0, 0)$ is not counted for $A = B = \set{0, 1, 2}$, since $0 + 0 \ne 1 + 0$.
The trivial quadruples with $a_1 = a_2$ and $b_1 = b_2$ always count, so $E(A, B) \ge \abs{A}\abs{B}$.
Also $E(A, B) \le \min(\abs{A}^2\abs{B}, \abs{A}\abs{B}^2)$.
The Cauchy–Schwarz inequality gives $E(A, B) \ge \abs{A}^2 \abs{B}^2 / \abs{A + B}$.
