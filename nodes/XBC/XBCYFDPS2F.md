---
tag: XBCYFDPS2F
kind: concept
name: Accessibility relation
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [NGHWZ9Y7ZV, 05AVARPXA2, 0X8NMST0J2, 061J5VGSPT, 0GJZW9JFZQ, YHGXV3SQDP]
sources:
  - url: https://en.wikipedia.org/wiki/Accessibility_relation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - wikipedia: en:3708585@r1320635173
    locator: Accessibility relation
    note: adopted
    mention: wikipedia://en/3708585
    sections: [Summary]
same_as:
  wikidata: Q2663311
  wikipedia: Accessibility relation
inventory: [BRP65H8828]
---

## Summary

The accessibility relation of a [[Kripke frame|NGHWZ9Y7ZV]] $(W, R)$ is the [[binary relation|05AVARPXA2]] $R \subseteq W \times W$; $w R v$ says that the world $v$ is a possible alternative to $w$.
The truth of $\square\varphi$ at $w$ depends on $\varphi$ at the worlds of $R[w] = \set{v : w R v}$ only.
The formula $\lozenge\varphi$ at $w$ asks for one such world where $\varphi$ holds.
The main properties are [[reflexive|0X8NMST0J2]], serial, [[symmetric|061J5VGSPT]], [[transitive|0GJZW9JFZQ]] and Euclidean, made exact in [[the definition|YHGXV3SQDP]].
Each of them matches one modal axiom, so the choice of properties of $R$ is the semantic form of the choice of axioms.

## Motivation

The reading "true in all possible worlds" makes every world see every world.
That reading cannot model knowledge, time or obligation, where the alternatives depend on the world.
For knowledge, $v$ is an alternative to $w$ when the agent at $w$ cannot rule out $v$.
For time, $v$ is an alternative to $w$ when $v$ is later than $w$.
For obligation, $v$ is an alternative to $w$ when $v$ is an ideal world by the norms of $w$.
A relation records these choices, and its properties express the intended laws.

## Notation

1. $R[w]$ is the set of successors of $w$; some authors write $R(w)$ or $w{\uparrow}$.
2. $w R^n v$ means that there is an $R$-path of length $n$ from $w$ to $v$, with $R^0$ the identity.
3. $R^{-1}$ is the converse relation, and $R^{*}$ is the reflexive transitive closure.
4. In multimodal logic each box $\square_i$ has its own relation $R_i$, see [[multimodal logic|ERG3KAQWYF]].

## Remarks

### Examples

1. In a card game, the relation "same own card" between deals is an [[equivalence relation|0G8VEZ3WTK]], the frame of knowledge in $\mathsf{S5}$, see [[the card game|81J8VDK9RX]].
2. The strict order $<$ on $\N$ is serial and transitive but not reflexive. It is the frame of "always in the future", see [[the order of the natural numbers|2SVYW67C85]].
3. The relation $\set{(a, b), (b, b)}$ is Euclidean, transitive and serial but neither reflexive nor symmetric, a frame of belief, see [[the Euclidean example|NS4AC3W4FM]].
4. The universal relation $W \times W$ has every property in the list.
5. The empty relation is transitive, symmetric and Euclidean, and it is not serial; on it every $\square\varphi$ is true.

### Non-examples

1. A neighbourhood function $N$ with $N(w) = \set{\set{a}, \set{b}}$ does not come from any accessibility relation, since it is not closed under intersection, see [[the neighbourhood example|G2X3PKG55F]].
2. A relation between worlds of two different frames is not an accessibility relation; it is a relation between models, such as a bisimulation.
3. A ternary relation, as in relevance logic, is not an accessibility relation in the sense of normal modal logic.

### Basic properties

1. Reflexivity, seriality, symmetry, transitivity and the Euclidean property match the axioms $\mathrm{T}$, $\mathrm{D}$, $\mathrm{B}$, $\mathrm{4}$ and $\mathrm{5}$, see [[common modal axiom schemata|FDFQFWPM4X]].
2. Reflexive implies serial, and the converse fails for $<$ on $\N$.
3. A reflexive Euclidean relation is an equivalence relation: from $w R v$ and $w R w$ the Euclidean property gives $v R w$, and symmetry with the Euclidean property gives transitivity.
4. A symmetric transitive relation is Euclidean: from $w R v$ and $w R u$ symmetry gives $v R w$, and transitivity gives $v R u$.
5. The truth of a formula of modal depth $d$ at $w$ depends only on the worlds $v$ with $w R^n v$ for some $n \le d$.

### History

Kripke's papers of 1959 and 1963 put the relation at the center of the semantics.
Similar relational ideas are in the work of Kanger and of Hintikka from the late 1950s; Hintikka used the relation for knowledge and belief.

### Common errors

1. Reading $\lozenge\varphi$ at $w$ as "$\varphi$ holds at some world" instead of "at some successor of $w$".
2. Assuming that a serial relation is reflexive, or that a Euclidean relation is symmetric; $\set{(a,b),(b,b)}$ refutes both.
3. Writing the Euclidean property as transitivity; Euclidean means that two successors of one world see each other.

## Explanations

### L1 human

The arrows of a Kripke frame tell which worlds each world can "see".
In a game of cards I see my own card but not the cards of the other player.
So every deal in which I hold the same card looks the same to me, and my arrows go to exactly these deals.
Because "looks the same" works in both directions and passes along, these arrows form groups.
For "later in time", the arrows point forward, and they never point back.

### L2 human

We check the five properties for $R = \set{(1,1), (1,2), (2,2)}$ on $W = \set{1, 2}$.

1. Reflexive: $(1,1)$ and $(2,2)$ are in $R$.
2. Serial: each world has a successor, since $R$ is reflexive.
3. Not symmetric: $(1,2) \in R$ but $(2,1) \notin R$.
4. Transitive: the only paths of length 2 are $1,1,2$, $1,2,2$, $1,1,1$ and $2,2,2$, and their end pairs are in $R$.
5. Not Euclidean: $1 R 2$ and $1 R 1$, but $(2,1) \notin R$.

So $R$ is a preorder, and the frame validates $\mathrm{T}$ and $\mathrm{4}$ but not $\mathrm{B}$ or $\mathrm{5}$.
The typical use is to read off from the properties of $R$ which axioms the frame validates.
A trap: the properties of $R$ match axioms on frames, not in single models.

### L3 human

From the algebraic view, $R$ gives the operator $\square_R X = \set{w : R[w] \subseteq X}$ on $\mathcal{P}(W)$, and $R$ can be read back from $\square_R$.
Frames are the atomic complete Boolean algebras with completely multiplicative operators.
Properties of $R$ such as reflexivity are equations in this algebra, such as $\square_R X \subseteq X$.
The correspondence of axioms and relational properties extends to the Sahlqvist formulas, a topic of [[modal model theory|SPQVNPZDTB]].
