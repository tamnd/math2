---
tag: KBYY281V8T
kind: counterexample
name: Liar paradox
aliases: [liar-sentence, epimenides-paradox, pseudomenos]
msc: ["03A05", "03F40"]
topics: [6Q4JJ2MMV8]
audience: ug2
uses: [3PRW76471J, 3K1AKGXF8A, 99XVFR5ZN5]
refutes:
  - target: 99XVFR5ZN5
    via: M6M7T09E36
sources:
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 1.1 Simple-falsity Liar"
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 1.2 Simple-untruth Liar"
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 1.3 Liar cycles"
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 4.1.3 Expressive power and 'revenge'"
  - url: https://en.wikipedia.org/wiki/Liar_paradox
    locator: History
---

## Counterexample

The claim refuted is the [[naive truth schema|99XVFR5ZN5]] over [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$.
Let $\mathcal{L}_T$ be the language of arithmetic with a new unary predicate $T$, and let $\mathsf{Q}_T$ be $\mathsf{Q}$ in the language $\mathcal{L}_T$.
We show that $\mathsf{Q}_T$ together with all instances of $T(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ is inconsistent.

1. The [[diagonal lemma|3PRW76471J]] holds for $\mathsf{Q}_T$, since its proof uses only the [[Gödel numbering|MFJXPAF0R0]] and the representability of the diagonal function. We apply it to the formula $\neg T(x)$.
2. It gives a sentence $\lambda$ of $\mathcal{L}_T$ with $\mathsf{Q}_T \vdash \lambda \leftrightarrow \neg T(\ulcorner \lambda \urcorner)$. This $\lambda$ is a *liar sentence*.
3. The instance of the naive truth schema for $\varphi := \lambda$ is $T(\ulcorner \lambda \urcorner) \leftrightarrow \lambda$.
4. Steps 2 and 3 give $T(\ulcorner \lambda \urcorner) \leftrightarrow \neg T(\ulcorner \lambda \urcorner)$, by transitivity of $\leftrightarrow$.
5. Assume $T(\ulcorner \lambda \urcorner)$. Step 4 gives $\neg T(\ulcorner \lambda \urcorner)$, a contradiction. So the theory proves $\neg T(\ulcorner \lambda \urcorner)$ by negation introduction.
6. Step 4, read from right to left, and step 5 give $T(\ulcorner \lambda \urcorner)$ by modus ponens.
7. Steps 5 and 6 give a sentence and its negation. So the theory is inconsistent, and it proves every sentence.

Step 5 uses negation introduction and not the law of excluded middle.
So the derivation is valid in intuitionistic logic as well.
The same argument, read in the standard model, is the proof of [[Tarski's undefinability theorem|YRV6SYK2BY]] (the undefinability theorem, not the truth definition); see [[its proof|M6M7T09E36]].

## Remarks

### The liar in ordinary language

The SEP entry gives two simple forms.
The *simple-falsity liar* is the sentence "this sentence is false".
If it is true, then it is false, as it says.
If it is false, then what it says holds, so it is true.
With the assumption that every sentence is true or false, the sentence is both true and false.
The tradition attributes a sentence of this type to Epimenides of Crete, who is said to have stated that all Cretans are liars.
For this reason the liar is also called the Epimenides paradox.
Wikipedia notes that the Epimenides sentence is not a strict paradox, because it is false without contradiction if one Cretan does not lie.

### The strengthened liar

The *simple-untruth liar* is the sentence "this sentence is not true".
It is the form of the formal derivation above.
A theory with [[truth-value gaps|4CBCWZQZ12]] can say that "this sentence is false" is neither true nor false.
That answer does not stop the untruth form.
A sentence that is neither true nor false is not true, and "not true" is exactly what the sentence says of itself.
So the untruth form is called the strengthened liar.

### Revenge

Each proposed solution classifies the liar in some way, for example as "gappy" or "not determinately true".
A new sentence can then say of itself that it has that status.
This new sentence is a *revenge liar* for the solution.
The SEP entry discusses the case of a paracomplete theory: it keeps $T(\ulcorner \varphi \urcorner)$ and $\varphi$ equivalent, so it cannot assert $\neg T(\ulcorner \lambda \urcorner)$.
If it did, it would assert $\lambda$, and then $T(\ulcorner \lambda \urcorner)$.
So the theory cannot state, in its own language, that the liar is not true.

### Liar cycles

Self-reference by one sentence is not necessary.
In the SEP example, Max says "what Agnes says is true", and Agnes says "what Max says is not true".
Then Max's claim is true if and only if Agnes's claim is true.
Agnes's claim is true if and only if Max's claim is not true.
So Max's claim is true if and only if it is not true.
The [[simultaneous diagonal lemma|R8TPVT9G5Z]] gives arithmetical versions of such cycles.
The [[Yablo paradox|6FJXAN1ND9]] goes further and uses an infinite sequence of sentences.

### Diagnoses

The main responses each give up one assumption of the derivation.

1. The [[Tarskian hierarchy|Z6MCGB0ZFX]] keeps classical logic and the truth schema, but forbids a language to contain its own truth predicate.
2. [[Kripke's theory of truth|ES71QTSTNV]] lets the liar be a [[truth-value gap|4CBCWZQZ12]] in [[strong Kleene logic|SZHA10A9X7]].
3. Dialetheism lets the liar be a [[truth-value glut|WH94DG6D3Q]], in a [[paraconsistent logic|C7YWCR87QJ]] such as the logic of paradox.
4. The [[revision theory of truth|ZQ4TWM7K6E]] keeps classical logic and treats truth as a circular definition, so that the liar has an unstable value.
5. [[Axiomatic theories of truth|KE8ZX8KVA3]] keep classical logic and select a consistent set of truth axioms.

## Explanations

### L1 human

Read the sentence "This sentence is not true" and ask whether it is true.
If it is true, then what it says holds, so it is not true.
If it is not true, then that is exactly what it says, so it is true.
Each answer leads to the other answer.
The problem is not about lying people: it is about the word "true".
Logicians use the liar to show that a language cannot talk about the truth of all of its own sentences in the simple way.

### L2 human

1. In arithmetic with a predicate $T$, the diagonal lemma gives a sentence $\lambda$ with $\lambda \leftrightarrow \neg T(\ulcorner \lambda \urcorner)$.
2. The instance of the truth schema for $\lambda$ is $T(\ulcorner \lambda \urcorner) \leftrightarrow \lambda$.
3. Together they give $T(\ulcorner \lambda \urcorner) \leftrightarrow \neg T(\ulcorner \lambda \urcorner)$.
4. A sentence of the form $p \leftrightarrow \neg p$ gives $\neg p$ (assume $p$ and get a contradiction), and then $p$.

The typical use is in proofs that a predicate cannot do some job.
If a formula $\mathrm{Tr}(x)$ were a truth definition for arithmetic, step 2 would hold for it, and the theory would be inconsistent.
The trap is to think that the liar needs a sentence that "points at itself" in a special way.
The diagonal lemma builds $\lambda$ with ordinary arithmetic, and liar cycles need no single self-referring sentence.

### L3 human

The liar is the semantic counterpart of [[Cantor's diagonal argument|0XCH8QVDCQ]] and of [[Russell's paradox|0HESMMSYEG]].
In each case a map from objects to properties of objects cannot be onto, because the diagonal property differs from every value.
[[Lawvere's fixed-point theorem|N84M16W19X]] gives a common categorical form of this pattern.
In logic, the same construction with provability in place of truth gives [[Gödel's first incompleteness theorem|X9WYNYE29C]] instead of a contradiction.
The theories of this topic, from [[Kripke's fixed points|ES71QTSTNV]] to [[McGee's theorem|GQW8RQVZJ4]], measure how much of the naive truth schema can survive the liar.
