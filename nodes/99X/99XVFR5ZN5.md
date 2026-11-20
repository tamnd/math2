---
tag: 99XVFR5ZN5
kind: statement
role: axiom
name: Naive truth schema
aliases: [unrestricted-t-schema, type-free-t-sentences]
msc: ["03A05", "03F25"]
topics: [6Q4JJ2MMV8]
audience: grad
about: [8FBF0EFFC9]
uses: [D8SD54M5PN, MFJXPAF0R0, DKFGQTRYZE]
sources:
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 4.1 Type-free T-sentences"
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 2.2 Principles of truth"
  - url: https://en.wikipedia.org/wiki/Semantic_theory_of_truth
    locator: Criteria for a definition of truth
---

## Statement

Let $\mathcal{L}_T$ be the [[language of arithmetic|D8SD54M5PN]] with one new unary predicate symbol $T$.
Fix a [[Gödel numbering|MFJXPAF0R0]], and write $\ulcorner \varphi \urcorner$ for the numeral of the code of $\varphi$.
The *naive truth schema* is the set of all [[sentences|DKFGQTRYZE]]
$$T(\ulcorner \varphi \urcorner) \leftrightarrow \varphi \qquad (\mathrm{T})$$
where $\varphi$ is any sentence of $\mathcal{L}_T$, including sentences that contain $T$.
Each instance is called a T-sentence or a T-biconditional.
The *naive truth theory* over a base theory $B$ is $B$ together with all instances of $(\mathrm{T})$.
The word "naive" means that no instance is excluded.

## Remarks

### Why each hypothesis is needed

1. The schema is safe when $\varphi$ ranges only over sentences without $T$. This typed schema gives the theory $\mathsf{TB}$, which is conservative over [[Peano arithmetic|HACXBCM7SS]]; see [[this example|H3EK7YJ0B4]].
2. The schema is also safe when the base theory cannot form self-referential sentences. The [[liar paradox|KBYY281V8T]] needs a liar sentence, and the [[diagonal lemma|3PRW76471J]] gives one over [[Robinson arithmetic|3K1AKGXF8A]].

### Consequences

1. Over $\mathsf{Q}$, the naive truth theory is inconsistent. This is the syntactic form of [[Tarski's undefinability theorem|YRV6SYK2BY]], and the [[liar paradox|KBYY281V8T]] gives the derivation step by step.
2. Even the instances for the sentences of a [[Yablo sequence|6FJXAN1ND9]] give an $\omega$-inconsistent theory, without any sentence that mentions its own code.

### Converse

The converse question asks which subsets of the schema are consistent with $\mathsf{PA}$.
Many are consistent, but the SEP entry reports McGee's result that there are uncountably many maximal consistent sets of T-sentences.
So no single natural subset is singled out by consistency alone.

### Generalizations

1. The naive satisfaction schema replaces truth of sentences by satisfaction of formulas; see [[the naive satisfaction schema|B20TDZV9WW]].
2. The schema can be stated for any language that can name its own sentences, for example a language with quotation names.

## Explanations

### L1 human

The schema says: the sentence "snow is white" is true exactly when snow is white.
It looks like the most basic fact about truth.
The schema asks this for every sentence, also for sentences that talk about truth.
For the sentence "this sentence is not true", the schema gives a contradiction.

### L2 human

1. Take the sentence $\varphi := (0 = 0)$. The instance is $T(\ulcorner 0 = 0 \urcorner) \leftrightarrow 0 = 0$.
2. Since $\mathsf{Q} \vdash 0 = 0$, the instance gives $T(\ulcorner 0 = 0 \urcorner)$.
3. Take a liar sentence $\lambda$ with $\mathsf{Q} \vdash \lambda \leftrightarrow \neg T(\ulcorner \lambda \urcorner)$. The instance for $\lambda$ gives $\lambda \leftrightarrow \neg \lambda$.

The schema is used as the standard of material adequacy for a truth definition.
The trap is to think that the schema is harmless because each instance looks harmless.
Each instance is consistent with $\mathsf{Q}$ by itself, but the instance for $\lambda$ together with $\mathsf{Q}$ is not.

### L3 human

The naive schema is the truth-theoretic analogue of naive comprehension in set theory, and the liar is the analogue of [[Russell's paradox|0HESMMSYEG]].
Each theory of truth in this topic keeps a part of the schema.
Typed theories keep the instances for sentences without $T$.
[[Kripke's theory|ES71QTSTNV]] keeps the intersubstitutivity of $T(\ulcorner \varphi \urcorner)$ and $\varphi$, but in a logic with gaps.
The theory [[KF|VQG258JQAD]] keeps the compositional clauses, and gives up some instances of the schema.
