---
tag: ES71QTSTNV
kind: statement
role: theorem
name: Kripke's theory of truth
aliases: [kripke-fixed-point-theorem, kripkes-fixed-points, grounded-truth]
msc: ["03A05", "03B50"]
topics: [6Q4JJ2MMV8]
audience: grad
about: [4CBCWZQZ12]
uses: [SZHA10A9X7, WP27CABPA4, MFJXPAF0R0, SFPSB6JPTC, 0RDJK7EQYY, 04RXTQA5ZA]
proofs: [M7E6ZXXBGB]
sources:
  - url: https://plato.stanford.edu/entries/self-reference/
    locator: "Self-Reference and Paradox, 3.2.1 Kripke's Theory of Truth"
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 4.1.1 Paracomplete"
  - url: https://en.wikipedia.org/wiki/Semantic_theory_of_truth
    locator: Kripke's theory of truth
history:
  first_stated: Kripke, 1975
  notes: The SEP entry on self-reference names the construction of the fixed point as one of the major contributions of Kripke (1975), "Outline of a theory of truth".
---

## Statement

Let $\mathcal{L}_T$ be arithmetic with a predicate $T$ and a [[Gödel numbering|MFJXPAF0R0]], and let $\mathrm{Sent}$ be the set of its sentence codes.
A *partial interpretation* of $T$ is a pair $(E, A)$ of disjoint sets: an extension and an anti-extension.
The value $\|\varphi\|_{(E, A)} \in \{1, 0, \mathrm{u}\}$ of a sentence in the [[standard model|WP27CABPA4]] is given by [[strong Kleene logic|SZHA10A9X7]].
The atom $T(t)$ gets $1$ if the value of $t$ is in $E$, $0$ if it is in $A$, and $\mathrm{u}$ otherwise.

The *jump* $\mathcal{J}(E, A) := (E', A')$ puts in $E'$ the codes of sentences of value $1$.
It puts in $A'$ the codes of sentences of value $0$ and all of $\mathbb{N} \setminus \mathrm{Sent}$.
Let $(E, A) \le (E_1, A_1)$ mean $E \subseteq E_1$ and $A \subseteq A_1$.
A *fixed point* satisfies $\mathcal{J}(E, A) = (E, A)$.
Pairs are *compatible* if $E \cap A_1 = A \cap E_1 = \emptyset$, and a fixed point is *intrinsic* if it is compatible with every fixed point.
The *stages* start at $(\emptyset, \emptyset)$, apply $\mathcal{J}$ at successors, and take unions at limit [[ordinals|0RDJK7EQYY]].

1. *(Monotonicity.)* If $(E, A) \le (E_1, A_1)$ and $\|\varphi\|_{(E, A)} \neq \mathrm{u}$, then $\|\varphi\|_{(E_1, A_1)} = \|\varphi\|_{(E, A)}$.
2. *(Least fixed point.)* The stages increase to a fixed point at a countable ordinal, and it is below every fixed point.
3. *(Semantic T-schema.)* In every fixed point, $\|T(\ulcorner \varphi \urcorner)\| = \|\varphi\|$ for each sentence $\varphi$.
4. *(Maximal fixed points.)* Every fixed point is below a maximal one.
5. *(Largest intrinsic fixed point.)* There is a largest intrinsic fixed point.
6. *(Examples.)* Take the [[liar|KBYY281V8T]] $\lambda$ and the [[truth-teller|XADBJH4872]] $\tau$ in the form of the [[diagonal lemma|SFPSB6JPTC]].
   Then $\lambda$ is $\mathrm{u}$ in every fixed point.
   The sentence $\tau$ is $1$ in one fixed point, $0$ in another, and $\mathrm{u}$ in the least and largest intrinsic ones.

## Remarks

### Why each hypothesis is needed

