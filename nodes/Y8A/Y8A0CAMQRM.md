---
tag: Y8A0CAMQRM
kind: definition
name: Hermitian K-theory
msc: [19G38, 19D23]
defines: CZZCPA2VQS
uses: [7W52X4N3NJ, 48P4A1CX85, BFFA03GE3V, NJQY3GHY7H, KG8D0N6712]
sources:
  - url: https://en.wikipedia.org/wiki/Witt_group
---

## Definition

Let $R$ be a [[ring with involution|7W52X4N3NJ]] $a \mapsto \bar a$ in which $2$ is invertible, and let $\varepsilon \in \set{1, -1}$.
Let $P$ be a finitely generated [[projective|BFFA03GE3V]] right $R$-module.
An *$\varepsilon$-hermitian form* on $P$ is a biadditive map $h \colon P \times P \to R$ such that:

1. $h(xa, yb) = \bar a \, h(x, y) \, b$ for all $x, y \in P$ and $a, b \in R$;
2. $h(y, x) = \varepsilon \overline{h(x, y)}$ for all $x, y \in P$;
3. the map $P \to \Hom_R(P, R)$, $x \mapsto h(x, -)$, is bijective.

Let $\mathcal{H}^\varepsilon(R)$ be the category whose objects are such pairs $(P, h)$ and whose morphisms are isometries.
Orthogonal sum makes it a symmetric monoidal category.
The *$\varepsilon$-hermitian K-theory* of $R$ is the [[K-theory of this symmetric monoidal category|NJQY3GHY7H]], written $GW^\varepsilon(R)$.
Its homotopy groups are the hermitian K-groups $GW^\varepsilon_n(R)$.

## Remarks

The group $GW^\varepsilon_0(R)$ is the Grothendieck group of isometry classes of $\varepsilon$-hermitian forms under orthogonal sum.
For a field $F$ of characteristic not $2$ with trivial involution and $\varepsilon = 1$, it is the [[Grothendieck–Witt group|KG8D0N6712]] $GW(F)$.
Example: $GW^1_0(\R) \cong \Z \oplus \Z$, by Sylvester's law of inertia.
Non-example: a form on $\R^2$ such as $h(x, y) = x_1 y_1$ fails clause 3, since $x \mapsto h(x, -)$ kills $(0, 1)$, so it is not an object of $\mathcal{H}^1(\R)$.
Forgetting the form gives a map to K-theory, and the hyperbolic construction $P \mapsto P \oplus \Hom_R(P, R)$ gives a map back.
On $\pi_0$, the cokernel of the hyperbolic map is the Witt group of $R$.
Notations vary: Karoubi writes ${}_\varepsilon L_n(R)$, and some authors write $KO$.
