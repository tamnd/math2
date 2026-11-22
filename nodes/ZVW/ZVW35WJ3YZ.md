---
tag: ZVW35WJ3YZ
kind: example
name: The pointwise product of two linear maps is not their composite
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
not_instance_of:
  - target: 00BKRZKMSS
    note: for S(x) = 2x and T(x) = 3x on R, the pointwise product is 6x², while the composite is 6x
uses: [05YBKMRVAR, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Definition and first consequences
---

## Example

Multiplying the outputs of two linear maps is a different operation from composing them, and it does not even give a linear map.
Let $S(x) = 2x$ and $T(x) = 3x$ on $\R$, which are both [[linear maps|0RJF668P1T]], and let $P$ be the pointwise product, $P(x) = S(x) \cdot T(x)$.

1. The pointwise product is $P(x) = 2x \cdot 3x = 6x^2$.
2. The [[composite|05YBKMRVAR]] is $(T \circ S)(x) = T(2x) = 6x$.
3. At $x = 1$ the two agree, since $P(1) = 6 = (T \circ S)(1)$, but at $x = 2$ we get $P(2) = 24$ and $(T \circ S)(2) = 12$, so $P \ne T \circ S$.
4. The map $P$ is not linear, because $P(1 + 1) = 24$ while $P(1) + P(1) = 12$.

So the pointwise product is not the composite, and it is not a linear map.

## Remarks

The pointwise product needs a way to multiply two outputs, so it needs a multiplication in the target.
A general vector space has no product of two vectors, and there the pointwise product is not defined at all.
The composite needs no such thing, which is one reason why composition is the product used for linear maps.

The pointwise sum behaves differently: $S + T$ is $x \mapsto 5x$, which is linear, and pointwise sums give the vector space structure on the [[space of linear maps|0X9MBPP2Z3]].
For maps $\R \to \R$ in general, the composite of $x \mapsto ax$ and $x \mapsto bx$ is $x \mapsto abx$, which is linear, while their pointwise product $x \mapsto abx^2$ is linear only when $ab = 0$.

## Explanations

### L1 human

Multiplying the outputs of two linear maps is not the same as doing one map after the other.
Here the product gives $6x^2$, whose graph is a parabola, while the composite gives $6x$, whose graph is a line.

### L2 human

In the [[algebra of endomorphisms|5JA4CYT1TB]] the product of two maps is their composite, not their pointwise product.
The same choice is made for matrices: the matrix product describes composition, and the entrywise product of two matrices is a different operation.
Watch out: when you see $TS$ for linear maps, read it as "first $S$, then $T$", never as a product of values.
