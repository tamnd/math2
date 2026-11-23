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

Take the frame with worlds $0, 1, 2$ and $0 R 1$, $0 R 2$ only, and make $p$ false everywhere.
The world $1$ has no successor, so $1 \models \square p$, and $0 \models \lozenge \square p$.
The world $2$ has no successor either, so $2 \not\models \lozenge p$, and $0 \not\models \square \lozenge p$.
So the axiom $\lozenge \square p \to \square \lozenge p$ fails at $0$, because the branches $1$ and $2$ never meet again.

Let $\mathfrak{F} = (W, R)$ be a Kripke frame and $w \in W$.
We show that $\lozenge \square p \to \square \lozenge p$ is valid at $w$ under all valuations if and only if the following holds.
$$\forall y \, \forall z \, \bigl(R(w, y) \wedge R(w, z) \to \exists u \, (R(y, u) \wedge R(z, u))\bigr)$$
So the formula locally [[corresponds|3RYBWYPJVD]] to confluence at $w$.

1. Assume confluence at $w$, fix a valuation, and assume $w \models \lozenge \square p$.
   So there is $y$ with $w R y$ and $y \models \square p$.
2. Let $w R z$.
   By confluence there is $u$ with $y R u$ and $z R u$.
3. From $y \models \square p$ and $y R u$ we get $u \models p$.
   With $z R u$ this gives $z \models \lozenge p$.
4. So every successor of $w$ satisfies $\lozenge p$, and $w \models \square \lozenge p$.
5. Conversely, assume confluence fails at $w$.
   So there are $y$ and $z$ with $w R y$, $w R z$ and no common successor.
6. Put $V(p) = \{u : y R u\}$, the set of successors of $y$.
7. Then $y \models \square p$, and $w R y$ gives $w \models \lozenge \square p$.
8. No successor $u$ of $z$ is a successor of $y$, so $u \not\models p$.
   Hence $z \not\models \lozenge p$.
9. With $w R z$ this gives $w \not\models \square \lozenge p$, so the formula fails at $w$.

## Remarks

The valuation in step 6 is the smallest one that makes $\square p$ true at $y$.
This is the minimal valuation of the Sahlqvist method, and in the opening frame it is empty, because $1$ has no successor.

The logic $\mathsf{S4.2}$ is $\mathsf{S4}$ with this axiom, and its frames are the reflexive transitive confluent frames.
Every frame with a top element that all worlds see is confluent.
A finite rooted frame that is reflexive, transitive and confluent has exactly one maximal cluster.
Two maximal clusters would give two successors of the root without a common successor.

## Explanations

### L1 human

Picture paths that start at one point and split into two branches.
The frame is confluent when any two branches can meet again later.
The axiom says: if it is possible that something becomes necessary, then in every case it stays possible.
It holds in every picture exactly when branches can always meet again.

### L2 human

Now add a world $3$ with $1 R 3$ and $2 R 3$ to the opening frame, so that the branches meet.
Under the minimal valuation $V(p) = \{3\}$ for $y = 1$, we get $1 \models \square p$ and $2 \models \lozenge p$.
The world $3$ has no successor, so $3 \models \square p$ but $3 \not\models \lozenge p$.
That does not matter, because $3$ is not a successor of $0$.
At $0$ the axiom holds under every valuation, as step 4 of the proof shows.
The typical use is in the theory of $\mathsf{S4.2}$, which is a modal companion of the intermediate logic of the weak excluded middle.
Watch out: the minimal valuation of step 6 can be empty, and the argument still works.
