---
tag: NGHWZ9Y7ZV
kind: concept
name: Kripke semantics
msc: ["03B45", "03B20"]
topics: [SKY7AQFG1V]
audience: grad
uses: [C3RZY20ETK, G8VGTW9P4F, 05AVARPXA2, 6BQ71KQ6QT]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Semantics of modal logic
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
same_as:
  wikidata: Q2462350
  wikipedia: Kripke semantics
---

## Summary

Kripke semantics reads "necessarily $p$" as "$p$ holds at every world that we can see from here".
A model is a set of worlds with arrows between them, and each world says which variables are true.
For example, take worlds $1$, $2$, $3$ with arrows $1 \to 2$, $1 \to 3$ and $2 \to 2$, and let $p$ be true only at $2$.
Then $\square p$ is false at $1$, because $1$ sees $3$, it is true at $2$, and it is true at $3$, which sees nothing.
The diamond $\lozenge p$ is true at $1$ and $2$, which both see $2$, and false at $3$.

A *Kripke frame* is a pair $\mathfrak{F} = (W, R)$ of a nonempty set $W$ of worlds and a [[binary relation|05AVARPXA2]] $R$ on $W$, the [[accessibility relation|XBCYFDPS2F]].
A *Kripke model* $\mathfrak{M} = (W, R, V)$ adds a valuation $V$ that gives each variable $p$ a set $V(p) \subseteq W$.
Truth of a [[modal formula|G8VGTW9P4F]] at a world is defined by induction, and the clause for the box is the following:
$$\mathfrak{M}, w \models \square\varphi \iff \mathfrak{M}, v \models \varphi \text{ for every } v \text{ with } w R v.$$
A formula is *valid on a frame* when it is true at every world under every valuation.
[[The definition of Kripke semantics|6BQ71KQ6QT]] gives all the clauses.

## Motivation

The box is not truth-functional, so no truth table can interpret it, as [[the truth-table example|H22GJGKD5M]] shows.
Leibniz spoke of necessity as truth in all possible worlds, and that reading interprets $\square p$ by a quantifier over worlds.
But one set of worlds with "true in all worlds" gives only one logic, $\mathsf{S5}$.
Kripke's step was to let each world see its own set of alternatives through a relation $R$.
Then conditions on $R$ give different logics: reflexive relations give $\mathsf{T}$, preorders give $\mathsf{S4}$, and equivalence relations give $\mathsf{S5}$.

So questions about axiom systems become questions about relations, which we can draw and check by hand.
The same pictures are the transition systems of computer science, where a world is a state of a program and an arrow is one step.
The completeness theorems of the [[canonical model|TVE4F04KME]] and the decision methods of [[filtration|6ZZSHAKG5F]] are all built on this semantics.

## Notation

Frames are written $\mathfrak{F} = (W, R)$ and models $\mathfrak{M} = (W, R, V)$.
Some authors write $\langle W, R, \Vdash \rangle$, with a forcing relation $\Vdash$ in place of $V$.
We write $R[w] = \{ v \in W : w R v \}$ for the successors of $w$, and $[\![\varphi]\!]^{\mathfrak{M}} = \{ w \in W : \mathfrak{M}, w \models \varphi \}$ for the truth set.
The three levels of validity are written $\mathfrak{M} \models \varphi$ (in the model), $\mathfrak{F} \models \varphi$ (on the frame) and $\mathsf{C} \models \varphi$ (on a class $\mathsf{C}$ of frames).
$\operatorname{Log}(\mathsf{C})$ is the set of formulas valid on every frame of $\mathsf{C}$.

## Remarks

### A first computation

Use the model of the Summary: $W = \{ 1, 2, 3 \}$, $R = \{ (1,2), (1,3), (2,2) \}$ and $V(p) = \{ 2 \}$.
The successor sets are $R[1] = \{ 2, 3 \}$, $R[2] = \{ 2 \}$ and $R[3] = \varnothing$.
A world is in $[\![\square p]\!]$ when its successor set lies inside $V(p)$, and in $[\![\lozenge p]\!]$ when its successor set meets $V(p)$:
$$[\![\square p]\!] = \{ 2, 3 \}, \qquad [\![\lozenge p]\!] = \{ 1, 2 \}.$$
Check: $R[1] \not\subseteq \{ 2 \}$ because of $3$, $R[2] \subseteq \{ 2 \}$, and $R[3] = \varnothing$ lies inside every set but meets none.
World $3$ is a dead end, so at $3$ every $\square\varphi$ is true and every $\lozenge\varphi$ is false.
[[The three-world model|6JXBZ2C9B4]] goes on to $\square\lozenge p$, $\lozenge\square p$ and a second variable.

### Three levels of validity

A formula can be true in one model and fail on the frame of that model.
Take $W = \{ 1, 2, 3 \}$ with $R = \{ (1, 2), (2, 3) \}$, which is not transitive.
With $V(p) = W$ the axiom $\mathrm{4}$, $\square p \to \square\square p$, is true everywhere, because $p$ is.
With $V(p) = \{ 2 \}$ it fails at $1$, since $\square p$ holds at $1$ and $\square p$ fails at $2$.
So $\mathrm{4}$ is true in the first model but not valid on the frame; see [[axiom 4 in a model that is not transitive|NA6H3978PW]].
Validity on a class of frames asks for more again, namely validity on every frame of the class.

### More frames to know

