---
tag: ZQ4TWM7K6E
kind: concept
name: Revision theory of truth
aliases: [revision-theory, rtt, revision-sequence]
msc: ["03A05", "03B50"]
topics: [6Q4JJ2MMV8]
audience: grad
uses: [WP27CABPA4, 0RDJK7EQYY, MFJXPAF0R0, 99XVFR5ZN5]
sources:
  - url: https://plato.stanford.edu/entries/truth-revision/
    locator: "The Revision Theory of Truth, 3.1 Revision rules"
  - url: https://plato.stanford.edu/entries/truth-revision/
    locator: "The Revision Theory of Truth, 3.2 Revision sequences"
  - url: https://plato.stanford.edu/entries/truth-revision/
    locator: "The Revision Theory of Truth, 4.5 The supervenience of semantics"
  - book: isbn:9780262071444
---

## Summary

The *revision theory of truth* treats "true" as a circularly defined predicate, whose meaning is a rule for revising hypotheses about its extension.
Over the [[standard model|WP27CABPA4]], a *hypothesis* is a set $h \subseteq \mathbb{N}$ of codes, the codes of the sentences hypothesized true.
The *revision rule* is $\rho(h) := \{\ulcorner \varphi \urcorner : \varphi \text{ is a sentence of } \mathcal{L}_T \text{ and } (\mathcal{N}, h) \models \varphi\}$.
A *revision sequence* is a sequence $(S_\zeta)$ of hypotheses, indexed by all [[ordinals|0RDJK7EQYY]], with two conditions.

1. $S_{\zeta + 1} = \rho(S_\zeta)$ for every ordinal $\zeta$.
2. At a limit $\eta$, a sentence that is stably in (stably out of) the sequence below $\eta$ is in (out of) $S_\eta$. Other sentences are free.

A sentence is *stably true* in $S$ if it is in $S_\zeta$ for all $\zeta$ from some ordinal on.
It is *categorically true* if it is stably true in every revision sequence.
Every stage is a classical model, so the theory keeps classical logic.

## Motivation

The [[naive truth schema|99XVFR5ZN5]] looks like a definition of truth: $T(\ulcorner \varphi \urcorner)$ is defined as $\varphi$.
But the definition is circular, because $\varphi$ may contain $T$.
For a circular definition, we can still compute: from a guess about the extension of $T$, the definition gives a better guess.
The revision theory studies this process.
It models the reasoning that the liar causes.
If the liar is true, then it is not true; if it is not true, then it is true.
The SEP entry states that the theory aims to model this reasoning within a two-valued context.

## Notation

