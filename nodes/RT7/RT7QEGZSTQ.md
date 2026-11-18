---
tag: RT7QEGZSTQ
kind: definition
name: Neighborhood semantics
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: research
defines: CN7HK9K1B6
uses: [G8VGTW9P4F, NGHWZ9Y7ZV, 00E0YZCERH, JS8W7PA6JK]
sources:
  - book: isbn:9780521295154
    locator: "Chellas, Modal Logic: An Introduction, chapters 7 to 9"
  - url: https://en.wikipedia.org/wiki/Neighborhood_semantics
    locator: lead section and Formal definition
---

## Definition

A *neighbourhood frame* is a pair $\mathfrak{F} = (W, N)$, where $W$ is a nonempty set of worlds and $N : W \to \mathcal{P}(\mathcal{P}(W))$ is a map.
The map $N$ assigns to each world $w$ a set $N(w)$ of subsets of $W$, the *neighbourhoods* of $w$.
A *neighbourhood model* $\mathfrak{M} = (W, N, V)$ adds a valuation $V$ that sends each variable to a subset of $W$.

Truth at a world is defined by induction on the [[modal formula|G8VGTW9P4F]].

1. $\mathfrak{M}, w \models p$ if and only if $w \in V(p)$; $\bot$ is true nowhere; $\to$ has its classical clause.
2. $\mathfrak{M}, w \models \square\varphi$ if and only if $[\![ \varphi ]\!] \in N(w)$, where $[\![ \varphi ]\!] = \set{v \in W : \mathfrak{M}, v \models \varphi}$ is the *truth set* of $\varphi$.

Validity in a model, in a frame and in a class of frames is defined as for [[Kripke models|NGHWZ9Y7ZV]].
A neighbourhood frame is

1. *supplemented*, or *monotone*, when each $N(w)$ is closed under supersets: $X \in N(w)$ and $X \subseteq Y$ imply $Y \in N(w)$;
2. *closed under intersections* when $X, Y \in N(w)$ imply $X \cap Y \in N(w)$;
3. said to *contain the unit* when $W \in N(w)$ for each $w$;
4. *augmented* when each $N(w)$ is supplemented and contains $\bigcap N(w)$, its *core*.

A *classical modal logic* is a set of formulas that contains the tautologies and is closed under modus ponens, uniform substitution and the rule
$$\mathrm{RE}: \quad \text{from } \varphi \leftrightarrow \psi \text{ infer } \square\varphi \leftrightarrow \square\psi.$$
$\mathsf{E}$ is the smallest classical modal logic, and the letters $\mathsf{M}$, $\mathsf{C}$ and $\mathsf{N}$ add the axioms
$$\mathrm{M}: \square(p \wedge q) \to \square p, \qquad \mathrm{C}: (\square p \wedge \square q) \to \square(p \wedge q), \qquad \mathrm{N}: \square\top.$$
So $\mathsf{EMC}$ is $\mathsf{E}$ with $\mathrm{M}$ and $\mathrm{C}$, and so on.

## Notation

1. Chellas writes a neighbourhood frame as $\langle W, N \rangle$ and calls a neighbourhood model a *minimal model*. Other texts write $\nu$ or $\mathcal{N}$ for $N$.
2. The spellings *neighbourhood* and *neighborhood* are both used.
3. The letters (m), (c) and (n) name the three closure conditions, and they match the axioms $\mathrm{M}$, $\mathrm{C}$ and $\mathrm{N}$.
4. With $\lozenge\varphi = \neg\square\neg\varphi$, the clause for the diamond is: $w \models \lozenge\varphi$ if and only if $W \setminus [\![ \varphi ]\!] \notin N(w)$.

## Remarks

1. Each Kripke frame $(W, R)$ gives the neighbourhood frame with $N(w) = \set{X \subseteq W : R[w] \subseteq X}$. The two truth clauses for $\square$ agree, see [[a Kripke frame as a neighbourhood frame|BJ59QH0AS8]].
2. This frame is augmented, with core $R[w]$. Conversely an augmented frame comes from the relation $R[w] = \bigcap N(w)$. So augmented frames and Kripke frames are the same thing.
3. On a finite set $W$, take a frame that is supplemented, closed under intersections and contains the unit. Then the frame is augmented, since $\bigcap N(w)$ is a finite intersection.
4. With no closure conditions, axiom $\mathrm{K}$ and necessitation can fail, see [[a neighbourhood model in which axiom K fails|G2X3PKG55F]]. So the logics of neighbourhood frames need not be [[normal|JS8W7PA6JK]].

## Explanations

### L1 human

In Kripke semantics, a world sees some other worlds, and "necessarily" means "in all of them".
In neighbourhood semantics, a world instead has a list of propositions, each a set of worlds, that count as necessary there.
A statement is necessary at a world when the set of worlds where it is true is on the list.

### L2 human

We evaluate $\square p$ and $\square q$ in a small model.

1. Take $W = \set{a, b}$, $N(a) = \set{\set{a}}$, $N(b) = \set{W}$, $V(p) = \set{a}$ and $V(q) = W$.
2. $[\![ p ]\!] = \set{a} \in N(a)$, so $\square p$ is true at $a$. It is false at $b$, since $\set{a} \notin N(b)$.
3. $[\![ q ]\!] = W \notin N(a)$, so $\square q$ is false at $a$, although $q$ is true everywhere.
4. So the rule "from $q$ infer $\square q$" fails on this frame, since $N(a)$ does not contain the unit.
5. $N(a)$ is not supplemented: $\set{a} \subseteq W$, but $W \notin N(a)$. Indeed $\square(p \wedge q) \to \square q$, an instance of $\mathrm{M}$, fails at $a$, since $[\![ p \wedge q ]\!] = \set{a}$.

The typical use is to model a notion of necessity that is not closed under logical consequence.
A trap: the clause uses the truth set of $\varphi$ in the whole model, not the truth values at some other worlds.

### L3 human

Neighbourhood frames are to the classical modal logics what Kripke frames are to the normal ones.
Algebraically, the neighbourhood frames on $W$ match the unary operations on $\mathcal{P}(W)$ one to one, by $f(X) = \set{w : X \in N(w)}$.
Under this match, the augmented frames, and so the Kripke frames, are those whose operation $f$ preserves all intersections.
The conditions (m), (c) and (n) say that $f$ preserves finite intersections, and "augmented" is their infinitary form.
