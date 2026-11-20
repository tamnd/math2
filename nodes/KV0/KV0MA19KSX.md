---
tag: KV0MA19KSX
kind: example
name: Provability in PA is not a materially adequate truth definition
msc: ["03A05", "03F40"]
topics: [6Q4JJ2MMV8]
audience: grad
not_instance_of:
  - target: 8FBF0EFFC9
    note: the provability predicate of PA is formally correct, but PA does not prove its T-sentences, so it fails material adequacy
uses: [8FBF0EFFC9, NB2BCZR40F, X9WYNYE29C, 4PZM5GJTR5, HACXBCM7SS]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel's_incompleteness_theorems
    locator: First incompleteness theorem
  - url: https://plato.stanford.edu/entries/tarski-truth/
    locator: "Tarski's Truth Definitions, 1.3 Material adequacy"
---

## Example

Let the object language be the language of arithmetic, and let the metalanguage be [[Peano arithmetic|HACXBCM7SS]] $\mathsf{PA}$ itself.
Let $\mathrm{Prov}(x)$ be the standard [[provability predicate|NB2BCZR40F]] of $\mathsf{PA}$.
Take $\mathrm{True}(x) :\iff \mathrm{Prov}(x)$ as a proposed truth definition.
We check the two conditions of the [[semantic conception of truth|8FBF0EFFC9]].

1. *Formal correctness holds.* $\mathrm{Prov}(x)$ is a formula of arithmetic of the form $\exists y\, \mathrm{Prf}(y, x)$. It does not contain a truth predicate.
2. *Material adequacy would need* $\mathsf{PA} \vdash \mathrm{Prov}(\ulcorner S \urcorner) \leftrightarrow S$ for every sentence $S$.
3. *First failure.* Let $G$ be the Gödel sentence, with $\mathsf{PA} \vdash G \leftrightarrow \neg \mathrm{Prov}(\ulcorner G \urcorner)$. If $\mathsf{PA}$ proved $\mathrm{Prov}(\ulcorner G \urcorner) \leftrightarrow G$, it would prove $G \leftrightarrow \neg G$.
4. $\mathsf{PA}$ is consistent, because the standard model satisfies it. So $\mathsf{PA}$ does not prove $G \leftrightarrow \neg G$, and the T-sentence for $G$ is not a theorem.
5. *Second failure.* Take $S := (0 = 1)$. The T-sentence $\mathrm{Prov}(\ulcorner 0 = 1 \urcorner) \leftrightarrow 0 = 1$ is equivalent in $\mathsf{PA}$ to $\neg \mathrm{Prov}(\ulcorner 0 = 1 \urcorner)$, that is, to $\mathrm{Con}(\mathsf{PA})$.
6. By [[Gödel's second incompleteness theorem|4PZM5GJTR5]], $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA})$. So this T-sentence is not a theorem either.
7. *Failure in the standard model.* By [[Gödel's first incompleteness theorem|X9WYNYE29C]], $G$ is true and not provable. So $\mathrm{Prov}(\ulcorner G \urcorner) \leftrightarrow G$ is false in the standard model.

So provability in $\mathsf{PA}$ is not a materially adequate definition of truth for arithmetic.

## Remarks

The example separates truth from provability.
Step 7 shows a difference in the standard model: provability is a proper part of truth.
Steps 3 to 6 show a weaker failure: even where the two agree, $\mathsf{PA}$ cannot prove that they agree.
If we replace $\mathsf{PA}$ by a stronger consistent, computably axiomatized theory, the same argument applies to its provability predicate.
For $\Sigma_1$ sentences the situation is better: provability in $\mathsf{Q}$ is a [[Σ1 truth predicate|SFEBD4RB0X]] in the standard model.

## Explanations

### L1 human

One could try to define "true" as "provable from the axioms of arithmetic".
Gödel found a sentence that says "I am not provable".
If this sentence were provable, it would be false, so the axioms would prove a false statement.
So it is not provable, and then what it says holds: it is true.
So "provable" and "true" are different, and provability is not a correct definition of truth.

### L2 human

1. Let $G$ satisfy $G \leftrightarrow \neg \mathrm{Prov}(\ulcorner G \urcorner)$ in $\mathsf{PA}$.
2. Suppose $\mathsf{PA} \vdash G$. Then $\mathrm{Prov}(\ulcorner G \urcorner)$ is a true $\Sigma_1$ sentence, so $\mathsf{PA}$ proves it, and then $\mathsf{PA} \vdash \neg G$.
3. Then $\mathsf{PA}$ is inconsistent, which is false. So $\mathsf{PA} \nvdash G$.
4. So $\neg \mathrm{Prov}(\ulcorner G \urcorner)$ is true, and by step 1, $G$ is true.
5. The T-sentence $\mathrm{Prov}(\ulcorner G \urcorner) \leftrightarrow G$ has a false left side and a true right side.

The typical use of this example is to explain why truth needs a stronger metalanguage than proof.
The trap is to conclude that some true sentences can never be proved at all: $G$ is provable in stronger theories, for example in $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$.
