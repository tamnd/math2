---
tag: ~abb8aebf
kind: example
name: True arithmetic taken as a set of axioms
msc: ["03B22", "03F40"]
topics: [H8QZY0RZXZ]
audience: ug2
not_instance_of:
  - target: ~113060c3
    note: the proposed axioms are all sentences true in the natural numbers, and this set is not decidable, so no procedure can check whether a sequence of formulas is a derivation
uses: [~113060c3, T62EJ749R5, X9WYNYE29C, 3K1AKGXF8A, 655K8Y7VS8, TN9G24VABN, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/True_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: lead section
---

## Example

Let $L_A$ be the first-order language of arithmetic, with the symbols $0$, $S$, $+$, $\cdot$ and $=$.
Let $\mathcal{N}$ be the structure of the natural numbers with their usual zero, successor, addition and multiplication.
True arithmetic is the set $\mathrm{TA}$ of all sentences of $L_A$ that are true in $\mathcal{N}$.
We propose a system $S_{\mathrm{TA}}$ with the formulas of $L_A$, the axioms $\mathrm{TA}$, and the rules modus ponens and generalization.
We check the four parts of a [[formal system|~113060c3]].

1. The alphabet of $L_A$ (the symbols above, the connectives, the quantifiers, parentheses and the variables $v_0, v_1, \dots$) is a decidable set.
2. The formulas of $L_A$ are defined by formation rules, and a parsing procedure decides whether a string is a formula.
3. Modus ponens and generalization have one or two premises, and a comparison of strings decides whether they apply.
4. The set of axioms is $\mathrm{TA}$. We show that $\mathrm{TA}$ is not [[decidable|T62EJ749R5]].

Proof of step 4.

5. Suppose, for a contradiction, that $\mathrm{TA}$ is decidable.
6. $\mathrm{TA}$ is consistent. All its members are true in $\mathcal{N}$, so by [[soundness|4A84VHDTHV]] every sentence derived from $\mathrm{TA}$ is true in $\mathcal{N}$, and a sentence and its negation are never both true there.
7. $\mathrm{TA}$ is [[negation complete|655K8Y7VS8]]: for each sentence $\varphi$, either $\varphi$ or $\neg \varphi$ is true in $\mathcal{N}$, so one of them lies in $\mathrm{TA}$.
8. $\mathrm{TA}$ contains the axioms of [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$, because each of them is true in $\mathcal{N}$.
9. A decidable set of axioms is [[computably enumerable|TN9G24VABN]]. So, by steps 5, 6 and 8, the first [[incompleteness theorem|X9WYNYE29C]] applies to $\mathrm{TA}$ and gives a sentence $G$ with $\mathrm{TA} \nvdash G$ and $\mathrm{TA} \nvdash \neg G$.
10. This contradicts step 7. So $\mathrm{TA}$ is not decidable.

So $S_{\mathrm{TA}}$ fails the condition that the set of axioms is decidable, and it is not a formal system.

## Remarks

The proposal looks attractive, because every true sentence has a derivation of one line.
But then the question "is this sequence a derivation" is as hard as the question "is this sentence true", and the formal system gives no method of checking.
The condition of decidable axioms excludes exactly this kind of cheating.

$\mathrm{TA}$ is not even computably enumerable.
If it were, we could decide a sentence $\varphi$ by listing $\mathrm{TA}$ until $\varphi$ or $\neg \varphi$ appears, and by step 7 one of them appears.
This contradicts step 10.
By [[Tarski's undefinability theorem|YRV6SYK2BY]], $\mathrm{TA}$ is not even definable by a formula of $L_A$.

If we replace $\mathrm{TA}$ by the [[Peano axioms|0QFT7Z76N5]], we get a formal system, because the axioms of Peano arithmetic form a decidable set.
The price is that some true sentences, such as the Gödel sentence of that system, are not theorems.

## Explanations

### L1 human

Suppose we allow every true fact about whole numbers as a starting rule.
Then every true fact has a proof of one line: "this is a rule".
But nobody can check such a proof, because nobody has a method to tell which facts about whole numbers are true.
A formal system must let a machine check each proof, so its starting rules must be recognizable by a machine.
Gödel's theorem shows that "all true facts" is not a list that a machine can recognize.

### L2 human

We compare two systems in the language of arithmetic.

1. Peano arithmetic $\mathsf{PA}$ has a decidable set of axioms: the finitely many basic axioms and every instance of the induction schema. A procedure checks whether a sentence has the shape of an induction axiom.
2. So $\mathsf{PA}$ is a formal system, and its theorems are computably enumerable.
3. $\mathsf{PA}$ is consistent, because $\mathcal{N}$ is a model of it, and it contains $\mathsf{Q}$. By the first incompleteness theorem, some sentence is neither proved nor refuted by $\mathsf{PA}$.
4. $\mathrm{TA}$ decides every sentence, by step 7, but it is not a formal system.

The typical use of this example is to explain why the definition of a formal system asks for decidable axioms.
A trap is to say that the incompleteness theorem shows "some true sentences have no proof".
Every true sentence has a proof in some system, for example in $S_{\mathrm{TA}}$.
The theorem says that no single consistent formal system that contains $\mathsf{Q}$ proves all of them.