1. Monotonicity needs a monotone scheme such as strong Kleene. A connective that maps $\mathrm{u}$ to $1$ breaks part 1, and the iteration need not reach a fixed point.
2. The third value is necessary. A fixed point with no value $\mathrm{u}$ would satisfy the classical T-schema, which [[Tarski's undefinability theorem|YRV6SYK2BY]] forbids.
3. The base model is the standard model. Over another base model, the same construction works, with sentences evaluated in that model.

### Consequences

A sentence is *grounded* if it has value $1$ or $0$ in the least fixed point.
Let $\sigma$ be the sentence with $\sigma \leftrightarrow T(\ulcorner \sigma \urcorner) \vee \neg T(\ulcorner \sigma \urcorner)$, in the same form as $\tau$.
Then $\sigma$ is ungrounded, but it is $1$ in the largest intrinsic fixed point; part 6 of the proof checks this.

1. In the least fixed point, $T$ is a truth predicate for its own language in the sense of part 3. The SEP entry calls this one of the major contributions of Kripke (1975).
2. The liar is a [[truth-value gap|4CBCWZQZ12]] in every fixed point; this is Kripke's diagnosis of the liar.
3. The fixed points give the intended models of the axiomatic theory [[KF|VQG258JQAD]].
4. A predicate for "has value $\mathrm{u}$" is not expressible in the language. The strengthened liar for such a predicate would get no consistent value. The SEP entry calls this the revenge problem.

### Converse

Part 3 does not give the classical T-schema: in a fixed point, $T(\ulcorner \lambda \urcorner) \leftrightarrow \lambda$ has value $\mathrm{u}$.
So the fixed points satisfy the [[naive truth schema|99XVFR5ZN5]] only in the form of equal values.

### Generalizations

1. The same construction works with other monotone schemes, for example weak Kleene logic or supervaluation.
2. The least fixed point of $\mathcal{J}$ is the least fixed point of a monotone operator on a complete partial order.
   Compare the [[Knaster-Tarski theorem|RHXP3HA64M]] and the [[Kleene fixed-point theorem|DDAHG7QRY8]].
   So it is an inductive definition of truth.

## History

The SEP entry on self-reference states that Kripke (1975) proposed stages of an iterative construction in place of fixed syntactic levels.
It quotes Kripke: "The ghost of the Tarski hierarchy is still with us."
Wikipedia states that the theory is based on partial logic, and that sentences with a value at the least fixed point are called grounded.

## Explanations

### L1 human

Start with a truth predicate that applies to nothing.
At the first stage, call "true" every sentence about numbers that is true.
At the next stage, also call "true" every sentence that says that one of these is true, and so on.
Some sentences, like the liar, never get a value: they are gaps.
At the end, the predicate "true" applies to exactly the sentences that are true, in a logic that allows gaps.

### L2 human

1. At stage $0$, $T(\ulcorner 0 = 0 \urcorner)$ has value $\mathrm{u}$, since $E_0$ is empty.
2. At stage $1$, $\ulcorner 0 = 0 \urcorner \in E_1$, since $0 = 0$ has value $1$ at stage $0$.
3. At stage $2$, $\ulcorner T(\ulcorner 0 = 0 \urcorner) \urcorner \in E_2$, since $T(\ulcorner 0 = 0 \urcorner)$ has value $1$ at stage $1$.
4. The liar $\lambda$ has value $\mathrm{u}$ at stage $0$. If it is $\mathrm{u}$ at stage $\alpha$, it is not added, so it stays $\mathrm{u}$.

The typical use is as the model for type-free truth with one truth predicate.
The trap is to think that the least fixed point satisfies $T(\ulcorner \lambda \urcorner) \vee \neg T(\ulcorner \lambda \urcorner)$: this disjunction has value $\mathrm{u}$.

### L3 human

The construction is a positive inductive definition, like the definition of the least fixed point of a monotone operator.
Its stages replace the levels of the [[Tarskian hierarchy|Z6MCGB0ZFX]], and they continue into the transfinite.
The axiomatic counterpart is the theory [[KF|VQG258JQAD]], and the classical rival is the [[revision theory|ZQ4TWM7K6E]].
