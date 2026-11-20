---
tag: ~e9e7c9af
kind: example
name: Truth for arithmetic defined in set theory
msc: ["03A05", "03C62"]
topics: [6Q4JJ2MMV8]
audience: grad
instance_of: [8FBF0EFFC9]
not_instance_of:
  - target: ~67eedfc4
    note: the truth predicate is an explicit definition inside ZF, a theory stronger than PA, and not a set of axioms for a new primitive predicate added to PA
uses: [8FBF0EFFC9, 0HE5WDQ9FJ, 1WTCZB4DVB, D8SD54M5PN, 0DSHAVH45F, EDRV3N0SA3]
sources:
  - url: https://plato.stanford.edu/entries/tarski-truth/
    locator: "Tarski's Truth Definitions, 1.3 Material adequacy"
  - url: https://en.wikipedia.org/wiki/Semantic_theory_of_truth
    locator: Definition of truth
---

## Example

The object language is the [[language of arithmetic|D8SD54M5PN]] $\{0, S, +, \cdot\}$.
The metalanguage is [[Zermelo-Fraenkel set theory|0HE5WDQ9FJ]] $\mathsf{ZF}$, with $\omega$ as the natural numbers and with the usual operations on $\omega$.
Code formulas of arithmetic by natural numbers, so that "$x$ is a formula" and "$x$ is a sentence" are defined in $\mathsf{ZF}$.
For a formula $\varphi$, write $\varphi^{\omega}$ for its translation into $\mathsf{ZF}$: quantifiers range over $\omega$, and $0, S, +, \cdot$ are read as the operations on $\omega$.

By [[definition by recursion|0DSHAVH45F]] on the complexity of formulas, $\mathsf{ZF}$ proves that there is a unique set $\mathrm{Sat}$ of pairs $(x, s)$ with these properties.
Here $x$ is a formula and $s$ is a finite sequence of elements of $\omega$ that gives values to the variables of $x$.

1. $(\ulcorner t_1 = t_2 \urcorner, s) \in \mathrm{Sat}$ iff the terms $t_1$ and $t_2$ have the same value under $s$.
2. $(\ulcorner \neg \varphi \urcorner, s) \in \mathrm{Sat}$ iff $(\ulcorner \varphi \urcorner, s) \notin \mathrm{Sat}$.
3. $(\ulcorner \varphi \wedge \psi \urcorner, s) \in \mathrm{Sat}$ iff both $(\ulcorner \varphi \urcorner, s)$ and $(\ulcorner \psi \urcorner, s)$ are in $\mathrm{Sat}$.
4. $(\ulcorner \forall v_i\, \varphi \urcorner, s) \in \mathrm{Sat}$ iff $(\ulcorner \varphi \urcorner, s[i \mapsto n]) \in \mathrm{Sat}$ for every $n \in \omega$.

This is the [[satisfaction|1WTCZB4DVB]] relation of the standard model.
Define $\mathrm{True}(x)$ iff $x$ is a sentence and $(x, \emptyset) \in \mathrm{Sat}$.
We check the conditions of the [[semantic conception of truth|8FBF0EFFC9]].

1. *Formal correctness.* $\mathrm{True}$ is defined by a formula of set theory in which $\mathrm{True}$ does not occur.
2. *The key lemma.* For each formula $\varphi(v_1, \dots, v_k)$, $\mathsf{ZF}$ proves $\forall n_1 \dots n_k \in \omega\,((\ulcorner \varphi \urcorner, (n_1, \dots, n_k)) \in \mathrm{Sat} \leftrightarrow \varphi^{\omega}(n_1, \dots, n_k))$.
3. *Proof of step 2 for atoms.* The value of a term under $s$ is computed by the recursion that builds the term. So clause 1 matches $(t_1 = t_2)^{\omega}$.
4. *Proof of step 2 for connectives.* Clauses 2 and 3 match $\neg$ and $\wedge$ in the translation, by the hypothesis for the parts.
5. *Proof of step 2 for quantifiers.* Clause 4 matches $(\forall v_i\,\varphi)^{\omega}$, which is $\forall n \in \omega\, \varphi^{\omega}$, by the hypothesis for $\varphi$.
6. Steps 3 to 5 give step 2 for every formula, by [[induction on formulas|EDRV3N0SA3]] in the meta-theory.
7. *Material adequacy.* For a sentence $\varphi$, step 2 with $k = 0$ gives $\mathsf{ZF} \vdash \mathrm{True}(\ulcorner \varphi \urcorner) \leftrightarrow \varphi^{\omega}$.

## Remarks

The definition works because $\mathsf{ZF}$ can form the set $\mathrm{Sat}$, an object that arithmetic cannot define by [[Tarski's undefinability theorem|YRV6SYK2BY]].
So the metalanguage is essentially stronger than the object language, as Tarski required.
One consequence is that $\mathsf{ZF}$ proves "every axiom of $\mathsf{PA}$ is true" and "truth is closed under the rules of logic", hence [[ZFC proves Con(PA)|1KSQAD4BWM]].
If we replace arithmetic by set theory itself as the object language, the construction fails: $\mathsf{ZF}$ has no truth definition for its own language.
It has only partial truth definitions, for example Levy's $\Sigma_n$ truth formulas, which the SEP entry describes.

## Explanations

### L1 human

Ordinary arithmetic cannot define "true sentence of arithmetic" by one formula.
Set theory is a larger language, and it can.
It builds, step by step, a table that says which formulas hold for which numbers.
Then "true" means "holds with no numbers plugged in".
For example, the table says that "$2 + 2 = 4$" holds, and so this sentence is true.

### L2 human

1. Take the sentence $\varphi := \forall v_1\, \neg(S(v_1) = 0)$.
2. By clause 4, $\mathrm{True}(\ulcorner \varphi \urcorner)$ iff $(\ulcorner \neg (S v_1 = 0) \urcorner, (n)) \in \mathrm{Sat}$ for every $n \in \omega$.
3. By clause 2, this holds iff $(\ulcorner S v_1 = 0 \urcorner, (n)) \notin \mathrm{Sat}$ for every $n$.
4. By clause 1, this holds iff $n + 1 \neq 0$ for every $n \in \omega$, which $\mathsf{ZF}$ proves.
5. So $\mathsf{ZF} \vdash \mathrm{True}(\ulcorner \varphi \urcorner)$, and the right side $\varphi^{\omega}$ is also a theorem of $\mathsf{ZF}$.

The typical use is in model theory and in proofs of consistency by truth.
The trap is to think that $\mathsf{ZF}$ proves every true sentence of arithmetic: it proves the T-sentences, but it does not decide every $\varphi^{\omega}$.
