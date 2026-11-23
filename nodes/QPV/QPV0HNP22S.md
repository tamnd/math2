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

Gentzen's theorem says that finitary arithmetic plus one principle, induction along a well-order of type $\varepsilon_0$, proves that Peano arithmetic is consistent.

Let PA be first-order [[Peano arithmetic|0QFT7Z76N5]].
Let PRA be primitive recursive arithmetic: the first-order theory with a function symbol for each [[primitive recursive function|5NVA2JRHPV]], its defining equations, and induction for quantifier-free formulas.
Fix the standard notation system for the ordinals below [[epsilon nought|KT50SMH3EC]], coded by natural numbers, with its primitive recursive order $\prec$.
Let $\operatorname{Con}(\mathrm{PA})$ be the arithmetical sentence that says that no PA proof ends with $0 = 1$.
For a formula $P(x)$, possibly with parameters, write $\operatorname{Prog}(P)$ for $\forall x \, (\forall y \prec x \; P(y) \to P(x))$.
Let $\mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0)$ be the schema of [[transfinite induction|0ZHQMQ2C1N]] along $\prec$ for quantifier-free formulas:

$$\operatorname{Prog}(P) \to \forall x \, P(x), \qquad P \text{ quantifier-free}.$$

**Theorem (Gentzen).**
$$\mathrm{PRA} + \mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0) \vdash \operatorname{Con}(\mathrm{PA}).$$

Books state the added principle in slightly different forms: as a rule of inference, as a schema, or as the statement that every primitive recursive descending sequence of notations is finite.
The structure of the proof, with the lemmas that it cites, is in [[the proof by reduction of derivations|NBBQ02FXSD]].

## Remarks

### The ordinal of a short derivation

Gentzen's idea is to give every derivation an ordinal and to show that removing a cut lowers it.
Take the true atomic sentences $A$: $0 = 0$ and $B$: $S0 = S0$, and the derivation that proves $\Rightarrow A \wedge B$ from $\Rightarrow A$ and $\Rightarrow B$, proves $A \wedge B \Rightarrow A$ from $A \Rightarrow A$, and cuts on $A \wedge B$ to get $\Rightarrow A$.
In the assignment of the [[proof|NBBQ02FXSD]], each initial sequent gets $1$, the rule with one premise adds $1$, and the rule with two premises and the cut take natural sums:

