---
tag: V9KVDFCXW7
kind: statement
role: lemma
name: Uniqueness of the model companion
aliases: [uniqueness-of-the-model-companion]
msc: ["03C10", "03C25"]
topics: [1A9JSC5YG8]
audience: grad
uses: [WSJ2QN9YTY, ERVV6RWNNX, 92SWXST1ZM, MVCH6N9SNW]
about: [68GG7QKN7C]
sources:
  - url: https://en.wikipedia.org/wiki/Model_complete_theory
    locator: Model companion and model completion
  - book: isbn:9780521587136
---

## Statement

Let $T$ be a [[theory|92SWXST1ZM]] in a signature $L$, and let $T_1$ and $T_2$ be [[model companions|WSJ2QN9YTY]] of $T$.
Then $T_1$ and $T_2$ have the same [[models|MVCH6N9SNW]].
So the model companion of $T$, when it exists, is unique up to equivalence of theories.

## Remarks

### Why each hypothesis is needed

- [[Model completeness|ERVV6RWNNX]] of both theories. The theory of fields and the theory $\mathrm{ACF}$ are both mutually model consistent with the theory of fields, but they are not equivalent. Only $\mathrm{ACF}$ is model complete.
- Mutual model consistency with the same $T$. The theories $\mathrm{ACF}_0$ and $\mathrm{ACF}_2$ are both model complete, but they are model companions of different theories, the fields of characteristic $0$ and of characteristic $2$.

### Consequences

- One can speak of *the* model companion $T^*$ of $T$.
- Two theories with the same universal consequences have the same model companion, if one of them has one. For example, the theory of fields and the theory of integral domains both have $\mathrm{ACF}$.
- A model complete theory is the model companion of each theory with the same universal consequences, in particular of its universal part.

### Converse

The converse question is whether every theory has a model companion.
The answer is no: the theory of groups has [[no model companion|5GS2AE651W]].

### Generalizations

Mutual model consistency is the same as having the same universal consequences.
So the lemma says: among all theories with a given universal part, at most one is model complete, up to equivalence.

## Explanations

### L1 human

A theory can have at most one model companion.
If two theories both describe the "closed" members of a class, they describe the same members.
For example, there is only one theory that plays this role for fields, the theory of algebraically closed fields.

### L2 human

We see the argument of the proof in the case of fields.

1. Suppose that $T_1 = \mathrm{ACF}$ and $T_2$ is another model companion of the theory of fields.
2. A model $M$ of $\mathrm{ACF}$ is a field, so it embeds into a model $N$ of $T_2$.
3. The field $N$ embeds into an algebraically closed field $M'$. By model completeness of $\mathrm{ACF}$, $M \preceq M'$.
4. Repeating gives a chain $M \subseteq N \subseteq M' \subseteq N' \subseteq \cdots$, and its union satisfies both $T_1$ and $T_2$.
5. So $M$ is elementarily equivalent to a model of $T_2$, and $M \models T_2$.

The typical use of the lemma is to identify a model companion found in two different ways.
A trap is to think that uniqueness gives existence: many theories have no model companion.

### L3 human

The lemma says that the model companion is an invariant of the universal part $T_\forall$.
It is the analogue of the uniqueness of the algebraic closure, but at the level of theories, without any uniqueness of the models themselves.
The proof uses only model completeness and the chain argument of [[Robinson's test|QHEADWYQ64]].
