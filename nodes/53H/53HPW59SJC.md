---
tag: 53HPW59SJC
kind: definition
name: Shimura variety
msc: [14G35, 11G18]
defines: QT4CF7ZKK5
uses: [2XS84PWE3S, SEH68BA1QQ, ZSM083M97C, PAA93R4WYD, EQSHJPE7H8]
sources:
  - url: https://en.wikipedia.org/wiki/Shimura_variety
---

## Definition

Let $\mathbb{S} = \operatorname{Res}_{\C/\R} \mathbb{G}_m$ be the Deligne torus, so that $\mathbb{S}(\R) = \C^\times$.
Let $G$ be a connected [[reductive group|2XS84PWE3S]] over $\Q$ and let $X$ be a $G(\R)$-conjugacy class of homomorphisms $h \colon \mathbb{S} \to G_\R$.
The pair $(G, X)$ is a *Shimura datum* if for every $h \in X$:

1. The [[Hodge structure|ZSM083M97C]] on the Lie algebra of $G_\R$ defined by $\operatorname{Ad} \circ h$ has only the types $(-1, 1)$, $(0, 0)$ and $(1, -1)$.
2. Conjugation by $h(i)$ is a Cartan involution of the adjoint group $G^{\mathrm{ad}}_\R$.
3. $G^{\mathrm{ad}}$ has no factor defined over $\Q$ on which the projection of $h$ is trivial.

Let $\mathbb{A}_f$ be the finite [[adeles|SEH68BA1QQ]] of $\Q$ and let $K \subseteq G(\mathbb{A}_f)$ be a compact open subgroup.
The *Shimura variety* of level $K$ is
$$\operatorname{Sh}_K(G, X) = G(\Q) \backslash \big( X \times G(\mathbb{A}_f) / K \big),$$
with $G(\Q)$ acting diagonally and $K$ acting on the right of $G(\mathbb{A}_f)$.

## Remarks

The conditions make $X$ a finite union of Hermitian [[symmetric spaces|PAA93R4WYD]], and $\operatorname{Sh}_K(G, X)$ is a finite disjoint union of quotients $\Gamma \backslash X^+$ by arithmetic subgroups $\Gamma$.
By the theorem of Baily and Borel, it is a [[quasi-projective variety|EQSHJPE7H8]] over $\C$, and it is smooth when $K$ is small enough.
By work of Shimura, Deligne and others it has a canonical model over a number field, the reflex field.

Example: let $G = \mathrm{GL}_2$ and let $X$ be the conjugacy class of $h(a + bi) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$.
Then $X$ is identified with $\C \setminus \R$, the union of the upper and lower half-planes, and the Shimura varieties $\operatorname{Sh}_K(\mathrm{GL}_2, X)$ are finite unions of [[modular curves|T5W0CMS0DM]].
For $G = \mathrm{GSp}_{2g}$ one obtains the Siegel modular varieties, which parametrize principally polarized abelian varieties of dimension $g$ with level structure.

Non-example: $G = \mathrm{GL}_3$ admits no Shimura datum, because the symmetric space of $\mathrm{SL}_3(\R)$ has no invariant complex structure, so clauses 1 and 2 cannot both hold.
