---
about:
- 0BMVBHTWV2
kind: statement
msc:
- 15A03
name: Coordinates in a basis via the basis matrix
role: theorem
sources:
- locator: src/section3-2.xml:746
  url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-2.xml#L746
tag: ~fb0fed49
uses:
- 0BMVBHTWV2
- 0KCQ9Y3QKA
---

## Statement

Let $\mathcal B = (b_1, \dots, b_n)$ be an ordered [[basis|0KCQ9Y3QKA]] of $\R^n$.
Let $P_{\mathcal B}$ be the matrix whose columns are $b_1, \dots, b_n$ in this order.
Then $P_{\mathcal B}$ is invertible, and for each vector $x \in \R^n$ the [[coordinate vector|0BMVBHTWV2]] $[x]_{\mathcal B}$ satisfies
$$x = P_{\mathcal B}\,[x]_{\mathcal B}, \qquad [x]_{\mathcal B} = P_{\mathcal B}^{-1}\,x.$$

## Remarks

The product $P_{\mathcal B}[x]_{\mathcal B}$ is the combination of the columns of $P_{\mathcal B}$ with the coordinates as weights. This is the expansion of $x$ in the basis.
The second formula follows from the first by multiplying with the inverse matrix.
