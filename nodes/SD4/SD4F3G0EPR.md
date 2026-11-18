---
tag: SD4F3G0EPR
kind: example
name: The axiom .2 corresponds to confluence
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: grad
instance_of: [3RYBWYPJVD]
uses: [3RYBWYPJVD, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Sahlqvist_formula
    locator: Examples of Sahlqvist formulas
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: Common normal modal logics
---

## Example

Let $\mathfrak{F} = (W, R)$ be a Kripke frame and $w \in W$.
We show that $\lozenge \square p \to \square \lozenge p$ is valid at $w$ under all valuations if and only if
$$\forall y \, \forall z \, \bigl(R(w, y) \wedge R(w, z) \to \exists u \, (R(y, u) \wedge R(z, u))\bigr).$$
So the formula locally [[corresponds|3RYBWYPJVD]] to confluence at $w$.

1. Assume confluence at $w$, a valuation, and $w \models \lozenge \square p$. So there is $y$ with $w R y$ and $y \models \square p$.
2. Let $w R z$. By confluence there is $u$ with $y R u$ and $z R u$.
3. From $y \models \square p$ and $y R u$ we get $u \models p$. With $z R u$ this gives $z \models \lozenge p$.
4. So every successor of $w$ satisfies $\lozenge p$, and $w \models \square \lozenge p$.
5. Conversely, assume confluence fails at $w$: there are $y$, $z$ with $w R y$, $w R z$ and no common successor.
6. Put $V(p) = \set{u : y R u}$, the set of successors of $y$.
7. Then $y \models \square p$, and $w R y$ gives $w \models \lozenge \square p$.
8. Every successor $u$ of $z$ is not a successor of $y$, so $u \not\models p$. Hence $z \not\models \lozenge p$.
9. With $w R z$ this gives $w \not\models \square \lozenge p$, so the formula fails at $w$.

## Remarks

The valuation in step 6 is the smallest one that makes $\square p$ true at $y$; this is the minimal valuation of the Sahlqvist method.
The logic $\mathsf{S4.2}$ is $\mathsf{S4}$ with this axiom, and its frames are the reflexive transitive confluent frames.
Every frame with a top element that all worlds see is confluent.
A finite rooted frame that is reflexive, transitive and confluent has exactly one maximal cluster, since two maximal clusters would give two successors of the root without a common successor.

## Explanations

### L1 human

Picture paths that start at one point and split into two branches.
The frame is confluent when any two branches can meet again later.
The axiom says: if it is possible that something becomes necessary, then in every case it stays possible.
It holds in every picture exactly when branches can always meet again.

### L2 human

1. Take $W = \set{0, 1, 2}$ with $0 R 1$ and $0 R 2$ only. The branches $1$ and $2$ have no common successor.
2. Put $p$ true at no world. The world $1$ has no successor, so $1 \models \square p$, and $0 \models \lozenge \square p$.
3. The world $2$ has no successor, so $2 \not\models \lozenge p$, and $0 \not\models \square \lozenge p$.
4. The axiom fails at $0$, as the correspondence predicts.

The typical use is in the theory of $\mathsf{S4.2}$, which is the modal companion of the intermediate logic of the weak excluded middle.
A trap: the minimal valuation of step 6 can be empty, as in this L2 example, where $y$ has no successors.
