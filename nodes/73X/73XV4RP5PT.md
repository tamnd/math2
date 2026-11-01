---
tag: 73XV4RP5PT
kind: definition
name: Field trace
msc: [12F05, 11R04]
defines: WPE5Z53QYJ
uses: [0NRYPM9Y27, 0RJF668P1T, 0RPDTWY2JS, 0GK1WB9R98]
sources:
  - url: https://en.wikipedia.org/wiki/Field_trace
---

## Definition

Let $L/K$ be a [[finite extension|0NRYPM9Y27]] and let $\alpha \in L$.
Let $m_\alpha \colon L \to L$ be the map $x \mapsto \alpha x$; it is a [[$K$-linear map|0RJF668P1T]] of the finite-dimensional $K$-vector space $L$.
The *trace* of $\alpha$ from $L$ to $K$ is $\mathrm{Tr}_{L/K}(\alpha) = \tr(m_\alpha) \in K$, the [[trace|0RPDTWY2JS]] of $m_\alpha$.

## Remarks

The map $\mathrm{Tr}_{L/K} \colon L \to K$ is $K$-linear, and $\mathrm{Tr}_{L/K}(c) = [L:K]\, c$ for $c \in K$.
It is transitive in towers: $\mathrm{Tr}_{M/K} = \mathrm{Tr}_{L/K} \circ \mathrm{Tr}_{M/L}$.
If the [[minimal polynomial|0GK1WB9R98]] of $\alpha$ over $K$ is $x^d + a_{d-1}x^{d-1} + \cdots + a_0$, then $\mathrm{Tr}_{L/K}(\alpha) = -[L:K(\alpha)]\, a_{d-1}$.
If $L/K$ is separable and $\sigma_1, \ldots, \sigma_n$ are the embeddings of $L$ over $K$ into an algebraic closure, then $\mathrm{Tr}_{L/K}(\alpha) = \sigma_1(\alpha) + \cdots + \sigma_n(\alpha)$.
The map $\mathrm{Tr}_{L/K}$ is not identically zero if and only if $L/K$ is separable.

Example: $L = \Q(i)$, $K = \Q$ and $\alpha = a + bi$ with $a, b \in \Q$.
Check: the matrix of $m_\alpha$ in the basis $1, i$ is $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$, so $\mathrm{Tr}(\alpha) = 2a$.

Non-example: the real part $a + bi \mapsto a$ is $\Q$-linear but is not the trace of $\Q(i)/\Q$; it is half of it, since $\mathrm{Tr}(1) = [\Q(i):\Q] = 2$.
