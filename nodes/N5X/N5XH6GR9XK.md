---
tag: N5XH6GR9XK
kind: example
name: The axiom □p → p under five readings of the box
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [C3RZY20ETK]
uses: [C3RZY20ETK, NGHWZ9Y7ZV, FDFQFWPM4X, 0X8NMST0J2]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
---

## Example

We test the axiom $\mathrm{T}$, the formula $\square p \to p$, under several readings of the box of [[modal logic|C3RZY20ETK]].
A reading accepts $\mathrm{T}$ when every instance of $\square p \to p$ is a law under that reading.
For the readings that reject $\mathrm{T}$, we use the following [[Kripke model|NGHWZ9Y7ZV]] $\mathfrak{M}$:
$$W = \{ w, v \}, \quad R = \{ (w, v) \}, \quad V(p) = \{ v \}.$$

1. Alethic reading, "it is necessary that $p$".
   What is necessary is true, so the reading accepts $\mathrm{T}$.
2. Epistemic reading, "the agent knows that $p$".
   Knowledge is factive, since a known proposition is true, so the reading accepts $\mathrm{T}$.
3. Doxastic reading, "the agent believes that $p$".
   An agent can believe a false proposition, so the reading rejects $\mathrm{T}$.
4. Deontic reading, "it is obligatory that $p$".
   Obligations can be broken, so the reading rejects $\mathrm{T}$.
   Deontic logic uses the weaker axiom $\mathrm{D}$, $\square p \to \lozenge p$, which says that what is obligatory is permitted.
5. Provability reading, "Peano arithmetic $\mathsf{PA}$ proves $p$".
   Since $\mathsf{PA}$ is sound, each arithmetical instance is true in $\mathbb{N}$.
   But $\mathsf{PA}$ does not prove all these instances, and the [[provability logic|WJK0YA4GP2]] $\mathsf{GL}$ does not contain $\square p \to p$.
6. Temporal reading, "$p$ holds at every strictly later time".
   Then $p$ can hold in the whole future and fail now, so the reading rejects $\mathrm{T}$.
7. Temporal reading, "$p$ holds now and at every later time".
   The present is included, so the reading accepts $\mathrm{T}$.

Now we check the countermodel.

8. The only successor of $w$ is $v$, and $v \in V(p)$, so $\mathfrak{M}, w \models \square p$.
9. Since $w \notin V(p)$, we have $\mathfrak{M}, w \not\models p$.
10. So $\square p \to p$ fails at $w$, as the rejecting readings predict.

## Remarks

One formula can be a law under one reading of the box and fail under another.
The frame condition explains the split.
By [[common modal axiom schemata|FDFQFWPM4X]], $\mathrm{T}$ is valid on a frame exactly when the relation is [[reflexive|0X8NMST0J2]], and in the countermodel $w$ does not see itself.

What happens if we add the pair $(w, w)$ to $R$?
Then $w$ sees a world where $p$ fails, namely $w$ itself, so $\square p$ becomes false at $w$.
At $v$, which has no successors, $p$ is true, so $\square p \to p$ holds there.
So $\mathrm{T}$ is now true at both worlds.

The strict temporal reading uses the relation "earlier than", which is irreflexive, so $\mathrm{T}$ fails.
The reading "now or later" uses "earlier than or equal", which is reflexive.
For the provability reading, see [[S4 is not the provability logic of PA|AXB7DEGR2D]].

## Explanations

### L1 human

The box can mean "necessarily", "known", "believed", "obligatory", "provable" or "always in the future".
The rule "if box $p$, then $p$" says that a boxed statement is true.
This is right for knowledge: if Ann knows it is raining, then it is raining.
It is wrong for belief, because Ann can believe it is raining on a dry day.
It is also wrong for duty, because a rule can say "pay the bill" and the bill can stay unpaid.

### L2 human

Read $\square p$ as "Bob believes $p$" and $p$ as "the train is late".
Suppose that Bob believes that the train is late, so $\square p$ is true.
In fact the train is on time, so $p$ is false.
Then $\square p \to p$ is false, so a logic of belief must not contain $\mathrm{T}$.
The typical use of such a test is to choose the axioms of a logic from the intended reading, and then the class of frames from the axioms.
Watch out: under the provability reading each instance of $\square p \to p$ is true in $\mathbb{N}$, but truth in $\mathbb{N}$ is not provability in $\mathsf{PA}$.
