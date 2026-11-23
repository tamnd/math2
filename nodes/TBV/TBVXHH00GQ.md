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

On the two-world frame with $0 R 1$ only, make $p$ true at $0$ alone.
The world $1$ has no successor, so $1 \models \square p$, and so $0 \models \square \square p$.
But $1 \not\models p$, so $0 \not\models \square p$, and the axiom $\square \square p \to \square p$ fails at $0$.
What went wrong is that no world lies between $0$ and $1$.

Let $\mathfrak{F} = (W, R)$ be a Kripke frame and $w \in W$.
We show that $\square \square p \to \square p$ is valid at $w$ under all valuations if and only if the following holds.
$$\forall y \, \bigl(R(w, y) \to \exists z \, (R(w, z) \wedge R(z, y))\bigr)$$
So the formula locally [[corresponds|3RYBWYPJVD]] to density at $w$, and it is valid on $\mathfrak{F}$ exactly when $R$ is dense.

1. Assume density at $w$, fix a valuation $V$, and assume $w \models \square \square p$.
   Let $w R y$.
2. By density there is $z$ with $w R z$ and $z R y$.
3. From $w \models \square \square p$ and $w R z$ we get $z \models \square p$.
   From $z R y$ we get $y \models p$.
4. So every successor of $w$ satisfies $p$, and $w \models \square p$.
5. Conversely, assume density fails at $w$.
   So there is $y$ with $w R y$ and no $z$ with $w R z$ and $z R y$.
6. Put $V(p) = W \setminus \{y\}$.
7. Let $w R z$ and $z R u$.
   Then $u \neq y$, since otherwise $z$ would be a middle point between $w$ and $y$.
   So $u \models p$, and therefore $w \models \square \square p$.
8. But $w R y$ and $y \not\models p$, so $w \not\models \square p$, and the formula fails at $w$.

## Remarks

The example shows the usual pattern of correspondence proofs.
One direction uses the frame property, and the other uses a minimal valuation that makes the antecedent true.
The valuation in step 6 is the complement of one point.
Indeed, the contrapositive of the axiom is $\lozenge \neg p \to \lozenge \lozenge \neg p$, and the minimal valuation for $\neg p$ is the single point $y$.

The converse formula $\square p \to \square \square p$ corresponds to transitivity, by the same method.
On the rationals with $<$ both formulas are valid.
On the integers with $<$ only transitivity holds, since nothing lies between $0$ and $1$.

## Explanations

### L1 human

A frame is dense when between a point and any point it sees, there is a third point.
The rationals with "less than" are dense: between $1$ and $2$ lies $1.5$.
The axiom says "if it is necessary that it is necessary, then it is necessary".
It holds in every picture exactly when the picture is dense.

### L2 human

Look at the integers with $<$, and put $V(p) = \mathbb{Z} \setminus \{1\}$.
Every $z > 0$ has all its successors above $z \geq 1$, so they differ from $1$, and $z \models \square p$.
So $0 \models \square \square p$.
But $0 < 1$ and $p$ fails at $1$, so $0 \not\models \square p$.
This is step 6 of the proof, applied to the pair $0 < 1$, which has no middle point.
The typical use is to read off a frame condition from an axiom and then prove completeness for that class of frames.
Watch out: density asks for a middle point for each pair, and it does not mean reflexivity; the rationals with $<$ are dense and irreflexive.
