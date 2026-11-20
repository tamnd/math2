---
tag: W4MSCKSG3D
kind: statement
role: theorem
name: Compositional truth over PA proves the consistency of PA
aliases: [ct-proves-con-pa, compositional-truth-ct, ct-minus-conservative]
msc: ["03F25", "03A05"]
topics: [6Q4JJ2MMV8]
audience: grad
about: [KE8ZX8KVA3]
uses: [KE8ZX8KVA3, HACXBCM7SS, 4NBAX3VRQ7, N238J43XNE, 1QD0KDDGYJ]
proofs: [2V7A0TMQN4]
sources:
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 3.3 Compositional truth"
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 1.2 Truth and reflection"
  - book: isbn:9780521115810
history:
  first_stated: Kotlarski, Krajewski and Lachlan, 1981
  notes: The SEP entry credits the conservativity of CT minus to Kotlarski, Krajewski and Lachlan (1981), with finitary proofs by Enayat and Visser (2015) and Leigh (2015). It credits the equivalence of CT with ACA to Takeuti (1987) and Feferman (1991).
---

## Statement

Use arithmetic with $0$, $S$, $=$ and predicates for addition and multiplication, so the closed terms are numerals.
Take $\neg$, $\vee$, $\exists$ as primitive; $\wedge$, $\to$, $\forall$ are abbreviations.
Let $\mathcal{L}_T$ add a unary predicate $T$, and let $A$ range over codes of sentences of the language of arithmetic.
Let $\mathrm{Tr}_0$ be the arithmetical formula for truth of atomic arithmetical sentences.
The *compositional axioms* are the following four sentences.

1. $\forall A\, (\mathrm{AtomSent}(A) \to (TA \leftrightarrow \mathrm{Tr}_0(A)))$.
2. $\forall A\, (T[\neg A] \leftrightarrow \neg TA)$.
3. $\forall A\, \forall B\, (T[A \vee B] \leftrightarrow (TA \vee TB))$.
4. $\forall A(v)\, (T[\exists v A(v)] \leftrightarrow \exists x\, T[A(\dot x)])$, where $A(v)$ has at most $v$ free and $A(\dot x)$ substitutes the numeral of $x$.

These are the SEP axioms 1, 2, 4 and 6; its axioms 3 and 5, for $\wedge$ and $\forall$, follow by the abbreviations.
$\mathsf{CT}^-$ is [[Peano arithmetic|HACXBCM7SS]] in $\mathcal{L}_T$ with these axioms, and with induction only for arithmetical formulas.
$\mathsf{CT}$ is $\mathsf{CT}^-$ with the [[induction schema|1QD0KDDGYJ]] for all formulas of $\mathcal{L}_T$.
Let $\mathrm{Con}(\mathsf{PA})$ be the [[consistency statement|4NBAX3VRQ7]] $\neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner)$, for the provability predicate $\mathrm{Prov}_{\mathsf{PA}}$.

1. *(Conservativity, cited.)* $\mathsf{CT}^-$ is a [[conservative extension|N238J43XNE]] of $\mathsf{PA}$ for arithmetical sentences.
2. *(Global reflection.)* $\mathsf{CT}$ proves that every arithmetical sentence provable in $\mathsf{PA}$ is true: $\mathsf{CT} \vdash \forall A\, (\mathrm{Prov}_{\mathsf{PA}}(A) \to TA)$.
3. *(Consistency.)* $\mathsf{CT} \vdash \mathrm{Con}(\mathsf{PA})$. So $\mathsf{CT}$ is not conservative over $\mathsf{PA}$.

Part 1 is cited without proof, and [[the proof|2V7A0TMQN4]] gives parts 2 and 3.

## Remarks

### Why each hypothesis is needed

1. *Induction for $\mathcal{L}_T$.* Without it, the theory is $\mathsf{CT}^-$, which is conservative by part 1. Since $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA})$, part 3 fails for $\mathsf{CT}^-$.
2. *The compositional axioms.* The typed T-sentences with full induction give $\mathsf{TB}$, which is [[conservative over PA|H3EK7YJ0B4]]. So the T-sentences alone do not prove $\mathrm{Con}(\mathsf{PA})$.
3. *Arithmetical sentences only.* The axioms speak about sentences without $T$. This typing keeps $\mathsf{CT}$ consistent; it has the standard model with $T$ interpreted as arithmetical truth.

### Consequences

1. By [[Gödel's second incompleteness theorem|4PZM5GJTR5]], $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA})$. So by part 3, $\mathsf{CT}$ proves an arithmetical sentence that $\mathsf{PA}$ does not prove.
2. $\mathsf{CT}$ proves each typed T-sentence, so it contains $\mathsf{TB}$.
3. The SEP entry states that $\mathsf{CT}$ and $\mathsf{ACA}$ are intertranslatable, with the same arithmetical theorems.

### Converse

The converse fails: $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ does not have the arithmetical strength of $\mathsf{CT}$.
By Lemma 1 of the proof, $\mathsf{CT}$ proves $T(\ulcorner \mathrm{Con}(\mathsf{PA}) \urcorner)$.
So the same proof, with one more true axiom, gives $\mathsf{CT} \vdash \mathrm{Con}(\mathsf{PA} + \mathrm{Con}(\mathsf{PA}))$.
By Gödel's second theorem, $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ does not prove this sentence.

### Generalizations

1. Let $S$ be a recursively axiomatized arithmetical theory. If $\mathsf{CT}$ proves that every axiom of $S$ is true, the same proof gives $\mathsf{CT} \vdash \mathrm{Con}(S)$.
2. The SEP entry reports that $\mathsf{CT}^-$ is relatively interpretable in $\mathsf{PA}$ and feasibly reducible to it. It also reports that these two results fail for finitely axiomatized base theories.

## History

The SEP entry reports that Kotlarski, Krajewski and Lachlan (1981) proved the conservativity of part 1 by model-theoretic means.
It reports that no finitary proof was available until Enayat and Visser (2015) and Leigh (2015).
It also reports, from Lachlan (1981), that not every model of $\mathsf{PA}$ expands to a model of $\mathsf{CT}^-$.

## Explanations

### L1 human

The theory $\mathsf{CT}$ has a predicate "true" with Tarski's rules: a negation is true when the sentence is not true, and so on.
With induction, $\mathsf{CT}$ shows that every axiom of $\mathsf{PA}$ is true, and that the logical rules keep truth.
So every theorem of $\mathsf{PA}$ is true, and the false sentence $0 = 1$ is not a theorem.
That is the consistency of $\mathsf{PA}$.

### L2 human

1. Lemma: $T$ commutes with $\neg$, $\vee$ and $\exists$, by the axioms.
2. So $T(\ulcorner 0 = S0 \urcorner)$ is false, by axiom 1.
3. By induction on the length of a proof, every line of every $\mathsf{PA}$ proof is true under all assignments.
4. So no $\mathsf{PA}$ proof ends with $0 = S0$.

The typical use is the standard example of a truth theory that is not conservative.
The trap is step 3: it is an induction on a formula that contains $T$, so $\mathsf{CT}^-$ cannot carry it out.

### L3 human

Global reflection is the natural strengthening of $\mathrm{Con}(\mathsf{PA})$; see [[reflection principles|NB485KFXKV]].
The SEP entry reports that uniform reflection over the typed uniform T-sentences derives the compositional axioms (Halbach 2001).
So $\mathsf{CT}$ is a form of reflection on $\mathsf{UTB}$.
