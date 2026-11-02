---
tag: 9AVE43G8RT
kind: definition
name: Prime radical
msc: [16N40, 16N60]
defines: WF117EJ2HF
uses: [0894J980RK, 0DDA6CY7GJ, E8K2MN5V1E]
sources:
  - url: https://en.wikipedia.org/wiki/Nilradical_of_a_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]].
The *prime radical* of $R$ is the intersection of all [[prime ideals|E8K2MN5V1E]] of $R$:
$$\operatorname{Nil}_*(R) = \bigcap_{P \text{ prime}} P.$$
It is a [[two-sided ideal|0DDA6CY7GJ]] of $R$.

## Remarks

Example: let $R$ be the ring of upper triangular $2 \times 2$ matrices over a field $k$ and $N$ its strictly upper triangular matrices.
Then $R/N \cong k \times k$, the prime ideals of $R$ are the kernels of the two maps $R \to k$ that take a diagonal entry, and their intersection is $N$.
Non-example: the matrix unit $e_{11}$ is not in the prime radical of $R$, since it is a nonzero idempotent, while every element of the prime radical is nilpotent.
Equivalent forms: $\operatorname{Nil}_*(R)$ is the smallest semiprime ideal of $R$, and it is the set of strongly nilpotent elements of $R$.
It is also called the lower nilradical or the Baer radical, and it is contained in the [[upper nilradical|3G2JQEYBEK]].
For a commutative ring it equals the [[nilradical|QQDN6EYQNJ]].
