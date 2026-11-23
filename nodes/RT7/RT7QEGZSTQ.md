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

In neighborhood semantics each world carries a list of the propositions that are necessary there.
A *neighborhood frame* is a pair $\mathfrak{F} = (W, N)$, where $W$ is a nonempty set of worlds and $N : W \to \mathcal{P}(\mathcal{P}(W))$ is a map.
The map $N$ assigns to each world $w$ a set $N(w)$ of subsets of $W$, the *neighborhoods* of $w$.
A *neighborhood model* $\mathfrak{M} = (W, N, V)$ adds a valuation $V$ that sends each variable to a subset of $W$.

Truth at a world is defined by induction on the [[modal formula|G8VGTW9P4F]].
The clauses for variables and connectives are classical: $\mathfrak{M}, w \models p$ exactly when $w \in V(p)$, and $\bot$ is true nowhere.
The truth set of $\varphi$ is $[\![ \varphi ]\!] = \{ v \in W : \mathfrak{M}, v \models \varphi \}$.
The clause for the box uses the truth set, and $\mathfrak{M}, w \models \square\varphi$ exactly when $[\![ \varphi ]\!] \in N(w)$.
Validity in a model, in a frame and in a class of frames is defined as for [[Kripke models|NGHWZ9Y7ZV]].

A neighborhood frame has one of the following properties when it holds for each world $w$:

1. *supplemented*, or *monotone*, when $X \in N(w)$ and $X \subseteq Y$ imply $Y \in N(w)$;
2. *closed under intersections* when $X, Y \in N(w)$ imply $X \cap Y \in N(w)$;
3. *contains the unit* when $W \in N(w)$;
4. *augmented* when $N(w)$ is supplemented and contains its *core* $\bigcap N(w)$.

### Classical modal logics

A *classical modal logic* is a set of formulas that contains the tautologies and is closed under modus ponens, uniform substitution and this rule:
$$\mathrm{RE}\colon \quad \text{from } \varphi \leftrightarrow \psi \text{ infer } \square\varphi \leftrightarrow \square\psi.$$
$\mathsf{E}$ is the smallest classical modal logic, and the letters $\mathsf{M}$, $\mathsf{C}$ and $\mathsf{N}$ add these axioms:
$$\mathrm{M}\colon \square(p \wedge q) \to \square p, \qquad \mathrm{C}\colon (\square p \wedge \square q) \to \square(p \wedge q), \qquad \mathrm{N}\colon \square\top.$$
So $\mathsf{EMC}$ is $\mathsf{E}$ with $\mathrm{M}$ and $\mathrm{C}$, and so on.

## Notation

Chellas writes a neighborhood frame as $\langle W, N \rangle$ and calls a neighborhood model a *minimal model*.
Other texts write $\nu$ or $\mathcal{N}$ for $N$.
The letters (m), (c) and (n) name the three closure conditions, and they match the axioms $\mathrm{M}$, $\mathrm{C}$ and $\mathrm{N}$.
With $\lozenge\varphi = \neg\square\neg\varphi$, the diamond is true at $w$ exactly when $W \setminus [\![ \varphi ]\!] \notin N(w)$.

## Remarks

Each Kripke frame $(W, R)$ gives the neighborhood frame with $N(w) = \{ X \subseteq W : R[w] \subseteq X \}$.
The two truth clauses for $\square$ agree, by [[a Kripke frame as a neighborhood frame|BJ59QH0AS8]].
This frame is augmented, with core $R[w]$.
Conversely, an augmented frame comes from the relation with $R[w] = \bigcap N(w)$.
So augmented frames and Kripke frames are the same thing.

On a finite set $W$, take a frame that is supplemented, closed under intersections and contains the unit.
Then the frame is augmented, since $N(w)$ is finite and nonempty, and $\bigcap N(w)$ is a finite intersection of its members.
With no closure conditions, axiom $\mathrm{K}$ and necessitation can fail, as in [[a neighborhood model in which axiom K fails|G2X3PKG55F]].
So the logics of neighborhood frames need not be [[normal|JS8W7PA6JK]].

## Explanations

### L1 human

In Kripke semantics, a world sees some other worlds, and "necessarily" means "in all of them".
In neighborhood semantics, a world instead has a list of propositions, each a set of worlds, that count as necessary there.
A statement is necessary at a world when the set of worlds where it is true is on the list.

### L2 human

We evaluate $\square p$ and $\square q$ in a small model.

1. Take $W = \{ a, b \}$, $N(a) = \{ \{ a \} \}$, $N(b) = \{ W \}$, $V(p) = \{ a \}$ and $V(q) = W$.
2. $[\![ p ]\!] = \{ a \} \in N(a)$, so $\square p$ is true at $a$.
   It is false at $b$, since $\{ a \} \notin N(b)$.
3. $[\![ q ]\!] = W \notin N(a)$, so $\square q$ is false at $a$, although $q$ is true everywhere.
4. So the rule "from $q$ infer $\square q$" fails on this frame, since $N(a)$ does not contain the unit.
5. $N(a)$ is not supplemented: $\{ a \} \subseteq W$, but $W \notin N(a)$.
   Indeed $\square(p \wedge q) \to \square q$, an instance of $\mathrm{M}$, fails at $a$, since $[\![ p \wedge q ]\!] = \{ a \}$.

You use neighborhood models for a notion of necessity that is not closed under logical consequence.
Watch out: the clause uses the truth set of $\varphi$ in the whole model, not only the truth values at some chosen worlds.

### L3 human

Neighborhood frames are to the classical modal logics what Kripke frames are to the normal ones.
Algebraically, the neighborhood frames on $W$ match the unary operations on $\mathcal{P}(W)$ one to one, by $f(X) = \{ w : X \in N(w) \}$.
Under this match, the augmented frames, and so the Kripke frames, are those whose operation $f$ preserves all intersections.
The conditions (m), (c) and (n) say that $f$ preserves finite intersections, and "augmented" is their infinitary form.
