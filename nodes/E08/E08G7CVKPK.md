---
tag: E08G7CVKPK
kind: statement
role: lemma
name: The inverse of a bijective linear map is linear
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
about: [0B8T10CE7N]
uses: [0XSJ25Z9M4, 0W766JAPSN]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Linear endomorphisms and isomorphisms
  - book: isbn:9780134860244
    locator: Section 2.4
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Statement

If a linear map can be undone, then the map that undoes it is linear too.

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear isomorphism|0XSJ25Z9M4]].
Then the [[inverse function|0W766JAPSN]] $T^{-1} \colon W \to V$ is linear, so $T^{-1}$ is again a linear isomorphism.

## Remarks

### Why the hypotheses are needed

Bijectivity is needed for $T^{-1}$ to exist as a function on all of $W$.
Linearity of $T$ is needed as well.
The bijection $x \mapsto x^3$ of $\R$ has the inverse $x \mapsto \sqrt[3]{x}$, which is not linear, since $\sqrt[3]{8} = 2$ while $8 \sqrt[3]{1} = 8$.

### What it gives you

The relation $V \cong W$ is symmetric, so $\cong$ is an equivalence relation.
The automorphisms of $V$ form a group $GL(V)$ under composition, since inverses stay inside.
For an invertible matrix $A$, the map $x \mapsto A^{-1}x$ is the inverse of $x \mapsto Ax$.
To show that an inverse is linear, it is enough to know that it exists, without finding a formula.

### The converse

If $T$ is a bijection and $T^{-1}$ is linear, then $T$ is linear, by the lemma applied to $T^{-1}$.

### Generalizations

The same holds for bijective homomorphisms of groups, rings and modules, with the same proof.
It fails for continuous maps, since a continuous bijection can have a discontinuous inverse.
For Banach spaces, the bounded inverse theorem says that a continuous linear bijection does have a continuous inverse.

## History

The lemma is part of the abstract theory of linear maps begun by Peano in 1888.
For matrices, the inverse of an invertible matrix already appears in Cayley's memoir of 1858.

## Explanations

### L1 human

If a linear map can be undone, then the undoing map is also linear.
So the inverse of a rotation is a rotation, and the inverse of a shear is a shear.

### L2 human

Let $T(x, y) = (x + y, \; y)$ on $\R^2$, a shear.

1. Solving $T(x, y) = (u, v)$ gives $y = v$ and $x = u - v$, so $T^{-1}(u, v) = (u - v, \; v)$.
2. This formula is linear, as the lemma predicts.
3. Check: $T(T^{-1}(3, 1)) = T(2, 1) = (3, 1)$.

The lemma saves the work of step 1 when only linearity of the inverse is needed.
