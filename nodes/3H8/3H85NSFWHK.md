---
tag: 3H85NSFWHK
kind: concept
name: Modal algebra
aliases: [modal-algebra, boolean-algebra-with-operators, bao]
msc: ["03G05", "03B45", "06E25"]
topics: [QYA4H5Y7VR]
audience: research
specializes: [0XADJKM699]
uses: [JCP47TNBSD, 0XADJKM699, D1TJYZZDCY, AJNZJD8442]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_algebra
    locator: lead section
  - url: https://en.wikipedia.org/wiki/General_frame
    locator: Operations and morphisms on general frames
  - url: https://plato.stanford.edu/entries/logic-algebraic-propositional/
    locator: "10. The Leibniz hierarchy"
  - book: isbn:9780521527149
    locator: Chapter 5
---

## Summary

A modal algebra is a [[Boolean algebra|0XADJKM699]] $A$ with a unary map $\Box$ such that $\Box 1 = 1$ and $\Box(x \land y) = \Box x \land \Box y$ for all $x, y \in A$; see [[the definition|JCP47TNBSD]].
More generally, a Boolean algebra with operators is a Boolean algebra with maps that preserve finite joins in each argument and send $0$ to $0$.
Modal algebras are the algebras of [[normal modal logics|D1TJYZZDCY]]: varieties of modal algebras correspond one to one, with inclusions reversed, to normal modal logics.
So each question about a normal modal logic becomes a question about a [[variety|AJNZJD8442]] of algebras.

## Motivation

The rules of a normal modal logic say that $\Box$ commutes with conjunction and that $\Box \top$ is a theorem.
These are exactly the identities $\Box(x \land y) = \Box x \land \Box y$ and $\Box 1 = 1$.
The Lindenbaum-Tarski algebra of a normal modal logic therefore carries such a map.
Kripke frames give modal algebras too: the power set of the set of worlds, with $\Box x$ the set of worlds all of whose successors lie in $x$.

## Notation

We write $(A, \Box)$, and $\Diamond x = \neg \Box \neg x$.
In the dual form one gives $\Diamond$, with $\Diamond 0 = 0$ and $\Diamond(x \lor y) = \Diamond x \lor \Diamond y$.
For a frame $(W, R)$, the *complex algebra* is $\mathfrak{F}^+ = (\mathcal{P}(W), [R])$, with $[R] x = \set{w : \forall v\, (w R v \Rightarrow v \in x)}$ and $\langle R \rangle x = \neg [R] \neg x$.
Texts on Boolean algebras with operators often write BAO, and $\mathbf{MA}$ for the variety of modal algebras.

## Remarks

### Examples

1. [[The complex algebra of a two-point frame|M15HYQH7KP]]: $W = \set{0, 1}$, $R = \set{(0, 1)}$; it refutes $\Box p \to p$.
2. [[The two modal algebras on the two-element Boolean algebra|WCWENEJ5GG]]: $\Box 0 = 0$ and $\Box 0 = 1$.
3. Every [[interior algebra|BDEX7HET71]] is a modal algebra that satisfies $\Box x \le x$ and $\Box x \le \Box \Box x$.
4. Every [[Magari algebra|PHWAN904PT]] is a modal algebra, with the extra identity of provability logic.
5. The Lindenbaum-Tarski algebra of a normal modal logic $\Lambda$, used in [[the algebraic completeness theorem|Z0S91AK9WG]].

### Non-examples

1. [[A diamond that sends $0$ to $1$|RXWW8J8RGJ]]: on the two-element algebra, $\Diamond x = 1$ for all $x$ fails $\Diamond 0 = 0$.
2. A Boolean algebra with $\Box x = \neg x$: then $\Box 1 = 0 \ne 1$ when $0 \ne 1$.
3. The map $\Diamond x = x \lor a$ with $0 < a < 1$ preserves joins, but $\Diamond 0 = a \ne 0$; its dual $\Box x = x \land \neg a$ fails $\Box 1 = 1$.

### Basic properties

1. $\Box$ is monotone, and $\Diamond$ preserves finite joins and sends $0$ to $0$.
2. A normal modal logic is complete for the variety of modal algebras that validate it, by [[this theorem|Z0S91AK9WG]].
3. Every modal algebra embeds into the complex algebra of its ultrafilter frame, by the [[Jónsson-Tarski theorem|HC5V2QFFWB]].
4. The variety of all modal algebras is the equivalent algebraic semantics of the global consequence relation of K; see [[algebraizable logic|CESWST3NWA]].

### History

Jónsson and Tarski introduced Boolean algebras with operators in two papers of 1951 and 1952, and they proved the representation theorem there.
The duality between modal algebras and descriptive general frames carries their names.
The link with modal logic became a standard tool in the 1970s, when Kripke-incomplete logics showed that frames are not enough.

### Common errors

1. Requiring $\Box x \le x$. That is the axiom T, and many modal algebras fail it.
2. Expecting every modal algebra to be the complex algebra of a frame. Only an embedding holds in general, and Kripke-incomplete logics exist.
3. Confusing $\Box$ and $\Diamond$ axioms: $\Box$ preserves meets and $1$; $\Diamond$ preserves joins and $0$.

## Explanations

### L1 human

A modal algebra is a Boolean algebra with one more operation, read as "necessarily".
"Necessarily true" is true, and "necessarily both" is the same as "both necessarily".
Sets of possible worlds are the main example.
Then "necessarily $x$" is the set of worlds from which every reachable world lies in $x$.

### L2 human

1. Take worlds $W = \set{0, 1}$, and let $0$ see $1$, and $1$ see nothing.
2. $\Box \set{1} = \set{0, 1}$: world $0$ sees only $1$, and world $1$ sees nothing, so both qualify.
3. $\Box \emptyset = \set{1}$: world $1$ qualifies with no successors, and world $0$ fails.
4. So $\Box \emptyset \not\le \emptyset$, and the axiom $\Box p \to p$ fails at world $1$.

The typical use: a formula is a theorem of $\Lambda$ iff its value is $1$ in all modal algebras of $\Lambda$; this replaces Kripke frames when they are not enough.
The trap: a world with no successors makes every $\Box$-formula true there.

### L3 human

Modal algebras are the Boolean algebras with one normal unary operator, the simplest Boolean algebras with operators.
The theory of BAOs covers [[relation algebras|GQK4DSA11K]] and [[cylindric algebras|1MDT9BF81H]] too, with binary operators and several unary operators.
Canonical extensions and [[Sahlqvist's theorem|S4SSDMETJM]] make this theory a tool for completeness proofs.
In abstract algebraic logic, the variety of modal algebras is the equivalent algebraic semantics of the global consequence of K; see [[algebraizable logic|CESWST3NWA]].
The local consequence relation of K has the same theorems, but its algebraic study needs the more general tools of the [[Leibniz hierarchy|6JT3CMJT8F]].
