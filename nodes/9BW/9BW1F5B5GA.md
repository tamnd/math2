---
tag: 9BW1F5B5GA
kind: example
name: True arithmetic taken as a set of axioms
msc: ["03B22", "03F40"]
topics: [H8QZY0RZXZ]
audience: ug2
not_instance_of:
  - target: 439M8B4DY2
    note: the proposed axioms are all sentences true in the natural numbers, and this set is not decidable, so no procedure can check whether a sequence of formulas is a derivation
uses: [439M8B4DY2, T62EJ749R5, X9WYNYE29C, 3K1AKGXF8A, 655K8Y7VS8, TN9G24VABN, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/True_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: lead section
---

## Example

Why not take every true sentence of arithmetic as an axiom?
Then every truth has a proof of one line, and incompleteness seems to disappear.
The answer is that the result is not a [[formal system|439M8B4DY2]] at all, because nobody can check its proofs.

Let $L_A$ be the first-order language of arithmetic, with the symbols $0$, $S$, $+$, $\cdot$ and $=$.
Let $\mathcal{N}$ be the natural numbers with their usual zero, successor, addition and multiplication.
True arithmetic is the set
$$\mathrm{TA} = \{ \sigma : \sigma \text{ is a sentence of } L_A \text{ and } \mathcal{N} \models \sigma \}.$$
We propose a system $S_{\mathrm{TA}}$ with the formulas of $L_A$, the axioms $\mathrm{TA}$, and the rules modus ponens and generalization, and we check the four parts of a formal system.

1. The alphabet of $L_A$ (the symbols above, the connectives, the quantifiers, parentheses and the variables $v_0, v_1, \dots$) is a decidable set.
2. A parsing procedure decides whether a string is a formula of $L_A$.
3. Modus ponens and generalization have at most two premises, and a comparison of strings decides whether they apply.
4. The set of axioms is $\mathrm{TA}$, and we now show that it is not [[decidable|T62EJ749R5]].

The proof of step 4 is by contradiction.

1. Suppose that $\mathrm{TA}$ is decidable.
2. $\mathrm{TA}$ is consistent.
   All its members are true in $\mathcal{N}$, so by [[soundness|4A84VHDTHV]] every sentence derived from $\mathrm{TA}$ is true in $\mathcal{N}$, and a sentence and its negation are never both true there.
3. $\mathrm{TA}$ is [[negation complete|655K8Y7VS8]]: for each sentence $\varphi$, either $\varphi$ or $\neg \varphi$ is true in $\mathcal{N}$, so one of them lies in $\mathrm{TA}$.
4. $\mathrm{TA}$ contains the axioms of [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$, because each of them is true in $\mathcal{N}$.
5. A decidable set of axioms is [[computably enumerable|TN9G24VABN]].
   So by steps 1, 2 and 4 the first [[incompleteness theorem|X9WYNYE29C]] applies, and it gives a sentence $G$ with $\mathrm{TA} \nvdash G$ and $\mathrm{TA} \nvdash \neg G$.
6. This contradicts step 3, so $\mathrm{TA}$ is not decidable.

So $S_{\mathrm{TA}}$ fails the condition that the set of axioms is decidable, and it is not a formal system.

## Remarks

### Why the condition is there

With $\mathrm{TA}$ as axioms, the question "is this list of formulas a derivation?" is as hard as the question "is this sentence true in $\mathbb{N}$?".
A formal system is supposed to replace the second question by the first, so the definition demands decidable axioms.
The condition excludes exactly this kind of cheating.

### How far from decidable

$\mathrm{TA}$ is not even computably enumerable.
If it were, we could decide a sentence $\varphi$ by listing $\mathrm{TA}$ until $\varphi$ or $\neg \varphi$ appears, and by step 3 one of them would appear.
That contradicts step 6.
By [[Tarski's undefinability theorem|YRV6SYK2BY]], $\mathrm{TA}$ is not even definable by a formula of $L_A$.

### The honest alternative

Replace $\mathrm{TA}$ by the [[Peano axioms|0QFT7Z76N5]] $\mathsf{PA}$, and you get a formal system.
Its axioms are the finitely many basic axioms and every instance of the induction schema, and a program can recognize the shape of an induction axiom.
$\mathsf{PA}$ is consistent, because $\mathcal{N}$ is a model of it, and it contains $\mathsf{Q}$.
So the first incompleteness theorem gives a sentence that $\mathsf{PA}$ neither proves nor refutes.
You can have checkable proofs or every truth, but not both.

## Explanations

### L1 human

Suppose we allow every true fact about whole numbers as a starting rule.
Then every true fact has a proof of one line: "this is a rule".
But nobody can check such a proof, because nobody has a method to tell which facts about whole numbers are true.
A formal system must let a machine check each proof, so a machine must recognize its starting rules.
Gödel's theorem shows that no machine recognizes the list of all true facts.

### L2 human

The example is a standard answer to a common misreading of incompleteness.
People often say that the first incompleteness theorem shows "some true sentences have no proof".
But every true sentence $\sigma$ has a proof in some system, for example in $S_{\mathrm{TA}}$, or in $\mathsf{PA}$ with $\sigma$ added as an axiom.
What the theorem says is that no single consistent formal system with decidable axioms that contains $\mathsf{Q}$ proves all true sentences.
The decidability of the axioms is the hypothesis that does the work, and $S_{\mathrm{TA}}$ shows what happens without it: we get every truth and lose the ability to check.
Watch out: negation completeness is not the problem.
$\mathrm{TA}$ is negation complete, and the price is paid in decidability.
