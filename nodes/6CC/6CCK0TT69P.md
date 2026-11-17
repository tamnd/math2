---
tag: 6CCK0TT69P
kind: concept
name: Friedman's A-translation
msc: ["03F25", "03F30", "03F55"]
topics: [8XY7JYZKFW]
audience: grad
uses: [Q11N8X99FK, PAQ4ZX2TX1, RXHJPVMPJH, 0QFT7Z76N5, HGJVM49PA4, NCDZ969V7X]
sources:
  - url: https://en.wikipedia.org/wiki/Friedman_translation
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Friedman_translation
    locator: Application
  - url: https://en.wikipedia.org/wiki/Heyting_arithmetic
    locator: Conservativity
---

## Summary

Let $A$ be a formula of a first-order language with $\bot$.
For a formula $B$ whose bound variables are not free in $A$, the *A-translation* $B^A$ is the formula obtained from $B$ by replacing each atomic subformula $P$, including $\bot$, by $P \vee A$.
Its main property: if [[Heyting arithmetic|RXHJPVMPJH]] proves $B$, then HA proves $B^A$, for every formula $A$.
Applied after the [[double-negation translation|HGJVM49PA4]], it turns a classical proof of $\exists y\, \varphi$ into an intuitionistic one, so it extracts witnesses from classical proofs.

## Motivation

The negative translation turns a proof of $\exists y\, \varphi(x, y)$ in [[Peano arithmetic|0QFT7Z76N5]] into a proof of $\neg \neg \exists y\, \varphi(x, y)$ in HA.
The double negation cannot be removed by a general rule of [[intuitionistic logic|Q11N8X99FK]].
But the derivation of $\neg \neg \exists y\, \varphi$ is uniform in the formula $\bot$: it never uses a property of $\bot$ except ex falso.
Replacing $\bot$ by the goal $\exists y\, \varphi$ itself turns $(\exists y\, \varphi \to \bot) \to \bot$ into $(\exists y\, \varphi \to \exists y\, \varphi) \to \exists y\, \varphi$.
The premise of this formula is provable, so its conclusion is.
The A-translation makes this replacement work in every derivation, with atoms included to keep ex falso sound.

## Notation

We write $B^A$; the letter $A$ in the name refers to the formula $A$ that is added to the atoms.
The translation is also called the Friedman translation, or the Friedman-Dragalin translation.
We write $\vdash_i$ for derivability in intuitionistic [[natural deduction|PAQ4ZX2TX1]] NJ.

## Remarks

### Examples

- For an equation $s = t$, $(s = t)^A = (s = t \vee A)$, and $\bot^A = \bot \vee A$, which is equivalent to $A$.
- For a negation, $(\neg B)^A = B^A \to \bot \vee A$, so the translation reads $\neg B$ as "$B$ implies $A$".
- [[Markov's rule for HA|Z22K35X95F]]: if HA proves $\neg \neg \exists y\, \varphi(x, y)$ with $\varphi$ quantifier-free, then HA proves $\exists y\, \varphi(x, y)$. The proof takes $A = \exists y\, \varphi(x, y)$.
- [[A witness from an infinite descent argument|KE1C94RNF3]]: the classical proof that no sequence of natural numbers decreases forever gives, after A-translation, an index $y \le f(0)$ with $f(y) \le f(y + 1)$.
- [[The conservativity of PA over HA for Pi-0-2 sentences|PY679V9MVR]] is the main application.

### Non-examples

- [[Replacing only falsity by A|K9KMSBSAKK]]: the map that replaces $\bot$ by $A$ and keeps the other atoms. The condition that fails: ex falso $\bot \to P$ becomes $A \to P$, which HA does not prove for $A = (0 = 0)$ and $P = (0 = 1)$.
- Replacing each atom $P$ by $P \wedge A$. The condition that fails: HA proves $0 = 0$, but not $0 = 0 \wedge A$ for $A = (0 = 1)$.
- The A-translation of PA proofs without the negative translation first. The condition that fails: for $A = \bot$, $(P \vee \neg P)^A$ is equivalent to $P \vee \neg P$, which HA does not prove for $P = \exists y\, T(x, x, y)$.

### Basic properties

- If $\mathsf{HA} \vdash B$, then $\mathsf{HA} \vdash B^A$. This is Lemma F2 and Lemma F3 of the [[proof of conservativity|ANXVZG97MG]].
- Ex falso for the translation: $\vdash_i A \to B^A$ for every formula $B$.
- For quantifier-free $\varphi$ in HA, $\mathsf{HA} \vdash \varphi^A \leftrightarrow \varphi \vee A$, because $\varphi$ is decidable.
- The translation commutes with the connectives and quantifiers, and with [[substitution|NCDZ969V7X]] of terms for variables not free in $A$.
- The same property holds for HA in all finite types, with the same proof.

### History

Harvey Friedman published the translation in 1978, and used it to show that PA and HA have the same provably recursive functions.
Albert Dragalin found the same method independently.
A refined version for minimal logic, in which only $\bot$ is replaced, was developed by Ulrich Berger, Wilfried Buchholz and Helmut Schwichtenberg for program extraction.

### Common errors

- To forget the atoms. Replacing only $\bot$ is sound in minimal logic, but not in intuitionistic logic with ex falso.
- To let a bound variable of $B$ capture a free variable of $A$. The bound variables of $B$ must be renamed first.
- To apply the method to $\Pi^0_3$ formulas. The [[non-example for Pi-0-3 sentences|HVHEKG9FA5]] shows that PA is not $\Pi^0_3$-conservative over HA.

## Explanations

### L1 human

A classical proof of "there is a number $y$ with property $P$" may only show that "no such number" leads to a contradiction.
Friedman's trick is to replace every "contradiction" in the proof by the goal itself, "there is such a number".
The rewritten proof is still correct, and its conclusion now gives the goal.
For example, a classical proof that a list of natural numbers cannot decrease forever becomes a search that finds the place where it stops decreasing.

### L2 human

We use the translation to remove a double negation.

1. Suppose HA proves $\neg \neg \exists y\, (y \cdot y = 4)$, that is, $(\exists y\, (y \cdot y = 4) \to \bot) \to \bot$.
2. Let $A = \exists y\, (y \cdot y = 4)$. The A-translation of the formula is $(\exists y\, (y \cdot y = 4 \vee A) \to \bot \vee A) \to \bot \vee A$.
3. HA proves it, by the main property.
4. The premise holds: from $y \cdot y = 4 \vee A$ we get $A$ in both cases, and then $\bot \vee A$.
5. So HA proves $\bot \vee A$, and ex falso in the first case gives $A$.

The typical use is the extraction of witnesses and bounds from classical proofs of $\Pi^0_2$ sentences.
A trap is to apply the translation directly to a classical proof; the negative translation must come first.

### L3 human

The A-translation is a continuation-passing transformation with answer type $A$: the negative translation uses the answer type $\bot$, and Friedman's step changes the answer type.
In algebraic terms, $p \mapsto p \vee a$ is a nucleus on a Heyting algebra, the closed nucleus of $a$, and the A-translation applies it to the atomic formulas.
The method works for HA in all finite types and for intuitionistic second-order arithmetic.
Together with the [[Dialectica interpretation|HZ17ES9PDY]] it shows that PA and HA have the same provably recursive functions, the functions definable in [[system T|A4WR995XZP]] at type 1.
Its refined form for minimal logic is used in program extraction from classical proofs.
