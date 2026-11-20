---
tag: BDEX7HET71
kind: concept
name: Interior algebra
aliases: [interior-algebra, closure-algebra, s4-algebra, topological-boolean-algebra]
msc: ["06E25", "03G05", "03B45"]
topics: [QYA4H5Y7VR]
audience: research
specializes: [0XADJKM699]
uses: [7X1HGZ6FK0, 0XADJKM699, 0RZH6W98HK, N60RVXSA5W]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_algebra
    locator: Definition; Open and closed elements; Relationships to other areas of mathematics
  - url: https://plato.stanford.edu/entries/logic-algebraic-propositional/
    locator: "5. The algebraic counterparts of classical and intuitionistic logic"
same_as:
  wikidata: Q10894825
  wikipedia: Interior algebra
---

## Summary

An interior algebra is a [[Boolean algebra|0XADJKM699]] $B$ with a map $I \colon B \to B$ such that $I1 = 1$, $Ix \le x$, $IIx = Ix$ and $I(x \land y) = Ix \land Iy$ for all $x, y$; see [[the definition|7X1HGZ6FK0]].
The axioms copy the rules of the [[interior|0RZH6W98HK]] operation of a topological space.
Interior algebras are the algebras of the modal logic [[S4|N60RVXSA5W]], with $I$ interpreting $\Box$, and their open elements form a Heyting algebra.
So they connect classical logic, intuitionistic logic and topology in one structure.

## Motivation

The interior of a set in a topological space obeys four simple laws, and these laws do not mention points.
Taking them as axioms on a Boolean algebra gives "topology without points".
The same four laws are the laws of necessity in S4: $\Box \top$, $\Box p \to p$, $\Box p \to \Box \Box p$ and $\Box(p \land q) \leftrightarrow \Box p \land \Box q$.
The open elements, those with $Ix = x$, behave like the propositions of intuitionistic logic.

## Notation

We write $(B, I)$, or $(B, \Box)$ when the modal reading is meant.
The dual closure operator is $Cx = \neg I \neg x$, and $(B, C)$ is a *closure algebra*; the two notions carry the same information.
Other names are *S4-algebra* and *topological Boolean algebra*.
$B^\circ = \set{x : Ix = x}$ is the set of open elements, and $\set{x : Cx = x}$ the set of closed elements.

## Remarks

### Examples

1. The power set of a topological space $X$ with the topological interior; for $\mathbb{R}$ see [[this example|WZF6Y41AEV]].
2. [[The Sierpiński space|XHWTMP0JBT]]: three open sets, and the open elements form a three-element chain.
3. [[Up-sets of a finite preorder|8GP4VQYFHJ]]: $I(x)$ is the largest up-set inside $x$; this is the [[Alexandrov topology|ATP1JK3V27]].
4. Any Boolean algebra with $I = \mathrm{id}$: every element is open, and $B^\circ = B$.

### Non-examples

1. [[A reflexive relation that is not transitive|5G6MKZQ453]]: its box operator fails $IIx = Ix$.
2. On a Boolean algebra with $0 \ne 1$, the map $Ix = 0$ fails $I1 = 1$.
3. The complement map $Ix = \neg x$ fails $Ix \le x$ at $x = 0$, since $\neg 0 = 1$.

### Basic properties

1. $I$ is monotone, and $I0 = 0$.
2. [[The open elements form a Heyting algebra|KCDVRED7B2]], with $x \Rightarrow y = I(\neg x \lor y)$; the closed elements form a [[co-Heyting algebra|6G03V0BVZT]].
3. An interior algebra is the same as a modal algebra that validates the S4 axioms; see [[modal algebra|3H85NSFWHK]].
4. Each finite interior algebra is isomorphic to the power set of a finite preorder, with $I x$ the largest up-set inside $x$. This follows from the [[Jónsson-Tarski theorem|HC5V2QFFWB]], since $Ix \le x$ and $IIx = Ix$ make the relation reflexive and transitive.
5. The [[Blok-Esakia theorem|BB9TA5Q9PN]] and the [[Gödel-McKinsey-Tarski translation|BXVNEN55MR]] relate S4 and its extensions to intuitionistic logic and its extensions.

### History

McKinsey and Tarski introduced closure algebras in "The Algebra of Topology" (Annals of Mathematics, 1944).
Early work used the closure operator as the primitive, and later work, in particular that of Blok, used the interior operator.
Esakia gave a duality between interior algebras and a class of ordered topological spaces.

### Common errors

1. Thinking that the open elements form a Boolean subalgebra. They are closed under $\land$ and $\lor$, but not under $\neg$.
2. Using the Boolean implication $\neg x \lor y$ on open elements. It is not open in general; the Heyting implication is $I(\neg x \lor y)$.
3. Forgetting that $I$ preserves finite meets only. In $\mathbb{R}$, the intersection of the open sets $(-1/n, 1/n)$ is $\set{0}$, which has empty interior.

## Explanations

### L1 human

In a plane, the inside of a disc is the disc without its edge.
Taking the inside twice changes nothing, and the inside of an overlap is the overlap of the insides.
An interior algebra keeps these rules and forgets the points and distances.
The sets equal to their own inside are the open sets, and they form a smaller family with its own logic.
In that logic, "$p$ or not $p$" is not always the whole space.

### L2 human

1. Take $X = \set{a, b}$ with open sets $\emptyset$, $\set{a}$, $X$.
2. Then $I\set{b} = \emptyset$, since no nonempty open set lies inside $\set{b}$.
3. The open elements are $\emptyset$, $\set{a}$, $X$.
4. The Heyting negation of $\set{a}$ is $I(\neg\set{a}) = I\set{b} = \emptyset$.
5. So $\set{a} \lor \neg \set{a} = \set{a} \ne X$ in the open elements.

The typical use: interior algebras turn questions about S4 and intuitionistic logic into questions about topology.
The trap: the complement of an open element is closed, and in general it is not open.

### L3 human

Interior algebras form a variety, and its lattice of subvarieties is dually isomorphic to the lattice of normal extensions of S4.
Every Heyting algebra is the algebra of open elements of its free Boolean extension, with a suitable interior operator.
The [[Blok-Esakia theorem|BB9TA5Q9PN]] is built on this fact.
On the dual side, finite interior algebras are finite preorders, and general ones are descriptive frames of S4; for Heyting algebras one gets [[Esakia duality|CD9Y7YP4EJ]].
The [[McKinsey-Tarski theorem|2VF0546VXK]] says that the real line validates exactly the theorems of S4, so its interior algebra generates the variety of interior algebras.
