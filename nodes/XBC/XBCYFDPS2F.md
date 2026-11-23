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

The accessibility relation says which worlds count as possible alternatives to which, and its shape decides which modal laws hold.
Take two worlds $1$ and $2$ with $R = \{ (1,1), (1,2), (2,2) \}$.
Each world sees itself, so the relation is reflexive, and $\square p \to p$ holds at every world for every choice of $p$.
World $1$ sees $2$ but $2$ does not see $1$, so the relation is not symmetric, and $p \to \square\lozenge p$ fails at $1$ when $p$ is true only at $1$.

The accessibility relation of a [[Kripke frame|NGHWZ9Y7ZV]] $(W, R)$ is the [[binary relation|05AVARPXA2]] $R \subseteq W \times W$, and $w R v$ says that $v$ is a possible alternative to $w$.
The truth of $\square\varphi$ and $\lozenge\varphi$ at $w$ depends only on $\varphi$ at the worlds of $R[w] = \{ v : w R v \}$.
The main properties are [[reflexive|0X8NMST0J2]], serial, [[symmetric|061J5VGSPT]], [[transitive|0GJZW9JFZQ]] and Euclidean, made exact in [[the definition|YHGXV3SQDP]].

## Motivation

The reading "true in all possible worlds" makes every world see every world.
That reading cannot model knowledge, time or obligation, where the alternatives depend on the world.
For knowledge, $v$ is an alternative to $w$ when the agent at $w$ cannot rule out $v$.
For time, $v$ is an alternative to $w$ when $v$ is later than $w$.
For obligation, $v$ is an alternative to $w$ when $v$ is an ideal world by the norms of $w$.

A relation records these choices, and its properties express the intended laws.
Each of the five properties matches one axiom, as [[common modal axiom schemata|FDFQFWPM4X]] proves, so the choice of properties of $R$ is the semantic form of the choice of axioms.
This match is what makes the completeness theorems of the [[canonical model|TVE4F04KME]] possible.

## Notation

We write $R[w]$ for the set of successors of $w$, and some authors write $R(w)$ or $w{\uparrow}$.
We write $w R^n v$ when an $R$-path of length $n$ leads from $w$ to $v$, with $R^0$ the identity.
$R^{-1}$ is the converse relation and $R^{*}$ is the reflexive transitive closure.
In [[multimodal logic|ERG3KAQWYF]] each box $\square_i$ has its own relation $R_i$.

## Remarks

### Reading the properties

Each property has a plain reading.
Reflexive says that the actual world is among its own alternatives, and serial says that every world has an alternative.
Symmetric says that each alternative sees back, and transitive says that an alternative of an alternative is an alternative.
Euclidean says that any two alternatives of one world are alternatives of each other.

### Three relations to know

In a card game, the relation "player 1 holds the same card" between deals is an [[equivalence relation|0G8VEZ3WTK]], the frame of knowledge in $\mathsf{S5}$; see [[the card game|81J8VDK9RX]].
The strict order $<$ on $\mathbb{N}$ is serial and transitive but not reflexive, and it is the frame of "at every later time"; see [[the order on the natural numbers|2SVYW67C85]].
The relation $\{ (a, b), (b, b) \}$ is Euclidean, transitive and serial, but neither reflexive nor symmetric, and it is a frame of belief; see [[the Euclidean example|NS4AC3W4FM]].
At the two extremes, the universal relation $W \times W$ has all five properties, and the empty relation is transitive, symmetric and Euclidean but not serial.

### How the properties combine

Every reflexive relation is serial, and $<$ on $\mathbb{N}$ shows that the converse fails.
A reflexive Euclidean relation is an equivalence relation.
For symmetry, $w R v$ and $w R w$ give $v R w$ by the Euclidean property.
For transitivity, $w R v$ and $v R u$ give $v R w$ by symmetry, and then $v R w$ and $v R u$ give $w R u$.
A symmetric transitive relation is Euclidean: from $w R v$ and $w R u$, symmetry gives $v R w$, and transitivity gives $v R u$.
These facts are why $\mathsf{KT5}$ and $\mathsf{KTB4}$ are two names for the same logic $\mathsf{S5}$.

### What is not an accessibility relation

A neighborhood function that gives a world the family $\{ \{ a \}, \{ b \} \}$ does not come from any relation, because the family is not closed under intersection; see [[the neighborhood example|G2X3PKG55F]].
A relation between the worlds of two different models, such as a [[bisimulation|X27BR4YP2Y]], is a relation between models, not the accessibility relation of one frame.
The ternary relation of relevance logic is not an accessibility relation in the sense of normal modal logic either.

### Watch out

The Euclidean property is not transitivity.
Transitivity is about a path $w R v R u$, and the Euclidean property is about two successors $v$ and $u$ of the same $w$.
The relation $\{ (a, b), (b, b) \}$ shows two more traps at once: it is serial but not reflexive, and Euclidean but not symmetric.
The third trap is to read $\lozenge\varphi$ at $w$ as "$\varphi$ at some world" instead of "$\varphi$ at some successor of $w$".

### History

Kripke's paper of 1959 treated $\mathsf{S5}$, where every world sees every world.
His papers of 1963 made the relation part of the semantics, so that different properties give different logics.
Kanger and Hintikka had related relational ideas in the 1950s, and Hintikka used a relation of this kind for knowledge and belief.

### Try it

First, is the relation $\{ (1, 2), (2, 1) \}$ on $\{ 1, 2 \}$ transitive?
No: $1 R 2$ and $2 R 1$ would need $1 R 1$, which is missing.

Second, is it Euclidean?
No: $1 R 2$ and $1 R 2$ would need $2 R 2$, which is missing.

## Explanations

### L1 human

The arrows of a Kripke frame tell which worlds each world can "see".
In a game of cards I see my own card but not the card of the other player.
So every deal in which I hold the same card looks the same to me, and my arrows go to exactly these deals.
Because "looks the same" works in both directions and passes along, these arrows form groups.
For "later in time", the arrows point forward and never back.

### L2 human

We check the five properties for $R = \{ (1,1), (1,2), (2,2) \}$ on $W = \{ 1, 2 \}$.
It is reflexive, since $(1,1)$ and $(2,2)$ are in $R$, and so it is serial.
It is not symmetric, since $(1,2) \in R$ and $(2,1) \notin R$.
It is transitive, because the paths of length two are $1,1,1$, $1,1,2$, $1,2,2$ and $2,2,2$, and their end pairs are all in $R$.
It is not Euclidean, since $1 R 2$ and $1 R 1$ would need $2 R 1$.
So $R$ is a preorder, and the frame validates $\mathrm{T}$ and $\mathrm{4}$ but not $\mathrm{B}$ or $\mathrm{5}$.
Check $\mathrm{B}$ with $V(p) = \{ 1 \}$: world $2$ sees only $2$, so $\lozenge p$ fails at $2$, and $\square\lozenge p$ fails at $1$ while $p$ holds there.
Watch out: the properties of $R$ match axioms on frames, not in single models.

### L3 human

From the algebraic view, $R$ gives the operator $\square_R X = \{ w : R[w] \subseteq X \}$ on $\mathcal{P}(W)$, and $R$ can be read back from $\square_R$.
Under this duality, Kripke frames correspond to the complete atomic Boolean algebras with completely multiplicative operators.
Properties of $R$ become inequalities in the algebra: reflexivity becomes $\square_R X \subseteq X$.
The match of axioms and relational properties extends to all [[Sahlqvist formulas|S4SSDMETJM]], and its limits are the subject of [[modal correspondence theory|3RYBWYPJVD]].
