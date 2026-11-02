---
tag: JBSSXP4FFY
kind: example
name: Category of modules
msc: [16D90, 13C60, "18E10"]
instance_of: [Y9CZ3MTNF1]
uses: [0NZ8JA25WK, 0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/Category_of_modules
same_as:
  wikidata: Q5051857
  wikipedia: Category of modules
---

## Example

Let $R$ be a [[ring|0B1261B5ED]] with identity.
The *category of left $R$-modules* $R\text{-}\mathbf{Mod}$ has the left [[$R$-modules|0NZ8JA25WK]] as objects and the $R$-linear maps as morphisms, with composition of maps.
A map $f \colon M \to N$ is $R$-linear when $f(x + y) = f(x) + f(y)$ and $f(rx) = r f(x)$ for all $x, y \in M$ and $r \in R$.
It is an [[abelian category|Y9CZ3MTNF1]].
Each $\Hom_R(M, N)$ is an abelian group under pointwise addition, and composition is bilinear.
The zero module is a zero object, and the direct sum $M \oplus N$ is both product and coproduct.
The kernel of $f \colon M \to N$ is the submodule $\set{x \in M : f(x) = 0}$ and the cokernel is $N / f(M)$.
As in abelian groups, each injective linear map is the kernel of its cokernel and each surjective linear map is the cokernel of its kernel.

## Remarks

For $R = \Z$ one gets the [[category of abelian groups|99ZVSM254K]], and for a field $R = k$ the category of vector spaces over $k$.
The module $R$ itself is a [[generator|CK08JW32WB]] and a [[projective object|YXMXAGVC1Q]], and the category has [[enough projectives|J2TX4TDPCX]] since every module is a quotient of a free module.
It also has enough injective objects, which is the basis for derived functors such as $\operatorname{Ext}$ and $\operatorname{Tor}$.
Two rings whose module categories are equivalent are called Morita equivalent; for example $R$ and the ring of $n \times n$ matrices over $R$ are Morita equivalent.

## Explanations

### L1 human

The category of modules over a ring gathers all modules and all linear maps between them.
It behaves much like linear algebra over a field, except that modules need not have bases.
For example, over $R = \Z$ the module $\Z/2\Z$ is not free, yet it is the cokernel of the map $\Z \to \Z$ given by multiplication by $2$.
