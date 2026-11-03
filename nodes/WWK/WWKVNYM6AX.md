---
tag: WWKVNYM6AX
kind: statement
role: lemma
name: Newman's lemma
msc: [68Q42, 03B70]
uses: [EDHK5KSGHY, Y83TQF6V6A, 0DQPNJNPYK]
about: [EDHK5KSGHY]
sources:
  - url: https://en.wikipedia.org/wiki/Newman's_lemma
same_as:
  wikidata: Q1208706
  wikipedia: Newman's lemma
---

## Statement

Let $(A, \to)$ be an abstract [[rewriting system|Y83TQF6V6A]] that is terminating.
Then $(A, \to)$ is [[confluent|EDHK5KSGHY]] if and only if it is locally confluent.

## Remarks

Confluence always implies local confluence, so the content is the converse.
Since the system is terminating, the converse of $\to^+$ (one or more steps) is a [[well-founded relation|0DQPNJNPYK]].
One proves by well-founded induction on $a$ that any two reducts $a \to^* b$ and $a \to^* c$ are joinable.
If $a \to b_1 \to^* b$ and $a \to c_1 \to^* c$, local confluence joins $b_1$ and $c_1$ at some $d$, and the induction hypothesis at $b_1$ and then at $c_1$ joins everything.
Termination is necessary: the system with $b \to a$, $b \to c$, $c \to b$, $c \to d$ is locally confluent but not confluent, because $b$ has the two normal forms $a$ and $d$.
In practice the lemma reduces confluence to checking finitely many local situations, such as the critical pairs of a term rewriting system.

## Explanations

### L1 human

Confluence asks that any two long computations from the same start can be brought together again.
Newman's lemma says that, if every computation stops, it is enough to check this for computations of a single step.
This is much easier, because one-step choices are often few and can be listed.
The condition that computations stop cannot be dropped: a system that goes around in circles can be locally confluent without being confluent.

### L2 human

Newman's lemma is the basic tool for proving that a rewriting system has unique normal forms.
For term rewriting systems, local confluence reduces further to the joinability of critical pairs, which is the basis of Knuth–Bendix completion.
For lambda calculus the lemma does not apply, since beta reduction is not terminating, and confluence is proved instead by parallel reduction.
