---
tag: 3K1AKGXF8A
kind: concept
name: Robinson arithmetic
aliases: [robinson-q]
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: grad
uses: [D8SD54M5PN, 92SWXST1ZM, MVCH6N9SNW, 0QFT7Z76N5, GCK0NN60E4]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
  - book: isbn:9780521857840
  - book: isbn:9780521701464
  - url: https://builds.openlogicproject.org/
    locator: Representability in Q
same_as:
  wikidata: Q928884
  wikipedia: Robinson arithmetic
---

## Summary

Robinson arithmetic $\mathsf{Q}$ is the arithmetic of a careful calculator: it can check every single computation, such as $2 + 2 = 4$, but it cannot prove a general law, such as $0 + x = x$.
That mix of strength and weakness makes it the standard base theory for the incompleteness theorems.

Exactly, $\mathsf{Q}$ is the first-order [[theory|92SWXST1ZM]] in the [[language of arithmetic|D8SD54M5PN]] with finitely many axioms and no induction.
Its seven axioms say that $S$ is injective with the nonzero elements as its range, and they give the recursive equations for $+$ and $\cdot$:
$$S x \ne 0, \quad S x = S y \to x = y, \quad x \ne 0 \to \exists y\,(x = S y),$$
$$x + 0 = x, \quad x + S y = S(x + y), \quad x \cdot 0 = 0, \quad x \cdot S y = x \cdot y + x.$$
An eighth axiom defines $<$ from $+$.
The [[formal definition|TT8MXRTVBM]] lists them as $\mathsf{Q}1$ to $\mathsf{Q}8$.
$\mathsf{Q}$ proves every true $\Sigma_1$ sentence, by [[Σ1-completeness|69234Z1V00]], and it [[represents every recursive function|BJF29XET83]].

## Motivation

Gödel's [[first incompleteness theorem|X9WYNYE29C]] holds for every consistent, recursively axiomatized theory that contains "enough arithmetic".
$\mathsf{Q}$ makes "enough arithmetic" precise, and it contains little more than the proof needs.
What the proof needs is that every computation can be verified, and verifying a computation means proving true equations and bounded facts about numerals.
Induction is not needed for that, because each computation is a finite object.

