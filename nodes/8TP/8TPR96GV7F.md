---
tag: 8TPR96GV7F
kind: definition
name: 2-category
msc: [18N10]
defines: CQACXG10JZ
uses: [BPH9SJ30Y0, ZY6R4H65P8, A2DE66937D, 28NQ0KRHD3, KYCPCC57FT]
sources:
  - url: https://en.wikipedia.org/wiki/2-category
---

## Definition

A *2-category* (or strict 2-category) is a category [[enriched|BPH9SJ30Y0]] over the [[category of small categories|ZY6R4H65P8]] $\mathbf{Cat}$ with the Cartesian product as tensor product.
Explicitly, a 2-category $\mathcal{K}$ consists of:

1. a class of objects;
2. for each pair of objects $a, b$, a [[category|A2DE66937D]] $\mathcal{K}(a, b)$ of 1-morphisms $f \colon a \to b$ and 2-morphisms $\theta \colon f \Rightarrow g$, whose composition is called vertical;
3. for each triple $a, b, c$, a [[functor|28NQ0KRHD3]] $\circ \colon \mathcal{K}(b, c) \times \mathcal{K}(a, b) \to \mathcal{K}(a, c)$, called horizontal composition;
4. for each object $a$, an identity 1-morphism $1_a$;

such that horizontal composition is strictly associative and $1_a$ and its identity 2-morphism are strict units for it.

## Remarks

That horizontal composition is a functor is the interchange law: $(\psi' \cdot \psi) \circ (\theta' \cdot \theta) = (\psi' \circ \theta') \cdot (\psi \circ \theta)$, where $\cdot$ is vertical composition.
Example: $\mathbf{Cat}$, with small categories as objects, functors as 1-morphisms and [[natural transformations|KYCPCC57FT]] as 2-morphisms, is a 2-category; composition of functors is strictly associative.
Non-example: rings, bimodules and bimodule maps, with composition of bimodules given by the tensor product, do not form a 2-category.
Take an $R$-$S$-bimodule $M$, an $S$-$T$-bimodule $N$ and a $T$-$U$-bimodule $P$.
The bimodules $(M \otimes_S N) \otimes_T P$ and $M \otimes_S (N \otimes_T P)$ are isomorphic but not equal in general, so strict associativity fails; they form a bicategory instead.
