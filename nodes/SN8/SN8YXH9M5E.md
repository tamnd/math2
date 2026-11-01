---
tag: SN8YXH9M5E
kind: definition
name: Tensor rank
msc: [15A69, 15A03]
defines: W84NTF77M0
uses: [000AYPA9AJ, 0BF2DE2SYK, 0ZC9YTXZRY]
sources:
  - url: https://en.wikipedia.org/wiki/Tensor_rank_decomposition
---

## Definition

Let $F$ be a field, let $d \ge 1$, and let $V_1, \ldots, V_d$ be finite-dimensional [[vector spaces|000AYPA9AJ]] over $F$.
A *simple tensor* in the [[tensor product|0BF2DE2SYK]] $V_1 \otimes \cdots \otimes V_d$ is a nonzero tensor of the form $v_1 \otimes \cdots \otimes v_d$ with $v_i \in V_i$.
The *rank* of a tensor $T \in V_1 \otimes \cdots \otimes V_d$ is the smallest integer $r \ge 0$ such that $T$ is a sum of $r$ simple tensors.
The zero tensor has rank $0$.

## Remarks

For $d = 2$ and $V_1 = F^m$, $V_2 = F^n$, a tensor is an $m \times n$ matrix, a simple tensor is a rank-one matrix $u v^T$, and the tensor rank is the [[rank of the matrix|0ZC9YTXZRY]].
Example: in $F^2 \otimes F^2 \otimes F^2$ with standard basis $e_1, e_2$, the tensor $T = e_1 \otimes e_1 \otimes e_1 + e_2 \otimes e_2 \otimes e_2$ has rank $2$.
The written sum shows rank at most $2$.
The tensor is not simple: flattening it to a $2 \times 4$ matrix gives rank $2$, while a simple tensor flattens to a matrix of rank $1$.
Non-example of rank $2$: over $\C$, the tensor $e_1 \otimes e_1 \otimes e_2 + e_1 \otimes e_2 \otimes e_1 + e_2 \otimes e_1 \otimes e_1$ has rank $3$, although it is a limit of tensors of rank $2$.
So the set of tensors of rank at most $r$ need not be closed, which leads to the notion of border rank.
The rank of a real tensor can be larger than its rank over $\C$.
Other names are canonical polyadic rank and CP rank.