1. $\mathcal{L}_T$ is the language of arithmetic with a unary predicate $T$, with a fixed [[Gödel numbering|MFJXPAF0R0]].
2. $(\mathcal{N}, h)$ is the classical expansion of $\mathcal{N}$ in which $T$ has extension $h$.
3. $\rho$ is the revision rule; the SEP entry writes $\tau_M$, with $M$ the ground model.
4. $S$ is a revision sequence, $S_\zeta$ its stage $\zeta$, and $S|_\eta$ its initial segment below $\eta$.
5. A sentence is *nearly stably true* in $S$ if there is $\theta$ such that for every $\zeta \ge \theta$ there is $n$ with $\ulcorner \varphi \urcorner \in S_{\zeta + m}$ for all $m \ge n$.
6. The theory $\mathsf{T}^*$ counts as valid the sentences stably true in every revision sequence. The theory $\mathsf{T}^{\#}$ counts the sentences nearly stably true in every revision sequence.

## Remarks

### Examples

1. The [[revision sequences for the liar|SK12Q51C0M]]: the liar changes its value at every successor stage, so it is neither stably true nor stably false.
2. The [[revision sequences for the truth-teller|RQNRNHSQQ0]]: the truth-teller keeps the value of the first hypothesis forever.
3. The sentence $T(\ulcorner 0 = 0 \urcorner)$ is categorically true. It is in every successor stage, since $0 = 0$ is true under every hypothesis. At limits it is stably in, so it stays in.
4. For the liar $\lambda$, the sentence $T(\ulcorner \lambda \urcorner) \vee \neg T(\ulcorner \lambda \urcorner)$ is categorically true. It is a tautology, so it is true in every classical model $(\mathcal{N}, S_\zeta)$.
5. The SEP entry states that $T(\ulcorner \neg A \urcorner) \leftrightarrow \neg T(\ulcorner A \urcorner)$ is valid in $\mathsf{T}^{\#}$ for every $A$. It also states that this fails in $\mathsf{T}^*$ for some language and ground model.

### Non-examples

1. A sequence that obeys the successor rule but not the limit rule is not a revision sequence; see [[this example|FAQ2XE4961]].
2. The stages of [[Kripke's construction|ES71QTSTNV]] are not hypotheses in this sense. They are three-valued pairs, and the jump is monotone, while the revision rule is not.
3. A single fixed point of $\rho$ does not exist. A fixed point $h = \rho(h)$ would give a classical model of all T-sentences, which contradicts the [[liar paradox|KBYY281V8T]].

### Basic properties

1. From every hypothesis $h$ there starts at least one revision sequence. The successor stages are fixed, and at limits we choose any value for the unstable sentences.
2. By the successor rule, $(\mathcal{N}, S_{\zeta + 1}) \models T(\ulcorner \varphi \urcorner)$ if and only if $(\mathcal{N}, S_\zeta) \models \varphi$. So each T-sentence holds "across one step".
3. If $\varphi$ and $\varphi \to \psi$ are stably true in $S$, then $\psi$ is stably true in $S$. Take the larger of the two starting ordinals; from there, both hold in each classical stage.
4. Every classical tautology is categorically true, since each stage is a classical model.
5. The rule $\rho$ is not monotone. For the liar, $\emptyset \subseteq \{\ulcorner \lambda \urcorner\}$, but $\ulcorner \lambda \urcorner \in \rho(\emptyset)$ and $\ulcorner \lambda \urcorner \notin \rho(\{\ulcorner \lambda \urcorner\})$.

### History

The SEP entry states that Herzberger and Gupta conceived the theory independently.
It names Herzberger (1982), Gupta (1982) and Belnap (1982) as the first publications, and the book of Gupta and Belnap (1993) as the locus classicus.
It credits the liberal limit rule, which lets unstable sentences take any value, to Gupta and Belnap (1993).

### Common errors

1. Thinking that the revision theory assigns the truth-teller a third value. The SEP entry stresses that "neither categorically true nor categorically false" differs from "neither true nor false".
2. Forgetting the limit rule. Without it, the values at limit stages are arbitrary, and even $T(\ulcorner 0 = 0 \urcorner)$ could fail at a limit.
3. Confusing stably true with true at some stage. The liar is true at infinitely many stages, but it is not stably true.

## Explanations

### L1 human

Suppose you do not know which sentences are true, so you make a guess.
Using the guess, you check each sentence and get a new list of true sentences.
You repeat this forever, also through infinite stages.
Ordinary sentences settle down to their correct value after a few steps.
The liar never settles: each round turns it from true to false or back.
The revision theory says that this endless change is the meaning of the paradox.

### L2 human

1. Start with $S_0 = \emptyset$. Then $T(\ulcorner 0 = 0 \urcorner)$ is false in $(\mathcal{N}, S_0)$.
2. $S_1 = \rho(S_0)$ contains $\ulcorner 0 = 0 \urcorner$, since $0 = 0$ is true. So $T(\ulcorner 0 = 0 \urcorner)$ is true in $(\mathcal{N}, S_1)$.
3. $S_2$ contains $\ulcorner T(\ulcorner 0 = 0 \urcorner) \urcorner$, by step 2.
4. Each sentence with $n$ nested $T$ over $0 = 0$ enters at stage $n + 1$ and stays.

The typical use is to classify sentences as categorical, stable in some sequences, or unstable.
The trap is to read a single stage as the truth: only the long-run behaviour counts.

### L3 human

The revision theory is a general theory of circular definitions, of which truth is one case.
Its classical stages make it the semantic background of the axiomatic theory [[FS|G062SH2PS0]].
[[McGee's theorem|GQW8RQVZJ4]] shows that this theory is $\omega$-inconsistent, which matches the fact that no single stage is a fixed point.
