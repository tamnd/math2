---
tag: HWJXMBNHQ0
kind: concept
name: Topological semantics of modal logic
msc: ["03B45", "54A05"]
topics: [SPQVNPZDTB]
audience: research
uses: [0CQHFPGJ45, 0RZH6W98HK, C3RZY20ETK, BDEX7HET71, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: Topological semantics
  - url: https://en.wikipedia.org/wiki/Interior_algebra
    locator: Topology
  - url: https://en.wikipedia.org/wiki/Interior_algebra
    locator: Derivative algebras
---

## Summary

On the real line, let $p$ be true on the closed interval $[0, 1]$.
Read $\square p$ as "$p$ holds at every point near here", and $\square p$ becomes true on the open interval $(0, 1)$, the interior of $[0, 1]$.
The endpoints drop out, because every interval around $0$ contains points where $p$ is false.
This is topological semantics: modal formulas denote regions of a space, and $\square$ takes the inner part of a region.

Exactly, a model is a [[topological space|0CQHFPGJ45]] $(X, \tau)$ with a valuation $V$ that gives each variable a subset of $X$.
The connectives act by Boolean operations on sets, and the box is the [[interior|0RZH6W98HK]] operator:
$$V(\square \varphi) = \mathrm{Int}\, V(\varphi), \qquad V(\lozenge \varphi) = \mathrm{Cl}\, V(\varphi).$$
A formula is valid in the space when its truth set is $X$ for every valuation.
The logic of all spaces is $\mathsf{S4}$, and by the [[McKinsey-Tarski theorem|2VF0546VXK]] it is also the logic of the real line.

## Motivation

The axioms of $\mathsf{S4}$ say three things about the box: $\square p \to p$, $\square p \to \square \square p$, and $\square (p \wedge q) \leftrightarrow \square p \wedge \square q$.
These are exactly Kuratowski's axioms for an interior operator: the interior lies inside the set, the interior of the interior is the interior, and interiors commute with finite intersections.
So $\mathsf{S4}$ can be read as the logic of "true throughout a neighborhood", a notion of stable or verifiable truth.

Kripke frames for $\mathsf{S4}$, the preorders, are special spaces, and spaces such as $\mathbb{R}$ have no Kripke counterpart.
So topology gives new models and new completeness theorems.
The same reading interprets intuitionistic logic, with open sets as propositions, through the [[Gödel-McKinsey-Tarski translation|BXVNEN55MR]].
Later work turns modal logic into a language for space, with formulas that describe regions, boundaries and connectedness.

## Notation

We write $V(\varphi)$, or $[\![ \varphi ]\!]$, for the truth set of $\varphi$, and $X, V, x \models \varphi$ for $x \in V(\varphi)$.
The symbols $\mathrm{Int}$ and $\mathrm{Cl}$ stand for interior and closure, and $d(A)$ is the derived set, the set of limit points of $A$.
The set of formulas valid in the space $X$ is $\mathrm{Log}(X)$.

## Remarks

### A first computation

Stay with $V(p) = [0, 1]$ on $\mathbb{R}$, and compute two formulas built from it:
$$V(\lozenge \square p) = \mathrm{Cl}\,(0, 1) = [0, 1], \qquad V(\square \lozenge p) = \mathrm{Int}\,[0, 1] = (0, 1).$$
So the McKinsey formula $\square \lozenge p \to \lozenge \square p$ holds everywhere under this valuation, since $(0, 1) \subseteq [0, 1]$.
Now let $p$ be true on the rationals $\mathbb{Q}$.
Every interval contains rationals and irrationals, so $V(\lozenge p) = \mathbb{R}$ and $V(\square p) = \emptyset$.
Then $\square \lozenge p$ is true everywhere and $\lozenge \square p$ is false everywhere, and the McKinsey formula fails at every point.
[[A topological model on the real line|A504D0J1NR]] works more valuations of this kind.

### Why every space validates S4

Each axiom is a property of the interior operator.
The axiom $\square p \to p$ is $\mathrm{Int}\, A \subseteq A$, and $\square p \to \square \square p$ holds because $\mathrm{Int}\, A$ is open, so $\mathrm{Int}\, \mathrm{Int}\, A = \mathrm{Int}\, A$.
The axiom $\mathrm{K}$ follows from $\mathrm{Int}(A \cap B) = \mathrm{Int}\, A \cap \mathrm{Int}\, B$, which uses that finite intersections of open sets are open.
Necessitation holds because $\mathrm{Int}\, X = X$.
The algebra $(\mathcal{P}(X), \mathrm{Int})$ is an [[interior algebra|BDEX7HET71]], and every interior algebra embeds into one of this form.

### Kripke frames as spaces

A preorder becomes a space when we declare its up-sets open, the Alexandrov topology.
Then $w$ is in the interior of $A$ exactly when every point above $w$ is in $A$, which is the Kripke clause for $\square$.
So [[Alexandrov spaces give Kripke semantics|CWZ1K5AN1N]] for $\mathsf{S4}$, and every finite space arises this way.
Two extreme cases show how the logic depends on the space.
In a discrete space $\mathrm{Int}\, A = A$, so $p \to \square p$ is valid.
In an infinite indiscrete space the interior of $A$ is $X$ or $\emptyset$, so $\square$ means "everywhere", and the logic is $\mathsf{S5}$.

### What it is not

Reading $\square$ as closure is not sound for $\mathsf{S4}$.
Then $\square p \to p$ would say $\mathrm{Cl}\, A \subseteq A$, which fails for $A = (0, 1)$ in $\mathbb{R}$.
A family of sets that is not closed under finite intersections gives no interior operator either.
[[A family not closed under intersection|KRK0SW60RE]] shows such a family refuting a theorem of $\mathsf{K}$; structures of that kind belong to [[neighborhood semantics|CN7HK9K1B6]].

### Other operators and spatial logics

Maps between spaces carry logics.
If $f \colon X \to Y$ is continuous, open and onto, then every formula valid in $X$ is valid in $Y$, because preimages under $f$ commute with interior.

In derivative semantics, $\lozenge$ is read as the derived set $d$ instead of the closure.
The logic of all spaces is then $\mathsf{wK4}$, the logic $\mathsf{K}$ plus $p \wedge \square p \to \square \square p$, and the axiom $\square p \to \square \square p$ holds exactly in the $T_D$ spaces.
This semantics sees more: it tells $\mathbb{R}$ apart from $\mathbb{R}^2$.
Adding the universal modality gives spatial logics that express connectedness, and the logic of $\mathbb{R}^n$ with it validates a connectedness axiom.

### Watch out

Do not assume that every space has logic $\mathsf{S4}$.
A discrete space validates $p \to \square p$, so its logic is $\mathsf{S4}$ plus that axiom.
Do not assume either that topological semantics is Kripke semantics in disguise.
It is only for Alexandrov spaces, and $\mathbb{R}$ is not one: the intersection of all neighborhoods of $0$ is $\{0\}$, which is not open.
So a point of $\mathbb{R}$ has no smallest neighborhood that could play the role of its set of successors.

### History

Alfred Tarski gave a topological semantics for intuitionistic logic in 1938.
J. C. C. McKinsey and Tarski published "The algebra of topology" in the Annals of Mathematics in 1944.
There they proved that $\mathsf{S4}$ is the logic of every dense-in-itself separable metric space, such as $\mathbb{R}$.
Leo Esakia studied derivative semantics and the duality theory of interior algebras.

### Try it

First, with $V(p) = (0, 1) \cup (1, 2)$ on $\mathbb{R}$, where does $\square \lozenge p$ hold?
The closure is $[0, 2]$ and its interior is $(0, 2)$, so $\square \lozenge p$ holds on $(0, 2)$, including the point $1$, where $p$ is false.

Second, does $\square (p \vee q) \to \square p \vee \square q$ hold in a discrete space?
Yes, since there $\square$ changes nothing, and the formula becomes $p \vee q \to p \vee q$.

## Explanations

### L1 human

Read "necessarily $p$" as "$p$ holds at every point near here".
For a region on the number line, this picks out the inner part of the region, without its edge.
The rules of the modal logic $\mathsf{S4}$ are exactly the rules for inner parts.
The inner part of a region lies inside it, and taking the inner part twice changes nothing.

### L2 human

We test the $\mathsf{S5}$ axiom $\lozenge p \to \square \lozenge p$ on $\mathbb{R}$ with $V(p) = (0, 1)$.
The closure of $(0, 1)$ is $[0, 1]$, so $\lozenge p$ holds on $[0, 1]$.
The interior of $[0, 1]$ is $(0, 1)$, so $\square \lozenge p$ holds on $(0, 1)$.
At the point $0$ the antecedent is true and the consequent false, so the axiom fails at $0$.
This shows that $\mathbb{R}$ is no $\mathsf{S5}$ space, and it is the typical use of the semantics: to refute a formula, draw a region with a boundary and look at a boundary point.
Watch out: truth at a point depends on all its neighborhoods, so you cannot check a box formula by looking at finitely many other points.

### L3 human

Topological semantics is the case of the algebraic semantics in interior algebras of the form $(\mathcal{P}(X), \mathrm{Int})$.
Neighborhood semantics generalizes it further: spaces are the neighborhood frames whose neighborhood systems are filters and that validate $\square p \to p$ and $\square p \to \square \square p$.
Derivative semantics relates modal logic to the Cantor-Bendixson rank: the derivative logic of the scattered spaces is the provability logic $\mathsf{GL}$.
The [[Blok-Esakia theorem|BB9TA5Q9PN]] and the Gödel-McKinsey-Tarski translation link these modal logics of space to the intermediate logics of open sets.