The frame $(\mathbb{N}, <)$ is the frame of "at every later time", and [[the order on the natural numbers|2SVYW67C85]] checks which axioms it validates.
The deals of a card game, with "I hold the same card in both deals" as the relation, form a frame of $\mathsf{S5}$; see [[the card game|81J8VDK9RX]].
The real line with the box read as the interior is a model of $\mathsf{S4}$ in the topological variant; see [[the interior operator of the real line|WZF6Y41AEV]].

### What is not a Kripke model

A two-valued truth table for $\square$ is not a Kripke semantics, and no such table gives the logic $\mathsf{K}$; see [[the truth-table example|H22GJGKD5M]].
A neighborhood model whose neighborhoods are not closed under intersection is not a Kripke model, and the axiom $\mathrm{K}$ fails in it; see [[the neighborhood example|G2X3PKG55F]].
A triple $(W, R, V)$ with $W = \varnothing$ is excluded too, because a frame needs at least one world.

### The rules you can use

Every frame validates every tautology and the axiom $\mathrm{K}$, and frame validity is preserved by modus ponens, necessitation and uniform substitution; see [[soundness of normal modal logics|E87G6ZTMTN]].
So $\operatorname{Log}(\mathsf{C})$ is a normal modal logic for every class $\mathsf{C}$, and the logic of all frames is $\mathsf{K}$, by [[completeness of K, T, D, K4, S4, B and S5|FXTCKYR3AQ]].
Each of the axioms $\mathrm{T}$, $\mathrm{D}$, $\mathrm{B}$, $\mathrm{4}$ and $\mathrm{5}$ is valid on a frame exactly when $R$ has a first-order property, by [[common modal axiom schemata|FDFQFWPM4X]].
Truth at $w$ depends only on the worlds that finite $R$-paths reach from $w$, so the submodel generated by $w$ gives the same truth values.

### Watch out

The first trap is to treat truth in a model as validity on the frame, as in the example of axiom $\mathrm{4}$ above.
The second trap is to forget the dead ends.
At a world with no successor, $\square\bot$ is true, so $\square p \to \lozenge p$ fails there; this is why the logic $\mathsf{D}$ asks for serial frames.
The third trap is to read $\lozenge\varphi$ as "$\varphi$ holds at some world".
In the model of the first computation, $p$ holds at world $2$, and still $\lozenge p$ is false at $3$, because $3$ does not see $2$.

### History

Kripke published a completeness theorem for quantified $\mathsf{S5}$ in 1959.
In 1963 he gave the relational semantics, with an accessibility relation, for the normal propositional logics, and in 1965 a version for intuitionistic logic.
Kanger and Hintikka had related ideas in the 1950s.

### Try it

First, in the model of the first computation, which worlds make $\lozenge\square p$ true?
World $1$ sees $2 \in [\![\square p]\!]$, world $2$ sees $2$, and world $3$ sees nothing, so the answer is $\{ 1, 2 \}$.

Second, is $\square p \to p$ valid on the frame with one world $w$ and $R = \varnothing$?
No: with $V(p) = \varnothing$, $\square p$ is true at $w$ because $w$ has no successor, and $p$ is false.

## Explanations

### L1 human

Picture some points, the possible worlds, with arrows between some of them.
At each world each basic statement is true or false.
"Necessarily $p$" holds at a world when $p$ holds at every world that its arrows reach.
"Possibly $p$" holds at a world when $p$ holds at one or more of the worlds that its arrows reach.
For example, take two worlds and one arrow from $u$ to $v$, with $p$ true only at $v$.
Then "necessarily $p$" holds at $u$, although $p$ itself is false at $u$.

### L2 human

We evaluate $\lozenge\square p$ in the model with $W = \{ 1, 2, 3 \}$, $R = \{ (1,2), (2,3), (3,3) \}$ and $V(p) = \{ 3 \}$.
We work from the inside out, so we first find the truth set of $\square p$.
World $3$ sees only $3$, and $3 \in V(p)$, so $\square p$ is true at $3$.
World $2$ sees only $3$, so $\square p$ is true at $2$.
World $1$ sees $2$, and $2 \notin V(p)$, so $\square p$ is false at $1$.
Now $\lozenge\square p$ holds at a world that sees $2$ or $3$, and every world does:
$$[\![\square p]\!] = \{ 2, 3 \}, \qquad [\![\lozenge\square p]\!] = \{ 1, 2, 3 \}.$$
So $\lozenge\square p$ is valid in the model, while $p$ is true only at $3$.
The typical use of such a computation is to show that a formula is not a theorem of a logic.
We build a frame of the logic and a world where the formula fails, and then soundness does the rest.

### L3 human

A Kripke frame $(W, R)$ gives the complex algebra $(\mathcal{P}(W), \cap, \cup, W \setminus -, \square_R)$ with $\square_R X = \{ w : R[w] \subseteq X \}$, a Boolean algebra with an operator.
Truth sets are values in this algebra.
Not every normal logic is the logic of a class of Kripke frames, and [[general frames|GGG7BB78JB]], which restrict the valuations to an algebra of sets, repair this.
[[Kripke incompleteness|W67YJQTT50]] and [[bisimulation|X27BR4YP2Y]] are topics of [[modal model theory|SPQVNPZDTB]].
Read as transition systems, the same structures are the models of temporal logics and of model checking.
A variant with preorders and persistent valuations is the semantics of [[intuitionistic logic|Q11N8X99FK]].
