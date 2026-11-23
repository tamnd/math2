---
tag: GGG7BB78JB
kind: concept
name: General frame
msc: ["03B45", "06E25"]
topics: [SPQVNPZDTB]
audience: research
uses: [NGHWZ9Y7ZV, 0XADJKM699, CQM84EW10G]
sources:
  - url: https://en.wikipedia.org/wiki/General_frame
    locator: Definition
  - url: https://en.wikipedia.org/wiki/General_frame
    locator: Types of frames
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: General frame semantics
---

## Summary

A general frame is a Kripke frame that comes with a fixed stock of propositions, and a valuation may only use propositions from that stock.
With fewer valuations there are fewer countermodels, so a general frame can validate formulas that its plain frame refutes.
Precisely, a *general frame* is a triple $(W, R, A)$, where $(W, R)$ is a [[Kripke frame|NGHWZ9Y7ZV]] and $A$ is a family of subsets of $W$, the *admissible sets*.
The family $A$ must be closed under finite unions, under complement in $W$, and under the operator
$$m_R(X) = \{ w \in W : w R v \text{ for some } v \in X \}.$$
A formula is *valid* on $(W, R, A)$ when it is true at every world under every valuation $V$ with $V(p) \in A$ for all variables $p$.
The *descriptive* general frames are the differentiated, tight and compact ones, and they are exactly the duals of modal algebras.
The [[definition of general and descriptive frames|6W9MEGN982]] states all of this formally.

## Motivation

Kripke frames are pleasant to work with, but they do not fit every normal modal logic.
Some logics are [[Kripke incomplete|W67YJQTT50]]: every Kripke frame that validates the logic also validates some formula that the logic cannot prove.
[[Modal algebras|3H85NSFWHK]] fit every normal logic, since each logic is the logic of its Lindenbaum-Tarski algebra, but they lose the picture of worlds and arrows.
General frames keep the picture and add just enough algebra to match every logic.

