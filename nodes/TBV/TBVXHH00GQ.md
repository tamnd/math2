---
tag: TBVXHH00GQ
kind: example
name: The density axiom corresponds to density
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: grad
instance_of: [3RYBWYPJVD]
uses: [3RYBWYPJVD, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Sahlqvist_formula
    locator: Examples of Sahlqvist formulas
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Example

Let $\mathfrak{F} = (W, R)$ be a Kripke frame and $w \in W$.
We show that $\square \square p \to \square p$ is valid at $w$ under all valuations if and only if
$$\forall y \, \bigl(R(w, y) \to \exists z \, (R(w, z) \wedge R(z, y))\bigr).$$
So the formula locally [[corresponds|3RYBWYPJVD]] to density at $w$, and it is valid on $\mathfrak{F}$ exactly when $R$ is dense.

1. Assume density at $w$, a valuation $V$, and $w \models \square \square p$. Let $w R y$.
2. By density there is $z$ with $w R z$ and $z R y$.
3. From $w \models \square \square p$ and $w R z$ we get $z \models \square p$. From $z R y$ we get $y \models p$.
4. So every successor of $w$ satisfies $p$, and $w \models \square p$.
5. Conversely, assume density fails at $w$: there is $y$ with $w R y$ and no $z$ with $w R z$ and $z R y$.
6. Put $V(p) = W \setminus \set{y}$.
7. Let $w R z$ and $z R u$. Then $u \neq y$, since otherwise $z$ would be a forbidden middle point. So $u \models p$, and $w \models \square \square p$.
8. But $w R y$ and $y \not\models p$, so $w \not\models \square p$. The formula fails at $w$.

## Remarks

The example shows the usual pattern of correspondence proofs: one direction uses the frame property, and the other direction uses a minimal valuation that makes the antecedent true.
The valuation in step 6 is the complement of a single point, which is the minimal choice for the formula $\square \square p \to \square p$ written as $\lozenge p \to \lozenge \lozenge p$ with $\neg p$ in place of $p$.
The converse formula $\square p \to \square \square p$ corresponds to transitivity, by the same method.
On the rationals with $<$ both formulas are valid, and on the integers with $<$ only transitivity holds.

## Explanations

### L1 human

A frame is dense when between a point and any point it sees, there is a third point.
The rationals with "less than" are dense: between $1$ and $2$ lies $1.5$.
The axiom says "if it is necessary that it is necessary, then it is necessary".
It holds in every picture exactly when the picture is dense.

### L2 human

1. Take $W = \set{0, 1}$ and $R = \set{(0, 1)}$. This frame is not dense at $0$.
2. Put $p$ true only at $0$.
3. The only successor of $0$ is $1$, and $1$ has no successor, so $1 \models \square p$, and $0 \models \square \square p$.
4. But $1 \not\models p$, so $0 \not\models \square p$.

The typical use is to read off a frame condition from an axiom and then prove completeness for that class of frames.
A trap: density says that some middle point exists for each pair, not that $R$ is reflexive; the frame of the rationals with $<$ is dense and irreflexive.
