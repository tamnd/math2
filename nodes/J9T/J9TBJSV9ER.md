---
tag: J9TBJSV9ER
kind: statement
role: theorem
name: Schauder's theorem on adjoints of compact operators
msc: [47B07, 47A05]
uses: [06GZ956657, 03TM135G0N, M2NEP1K5AE, VCHS7PH0NF, 4A82S5FVRT]
about: [M2NEP1K5AE, VCHS7PH0NF]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_operator
---

## Statement

Let $X$ and $Y$ be [[Banach spaces|06GZ956657]] over $\R$ or $\C$, with [[continuous duals|4A82S5FVRT]] $X'$ and $Y'$.
Let $T \colon X \to Y$ be a [[bounded linear map|03TM135G0N]], and let $T' \colon Y' \to X'$, $T'(g) = g \circ T$, be its [[dual operator|VCHS7PH0NF]].
Then $T$ is a [[compact operator|M2NEP1K5AE]] if and only if $T'$ is a compact operator.

## Remarks

For the forward direction, let $K$ be the closure of the image of the unit ball of $X$; it is a compact metric space.
The functionals in the unit ball of $Y'$, restricted to $K$, form a bounded and equicontinuous family of continuous functions on $K$.
By the Arzelà–Ascoli theorem, every sequence $(g_n)$ in this ball has a subsequence that converges uniformly on $K$, and then $(T' g_n)$ converges in $X'$.
For the converse, apply the forward direction to $T'$: the bidual $T''$ is compact, and $T$ is its restriction to $X$ under the canonical isometric embeddings $X \subseteq X''$ and $Y \subseteq Y''$.
In a Hilbert space $H$, the same theorem says that a bounded operator $T$ is compact if and only if its Hilbert space adjoint $T^*$ is compact.

## Explanations

### L1 human

A compact operator squeezes the unit ball into a set that is almost finite-dimensional.
Every operator $T$ has a partner $T'$ that acts on linear functionals, the dual operator.
The theorem says that $T$ squeezes in this strong way exactly when its partner does.

### L2 human

The theorem lets one move compactness between a space and its dual.
It is a key step in the Riesz–Schauder theory of compact operators: it shows that $T - \lambda$ and $T' - \lambda$ have kernels of the same finite dimension for $\lambda \ne 0$.
It also shows that the compact operators on a Hilbert space form a closed ideal stable under the adjoint, which is why the quotient by them is a C*-algebra.