The same device runs through the rest of modal model theory.
The proof of the [[Goldblatt-Thomason theorem|GX5E3GNRCS]] moves between frames, general frames and algebras.
The canonicity half of [[Sahlqvist's theorem|S4SSDMETJM]] is a statement about descriptive frames.
Esakia duality, behind the [[Blok-Esakia theorem|BB9TA5Q9PN]], is the same idea for Heyting algebras.

## Notation

We write $\mathfrak{g} = (W, R, A)$ for a general frame, and $\mathfrak{g}^*$ for its *complex algebra* $(A, \cup, W \setminus \cdot, \emptyset, m_R)$.
For a modal algebra $\mathfrak{B}$, its *dual general frame* is written $\mathfrak{B}_*$.
Many books write $\langle R \rangle X$ or $\lozenge X$ for $m_R(X)$.
Some write $(W, R, P)$ and call the admissible sets *propositions*.

## Remarks

### A first general frame

Take two worlds $a$ and $b$ that see each other and themselves, so $R = W \times W$.
Admit only the two sets $\emptyset$ and $W$.
These are closed under union and complement, and the operator $m_R$ maps them to themselves.
$$m_R(\emptyset) = \emptyset, \qquad m_R(W) = W$$
So $(W, R, \{\emptyset, W\})$ is a general frame.
Under an admissible valuation, $p$ is true everywhere or nowhere.
So $p \to \square p$ is valid on the general frame: when $p$ is true at all worlds, so is $\square p$.
On the plain Kripke frame the same formula fails, with $p$ true at $a$ only, because $a$ sees $b$.

### Full frames and finite frames

At the other extreme, admit every subset.
The triple $(W, R, \mathcal{P}(W))$ is a general frame, and its valid formulas are those of the Kripke frame $(W, R)$, since every valuation is admissible.
The example [[full frames are general frames|ZJSX7AASB4]] checks this, so Kripke semantics is the special case with all sets admitted.
When $W$ is finite, the full frame is also descriptive, as [[a finite full frame is descriptive|1CEKMPZX9P]] shows condition by condition.
For an infinite $W$ the full frame is not compact: the cofinite sets $W \setminus \{w\}$ have the finite intersection property and an empty intersection.

### What fails to be one, and what fails to be descriptive

On $(\mathbb{N}, <)$, the family of finite sets is not a general frame, because the complement of a finite set is infinite.
Add the cofinite sets, and closure holds, since $m_<$ of a finite nonempty set with largest element $m$ is $\{0, \dots, m - 1\}$, and $m_<$ of a cofinite set is $\mathbb{N}$.
The result is refined but not compact, as [[a refined frame that is not descriptive|F5WN5GCAEQ]] shows.
The sets $\{n+1, n+2, \dots\}$ meet in finite groups but have no common point.

### The rules you can use

Under an admissible valuation the truth set of every formula is admissible, because $\neg$, $\vee$ and $\lozenge$ are computed by complement, union and $m_R$.
So validity on a general frame is closed under modus ponens, necessitation and uniform substitution, and the formulas valid on $\mathfrak{g}$ form a normal modal logic.
Every normal modal logic is the logic of one descriptive general frame, its canonical general frame.
Descriptive frames and modal algebras are dually equivalent, by the [[Jónsson-Tarski representation theorem|HC5V2QFFWB]].
A formula valid on $(W, R)$ is valid on every $(W, R, A)$, because admissible valuations are valuations; the first general frame above shows that the converse fails.

### Watch out

A general frame of a logic need not sit over a Kripke frame of that logic.
In the first example, $p \to \square p$ holds on the general frame and fails on $(W, R)$.
So when you build a countermodel for a logic on a general frame, you cannot forget the admissible sets afterwards.
A second slip is to check closure under union and complement only.
With $W = \{0, 1\}$, $0 R 1$ and admissible sets $\emptyset$ and $W$, the operator gives $m_R(W) = \{0\}$, which is missing, so truth sets of modal formulas leave the family.

### History

Bjarni Jónsson and Alfred Tarski introduced Boolean algebras with operators, and their representation by relational structures, in 1951.
General frames grew in the 1970s, in work of Thomason, Goldblatt and Esakia, as the frame side of the algebraic semantics of modal logic.

### Try it

First, on $(\mathbb{N}, <)$ with the finite and cofinite sets admissible, compute $m_<(\{2, 5\})$.
The worlds below $5$ see $5$, so the answer is $\{0, 1, 2, 3, 4\}$, a finite set as expected.

Second, is $\square p \to p$ valid on the general frame of the first example?
Yes: both worlds see themselves, so $\square p \to p$ holds under every valuation of the full frame, and hence under the admissible ones.

## Explanations

### L1 human

A Kripke frame is a picture of points and arrows, and a statement may be true on any group of points.
A general frame adds a list of allowed groups, and statements may only be true on allowed groups.
With two points that see each other and only "none" and "both" allowed, a statement is true at both points or at neither.
Then "if it is true here, it is true at every point I can see" never fails.
Fewer allowed groups mean fewer ways to break a law, so more laws hold.

### L2 human

Here is a typical check that a family is admissible.
Take $W = \{0, 1, 2\}$ with $0 R 1$ and $1 R 2$, and start from the set $\{2\}$.
The family must contain the operator values, so we compute them:
$$m_R(\{2\}) = \{1\}, \qquad m_R(\{1\}) = \{0\}, \qquad m_R(\{0\}) = \emptyset.$$
So the family contains every singleton, and with unions it contains every subset.
The smallest general frame on this finite frame that admits $\{2\}$ is the full frame.
This shows the typical use of the operator condition: it forces many sets into the family, and on a finite rooted chain it forces all of them.

### L3 human

General frames are set representations of modal algebras, and descriptive frames are the canonical ones.
Through Stone duality, a descriptive frame is a [[Stone space|6KQ6E3YHKR]] with a relation whose point images are closed and whose operator $m_R$ sends clopen sets to clopen sets.
Results such as [[Sahlqvist's theorem|S4SSDMETJM]] and the [[Goldblatt-Thomason theorem|GX5E3GNRCS]] are proved by moving between Kripke frames, general frames and algebras.
The ultrafilter extension of a Kripke frame is the dual of its full complex algebra, and it is the bridge between frames and descriptive frames.
