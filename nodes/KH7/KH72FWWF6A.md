---
tag: KH72FWWF6A
kind: example
name: A valuation that is not an up-set
msc: ["03B20"]
topics: [38EQ20GR7M]
audience: grad
not_instance_of:
  - target: 35VKJY77TY
    note: the valuation of p is not an up-set, so persistence fails and the axiom p -> (q -> p) is refuted
uses: [5GTQ69W47T, ETCE287E2R]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Semantics of intuitionistic logic
---

## Example

Let $W = \set{u, v}$ with $u \leq v$, and let $V(p) = \set{u}$ and $V(q) = \set{u, v}$.
We use the forcing clauses of [[Kripke semantics|5GTQ69W47T]] with this $V$.

1. $V(p)$ is not an [[up-set|ETCE287E2R]]: $u \in V(p)$ and $u \leq v$, but $v \notin V(p)$.
2. Persistence fails for $p$: $u \Vdash p$ and $v \nVdash p$.
3. $u \Vdash q \to p$ would need $v \Vdash p$, since $v \geq u$ forces $q$. So $u \nVdash q \to p$.
4. $u \Vdash p$, so $u \nVdash p \to (q \to p)$, by the clause for $\to$ at $v = u$.
5. The formula $p \to (q \to p)$ is axiom 1 of $\mathsf{IPC}$. So soundness fails for this structure.

## Remarks

The example shows why valuations must be up-sets: the axiom $\varphi \to (\psi \to \varphi)$ says that a known fact stays known.
If only one variable has a valuation that is not an up-set, the formulas that do not contain it are still evaluated soundly.
Another fix is to change the semantics: a structure with arbitrary valuations is a model of the modal logic $\mathsf{S4}$, and intuitionistic formulas must then be translated by the Gödel-McKinsey-Tarski translation.

## Explanations

### L1 human

Suppose that today we know $p$, but tomorrow we have forgotten it.
Then "if $q$, then $p$" fails today, since tomorrow $q$ holds and $p$ does not.
So "if $p$, then if $q$ then $p$" fails today, although it is a law of logic.
Kripke models forbid forgetting, and this is why they are sound.

### L2 human

1. Change the valuation to $V(p) = \set{u, v}$, which is an up-set.
2. Then $v \Vdash p$, so $u \Vdash q \to p$, and $u \Vdash p \to (q \to p)$.
3. Change it instead to $V(p) = \set{v}$. Then $u \nVdash p$, and $v \Vdash q \to p$ since $v \Vdash p$. So $u$ forces the axiom.

The typical use of this example is as a check of a definition: a semantics that allows forgetting is not a semantics of intuitionistic logic.
A trap: the failure is not in the clause for $\to$, which is the intuitionistic clause; it is in the valuation.
