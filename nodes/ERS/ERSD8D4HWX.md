---
tag: ERSD8D4HWX
kind: statement
role: lemma
name: Morse lemma
msc: [57R70, 58K05]
uses: [F45VQ47GPV, KPQ96640ZJ, 0YTCMFB4HC, 0693Y2METT]
about: [KPQ96640ZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Morse_theory
---

## Statement

Let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$, and let $f \colon M \to \R$ be smooth.
Let $p$ be a nondegenerate [[critical point|0YTCMFB4HC]] of $f$ of index $\lambda$, in the sense of [[Morse functions|KPQ96640ZJ]].
Then there is a chart $(U, (x_1, \dots, x_n))$ of $M$ with $p \in U$ and $x_i(p) = 0$ for all $i$, such that on $U$
$$f = f(p) - x_1^2 - \cdots - x_\lambda^2 + x_{\lambda+1}^2 + \cdots + x_n^2.$$

## Remarks

The idea of the proof is this.
Work in a chart centred at $p$ with $f(p) = 0$; by Taylor's formula with integral remainder, $f(x) = \sum_{i,j} x_i x_j h_{ij}(x)$ with $h_{ij}$ smooth, symmetric in $i, j$, and $h_{ij}(0) = \frac{1}{2} \partial^2 f / \partial x_i \partial x_j(0)$.
Since the matrix $(h_{ij}(0))$ is invertible, one can complete squares one variable at a time, as in the diagonalisation of a quadratic form, with smooth coefficients near $0$.
Sylvester's law of inertia shows that the number of minus signs is the index of the [[Hessian|0693Y2METT]].
Example: $f(x, y) = x^2 - y^2 + y^3$ has a nondegenerate critical point of index $1$ at the origin, and near it the change $u = x$, $v = y \sqrt{1 - y}$ gives $f = u^2 - v^2$.
Nondegeneracy is needed: $f(x) = x^3$ cannot be written as $\pm x_1^2$ in any chart near $0$, since it changes sign at $0$.

## Explanations

### L1 human

Near a clean peak, pit or saddle, a function looks exactly like a sum of squares with some minus signs, once one chooses the right curved coordinates.
The number of minus signs counts the independent downhill directions.
So the local picture at a nondegenerate critical point is completely determined by one integer.

### L2 human

The Morse lemma is the local input of Morse theory.
It shows that nondegenerate critical points are isolated, and it describes how the sublevel set $\set{f \le c}$ changes when $c$ passes a critical value: a handle of index $\lambda$ is attached.
This leads to handle decompositions, to the Morse inequalities, and to Morse homology.
It is the simplest case of the classification of singularities of smooth functions.
