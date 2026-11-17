---
tag: QPV0HNP22S
kind: statement
role: theorem
name: Gentzen's consistency proof
msc: ["03F30", "03F15", "03F05"]
topics: [XTTKZTYDSD]
audience: grad
uses: [0QFT7Z76N5, KT50SMH3EC, 0ZHQMQ2C1N, 4PZM5GJTR5, 5NVA2JRHPV]
about: [0QFT7Z76N5]
history:
  posed_by: "Gerhard Gentzen"
  first_stated: "1936"
  notes: "Published in Mathematische Annalen in 1936; a second version with ordinals assigned to sequent derivations appeared in 1938."
sources:
  - url: https://en.wikipedia.org/wiki/Gentzen's_consistency_proof
    locator: Gentzen's theorem
  - url: https://en.wikipedia.org/wiki/Gentzen's_consistency_proof
    locator: Relation to Hilbert's program and Gödel's theorem
same_as:
  wikidata: Q5533794
  wikipedia: Gentzen's consistency proof
---

## Statement

Let PA be first-order [[Peano arithmetic|0QFT7Z76N5]].
Let PRA be primitive recursive arithmetic: the first-order theory with a function symbol for each [[primitive recursive function|5NVA2JRHPV]], its defining equations, and induction for quantifier-free formulas.
Fix the standard notation system for the ordinals below [[epsilon nought|KT50SMH3EC]], coded by natural numbers, with its primitive recursive order $\prec$.
Let $\operatorname{Con}(\mathrm{PA})$ be the arithmetic sentence that says that no PA-proof ends with $0 = 1$.

For a formula $P(x)$, possibly with parameters, write $\operatorname{Prog}(P)$ for $\forall x \, (\forall y \prec x \; P(y) \to P(x))$.
Let $\mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0)$ be the schema of [[transfinite induction|0ZHQMQ2C1N]] along $\prec$ for quantifier-free formulas:
$$\operatorname{Prog}(P) \to \forall x \, P(x), \qquad P \text{ quantifier-free}.$$

**Theorem (Gentzen).**
$$\mathrm{PRA} + \mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0) \vdash \operatorname{Con}(\mathrm{PA}).$$

Books state the added principle in slightly different forms.
It can be a rule of inference, a schema, or the statement that every primitive recursive descending sequence of notations is finite.
The structure of the proof, with the lemmas that it cites, is in [[the proof by reduction of derivations|NBBQ02FXSD]].

## Remarks

### Why each hypothesis is needed

- The induction principle: PRA alone does not prove $\operatorname{Con}(\mathrm{PA})$. Every theorem of PRA is a theorem of PA, and PA does not prove $\operatorname{Con}(\mathrm{PA})$ by [[Gödel's second incompleteness theorem|4PZM5GJTR5]].
- The length $\varepsilon_0$: for a notation $a$ below $\varepsilon_0$, PA proves transfinite induction up to $a$, by [[transfinite induction in arithmetic|ZE54ABPMJ0]]. So $\mathrm{PRA} + \mathrm{QF}\text{-}\mathrm{TI}(a)$ is contained in PA, and it does not prove $\operatorname{Con}(\mathrm{PA})$.
- The standard notation system: the length of the order is not enough. There is a primitive recursive order of type $\omega$ along which transfinite induction proves $\operatorname{Con}(\mathrm{PA})$: [[the artificial notation system of type ω|PXMATF6B16]]. The theorem has content because the standard order is natural, and its well-foundedness can be seen by the [[comparison of Cantor normal forms|DXKWBFWCE0]].

### Consequences

- PA does not prove $\mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0)$, if PA is consistent. With [[transfinite induction in arithmetic|ZE54ABPMJ0]], this shows that $\varepsilon_0$ is the [[proof-theoretic ordinal|C72RBH0CDR]] of PA.
- The theorem is a [[relative consistency proof|X3G0RG2GPZ]]: the [[consistency|VM8TQ70CVJ]] of PA reduces to a principle that uses only finite objects, the notations, and one transfinite step.
- The method gives an [[ordinal analysis|C5E5TG8PGP]] of PA, the first in the subject.

### Converse

The conclusion fails when $\varepsilon_0$ is replaced by any smaller notation, by the second hypothesis above.
So $\varepsilon_0$ is the least length of a standard notation along which quantifier-free transfinite induction proves the consistency of PA.

### Generalizations

- The same method, with larger notation systems, gives the consistency of stronger theories: the Feferman-Schütte ordinal for predicative analysis and the Bachmann-Howard ordinal for theories of inductive definitions.
- Other proofs of the consistency of PA use Ackermann's method with [[Hilbert's epsilon calculus|TH5ZKCKN3W]], infinitary derivations with the [[ω-rule|XAMKAB1BZM]], or Gödel's [[Dialectica interpretation|HZ17ES9PDY]]. Each one uses a principle that PA does not prove.

## History

Gerhard Gentzen published the first proof in Mathematische Annalen in 1936.
An earlier version was withdrawn before publication, after Paul Bernays objected to a method used in it.
In 1938 Gentzen published a new version, with the sequent calculus and an assignment of ordinals to derivations, and this version is the one in most textbooks.
In 1943 he proved that PA proves transfinite induction up to each ordinal below $\varepsilon_0$, which shows that the ordinal is the least possible.
Wilhelm Ackermann gave a consistency proof with the epsilon substitution method in 1940.

## Explanations

### L1 human

Gödel showed that the usual axioms for the natural numbers cannot prove that they never lead to a contradiction.
Gentzen found an extra principle that is enough to prove it.
The principle is induction along a long, but explicit, ordering of finite symbols, of length $\varepsilon_0$.
The proof turns a supposed proof of $0 = 1$ into a "simpler" proof of $0 = 1$, again and again.
Each proof gets a label from the ordering, and the labels go down at each step.
Since the labels cannot go down for ever, no proof of $0 = 1$ exists.

### L2 human

We follow one reduction step on a small case.

1. Suppose a derivation of the empty sequent ends with a cut on $A \wedge B$. The left premise derives $\Rightarrow A \wedge B$ from $\Rightarrow A$ and $\Rightarrow B$. The right premise derives $A \wedge B \Rightarrow$ from $A \Rightarrow$.
2. The reduction replaces this cut by one cut on $A$, with the premises $\Rightarrow A$ and $A \Rightarrow$.
3. The new cut formula $A$ has fewer logical symbols than $A \wedge B$, and the part of the derivation that proves $B$ is removed.
4. The ordinal assignment gives the new derivation a smaller ordinal, because the degree of the cut drops.

The typical use of the theorem is as the model of an ordinal analysis: assign ordinals to derivations, and show that a reduction lowers them.
The trap: the theorem does not make the consistency of PA "more certain" by finitary means alone.
It uses transfinite induction up to $\varepsilon_0$, which PA itself cannot prove.

### L3 human

Gentzen's proof is the origin of [[ordinal analysis|C5E5TG8PGP]] and of structural proof theory.
Its two parts recur in every later analysis.
A well-ordering proof, as in [[transfinite induction in arithmetic|ZE54ABPMJ0]], gives the lower bound.
A reduction of derivations with an ordinal assignment gives the upper bound.
Read against [[Hilbert's program|P1RW6JWX73]], the theorem locates what goes beyond finitary reasoning in the consistency of PA.
It is one instance of well-foundedness, for a primitive recursive order of type $\varepsilon_0$.