The finite list of axioms has a second use.
If $\psi$ is the conjunction of the axioms, then $\mathsf{Q} \vdash \varphi$ holds exactly when $\psi \to \varphi$ is logically valid.
So the undecidability of $\mathsf{Q}$ passes to pure logic, which is [[Church's theorem|VA6BNNY2YC]].
Later pages build on $\mathsf{Q}$: [[Peano arithmetic|HACXBCM7SS]] adds induction to it, and the [[fragments of PA|T70PYM1F36]] add induction in measured amounts.

## Notation

The theory is written $\mathsf{Q}$, after Raphael Robinson.
The axioms $\mathsf{Q}1$ to $\mathsf{Q}7$ are the original ones, and $\mathsf{Q}8$ is the defining axiom $x < y \leftrightarrow \exists v\,(v + S x = y)$.
Some books leave out $<$, and others take it as primitive with their own axioms for it.
These choices give the same theorems in the common language $\{0, S, +, \cdot\}$, because a defining axiom gives an [[extension by definitions|GCK0NN60E4]].
For a closed term $t$, we write $t^{\mathfrak{N}}$ for its value in the standard model, and $\overline{n}$ is the numeral of $n$.

## Remarks

### A first proof: 2 + 2 = 4

The numeral $\overline{2}$ is $SS0$, so we must prove $SS0 + SS0 = SSSS0$.
Axiom $\mathsf{Q}5$, with $x = SS0$ and $y = S0$, peels one $S$ off the right summand:
$$SS0 + SS0 = S(SS0 + S0).$$
Axiom $\mathsf{Q}5$ again, now with $y = 0$, peels off the next one:
$$SS0 + S0 = S(SS0 + 0).$$
Axiom $\mathsf{Q}4$ ends the recursion, since $SS0 + 0 = SS0$.
Now substitute back, which the equality rules of logic allow:
$$SS0 + S0 = SSS0, \qquad SS0 + SS0 = S(SSS0) = SSSS0.$$
That is $\overline{2} + \overline{2} = \overline{4}$.
Every true equation between closed terms has a proof of this kind, and only the recursion equations are used.

### What Q cannot prove

The sentence $\forall x\,(0 + x = x)$ is true in $\mathbb{N}$, and $\mathsf{Q}$ proves each instance $0 + \overline{n} = \overline{n}$ by the method above.
Yet $\mathsf{Q}$ does not prove the universal sentence.
To see why, you need a model of $\mathsf{Q}$ in which the sentence is false.
[[A model in which addition is not commutative|PR8Z1YPJDK]] adds two elements $a$ and $b$ to $\mathbb{N}$ and sets $x + a = b$ and $x + b = a$.
All eight axioms hold there, and $0 + a = b \ne a$.

By [[soundness|4A84VHDTHV]], a sentence that is false in some model of $\mathsf{Q}$ is not a theorem.
The same model refutes the commutativity of $+$ and of $\cdot$, the associativity of $+$, and $\forall x\,(S x \ne x)$.
So $\mathsf{Q}$ is not $\omega$-complete: it proves $\varphi(\overline{n})$ for each $n$ but not $\forall x\, \varphi(x)$.
These gaps are exactly what induction fills, and [[Peano arithmetic|HACXBCM7SS]] proves all of them.

### Models and non-models

The [[standard model is a model of Q|WXHVSE066S]], and this gives the consistency of $\mathsf{Q}$.
The integers with $S(n) = n + 1$ are [[not a model of Q|QXFENZWRWM]], since $S(-1) = 0$ breaks $\mathsf{Q}1$.
No finite structure is a model either, since an injective map of a finite set onto itself hits $0$.

Two nearby theories are not extensions of $\mathsf{Q}$.
[[Presburger arithmetic|4W0E9G7PPV]] has induction but no multiplication, and it is decidable, so it lacks the strength of $\mathsf{Q}$.
The second-order [[Peano axioms|0QFT7Z76N5]] are not a first-order theory at all, though their first-order version [[Peano arithmetic|HACXBCM7SS]] extends $\mathsf{Q}$.

### What Q can do

The positive facts all concern numerals.
For each closed term $t$, $\mathsf{Q} \vdash t = \overline{t^{\mathfrak{N}}}$, and for $n \ne m$, $\mathsf{Q} \vdash \overline{n} \ne \overline{m}$.
For each $n$, $\mathsf{Q}$ proves that the elements below $\overline{n}$ are exactly the numerals below it, and that every $x$ is below, equal to or above $\overline{n}$:
$$\forall x\,\bigl(x < \overline{n} \leftrightarrow (x = \overline{0} \lor \cdots \lor x = \overline{n - 1})\bigr), \qquad \forall x\,(x < \overline{n} \lor x = \overline{n} \lor \overline{n} < x).$$
From these, $\mathsf{Q}$ decides every $\Delta_0$ sentence, and [[Σ1-completeness|69234Z1V00]] follows.
[[Representability|BJF29XET83]] then shows that $\mathsf{Q}$ can follow every computation.

### Essential undecidability

$\mathsf{Q}$ is essentially undecidable: every consistent theory in $L_A$ that contains $\mathsf{Q}$ is undecidable.
Tarski, Mostowski and Robinson proved this.
It gives the first incompleteness theorem for every consistent [[recursively axiomatizable|3ANXZC3BEG]] extension of $\mathsf{Q}$, because a complete recursively axiomatized theory is decidable.
The [[weak theories of arithmetic|Q5MT8WY7JM]] push this further, to the theory $\mathsf{R}$, which is not finitely axiomatized.

### Watch out

Do not expect $\mathsf{Q}$ to prove the laws of school algebra.
It proves $\overline{2} + \overline{3} = \overline{3} + \overline{2}$, because both sides compute to $\overline{5}$, but not $\forall x\, \forall y\,(x + y = y + x)$.

Do not think that incompleteness needs induction.
$\mathsf{Q}$ has none, and Gödel's first theorem holds for it.

Do not think that $\mathsf{Q}$ proves every true $\Pi_1$ sentence.
The sentence $\forall x\,(0 + x = x)$ is a true $\Pi_1$ sentence that $\mathsf{Q}$ does not prove.

### History

Raphael Robinson introduced the theory in 1950, as a finite axiom system that is essentially undecidable.
It appeared with full proofs in *Undecidable Theories* by Tarski, Mostowski and Robinson in 1953.
The book used $\mathsf{Q}$ to show that many theories are undecidable: a theory is undecidable if some consistent extension of it interprets $\mathsf{Q}$.

### Try it

First, prove $\overline{1} \cdot \overline{1} = \overline{1}$ in $\mathsf{Q}$.
By $\mathsf{Q}7$ and $\mathsf{Q}6$, $S0 \cdot S0 = S0 \cdot 0 + S0 = 0 + S0$, and $0 + S0 = S(0 + 0) = S0$ by $\mathsf{Q}5$ and $\mathsf{Q}4$.

Second, in the model with $a$ and $b$, compute $(0 + a) + a$ and $0 + (a + a)$, and say which law of $\mathbb{N}$ fails.
The rules give $(0 + a) + a = b + a = b$ and $0 + (a + a) = 0 + b = a$, so the associativity of addition fails.

## Explanations

### L1 human

Robinson arithmetic is a short list of rules about the whole numbers.
The rules say how "next" behaves, how to add and multiply one step at a time, and what "less than" means.
With these rules you can check any single calculation, such as $2 + 2 = 4$ or $3 \cdot 4 = 12$.
But the rules contain no induction, so they cannot prove a law about all numbers, such as $x + y = y + x$.
Logicians like this theory because it is tiny, and still Gödel's incompleteness theorem applies to it.

### L2 human

Here is a second calculation: we prove $\overline{2} \cdot \overline{2} = \overline{4}$ in $\mathsf{Q}$.
Axiom $\mathsf{Q}7$ peels one $S$ off the right factor, twice:
$$\overline{2} \cdot SS0 = \overline{2} \cdot S0 + \overline{2}, \qquad \overline{2} \cdot S0 = \overline{2} \cdot 0 + \overline{2}.$$
Axiom $\mathsf{Q}6$ gives $\overline{2} \cdot 0 = 0$, so $\overline{2} \cdot S0 = 0 + \overline{2}$.
Axiom $\mathsf{Q}5$ twice and $\mathsf{Q}4$ give $0 + SS0 = S(0 + S0) = SS(0 + 0) = SS0$.
So $\overline{2} \cdot \overline{2} = \overline{2} + \overline{2}$, and the first proof in Remarks gives $\overline{4}$.

The typical use of $\mathsf{Q}$ is as the weakest theory to which a theorem applies, as in "every consistent recursively axiomatized extension of $\mathsf{Q}$ is incomplete".
Watch the step $0 + \overline{2} = \overline{2}$.
It is provable for this numeral, but $0 + x = x$ is not provable for a variable $x$.

### L3 human

$\mathsf{Q}$ sits at the bottom of a chain of theories ordered by the induction they allow: $\mathsf{Q} \subseteq \mathsf{I}\Delta_0 \subseteq \mathsf{I}\Sigma_1 \subseteq \mathsf{PA}$.
The [[fragments of PA|T70PYM1F36]] study this chain.
Models of $\mathsf{Q}$ are easy to build, and their non-standard elements need not satisfy any algebraic law beyond the axioms.
Yet $\mathsf{Q}$ is essentially undecidable, and its failure to prove $\forall x\,(0 + x = x)$ is a $\Pi_1$ gap of the kind that incompleteness predicts.
The theory $\mathsf{R}$ is weaker still and also essentially undecidable; see [[weak theories of arithmetic|Q5MT8WY7JM]].
[[Σ1-completeness|69234Z1V00]] is the sharp form of what $\mathsf{Q}$ does, and it is all that the [[incompleteness theorems|HXHHWY3328]] need from arithmetic.
