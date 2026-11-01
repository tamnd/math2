---
tag: W635VBXEXG
kind: statement
role: theorem
name: Existence of transcendence bases
msc: [12F20]
uses: [0WQ1A8SHTZ, KV4PT6KW10, E45PA267S4, 04RXTQA5ZA, 09EYMKMSB9, 00MS9VMQ9Z]
about: [E45PA267S4]
sources:
  - url: https://en.wikipedia.org/wiki/Transcendental_extension
---

## Statement

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]].
Let $S \subseteq T \subseteq L$ be subsets such that $S$ is [[algebraically independent|KV4PT6KW10]] over $K$ and $L$ is [[algebraic|09EYMKMSB9]] over $K(T)$.
Then there is a [[transcendence basis|E45PA267S4]] $B$ of $L/K$ with $S \subseteq B \subseteq T$.
In particular, taking $S = \emptyset$ and $T = L$, every field extension has a transcendence basis.

## Remarks

Apply [[Zorn's lemma|04RXTQA5ZA]] to the algebraically independent sets $A$ with $S \subseteq A \subseteq T$, ordered by inclusion; a union of a chain is independent, since a polynomial relation involves only finitely many elements.
Let $B$ be a maximal one.
Each $t \in T$ is algebraic over $K(B)$, since otherwise $B \cup \set{t}$ would be a larger independent set.
So $K(T)$ is algebraic over $K(B)$, and $L$ is algebraic over $K(B)$ by transitivity of algebraic extensions.
For a finitely generated extension $L = K(t_1, \dots, t_n)$, Zorn's lemma is not needed, and one gets a transcendence basis among $t_1, \dots, t_n$.

## Explanations

### L1 human

Every field extension can be split into a free part and an algebraic part.
One can choose the free variables among any given generators, and one can start from any free variables one already has.

### L2 human

This is the analogue of the theorem that [[every vector space has a basis|00MS9VMQ9Z]], and the proof is the same Zorn's lemma argument.
Together with the exchange property, it gives that all transcendence bases have the same cardinality, which defines the [[transcendence degree|D7TR0YWR9H]].
It is used to write every extension as a [[purely transcendental extension|G5PVJMM37Z]] followed by an algebraic one.
