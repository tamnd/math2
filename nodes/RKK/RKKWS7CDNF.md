---
tag: RKKWS7CDNF
kind: statement
role: theorem
name: Mackey–Arens theorem
msc: [46A20]
uses: [R68HNB5SVR, B6GY2KJMWW, 4A82S5FVRT, P6KHVSTPZV, W18EY4E5TH]
about: [W18EY4E5TH, P6KHVSTPZV, R68HNB5SVR]
sources:
  - url: https://en.wikipedia.org/wiki/Mackey–Arens_theorem
same_as:
  wikidata: Q104841505
  wikipedia: Mackey–Arens theorem
---

## Statement

Let $\mathbb{K}$ be $\R$ or $\C$, let $(X, Y, \langle \cdot, \cdot \rangle)$ be a [[dual pair|R68HNB5SVR]] over $\mathbb{K}$, and let $\mathcal{T}$ be a [[locally convex|B6GY2KJMWW]] topology on $X$.
Say that $\mathcal{T}$ is *compatible* with the pair if the [[continuous dual|4A82S5FVRT]] of $(X, \mathcal{T})$ is exactly the set of linear forms $x \mapsto \langle x, y \rangle$ with $y \in Y$.
Then $\mathcal{T}$ is compatible with the pair if and only if
$$\sigma(X, Y) \subseteq \mathcal{T} \subseteq \tau(X, Y),$$
where $\sigma(X, Y)$ is the [[weak topology|P6KHVSTPZV]] and $\tau(X, Y)$ is the [[Mackey topology|W18EY4E5TH]].

## Remarks

The weak topology is compatible by construction, and it is the coarsest topology for which all the forms $\langle \cdot, y \rangle$ are continuous.
If $\mathcal{T}$ is compatible, each $\mathcal{T}$-neighbourhood of $0$ contains a closed convex balanced neighbourhood $U$ of $0$.
Its polar $U^\circ$ in $Y$ is convex, balanced and $\sigma(Y, X)$-compact by the [[Banach–Alaoglu theorem|1BXEJXQ2YT]], and $U = U^{\circ\circ}$ by the [[bipolar theorem|FX5PWKCMBQ]].
So $U$ is a $\tau(X, Y)$-neighbourhood of $0$, which gives $\mathcal{T} \subseteq \tau(X, Y)$.
That $\tau(X, Y)$ itself is compatible is the harder half; it uses the [[bipolar theorem|FX5PWKCMBQ]] and a compactness argument in the algebraic dual of $Y$.
Example: for a normed space $E$, the weak topology $\sigma(E, E')$ and the norm topology are both compatible with the pair $(E, E')$, so they have the same continuous linear forms.
A consequence: all compatible topologies have the same closed convex sets.
Indeed, by the Hahn–Banach separation theorem, a closed convex set is an intersection of closed half-spaces defined by continuous forms.

## Explanations

### L1 human

Different topologies on a space can give the same continuous linear forms.
The theorem describes all of them at once: they are exactly the locally convex topologies between the weak topology and the Mackey topology.
So the set of continuous linear forms pins down a whole interval of topologies, with a smallest and a largest element.

### L2 human

In duality theory one often starts from a dual pair and asks which topologies on one side give the other side as dual.
The Mackey–Arens theorem answers this completely.
It explains why closed convex sets and bounded sets depend only on the dual pair: they are the same for all compatible topologies.
For bounded sets this is Mackey's theorem.
It also shows that the [[Mackey topology|W18EY4E5TH]] is natural: metrizable and barrelled locally convex spaces carry their Mackey topology.
The proof rests on the [[bipolar theorem|FX5PWKCMBQ]] and on [[Banach–Alaoglu|1BXEJXQ2YT]] compactness.
