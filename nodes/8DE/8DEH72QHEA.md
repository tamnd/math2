---
tag: 8DEH72QHEA
kind: definition
name: f-vector and h-vector
msc: ["05E45", 52B05]
defines: DCK64GFPD7
uses: [V8GZ0W1ZZ5, 0GBZM0MT0F]
sources:
  - url: https://en.wikipedia.org/wiki/H-vector
---

## Definition

Let $\Delta$ be a finite [[simplicial complex|V8GZ0W1ZZ5]] of dimension $d - 1$, with $d \ge 1$.
For $-1 \le i \le d - 1$, let $f_i$ be the number of faces of $\Delta$ of dimension $i$, that is, with $i + 1$ vertices; so $f_{-1} = 1$ counts the empty face.
The *f-vector* of $\Delta$ is $(f_{-1}, f_0, \dots, f_{d-1})$.
The *h-vector* of $\Delta$ is the sequence $(h_0, h_1, \dots, h_d)$ defined by
$$\sum_{i=0}^{d} h_i \, t^{d-i} = \sum_{i=0}^{d} f_{i-1} \, (t - 1)^{d-i}.$$

## Remarks

Comparing coefficients gives $h_k = \sum_{i=0}^{k} (-1)^{k-i} \binom{d-i}{k-i} f_{i-1}$.
In particular $h_0 = 1$, $h_1 = f_0 - d$, and $h_0 + h_1 + \dots + h_d = f_{d-1}$.
The f-vector can be recovered from the h-vector, so both carry the same information.
For a simplicial polytope of dimension $d$ one uses the f-vector and h-vector of its boundary complex, which has dimension $d - 1$.

Example: the boundary of an octahedron has $d = 3$ and $f = (1, 6, 12, 8)$.
Then $(t-1)^3 + 6(t-1)^2 + 12(t-1) + 8 = t^3 + 3t^2 + 3t + 1$, so $h = (1, 3, 3, 1)$, and indeed $1 + 3 + 3 + 1 = 8 = f_2$.

Non-example of a nice property: the h-vector can have negative entries.
For two disjoint edges, $d = 2$ and $f = (1, 4, 2)$, and $(t-1)^2 + 4(t-1) + 2 = t^2 + 2t - 1$ gives $h = (1, 2, -1)$.
