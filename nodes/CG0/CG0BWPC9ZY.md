---
tag: CG0BWPC9ZY
kind: definition
name: Tensor product of algebras
msc: [13B02, 16S10, 15A69]
defines: 1735VGRT2P
uses: [0310REJJY8, DPBJ04JMH8, F0HQXQ0HCD, 0VTH8KPCG2]
sources:
  - url: https://en.wikipedia.org/wiki/Tensor_product_of_algebras
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $A$, $B$ be [[$R$-algebras|DPBJ04JMH8]].
The *tensor product* $A \otimes_R B$ is the [[tensor product of $R$-modules|F0HQXQ0HCD]] with the multiplication determined by
$$(a \otimes b)(a' \otimes b') = aa' \otimes bb' \quad \text{for } a, a' \in A,\ b, b' \in B,$$
extended bilinearly to finite sums.
With this multiplication and identity $1 \otimes 1$, it is an $R$-algebra, with structure map $r \mapsto r \otimes 1 = 1 \otimes r$.

## Remarks

The multiplication is well defined because the formula is $R$-bilinear in each pair of arguments.
The maps $a \mapsto a \otimes 1$ and $b \mapsto 1 \otimes b$ are $R$-algebra [[homomorphisms|0VTH8KPCG2]], and their images commute.
If $A$ and $B$ are commutative, then $A \otimes_R B$ is commutative, and it has a universal property.
For every commutative $R$-algebra $C$ and $R$-algebra maps $f \colon A \to C$, $g \colon B \to C$, there is exactly one $R$-algebra map $h \colon A \otimes_R B \to C$ with $h(a \otimes b) = f(a) g(b)$.

Example: $R[x] \otimes_R R[y] \cong R[x, y]$, with $x^i \otimes y^j \mapsto x^i y^j$; both sides are free $R$-modules with these bases, and the map respects products.
Another example is $\C \otimes_\R \C \cong \C[t]/(t^2 + 1) \cong \C \times \C$, by the Chinese remainder theorem, since $t^2 + 1 = (t - i)(t + i)$ over $\C$.

Non-example: the direct product $A \times B$ with componentwise operations is in general not $A \otimes_R B$.
For $A = B = \Q[x]$ over $R = \Q$, the product $\Q[x] \times \Q[x]$ has zero divisors, such as $(1, 0)(0, 1) = 0$, while $\Q[x] \otimes_\Q \Q[x] \cong \Q[x, y]$ is an integral domain.
