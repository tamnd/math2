---
tag: N3BWQRFQCC
kind: statement
role: theorem
name: Knower paradox
aliases: [kaplan-montague-paradox, paradox-of-the-knower]
msc: ["03A05", "03B42"]
topics: [6Q4JJ2MMV8]
audience: grad
about: [EA34W4ERRE]
uses: [3PRW76471J, 3K1AKGXF8A, G989VP2NGP, MFJXPAF0R0]
proofs: [ZBK9J8Y3FV]
sources:
  - url: https://plato.stanford.edu/entries/epistemic-paradoxes/
    locator: "Epistemic Paradoxes, 5.1 The Knower Paradox"
  - url: https://en.wikipedia.org/wiki/Knower_paradox
    locator: Formulation
  - url: https://en.wikipedia.org/wiki/Knower_paradox
    locator: History
history:
  first_stated: Kaplan and Montague, 1960
  notes: Wikipedia reports that Kaplan and Montague rediscovered and named the paradox in "A Paradox Regained" (1960), and that a version is in chapter 9 of Bradwardine's Insolubilia.
---

## Statement

Let $\mathcal{L}_K$ be the language of arithmetic with a unary predicate $K$, read "is known".
Fix a [[Gödel numbering|MFJXPAF0R0]], and let $S$ be a set of sentences of $\mathcal{L}_K$ closed under first-order derivability.

1. *(Knower.)* Suppose $S$ contains [[Robinson arithmetic|3K1AKGXF8A]] and two principles hold.
   - *Factivity:* $S$ contains $K(\ulcorner \varphi \urcorner) \to \varphi$ for every sentence $\varphi$ of $\mathcal{L}_K$.
   - *[[Necessitation|G989VP2NGP]]:* if $\varphi \in S$, then $K(\ulcorner \varphi \urcorner) \in S$.

   Then $S$ is inconsistent.
2. *(Belief version.)* Replace $K$ by a predicate $B$, read "is believed", and replace factivity by three principles, for all sentences $\varphi, \psi$.
   - *Closure:* $S$ contains $B(\ulcorner \varphi \to \psi \urcorner) \to (B(\ulcorner \varphi \urcorner) \to B(\ulcorner \psi \urcorner))$.
   - *Positive introspection:* $S$ contains $B(\ulcorner \varphi \urcorner) \to B(\ulcorner B(\ulcorner \varphi \urcorner) \urcorner)$.
   - *Belief in accuracy:* $S$ contains $B(\ulcorner B(\ulcorner \varphi \urcorner) \to \varphi \urcorner)$.

   If $S$ contains $\mathsf{Q}$ and is closed under necessitation for $B$, then $B(\ulcorner \psi \urcorner) \in S$ for every sentence $\psi$.

## Remarks

### Why each hypothesis is needed

1. Without necessitation, $\mathsf{Q}$ plus factivity is consistent: interpret $K$ by the empty set in the standard model.
2. Without factivity, necessitation is consistent: interpret $K$ by the set of all numbers in the standard model.
3. Necessitation must apply to theorems that use factivity. Let $E$ be the set of codes of theorems of $\mathsf{Q}$ in $\mathcal{L}_K$. Then $(\mathcal{N}, E)$ satisfies factivity, and $E$ contains every theorem of $\mathsf{Q}$.
4. The [[diagonal lemma|3PRW76471J]] is the only use of $\mathsf{Q}$. Any base theory that proves the diagonal lemma works.

### Consequences

1. Knowledge cannot be a predicate of sentences that is both factive and closed under proof in the same theory. This is the form in which the result limits [[epistemic logic|EA34W4ERRE]] with a knowledge predicate.
2. Factivity alone is a weakening of the [[naive truth schema|99XVFR5ZN5]] to one direction. So part 1 shows that one direction of the truth schema plus necessitation for $T$ is inconsistent.
3. Provability in $\mathsf{PA}$ satisfies necessitation, so by part 1 it is not factive in $\mathsf{PA}$. [[Löb's theorem|3HD30YG3DG]] gives the exact instances of factivity that $\mathsf{PA}$ proves.

### Converse

The theory with necessitation and factivity only for sentences without $K$ is consistent.
An example is $\mathsf{PA}$ with $K$ read as truth for arithmetical sentences and as false for other sentences.

### Generalizations

Part 2 shows that the paradox does not need factivity.
An agent who is closed under logic, introspective, and believes that each of its beliefs is accurate, believes every sentence.

## History

The SEP entry describes the version of Kaplan and Montague (1960) as "this sentence is known to be false", taken from the surprise test paradox.
It reports that later authors switched to the cleaner form "no one knows this very sentence".
Wikipedia reports that Kaplan and Montague gave the paradox its current name, and that a version is in chapter 9 of Bradwardine's *Insolubilia*.

## Explanations

### L1 human

Consider the sentence "Nobody knows this sentence".
If somebody knew it, it would be true, because knowledge implies truth, so nobody would know it.
So nobody knows it, and we have just proved this.
But a proof gives knowledge, so now somebody knows it.
The theorem says that "known" cannot obey both of these principles in a precise language.

### L2 human

1. The diagonal lemma gives $\kappa$ with $\kappa \leftrightarrow \neg K(\ulcorner \kappa \urcorner)$, "this sentence is not known".
2. Factivity for $\kappa$ and step 1 give $K(\ulcorner \kappa \urcorner) \to \neg K(\ulcorner \kappa \urcorner)$, so $\neg K(\ulcorner \kappa \urcorner)$.
3. By step 1, $\kappa$ is a theorem.
4. Necessitation gives $K(\ulcorner \kappa \urcorner)$, which contradicts step 2.

The typical use is to show that a knowledge predicate needs a hierarchy, a restriction, or a weaker logic, as for truth.
The trap is to think that the proof needs the full truth schema: one direction of it, plus necessitation, suffices.

### L3 human

The knower is the liar with truth replaced by a weaker, factive notion.
In modal logic, factivity and necessitation are the principles T and N, and they are consistent for a modal operator.
The paradox arises only when knowledge is a predicate of codes, so that the diagonal lemma applies.
