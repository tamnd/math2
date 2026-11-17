---
tag: EQR2AMD0GQ
kind: example
name: The consistency of PA belongs to true arithmetic
msc: ["03F30", "03F40"]
topics: [QHCRN4JVG0]
audience: grad
instance_of: [DX0KPMH4QZ]
uses: [DX0KPMH4QZ, HACXBCM7SS, MFJXPAF0R0, 4A84VHDTHV, 4PZM5GJTR5, EQH7XTZ29V, 69234Z1V00]
sources:
  - url: https://en.wikipedia.org/wiki/True_arithmetic
    locator: Definition
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Second incompleteness theorem
---

## Example

Fix a [[Gödel numbering|MFJXPAF0R0]] and let $\mathrm{Prf}_{\mathsf{PA}}(p, x)$ be a $\Delta_0$ formula expressing "$p$ codes a proof in $\mathsf{PA}$ of the formula with code $x$".
Let $\mathrm{Con}(\mathsf{PA})$ be the sentence $\forall p \, \neg \mathrm{Prf}_{\mathsf{PA}}(p, \ulcorner 0 = S0 \urcorner)$.
We show that $\mathrm{Con}(\mathsf{PA}) \in \mathrm{TA}$, the set of sentences of [[true arithmetic|DX0KPMH4QZ]].

1. $\mathrm{Con}(\mathsf{PA})$ is a $\Pi_1$ sentence: one unbounded $\forall$ in front of a $\Delta_0$ formula.
2. $\mathfrak{N}$ is a model of [[Peano arithmetic|HACXBCM7SS]]: each axiom is true of the natural numbers.
3. By [[soundness|4A84VHDTHV]], every theorem of $\mathsf{PA}$ is true in $\mathfrak{N}$. The sentence $0 = S0$ is false in $\mathfrak{N}$, so it is not a theorem.
4. So no natural number $p$ codes a proof of $0 = S0$. Since $\mathrm{Prf}_{\mathsf{PA}}$ defines the proof relation in $\mathfrak{N}$, $\mathfrak{N} \models \neg \mathrm{Prf}_{\mathsf{PA}}(\overline{p}, \ulcorner 0 = S0 \urcorner)$ for each $p$.
5. By step 4, $\mathfrak{N} \models \mathrm{Con}(\mathsf{PA})$, so $\mathrm{Con}(\mathsf{PA}) \in \mathrm{TA}$.

So $\mathrm{TA}$ contains $\mathrm{Con}(\mathsf{PA})$, although $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA})$ by the [[second incompleteness theorem|4PZM5GJTR5]].

## Remarks

The argument works in a set-theoretic metatheory, where $\mathfrak{N}$ is a set and soundness applies; it is not a proof inside $\mathsf{PA}$.
For $\Pi_1$ sentences, truth has a special form: a false $\Pi_1$ sentence has a counterexample, and then $\mathsf{Q}$ refutes it by [[$\Sigma_1$-completeness|69234Z1V00]].
So $\mathrm{Con}(\mathsf{PA})$ is not refutable in $\mathsf{PA}$, and it is independent of $\mathsf{PA}$.
[[This example|EQH7XTZ29V]] shows that adding it to $\mathsf{PA}$ gives a stronger theory.
The same argument shows that $\mathrm{Con}(T) \in \mathrm{TA}$ for every recursively axiomatized theory $T$ with $\mathfrak{N} \models T$, for example $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$.

## Explanations

### L1 human

$\mathrm{Con}(\mathsf{PA})$ says, in the language of numbers, "no number codes a proof of $0 = 1$ from the axioms of Peano arithmetic".
Every axiom of Peano arithmetic is true of the natural numbers, and true statements lead only to true statements.
So no proof of the false statement $0 = 1$ exists, and the consistency statement is true.
It is therefore a member of true arithmetic, although Peano arithmetic cannot prove it.

### L2 human

We check one instance of the universal statement.

1. Take $p = 0$. The number $0$ codes no sequence of formulas ending in $0 = S0$ under a standard numbering.
2. $\neg \mathrm{Prf}_{\mathsf{PA}}(\overline{0}, \ulcorner 0 = S0 \urcorner)$ is a true $\Delta_0$ sentence, so $\mathsf{Q}$ proves it.
3. The same holds for every numeral $\overline{p}$, by step 4 of the example and $\Sigma_1$-completeness.
4. $\mathsf{PA}$ proves each instance, but not the universal sentence.

The typical use is as the simplest member of $\mathrm{TA} \setminus \mathsf{PA}$.
A trap is to think that "each instance is provable" gives "the universal sentence is provable"; that would need the $\omega$-rule, which $\mathsf{PA}$ lacks.
