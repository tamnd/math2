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

Robinson arithmetic $\mathsf{Q}$ is the first-order [[theory|92SWXST1ZM]] in the [[language of arithmetic|D8SD54M5PN]] with finitely many axioms and no induction.
Its axioms say that $S$ is injective with range the nonzero elements, give the recursive equations for $+$ and $\cdot$, and define $<$ from $+$.
The [[definition page|TT8MXRTVBM]] lists them as $\mathsf{Q}1$ to $\mathsf{Q}8$.
$\mathsf{Q}$ proves every true $\Sigma_1$ sentence, by the [[Σ1-completeness theorem|69234Z1V00]], and it [[represents every recursive function|BJF29XET83]].
It fails to prove simple universal laws, such as $\forall x\,(0 + x = x)$.
Because it is finitely axiomatized and still represents all recursive functions, it is the standard base theory for incompleteness and undecidability results.

## Motivation

Gödel's [[incompleteness theorems|X9WYNYE29C]] hold for every consistent, recursively axiomatized theory that contains "enough arithmetic".
$\mathsf{Q}$ makes "enough arithmetic" precise: it contains exactly what the proof needs and little more.
What the proof needs is that every computation can be verified, and verifying a computation means proving true equations and bounded facts about numerals.
Induction is not needed for that, because each computation is a finite object.
A finite axiom list has a further use.
If $\psi$ is the conjunction of the axioms of $\mathsf{Q}$, then $\mathsf{Q} \vdash \varphi$ holds if and only if $\psi \to \varphi$ is logically valid.
So the undecidability of $\mathsf{Q}$ transfers to pure logic, which is [[Church's theorem|VA6BNNY2YC]].

## Notation

The theory is written $\mathsf{Q}$; the name refers to Raphael Robinson.
The axioms are numbered $\mathsf{Q}1$ to $\mathsf{Q}7$ for the original axioms and $\mathsf{Q}8$ for the defining axiom of $<$.
Some books leave out $<$; others take it as primitive with their own axioms for it.
These choices give the same theorems in the common language $\set{0, S, +, \cdot}$, because a defining axiom gives an [[extension by definitions|GCK0NN60E4]].
For a closed term $t$, we write $t^{\mathfrak{N}}$ for its value in the standard model, and $\overline{n}$ is the numeral of $n$.

## Remarks

### Examples

- The standard model $\mathfrak{N}$ is a model of $\mathsf{Q}$; [[this example|WXHVSE066S]] checks the eight axioms.
- The set $\N \cup \set{a, b}$ with suitable operations is a model of $\mathsf{Q}$ in which $0 + a \ne a$ and $a + 0 \ne 0 + a$; [[this example|PR8Z1YPJDK]] builds it and checks every axiom.
- $\mathsf{Q} \vdash \overline{2} + \overline{2} = \overline{4}$. By $\mathsf{Q}5$ twice, $\overline{2} + S S 0 = S(\overline{2} + S 0) = S S(\overline{2} + 0)$. By $\mathsf{Q}4$, this equals $S S \overline{2}$, which is $\overline{4}$.

### Non-examples

- The integers with $S(n) = n + 1$ are not a model of $\mathsf{Q}$, since $S(-1) = 0$ violates $\mathsf{Q}1$; [[this non-example|QXFENZWRWM]] gives the details.
- [[Presburger arithmetic|B66JYY3K58]] is not an extension of $\mathsf{Q}$, because its language has no multiplication. It has induction, but it is decidable, so it lacks the strength of $\mathsf{Q}$.
- The second-order [[Peano axioms|0QFT7Z76N5]] are not a first-order theory, so they are not a theory in the sense of $\mathsf{Q}$; their first-order version [[Peano arithmetic|HACXBCM7SS]] extends $\mathsf{Q}$.

### Basic properties

- $\mathsf{Q}$ is consistent, because $\mathfrak{N} \models \mathsf{Q}$ and a theory with a model is consistent.
- For each closed term $t$, $\mathsf{Q} \vdash t = \overline{t^{\mathfrak{N}}}$. For $n \ne m$, $\mathsf{Q} \vdash \overline{n} \ne \overline{m}$.
- $\mathsf{Q}$ proves every true $\Delta_0$ sentence and refutes every false one. It proves every true $\Sigma_1$ sentence; see [[the Σ1-completeness theorem|69234Z1V00]].
- $\mathsf{Q} \vdash \forall x\,\bigl(x < \overline{n} \leftrightarrow (x = \overline{0} \lor \cdots \lor x = \overline{n - 1})\bigr)$ for each $n$, and $\mathsf{Q} \vdash \forall x\,(x < \overline{n} \lor x = \overline{n} \lor \overline{n} < x)$.
- Every recursive function is representable in $\mathsf{Q}$; see [[the representability theorem|BJF29XET83]].
- $\mathsf{Q}$ does not prove $\forall x\,(0 + x = x)$, $\forall x\, \forall y\,(x + y = y + x)$, $\forall x\, \forall y\, (x \cdot y = y \cdot x)$ or $\forall x\,(S x \ne x)$. The model of [[this example|PR8Z1YPJDK]] refutes each of them.
- So $\mathsf{Q}$ is not $\omega$-complete: it proves $0 + \overline{n} = \overline{n}$ for each $n$, but not $\forall x\,(0 + x = x)$.
- $\mathsf{Q}$ is essentially undecidable: every consistent theory in $L_A$ that contains $\mathsf{Q}$ is undecidable. Tarski, Mostowski and Robinson proved this.
  It implies the first [[incompleteness theorem|X9WYNYE29C]] for $\mathsf{Q}$, because a complete recursively axiomatized theory is decidable.
- $\mathsf{Q}$ is incomplete, and so is every consistent, [[recursively axiomatizable|3ANXZC3BEG]] extension of it.

### History

Raphael Robinson introduced the theory in 1950, as a finite axiom system that is essentially undecidable.
It was published with full proofs in the book *Undecidable Theories* by Tarski, Mostowski and Robinson (1953).
The book used $\mathsf{Q}$ to show that many theories are undecidable: a theory is undecidable if some consistent extension of it interprets $\mathsf{Q}$.

### Common errors

- To think that $\mathsf{Q}$ proves the laws of school algebra. It proves each numerical instance, such as $\overline{2} + \overline{3} = \overline{3} + \overline{2}$, but not the universal law.
- To think that incompleteness needs induction. $\mathsf{Q}$ has none, and Gödel's first theorem holds for it.
- To think that $\mathsf{Q}$ proves all true $\Pi_1$ sentences. The sentence $\forall x\,(0 + x = x)$ is a true $\Pi_1$ sentence that $\mathsf{Q}$ does not prove.

## Explanations

### L1 human

Robinson arithmetic is a short list of eight rules about the whole numbers.
The rules say how "next" behaves, how to add and multiply step by step, and what "less than" means.
With these rules one can check any single calculation, such as $2 + 2 = 4$ or $3 \cdot 4 = 12$.
But the rules contain no induction, so they cannot prove a law about all numbers, such as $x + y = y + x$.
Logicians like this theory because it is tiny, and still Gödel's incompleteness theorem applies to it.

### L2 human

We prove $\overline{2} \cdot \overline{2} = \overline{4}$ in $\mathsf{Q}$, writing out each axiom use.

1. $\overline{2} \cdot S S 0 = \overline{2} \cdot S 0 + \overline{2}$, by $\mathsf{Q}7$.
2. $\overline{2} \cdot S 0 = \overline{2} \cdot 0 + \overline{2}$, by $\mathsf{Q}7$, and $\overline{2} \cdot 0 = 0$, by $\mathsf{Q}6$.
3. $0 + \overline{2} = S S(0 + 0)$, by $\mathsf{Q}5$ twice, and $0 + 0 = 0$, by $\mathsf{Q}4$. So $\overline{2} \cdot S 0 = \overline{2}$.
4. So $\overline{2} \cdot \overline{2} = \overline{2} + \overline{2}$, and the Examples section gives $\overline{2} + \overline{2} = \overline{4}$.

The typical use of $\mathsf{Q}$ is as the weakest theory to which a theorem applies: "every consistent recursively axiomatized extension of $\mathsf{Q}$ is incomplete".
A trap is step 3: $0 + \overline{2} = \overline{2}$ is provable for this numeral, but $0 + x = x$ is not provable for a variable $x$.

### L3 human

$\mathsf{Q}$ sits at the bottom of a hierarchy of arithmetic theories, the [[fragments of PA|T70PYM1F36]], ordered by strength: $\mathsf{Q} \subseteq \mathsf{I}\Delta_0 \subseteq \mathsf{I}\Sigma_1 \subseteq \mathsf{PA}$.
Its models are easy to build, and its non-standard models need not satisfy any algebraic law beyond the axioms.
Yet $\mathsf{Q}$ is essentially undecidable, and its failure to prove $\forall x\,(0 + x = x)$ is a $\Pi_1$ gap of the kind that incompleteness predicts.
The theory $\mathsf{R}$ of Tarski, Mostowski and Robinson is weaker still, and it is also essentially undecidable; see [[weak theories of arithmetic|Q5MT8WY7JM]].
The [[Σ1-completeness theorem|69234Z1V00]] is the sharp form of what $\mathsf{Q}$ does: it proves all true $\Sigma_1$ sentences, and that suffices for the incompleteness theorems.
