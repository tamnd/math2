---
tag: SADS3RT2V4
kind: definition
name: Modal logic S4
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
defines: N60RVXSA5W
uses: [JS8W7PA6JK, FDFQFWPM4X, YHGXV3SQDP, 0VABYWJWH9]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Definition

The logic $\mathsf{S4} = \mathsf{KT4}$ is the smallest [[normal modal logic|JS8W7PA6JK]] that contains the axioms
$$\mathrm{T}: \square p \to p \qquad \text{and} \qquad \mathrm{4}: \square p \to \square\square p.$$
Its two standard extensions are the smallest normal logics that contain $\mathsf{S4}$ and one more axiom:

1. $\mathsf{S4.2} = \mathsf{S4} + \lozenge\square p \to \square\lozenge p$;
2. $\mathsf{S4.3} = \mathsf{S4} + \square(\square p \to q) \vee \square(\square q \to p)$.

A frame $(W, R)$ is an $\mathsf{S4}$-frame when $R$ is a [[preorder|0VABYWJWH9]], that is, reflexive and transitive in the sense of [[the accessibility relation|YHGXV3SQDP]].
A preorder is directed when $w R v$ and $w R u$ imply some $x$ with $v R x$ and $u R x$, and connected when $w R v$ and $w R u$ imply $v R u$ or $u R v$.

## Notation

The name comes from the fourth of the systems of Lewis and Langford (1932); $\mathsf{KT4}$ shows the axioms.
The axioms of $\mathsf{S4.2}$ and $\mathsf{S4.3}$ are often named $.2$ and $.3$.

## Remarks

1. By [[common modal axiom schemata|FDFQFWPM4X]], $\mathsf{S4}$ is valid on a frame if and only if the frame is a preorder.
2. $\mathsf{S4.2}$ is the logic of directed preorders, and $\mathsf{S4.3}$ is the logic of connected preorders. Each axiom is valid on a preorder exactly when the preorder has that property.
3. $\mathsf{S4}$ is complete for preorders, see [[the completeness theorem|FXTCKYR3AQ]], and for finite preorders, see [[the finite model property theorem|XNPJK6B921]].
4. The full discussion, with the topological reading and the link to intuitionistic logic, is in [[modal logic S4|N60RVXSA5W]].

## Explanations

### L1 human

The logic $\mathsf{S4}$ has two laws of necessity: what is necessary is true, and what is necessary is necessarily necessary.
Its worlds are arranged by a relation in which every world sees itself and two steps can be made in one.
An example is the relation "at the same time or later" on days.

### L2 human

We check the axiom $.2$ on the directed preorder $W = \set{r, a, b, c}$ with all loops and $r R a$, $r R b$, $r R c$, $a R c$, $b R c$.

1. The relation is reflexive by the loops, and transitive since every path of two steps ends at a world that the start already sees.
2. It is directed: any two successors of $r$ see $c$, and $a$, $b$, $c$ see $c$.
3. Take $V(p) = \set{c}$. Then $\square p$ holds exactly at $c$, so $\lozenge\square p$ holds at every world.
4. $\lozenge p$ holds at every world, since each world sees $c$; so $\square\lozenge p$ holds at every world, and $.2$ holds here.

The typical use is to place a logic between $\mathsf{S4}$ and $\mathsf{S5}$ by a property of preorders.
A trap: $.2$ and $.3$ are valid on preorders with the property, but on frames that are not preorders their frame conditions are different.

### L3 human

Preorders are the frames of $\mathsf{S4}$, and the upward closed sets of a preorder form an Alexandrov topology; $\square$ is then its interior operator.
This is the start of the topological semantics of $\mathsf{S4}$, treated in [[modal model theory|SPQVNPZDTB]].
