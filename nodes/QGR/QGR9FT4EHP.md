---
tag: QGR9FT4EHP
kind: example
name: The proof predicate of Peano arithmetic is decidable
msc: ["03F40", "03F30"]
topics: [HXHHWY3328]
audience: grad
instance_of: [6M12VR1GT6]
uses: [6M12VR1GT6, MPSCREYC3M, 5NVA2JRHPV, TN9G24VABN]
sources:
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: First-order theory of arithmetic
  - book: isbn:9780521857840
---

## Example

[[First-order Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$ has infinitely many axioms, yet a program can check any proposed proof in it.
The axioms are six basic axioms about $0, S, +, \cdot$ and one induction axiom for each formula $\varphi(v, \vec{w})$, the universal closure of
$$(\varphi(0) \wedge \forall v \, (\varphi(v) \to \varphi(S v))) \to \forall v \, \varphi(v).$$
We show by [[arithmetization of syntax|6M12VR1GT6]] that the relation $\mathrm{Prf}_{\mathsf{PA}}(y, x)$, "$y$ codes a proof in $\mathsf{PA}$ of the formula with code $x$", is [[primitive recursive|5NVA2JRHPV]].

1. The six basic axioms have six fixed codes $a_1, \ldots, a_6$, and the test $x = a_1 \vee \cdots \vee x = a_6$ is primitive recursive.
2. There is a primitive recursive function $\mathrm{Ind}(f, i)$ that gives the code of the induction axiom for the formula with code $f$ and the variable $v_i$.
   It is built from substitution and concatenation of codes.
3. The formula and the variable of an induction axiom are parts of it, so their codes are smaller than the code of the axiom.
4. So $x$ codes an induction axiom exactly when $\exists f < x \, \exists i < x \, (\mathrm{Form}(f) \wedge x = \mathrm{Ind}(f, i))$.
   This is a bounded search over a primitive recursive relation, so it is primitive recursive.
5. By steps 1 and 4, $\mathrm{Ax}_{\mathsf{PA}}(x)$ is primitive recursive.
   The logical axioms of the proof system form a primitive recursive set by the same argument.
6. Modus ponens at line $i$ of $y$ is the test $\exists j < i \, \exists k < i \, ((y)_k = 2^{9} * (y)_j * 2^{3} * (y)_i * 2^{11})$.
   Here $2^9$, $2^3$ and $2^{11}$ code the strings $($, $\to$ and $)$, and $(y)_i$ is the code of line $i$.
7. $\mathrm{Prf}_{\mathsf{PA}}(y, x)$ says that $y$ codes a sequence, that each line is an axiom or follows from earlier lines by a rule, and that the last line has code $x$.
   All quantifiers are bounded by the length of $y$, so the relation is primitive recursive.
8. A primitive recursive relation is decidable, so a program decides whether a given number codes a proof in $\mathsf{PA}$ of a given formula.

## Remarks

The set of theorems of $\mathsf{PA}$ is $\{ x : \exists y \, \mathrm{Prf}_{\mathsf{PA}}(y, x) \}$, so it is [[computably enumerable|TN9G24VABN]]: list all $y$ and print the last line of each proof.
It is not decidable, because every consistent extension of $\mathsf{Q}$ is undecidable.
So the quantifier $\exists y$ cannot be replaced by a bounded one.
Checking a proof is mechanical, and finding one is not.

The same check works for $\mathsf{ZFC}$, whose separation and replacement schemes are decidable sets of formulas for the same reason as the induction scheme.
What breaks the example is an axiom set that a program cannot recognize.
If we add to $\mathsf{PA}$ every true sentence of arithmetic, step 5 fails, and the theory has [[no decidable axiom set at all|69TTX21TRJ]].

## Explanations

### L1 human

Peano arithmetic has infinitely many axioms, one induction axiom for each formula.
Still, a program can tell whether a given formula is one of them, just by looking at its shape.
So a program can check any proposed proof in Peano arithmetic, line by line.
Checking a proof is mechanical, while finding a proof is not, and that difference is at the heart of incompleteness.

### L2 human

Take the formula $\varphi(v) := 0 + v = v$.
Its induction axiom is
$$(0 + 0 = 0 \wedge \forall v \, (0 + v = v \to 0 + S v = S v)) \to \forall v \, (0 + v = v).$$
Given the code of this sentence, the test of step 4 searches below it for the code of $\varphi$ and the index of $v$, computes $\mathrm{Ind}$ on them, and finds a match.
A proof of $\forall v \, (0 + v = v)$ uses this axiom, proofs of the two parts of the hypothesis, and modus ponens, and each of its lines passes the same kind of test.
This is the typical use of the example: it makes $\mathrm{Prov}_{\mathsf{PA}}(x) := \exists y \, \mathrm{Prf}_{\mathsf{PA}}(y, x)$ a $\Sigma_1$ formula, the [[provability predicate|NB2BCZR40F]] of $\mathsf{PA}$.
