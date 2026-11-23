---
tag: S7CGCSAVMN
kind: example
name: A non-normal world refutes necessitation
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [8PAJMAN8DM]
uses: [8PAJMAN8DM, G989VP2NGP, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Impossible_world
    locator: Non-normal modal logics
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Example

Draw $w$ with a loop and an arrow to $n$, and give $n$ a loop.
Make $w$ normal and $n$ non-normal, so that every boxed formula is false at $n$ without looking at its successors.
Then the law $p \vee \neg p$ is necessary at $w$, but not necessarily necessary.

Let $W = \{w, n\}$, $N = \{w\}$, $R = \{(w, w), (w, n), (n, n)\}$, and let $V$ be any valuation.
This is a [[Kripke model|NGHWZ9Y7ZV]] with a non-normal world $n$, an [[impossible world|8PAJMAN8DM]] in Kripke's sense.
The relation $R$ is reflexive, so the model is one of Kripke's models for $\mathsf{S2}$.
We show that $\square(p \vee \neg p)$ is true at $w$, but $\square \square(p \vee \neg p)$ is false at $w$.

1. The connectives $\vee$ and $\neg$ are classical at every world, so $p \vee \neg p$ is true at $w$ and at $n$.
2. The world $w$ is normal, and both of its successors $w$ and $n$ make $p \vee \neg p$ true.
   So $w \models \square(p \vee \neg p)$.
3. The world $n$ is non-normal, so every formula $\square \varphi$ is false at $n$.
   In particular, $n \not\models \square(p \vee \neg p)$.
4. Since $w R n$, we get $w \not\models \square \square(p \vee \neg p)$.
5. Step 2 works at every normal world of every model, because all worlds are classical, so $\square(p \vee \neg p)$ is valid.
   This model shows that $\square \square(p \vee \neg p)$ is not valid.

## Remarks

The example shows that the rule of [[necessitation|G989VP2NGP]] fails in Kripke's semantics with non-normal worlds.
From the valid $\square(p \vee \neg p)$ it does not yield $\square \square(p \vee \neg p)$.
This matches the Lewis systems $\mathsf{S2}$ and $\mathsf{S3}$, which contain $\square A$ for every tautology $A$ but do not prove $\square \square(p \vee \neg p)$.
If $n$ is made normal, the model becomes an ordinary reflexive Kripke model, and $\square \square(p \vee \neg p)$ becomes true at $w$.

## Explanations

### L1 human

A normal world checks "necessarily" by looking at the worlds it can see.
A non-normal world says "no" to every claim of necessity, even for laws of logic.
So a law of logic is necessary at a normal world, but "necessarily necessary" fails as soon as a non-normal world is visible.

### L2 human

Now check $\square p \to p$ in the same model, with $p$ false at $w$.
At $w$, $\square p$ would need $p$ at the successor $w$, so $\square p$ is false and the implication holds.
At $n$, $\square p$ is false by definition, so the implication holds there too.
In fact $\square \varphi \to \varphi$ holds at every normal world of a reflexive model, which is why $\mathsf{S2}$ keeps the axiom T.
The typical use of this model is to separate $\mathsf{S2}$ from normal logics such as $\mathsf{T}$.
Watch out: validity is checked only at normal worlds, and at $n$ even $\square(p \vee \neg p)$ fails.
