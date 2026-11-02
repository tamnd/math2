---
tag: GAMHZY8TWV
kind: statement
role: theorem
name: Pointwise Kan extension formula
msc: [18A40, 18A30]
uses: [RN9D96ESWN, PC6HG1JEGM, BJS1CGTKQ5, CHS5AFJGWE]
about: [RN9D96ESWN]
sources:
  - url: https://en.wikipedia.org/wiki/Kan_extension
---

## Statement

Let $\mathcal{A}$ be a small category, let $\mathcal{B}$ be a locally small category, and let $\mathcal{C}$ be a category that has all small [[colimits|BJS1CGTKQ5]].
Let $K \colon \mathcal{A} \to \mathcal{B}$ and $F \colon \mathcal{A} \to \mathcal{C}$ be functors.
For an object $b$ of $\mathcal{B}$, let $(K \downarrow b)$ be the [[comma category|PC6HG1JEGM]] of pairs $(a, f)$ with $a$ in $\mathcal{A}$ and $f \colon K(a) \to b$.
Let $P_b \colon (K \downarrow b) \to \mathcal{A}$ send $(a, f)$ to $a$.
Then the [[left Kan extension|RN9D96ESWN]] of $F$ along $K$ exists, and for each object $b$ of $\mathcal{B}$
$$(\mathrm{Lan}_K F)(b) = \operatorname{colim} \big( F \circ P_b \colon (K \downarrow b) \to \mathcal{C} \big).$$

## Remarks

The comma category $(K \downarrow b)$ is small because $\mathcal{A}$ is small and $\mathcal{B}$ is locally small, so the colimit exists.
A morphism $g \colon b \to b'$ induces a functor $(K \downarrow b) \to (K \downarrow b')$ by composing with $g$, and hence a map between the colimits; this makes $b \mapsto (\mathrm{Lan}_K F)(b)$ a functor.
The component $\eta_a$ is the colimit injection at the object $(a, \id_{K(a)})$.
The universal property is checked by turning a natural transformation $F \Rightarrow G \circ K$ into a compatible family of cocones, one for each $b$.

Dually, suppose that $\mathcal{C}$ has all small [[limits|CHS5AFJGWE]].
Then $(\mathrm{Ran}_K F)(b)$ is the limit of $F$ over the comma category $(b \downarrow K)$ of pairs $(a, f \colon b \to K(a))$.
When $K$ is fully faithful, the unit $\eta \colon F \Rightarrow (\mathrm{Lan}_K F) \circ K$ is an isomorphism.
The reason is that $(a, \id_{K(a)})$ is then a terminal object of $(K \downarrow K(a))$.

Example: view a group $G$ and a subgroup $H$ as one-object categories, and let $K$ be the inclusion.
Let $F$ be a representation of $H$ on a vector space $V$ over a field $k$.
Then the formula gives the induced representation $k[G] \otimes_{k[H]} V$ of $G$.

## Explanations

### L1 human

The formula builds the extended functor one object at a time.
At an object $b$, it collects all values $F(a)$ for which $K(a)$ maps into $b$ and glues them together by a colimit.
So the extension at $b$ is the best approximation of $F$ seen from everything that lies over $b$.

### L2 human

This is the standard way to show that Kan extensions exist, and it is the version used in most applications.
Taking $\mathcal{B} = \mathbf{1}$ recovers the colimit of $F$.
Taking $K$ to be the Yoneda embedding of $\mathcal{A}$ extends $F$ to a colimit-preserving functor on presheaves.
This is the basis of the nerve and realization adjunctions.
A Kan extension computed by this formula is called pointwise.
In the language of coends the formula reads $(\mathrm{Lan}_K F)(b) = \int^{a} \mathcal{B}(K(a), b) \cdot F(a)$.
Here $S \cdot c$ is the coproduct of copies of $c$ indexed by the set $S$.
