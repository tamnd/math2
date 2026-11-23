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

The consistency of $\mathsf{PA}$ is a true sentence that $\mathsf{PA}$ cannot prove.
Fix a [[Gödel numbering|MFJXPAF0R0]] and let $\mathrm{Prf}_{\mathsf{PA}}(p, x)$ be a $\Delta_0$ formula expressing "$p$ codes a proof in $\mathsf{PA}$ of the formula with code $x$".
Let $\mathrm{Con}(\mathsf{PA})$ be the sentence $\forall p \, \neg \mathrm{Prf}_{\mathsf{PA}}(p, \ulcorner 0 = S0 \urcorner)$.
We show that $\mathrm{Con}(\mathsf{PA}) \in \mathrm{TA}$, the set of sentences of [[true arithmetic|DX0KPMH4QZ]].

1. $\mathrm{Con}(\mathsf{PA})$ is a $\Pi_1$ sentence: one unbounded $\forall$ in front of a $\Delta_0$ formula.
2. $\mathfrak{N}$ is a model of [[Peano arithmetic|HACXBCM7SS]], since each axiom is true of the natural numbers.
3. By [[soundness|4A84VHDTHV]], every theorem of $\mathsf{PA}$ is true in $\mathfrak{N}$.
   The sentence $0 = S0$ is false in $\mathfrak{N}$, so it is not a theorem.
4. So no natural number $p$ codes a proof of $0 = S0$.
   Since $\mathrm{Prf}_{\mathsf{PA}}$ defines the proof relation in $\mathfrak{N}$, we get $\mathfrak{N} \models \neg \mathrm{Prf}_{\mathsf{PA}}(\overline{p}, \ulcorner 0 = S0 \urcorner)$ for each $p$.
5. By step 4, $\mathfrak{N} \models \mathrm{Con}(\mathsf{PA})$, so $\mathrm{Con}(\mathsf{PA}) \in \mathrm{TA}$.

So $\mathrm{TA}$ contains $\mathrm{Con}(\mathsf{PA})$, although $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA})$ by the [[second incompleteness theorem|4PZM5GJTR5]].

## Remarks

The argument runs in a set-theoretic metatheory, where $\mathfrak{N}$ is a set and soundness applies; it is not a proof inside $\mathsf{PA}$.

$\mathsf{PA}$ does not refute $\mathrm{Con}(\mathsf{PA})$ either, because $\mathsf{PA}$ proves only true sentences.
So $\mathrm{Con}(\mathsf{PA})$ is independent of $\mathsf{PA}$, and [[the non-conservativity example|EQH7XTZ29V]] shows that adding it gives a stronger theory.

$\Pi_1$ sentences have a special feature.
A false $\Pi_1$ sentence has a numerical counterexample, and then $\mathsf{Q}$ refutes it by [[$\Sigma_1$-completeness|69234Z1V00]].
So every $\Pi_1$ sentence that a consistent extension of $\mathsf{Q}$ fails to refute is true.

The same argument shows that $\mathrm{Con}(T) \in \mathrm{TA}$ for every recursively axiomatized theory $T$ with $\mathfrak{N} \models T$, for example $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$.

## Explanations

### L1 human

$\mathrm{Con}(\mathsf{PA})$ says, in the language of numbers, "no number codes a proof of $0 = 1$ from the axioms of Peano arithmetic".
Every axiom of Peano arithmetic is true of the natural numbers, and true statements lead only to true statements.
So no proof of the false statement $0 = 1$ exists, and the consistency statement is true.
It belongs to true arithmetic, although Peano arithmetic cannot prove it.

### L2 human

We check one instance of the universal statement.

1. Take $p = 0$.
   Under a standard numbering, the number $0$ codes no sequence of formulas ending in $0 = S0$.
2. So $\neg \mathrm{Prf}_{\mathsf{PA}}(\overline{0}, \ulcorner 0 = S0 \urcorner)$ is a true $\Delta_0$ sentence, and $\mathsf{Q}$ proves it.
3. The same holds for every numeral $\overline{p}$, by step 4 of the example and $\Sigma_1$-completeness.
4. So $\mathsf{PA}$ proves each instance, but not the universal sentence.

The typical use is as the simplest member of $\mathrm{TA}$ that $\mathsf{PA}$ does not prove.
Watch out: "each instance is provable" does not give "the universal sentence is provable".
That step would need the $\omega$-rule, which $\mathsf{PA}$ lacks.
