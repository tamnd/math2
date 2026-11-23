---
tag: 6BQ71KQ6QT
kind: definition
name: Kripke semantics
msc: ["03B45", "03B20"]
topics: [SKY7AQFG1V]
audience: grad
defines: NGHWZ9Y7ZV
uses: [G8VGTW9P4F, 05AVARPXA2, 00E0YZCERH, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Semantics of modal logic
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Definition

We define frames, models, truth at a world, and the three levels of validity and the two consequence relations.

A *Kripke frame* is a pair $\mathfrak{F} = (W, R)$, where $W$ is a nonempty set of worlds and $R \subseteq W \times W$ is a [[binary relation|05AVARPXA2]], the accessibility relation.
A *Kripke model* is a triple $\mathfrak{M} = (W, R, V)$, where $(W, R)$ is a frame and $V$ maps each propositional variable to an element of the [[power set|00E0YZCERH]] of $W$.
Truth of a [[modal formula|G8VGTW9P4F]] at a world $w \in W$ is defined by [[structural induction|12MQ2NJ29A]]:

1. $\mathfrak{M}, w \models p$ if and only if $w \in V(p)$;
2. $\mathfrak{M}, w \not\models \bot$;
3. $\mathfrak{M}, w \models \varphi \to \psi$ if and only if $\mathfrak{M}, w \not\models \varphi$ or $\mathfrak{M}, w \models \psi$;
4. $\mathfrak{M}, w \models \square\varphi$ if and only if $\mathfrak{M}, v \models \varphi$ for every $v \in W$ with $w R v$.

Validity and consequence are defined as follows.

1. $\varphi$ is *valid in* $\mathfrak{M}$, written $\mathfrak{M} \models \varphi$, when $\mathfrak{M}, w \models \varphi$ for every $w \in W$.
2. $\varphi$ is *valid on the frame* $\mathfrak{F}$, written $\mathfrak{F} \models \varphi$, when $(W, R, V) \models \varphi$ for every valuation $V$.
3. $\varphi$ is *valid on a class* $\mathsf{C}$ of frames when $\mathfrak{F} \models \varphi$ for every $\mathfrak{F} \in \mathsf{C}$.
4. $\varphi$ is a *local consequence* of $\Gamma$ over $\mathsf{C}$ when every world, of every model on a frame in $\mathsf{C}$, that makes all of $\Gamma$ true also makes $\varphi$ true.
5. $\varphi$ is a *global consequence* of $\Gamma$ over $\mathsf{C}$ when every model on a frame in $\mathsf{C}$ in which all of $\Gamma$ is valid also validates $\varphi$.

## Notation

We write $R[w] = \{ v : w R v \}$ and $[\![\varphi]\!]^{\mathfrak{M}} = \{ w : \mathfrak{M}, w \models \varphi \}$, and we drop $\mathfrak{M}$ when the model is fixed.
The pair $(\mathfrak{M}, w)$ is a pointed model.
Local consequence is written $\Gamma \models_{\mathsf{C}} \varphi$ and global consequence $\Gamma \models^{g}_{\mathsf{C}} \varphi$.

## Remarks

### Reading the clauses

The first three clauses are the truth table of classical logic, applied at one world at a time.
Only the box clause looks at other worlds, and it looks only at the successors of $w$.
From the abbreviations we get the derived clauses: $w \models \neg\varphi$ if and only if $w \not\models \varphi$, and $w \models \lozenge\varphi$ if and only if some $v$ with $w R v$ has $v \models \varphi$.
In terms of truth sets, the two modal clauses read as follows:
$$[\![\square\varphi]\!] = \{ w : R[w] \subseteq [\![\varphi]\!] \}, \qquad [\![\lozenge\varphi]\!] = \{ w : R[w] \cap [\![\varphi]\!] \neq \varnothing \}.$$
The truth value of $\varphi$ at $w$ depends only on the values of $V$ at the variables of $\varphi$, by induction on $\varphi$.

### Why the levels differ

Validity on a frame quantifies over all valuations, and that is why it is stronger than validity in one model.
On the frame $(\{ w \}, \varnothing)$, the formula $\square p \to p$ is true under $V(p) = \{ w \}$.
It is not valid on the frame, because under $V(p) = \varnothing$ the formula $\square p$ is true at $w$ and $p$ is false.
In contrast, the axiom $\square(p \to q) \to (\square p \to \square q)$ is valid on every frame, since at each successor $v$ the formulas $p \to q$ and $p$ give $q$.

The two consequence relations also differ.
Global consequence allows the step from $p$ to $\square p$, and local consequence does not.
So local consequence satisfies the deduction theorem and global consequence does not; see [[the global consequence example|R6MA6TFN5K]].
The concept page [[Kripke semantics|NGHWZ9Y7ZV]] has the examples and the history.

## Explanations

### L1 human

A frame is a set of points with arrows.
A model also says, at each point, which basic statements are true.
A statement with a box is true at a point when the statement inside is true at every point that the arrows reach.
For example, if a point has no arrows at all, then every box statement is true there.

### L2 human

We test the formula $\square p \to \square\square p$ on the frame with $W = \{ 1, 2, 3 \}$ and $R = \{ (1,2), (2,3) \}$.
Take $V(p) = \{ 2 \}$.
Then $\square p$ is true at $1$, since the only successor $2$ is in $V(p)$.
But $\square p$ is false at $2$, since its successor $3$ is not in $V(p)$.
So $\square\square p$ is false at $1$, and the formula fails at $1$.
The formula is therefore not valid on this frame, although it is true at every world under $V(p) = W$.
The typical use of the definitions is to keep the three levels apart: model, frame and class of frames.
Watch out: global consequence allows the step from $p$ to $\square p$, but the formula $p \to \square p$ is not valid.

### L3 human

Validity on a frame is a second-order condition on $R$, because it quantifies over all subsets $V(p)$ of $W$.
For the common axioms this second-order condition is equivalent to a first-order one; see [[common modal axiom schemata|FDFQFWPM4X]] and the [[standard translation|YW6YGBMVQY]].
Which formulas have such a first-order equivalent is the subject of [[modal correspondence theory|3RYBWYPJVD]] and of [[Sahlqvist's theorem|S4SSDMETJM]].
