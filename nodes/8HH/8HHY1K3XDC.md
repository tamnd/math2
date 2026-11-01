---
tag: 8HHY1K3XDC
kind: definition
name: Field norm
msc: [12F05, 11R04]
defines: KRNFEZWPY0
uses: [0NRYPM9Y27, 0RJF668P1T, 03F5KP94K0, 0GK1WB9R98]
sources:
  - url: https://en.wikipedia.org/wiki/Field_norm
---

## Definition

Let $L/K$ be a [[finite extension|0NRYPM9Y27]] and let $\alpha \in L$.
Let $m_\alpha \colon L \to L$ be the map $x \mapsto \alpha x$; it is a [[$K$-linear map|0RJF668P1T]] of the finite-dimensional $K$-vector space $L$.
The *norm* of $\alpha$ from $L$ to $K$ is $N_{L/K}(\alpha) = \det(m_\alpha) \in K$, the [[determinant|03F5KP94K0]] of $m_\alpha$.

## Remarks

The norm is multiplicative: $N_{L/K}(\alpha\beta) = N_{L/K}(\alpha) N_{L/K}(\beta)$, and $N_{L/K}(c) = c^{[L:K]}$ for $c \in K$.
It is transitive in towers: $N_{M/K} = N_{L/K} \circ N_{M/L}$.
If the [[minimal polynomial|0GK1WB9R98]] of $\alpha$ over $K$ is $x^d + a_{d-1}x^{d-1} + \cdots + a_0$, then $N_{L/K}(\alpha) = \left((-1)^d a_0\right)^{[L:K(\alpha)]}$.
If $L/K$ is separable and $\sigma_1, \ldots, \sigma_n$ are the embeddings of $L$ over $K$ into an algebraic closure, then $N_{L/K}(\alpha) = \sigma_1(\alpha) \cdots \sigma_n(\alpha)$.

Example: $L = \Q(i)$, $K = \Q$ and $\alpha = a + bi$ with $a, b \in \Q$.
Check: in the basis $1, i$, the map $m_\alpha$ sends $1 \mapsto a + bi$ and $i \mapsto -b + ai$, so its matrix is $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ and $N(\alpha) = a^2 + b^2$.

Non-example: the complex absolute value $a + bi \mapsto \sqrt{a^2 + b^2}$ is not the norm of $\Q(i)/\Q$, since it does not take values in $\Q$; for example $\abs{1 + i} = \sqrt{2}$.
