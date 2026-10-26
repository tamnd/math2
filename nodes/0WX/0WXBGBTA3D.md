---
tag: 0WXBGBTA3D
kind: statement
role: proposition
name: Gram–Schmidt vectors are orthogonal
msc: [15A63, 65F25]
uses: [0VT6P0GNQR, 0TS7VZJBWD]
sources:
  - url: https://en.wikipedia.org/wiki/Gram–Schmidt_process
    locator: Properties
---

## Statement

Let $V$ be an inner product space over $\R$ or $\C$, and let $v_1, \dots, v_k \in V$ be linearly independent.
Let $u_1, \dots, u_k$ be the vectors of the [[Gram–Schmidt process|0VT6P0GNQR]].
Then $u_1, \dots, u_k$ are nonzero and pairwise [[orthogonal|0Y2X7P2WB7]], and
$$\operatorname{span}(u_1, \dots, u_j) = \operatorname{span}(v_1, \dots, v_j) \qquad (1 \le j \le k).$$

## Remarks

The proof is by induction on $j$: by construction, $\langle u_j, u_i \rangle = 0$ for $i < j$.
The vector $u_j$ is nonzero, because $v_j$ is not in $\operatorname{span}(v_1, \dots, v_{j-1})$.
If the $v_i$ are only spanning, then the process produces some zero vectors, and dropping them still gives an orthogonal family with the same span.

## Explanations

### L1 human

The vectors made by Gram–Schmidt are really perpendicular to each other.
Also, the first $j$ new vectors span the same space as the first $j$ old vectors.
So no information is lost at any step.
