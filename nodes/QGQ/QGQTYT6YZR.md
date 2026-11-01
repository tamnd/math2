---
tag: QGQTYT6YZR
kind: definition
name: Lagrange interpolation
msc: [41A05, 65D05]
defines: 237KR6FRCK
uses: [0QA8CHH8MG, 0Q9EZS90GY, SS1YMS2NPC]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange_polynomial
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]], let $n \ge 0$, let $x_0, \dots, x_n \in K$ be pairwise distinct, and let $y_0, \dots, y_n \in K$.
For $j = 0, \dots, n$, the Lagrange basis polynomial is
$$\ell_j(x) = \prod_{k \ne j} \frac{x - x_k}{x_j - x_k} \in K[x].$$
The Lagrange interpolation polynomial of the data is
$$L(x) = \sum_{j=0}^{n} y_j \, \ell_j(x).$$

## Remarks

Each $\ell_j$ has degree $n$, with $\ell_j(x_j) = 1$ and $\ell_j(x_k) = 0$ for $k \ne j$.
So $L$ has degree at most $n$ and $L(x_i) = y_i$ for all $i$: it is the unique [[interpolation polynomial|SS1YMS2NPC]] of the data.
Example: for the data $(0, 1)$, $(1, 3)$, $(2, 7)$, the basis polynomials are $\ell_0 = \frac{(x-1)(x-2)}{2}$, $\ell_1 = -x(x-2)$ and $\ell_2 = \frac{x(x-1)}{2}$.
Then $L = \ell_0 + 3 \ell_1 + 7 \ell_2 = x^2 + x + 1$, and indeed $L(0) = 1$, $L(1) = 3$, $L(2) = 7$.
Non-example: if two nodes coincide, $x_j = x_k$ with $j \ne k$, the denominator $x_j - x_k$ is $0$ and the formula has no meaning.

## Explanations

### L1 human

Each basis polynomial is a switch that is on at one node and off at all others.
Weighting the switches by the wanted values gives a polynomial through all the points.