$$o(\Rightarrow A \wedge B) = 1 \mathbin{\#} 1 = 2, \qquad o(A \wedge B \Rightarrow A) = 1 + 1 = 2, \qquad 2 \mathbin{\#} 2 = 4.$$

The cut formula $A \wedge B$ has one logical symbol, so the sequents above the cut have height $1$ and the end sequent has height $0$.
A drop of height by $1$ puts the value through $\alpha \mapsto \omega^\alpha$ once, so the whole derivation gets $\omega^4$.
The reduction replaces the cut on $A \wedge B$ by a cut on $A$ with the premises $\Rightarrow A$ and $A \Rightarrow A$.
That cut is atomic, no height drops, and the new value is $1 \mathbin{\#} 1 = 2 \prec \omega^4$.

### Why each hypothesis is needed

The induction principle is needed.
Every theorem of PRA is a theorem of PA, and PA does not prove $\operatorname{Con}(\mathrm{PA})$ by [[Gödel's second incompleteness theorem|4PZM5GJTR5]].

The full length $\varepsilon_0$ is needed.
For each notation $a$ below $\varepsilon_0$, PA proves transfinite induction up to $a$, by [[transfinite induction in arithmetic|ZE54ABPMJ0]].
So $\mathrm{PRA} + \mathrm{QF}\text{-}\mathrm{TI}(a)$ is contained in PA, and it does not prove $\operatorname{Con}(\mathrm{PA})$.

The standard notation system is needed, not just its length.
[[An artificial order of type ω|PXMATF6B16]] hides $\operatorname{Con}(\mathrm{PA})$ in its definition, so induction along it proves $\operatorname{Con}(\mathrm{PA})$ for a cheap reason.
The theorem has content because the standard order is natural, and its well-foundedness can be seen by the [[comparison of Cantor normal forms|DXKWBFWCE0]].

### What it gives you

If PA is consistent, then PA does not prove $\mathrm{QF}\text{-}\mathrm{TI}(\varepsilon_0)$, since otherwise PA would prove its own consistency.
Together with [[transfinite induction in arithmetic|ZE54ABPMJ0]], this makes $\varepsilon_0$ the [[proof-theoretic ordinal|C72RBH0CDR]] of PA.
The theorem is a [[relative consistency proof|X3G0RG2GPZ]]: the [[consistency|VM8TQ70CVJ]] of PA reduces to a principle about finite objects, the notations, plus one transfinite step.
The method gives the first [[ordinal analysis|C5E5TG8PGP]] in the subject.

### The converse and generalizations

The conclusion fails when $\varepsilon_0$ is replaced by any smaller notation, by the second hypothesis above.
So $\varepsilon_0$ is the least length of a standard initial segment along which quantifier-free induction proves the consistency of PA.
With larger notation systems, the same method gives the consistency of stronger theories, for example with $\Gamma_0$ for predicative analysis and the Bachmann-Howard ordinal for $\mathrm{ID}_1$.
Other consistency proofs of PA use the [[epsilon substitution method|F5HTHB46SH]], infinitary derivations with the [[ω-rule|XAMKAB1BZM]], or Gödel's [[Dialectica interpretation|HZ17ES9PDY]], and each uses a principle that PA does not prove.

## History

Gentzen published the first consistency proof of PA in Mathematische Annalen in 1936.
In 1938 he published a new version, with the sequent calculus and an assignment of ordinals to derivations, and most textbooks follow it.
In 1943 he showed that PA does not prove transfinite induction up to $\varepsilon_0$, while it proves it up to each smaller ordinal, so the ordinal is the least possible.
Ackermann gave a consistency proof by the epsilon substitution method in 1940.

## Explanations

### L1 human

Gödel showed that the usual axioms for the natural numbers cannot prove that they never lead to a contradiction.
Gentzen found an extra principle that is enough to prove it.
The principle is induction along a long, but explicit, ordering of finite symbols, of length $\varepsilon_0$.
The proof turns a supposed proof of $0 = 1$ into a simpler proof of $0 = 1$, again and again.
Each proof gets a label from the ordering, and the labels go down at each step.
Labels cannot go down for ever, so no proof of $0 = 1$ exists.

### L2 human

How does one reduction step lower the ordinal in general?
Suppose a derivation of the empty sequent ends with a cut on $A \wedge B$, whose left premise $\Rightarrow A \wedge B$ comes from $\Rightarrow A$ and $\Rightarrow B$, and whose right premise $A \wedge B \Rightarrow$ comes from $A \Rightarrow$.
The reduction replaces this cut by one cut on $A$, with the premises $\Rightarrow A$ and $A \Rightarrow$.
The new cut formula has fewer logical symbols, and the part of the derivation that proves $B$ is dropped.
The tower of $\omega$'s in the assignment loses a level, as in the computation of $\omega^4$ above, so the ordinal falls.
This is the typical use: the theorem is the model of every ordinal analysis.
Watch out: the proof does not make the consistency of PA certain by finitary means alone, because it uses induction up to $\varepsilon_0$, which PA cannot prove.

### L3 human

Gentzen's proof is the origin of [[ordinal analysis|C5E5TG8PGP]] and of structural proof theory.
Its two parts recur in every later analysis: a well-ordering proof, as in [[transfinite induction in arithmetic|ZE54ABPMJ0]], gives the lower bound, and a reduction of derivations with an ordinal assignment gives the upper bound.
Read against [[Hilbert's program|P1RW6JWX73]], the theorem isolates what goes beyond finitary reasoning in the consistency of PA.
It is a single instance of well-foundedness, for a primitive recursive order of type $\varepsilon_0$.
