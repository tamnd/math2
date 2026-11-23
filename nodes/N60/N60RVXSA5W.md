---
tag: N60RVXSA5W
kind: concept
name: Modal logic S4
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [JS8W7PA6JK, FDFQFWPM4X, 0VABYWJWH9, XVYMEZKH7R]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Interior_algebra
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Summary

Read the days $0, 1, 2, \dots$ with the relation "the same day or later", and let $p$ be true from day $3$ on.
Then $\square p$, "now and at every later day", is true at day $3$ and after, and false before.
At day $3$ the formula $\square\square p$ is true too, because every later day also has $\square p$.
$\mathsf{S4}$ is the modal logic of this kind of relation: what holds from now on holds now, and it still holds from every later point on.

Exactly, $\mathsf{S4} = \mathsf{KT4}$ is the smallest [[normal modal logic|JS8W7PA6JK]] that contains the two axioms below, as in [[the definition|SADS3RT2V4]]:
$$\mathrm{T}\colon \square p \to p, \qquad \mathrm{4}\colon \square p \to \square\square p.$$
It is sound and complete for the frames whose relation is a [[preorder|0VABYWJWH9]], that is reflexive and transitive, and also for the finite preorders.

## Motivation

Several readings of the box lead to preorders.
For knowledge, $\mathrm{T}$ says that what is known is true, and $\mathrm{4}$ says that an agent who knows something knows that she knows it.
For time with "now or later", the relation $\le$ is reflexive and transitive.
For informal provability, Gödel read $\square\varphi$ as "$\varphi$ has been proved", and both axioms hold under that reading.

$\mathsf{S4}$ is also where modal logic meets topology and constructive logic.
If you read $\square$ as the [[interior|0RZH6W98HK]] of a set in a [[topological space|0CQHFPGJ45]], the theorems of $\mathsf{S4}$ are exactly the laws of interior.
Gödel's translation embeds [[intuitionistic logic|Q11N8X99FK]] into $\mathsf{S4}$, so questions about constructive proofs become questions about preorders.
Sub-area 21 returns to both links in the [[McKinsey-Tarski theorem|2VF0546VXK]] and the [[Gödel-McKinsey-Tarski translation|BXVNEN55MR]].

## Notation

The name is the fourth system of Lewis and Langford, and $\mathsf{KT4}$ lists the axioms over $\mathsf{K}$.
Its best known extensions are $\mathsf{S4.2}$, which adds $\lozenge\square p \to \square\lozenge p$, and $\mathsf{S4.3}$, which adds $\square(\square p \to q) \vee \square(\square q \to p)$.
In the topological reading one writes $[\![\square\varphi]\!] = \operatorname{int}[\![\varphi]\!]$ and $[\![\lozenge\varphi]\!] = \operatorname{cl}[\![\varphi]\!]$.

## Remarks

### Seven modalities

A modality is a string of boxes and diamonds in front of $p$.
In $\mathsf{S4}$, $\square\square p \leftrightarrow \square p$ holds by $\mathrm{4}$ and the instance $\square\square p \to \square p$ of $\mathrm{T}$, and dually $\lozenge\lozenge p \leftrightarrow \lozenge p$.
So each block of equal symbols shrinks to one symbol, and [[the reduction of □◇□◇ to □◇|G2ABW0XS0H]] shortens every alternating string of length four.
Every modality is then equivalent to one of seven:
$$p, \quad \square p, \quad \lozenge p, \quad \square\lozenge p, \quad \lozenge\square p, \quad \square\lozenge\square p, \quad \lozenge\square\lozenge p.$$
No two of them are equivalent, as small preorders show.
In $\mathsf{K4}$ the list is infinite, and in $\mathsf{S5}$ it shrinks to $p$, $\square p$ and $\lozenge p$.

### Box as interior

On the real line with $V(p) = [0, 1]$, the box gives the interior and the diamond gives the closure:
$$[\![\square p]\!] = (0, 1), \qquad [\![\lozenge p]\!] = [0, 1].$$
Axiom $\mathrm{T}$ holds because $(0, 1) \subseteq [0, 1]$, and $\mathrm{4}$ holds because the interior of an open set is the set itself.
The [[interior example on the real line|WZF6Y41AEV]] checks every axiom this way and refutes two formulas that are not theorems.
The algebras of this reading are the [[interior algebras|BDEX7HET71]].

### What S4 does not prove

$\mathsf{S4}$ does not prove $\lozenge\square p \to \square\lozenge p$, because a preorder with a root and two end points refutes it; see [[the branching preorder|HWYJG3GCQJ]].
It does not prove axiom $\mathrm{5}$, $\lozenge p \to \square\lozenge p$, so $\mathsf{S4} \ne \mathsf{S5}$; see [[axiom 5 is not a theorem of S4|A2JGSWCMT5]].
It does not prove axiom $\mathrm{B}$, $p \to \square\lozenge p$, because a preorder need not be symmetric; see [[the failure of B on a non-symmetric frame|X88XTHRFG9]].
Every equivalence relation is a preorder, so $\mathsf{S4} \subseteq \mathsf{S5}$, and the three formulas show that the inclusion is strict.

