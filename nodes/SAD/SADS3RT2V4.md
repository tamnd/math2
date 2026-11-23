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

The logic $\mathsf{S4}$ adds to $\mathsf{K}$ the two laws "what is necessary is true" and "what is necessary is necessarily necessary".
Exactly, $\mathsf{S4} = \mathsf{KT4}$ is the smallest [[normal modal logic|JS8W7PA6JK]] that contains these axioms:
$$\mathrm{T}\colon \square p \to p, \qquad \mathrm{4}\colon \square p \to \square\square p.$$
Its two standard extensions are the smallest normal modal logics that contain $\mathsf{S4}$ and one more axiom.

1. $\mathsf{S4.2}$ adds the axiom $.2$, which is $\lozenge\square p \to \square\lozenge p$.
2. $\mathsf{S4.3}$ adds the axiom $.3$, which is $\square(\square p \to q) \vee \square(\square q \to p)$.

A frame $(W, R)$ is an $\mathsf{S4}$-frame when $R$ is a [[preorder|0VABYWJWH9]], that is, reflexive and transitive in the sense of the [[accessibility relation|YHGXV3SQDP]].
A preorder is *directed* when $w R v$ and $w R u$ imply that $v R x$ and $u R x$ for some $x$.
It is *connected* when $w R v$ and $w R u$ imply $v R u$ or $u R v$.

## Notation

The name is the fourth of the systems $\mathsf{S1}$ to $\mathsf{S5}$ of Lewis and Langford (1932), and $\mathsf{KT4}$ lists the axioms.
The extra axioms of $\mathsf{S4.2}$ and $\mathsf{S4.3}$ are often written $.2$ and $.3$.

## Remarks

Each axiom is there for one property of the relation.
By the [[common modal axiom schemata|FDFQFWPM4X]], $\mathrm{T}$ is valid on a frame exactly when the frame is reflexive, and $\mathrm{4}$ exactly when it is transitive.
So $\mathsf{S4}$ is valid on a frame exactly when the frame is a preorder.
On preorders, $.2$ is valid exactly on the directed ones and $.3$ exactly on the connected ones.

A connected preorder is directed: if $v R u$, take $x = u$, since $v R u$ and $u R u$.
So $\mathsf{S4.2} \subseteq \mathsf{S4.3}$.
The converse fails on a directed preorder that is not connected.
Take the worlds $r, a, b, c$ with all loops and the arrows $r R a$, $r R b$, $r R c$, $a R c$, $b R c$.
Any two successors of a world see $c$, so it is directed, but $a$ and $b$ do not see each other, so it is not connected.

$\mathsf{S4}$ is complete for preorders by [[the completeness theorem|FXTCKYR3AQ]], and for finite preorders by [[the finite model property theorem|XNPJK6B921]].
The concept page [[modal logic S4|N60RVXSA5W]] gives the topological reading and the link to intuitionistic logic.

## Explanations

### L1 human

The logic $\mathsf{S4}$ has two laws of necessity: what is necessary is true, and what is necessary is necessarily necessary.
Its worlds are arranged by a relation in which every world sees itself, and two steps can be made in one.
An example is the relation "on the same day or later" on days.

### L2 human

We check that the four-world frame above validates $.2$ but not $.3$.
For $.2$, every world sees $c$, so for every valuation each world sees the one world $c$.
If $\lozenge\square p$ is true at a world $w$, some successor $v$ of $w$ has $\square p$, and $v$ sees $c$, so $p$ is true at $c$.
Then every successor of $w$ sees the $p$-world $c$, so $\square\lozenge p$ is true at $w$.
For $.3$, put $V(p) = \{ a, c \}$ and $V(q) = \{ b, c \}$.
At $a$, $\square p$ is true and $q$ is false, so $\square(\square p \to q)$ is false at $r$.
At $b$, $\square q$ is true and $p$ is false, so $\square(\square q \to p)$ is false at $r$.
So $.3$ fails at $r$, and you place a logic between $\mathsf{S4}$ and $\mathsf{S5}$ by a property of preorders in just this way.

### L3 human

The upward closed sets of a preorder form an Alexandrov topology, and $\square$ is then its interior operator.
This is the start of the [[topological semantics of modal logic|HWJXMBNHQ0]], where $\mathsf{S4}$ is the logic of all topological spaces.