### The rules you can use

$\mathsf{S4}$ is the logic of all preorders and of all finite preorders, by [[the completeness theorem|FXTCKYR3AQ]] and [[the finite model property theorem|XNPJK6B921]].
So it is decidable, and its satisfiability problem is PSPACE-complete, by Ladner's [[complexity theorem|1P2B0C7CQ4]].
$\mathsf{S4.2}$ is the logic of directed preorders, where two successors of a world have a common successor.
$\mathsf{S4.3}$ is the logic of connected preorders, where two successors of a world are comparable.
Gödel's translation $t$ boxes atoms and implications, with $t(p) = \square p$ and $t(\varphi \to \psi) = \square(t\varphi \to t\psi)$.
A formula $\varphi$ is an intuitionistic theorem if and only if $\mathsf{S4}$ proves $t\varphi$.

### Watch out

The two mixed modalities $\square\lozenge p$ and $\lozenge\square p$ are not equivalent in $\mathsf{S4}$, and neither implies the other.
On the real line, $V(p) = \mathbb{Q}$ makes $\square\lozenge p$ true everywhere and $\lozenge\square p$ false everywhere.
On the branching preorder above, $\lozenge\square p$ is true at the root and $\square\lozenge p$ is false.
A second slip is to think that every $\mathsf{S4}$-frame is a partial order.
A preorder may have clusters of distinct worlds that see each other, such as two worlds $a$ and $b$ with $a R b$ and $b R a$.

### History

Lewis and Langford introduced $\mathsf{S4}$ in Symbolic Logic in 1932.
In 1933 Gödel gave the axioms $\mathrm{K}$, $\mathrm{T}$ and $\mathrm{4}$ with necessitation, noted that they give Lewis's $\mathsf{S4}$, and proposed the translation of intuitionistic logic.
McKinsey proved the decidability of $\mathsf{S2}$ and $\mathsf{S4}$ in 1941.
McKinsey and Tarski gave the topological reading in 1944 and proved the faithfulness of Gödel's translation in 1948.

### Try it

First, on the days $0, 1, 2, \dots$ with $\le$, let $p$ be true at the even days only, and decide where $\square\lozenge p$ is true.
At every day some later day is even, so $\lozenge p$ is true everywhere and $\square\lozenge p$ is true everywhere.

Second, in the same model, where is $\lozenge\square p$ true?
Nowhere, because $\square p$ would need $p$ at all later days, and every day has a later odd day.

## Explanations

### L1 human

In $\mathsf{S4}$, "necessary" behaves like "true now and at every later time".
If something will always hold from now on, then it holds now, which is axiom $\mathrm{T}$.
If something will always hold from now on, then at every later time it still always holds from then on, which is axiom $\mathrm{4}$.
For example, if from Monday on the shop is always open, then from Tuesday on it is always open too.

### L2 human

We test axiom $\mathrm{5}$ on the real line with $\square$ as interior and $V(p) = [0, 1]$.
First compute $\lozenge p$ as the closure of $[0, 1]$, which is $[0, 1]$ itself.
Then compute $\square\lozenge p$ as the interior of that set:
$$[\![\square\lozenge p]\!] = \operatorname{int}[0, 1] = (0, 1).$$
At the point $0$, $\lozenge p$ is true and $\square\lozenge p$ is false, so $\lozenge p \to \square\lozenge p$ fails at $0$.
Check: every small window around $0$ contains negative numbers, which lie outside $[0, 1]$, so $0$ is not an interior point.
This is the typical use of the topological reading: intervals and dense sets give quick countermodels for $\mathsf{S4}$.
Watch out: a single space can validate more than $\mathsf{S4}$, since a discrete space makes $\square p \leftrightarrow p$ valid.

### L3 human

The open elements of an interior algebra form a Heyting algebra, and this is the algebraic form of Gödel's translation.
McKinsey and Tarski showed that $\mathsf{S4}$ is the logic of the real line, and of many other spaces, in the topological reading; see [[topological semantics of modal logic|HWJXMBNHQ0]].
The upsets of a preorder form a topology in which $\square$ is the interior, so Kripke frames of $\mathsf{S4}$ are a special case of spaces.
The logics between $\mathsf{S4}$ and $\mathsf{S5}$, such as $\mathsf{S4.2}$ and $\mathsf{S4.3}$, are modal companions of intermediate logics, and the normal extensions of the logic $\mathsf{Grz}$ match the intermediate logics by the [[Blok-Esakia theorem|BB9TA5Q9PN]].
