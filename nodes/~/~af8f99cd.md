---
tag: ~af8f99cd
kind: statement
role: theorem
name: Conservativity of Peano arithmetic over Heyting arithmetic for Pi-0-2 sentences
msc: ["03F25", "03F30", "03F55"]
topics: [8XY7JYZKFW]
audience: grad
uses: [0QFT7Z76N5, RXHJPVMPJH, ~10a427f4, ~c9a9f7c2, N238J43XNE, ~1fdd6e12, ~b2915593]
about: [~10a427f4, CK8ZQRN183, ~fc5d3da7]
proofs: [~32493866]
sources:
  - url: https://en.wikipedia.org/wiki/Friedman_translation
    locator: Application
  - url: https://en.wikipedia.org/wiki/Heyting_arithmetic
    locator: Conservativity
history:
  notes: "Harvey Friedman published the proof by the A-translation in 1978. Albert Dragalin found the same method independently."
---

## Statement

Let PA be [[Peano arithmetic|0QFT7Z76N5]] and HA [[Heyting arithmetic|RXHJPVMPJH]], in the language $0, S, +, \cdot, =$.
Let $\varphi(x, y)$ be a quantifier-free formula whose free variables are among $x$ and $y$.

**Theorem.** If $\mathsf{PA} \vdash \forall x\, \exists y\, \varphi(x, y)$, then $\mathsf{HA} \vdash \forall x\, \exists y\, \varphi(x, y)$.

In other words, PA is a $\Pi^0_2$-[[conservative extension|N238J43XNE]] of HA, for $\Pi^0_2$ sentences with a quantifier-free matrix.
The theorem also holds with several variables $x_1, \dots, x_k$ in place of $x$, with the same proof.

## Remarks

### Why each hypothesis is needed

- The matrix must be decidable. For $\Pi^0_3$ sentences the theorem fails: the [[non-example|~ca230195]] gives a sentence $\forall x\, \exists y\, \forall z\, \psi$ provable in PA but not in HA.
- The conclusion needs the sentence form $\forall x\, \exists y$. A classically provable disjunction $\exists y\, T(x, x, y) \vee \neg \exists y\, T(x, x, y)$, with Kleene's predicate $T$, is not provable in HA, so the theorem does not extend to arbitrary formulas.
- The two theories must have the same axioms. For example, PA + "PA is consistent" is not conservative over HA, because it proves the $\Pi^0_1$ sentence $\mathrm{Con}(\mathsf{PA})$, which HA does not prove.

### Consequences

- PA and HA have the same provably recursive functions: if PA proves that a program halts on every input, so does HA.
- [[Markov's rule|~1fdd6e12]]: if HA proves $\neg \neg \exists y\, \varphi(x, y)$ with $\varphi$ quantifier-free, then HA proves $\exists y\, \varphi(x, y)$.
- With the existence property of HA, a closed $\Sigma^0_1$ theorem $\exists y\, \varphi(y)$ of PA has a numeral witness $n$ with $\mathsf{HA} \vdash \varphi(\overline{n})$.
- By realizability, a theorem $\forall x\, \exists y\, \varphi$ of PA has a computable witness function $f$ with $\varphi(x, f(x))$ true for all $x$.

### Converse

The converse holds: HA is a part of PA, so every theorem of HA is a theorem of PA.
So PA and HA prove the same $\Pi^0_2$ sentences with quantifier-free matrix.

### Generalizations

- The same holds with function symbols for all primitive recursive functions. Then every $\Pi^0_2$ sentence is equivalent in HA to one of the form above.
- The same holds for arithmetic in all finite types, $\mathsf{PA}^\omega$ over $\mathsf{HA}^\omega$, by the same proof.
- PA is conservative over HA for all negative formulas, by the [[negative translation|~b2915593]].
- The [[Dialectica interpretation|HZ17ES9PDY]] gives a stronger form: the witness $y$ is given by a term of [[Gödel's system T|~62fef358]].

## History

Harvey Friedman published the proof by the A-translation in 1978.
Albert Dragalin found the same method independently.
The result also follows from Gödel's [[Dialectica interpretation|HZ17ES9PDY]], which is older, but the A-translation gives a short proof inside HA.

## Explanations

### L1 human

Some mathematicians accept only proofs that do not use the law of excluded middle.
The theorem says that for a large class of statements this restriction loses nothing.
These are the statements "for every number $x$ there is a number $y$ with a property that can be checked by calculation".
For example, "for every $x$ there is a prime $y$ larger than $x$" has this form.
If such a statement has a classical proof in arithmetic, it also has an intuitionistic proof.

### L2 human

We follow the theorem for $\forall x\, \exists y\, (x < y \wedge y \text{ is prime})$, written with quantifier-free $\varphi$ in a language with primitive recursive symbols.

1. Suppose a proof in PA uses excluded middle, for example a proof by contradiction in the style of Euclid.
2. The negative translation turns it into an HA proof of $\neg \forall y\, \neg \varphi(x, y)$.
3. The A-translation with $A = \exists y\, \varphi(x, y)$ turns this into an HA proof of $\exists y\, \varphi(x, y)$.
4. So HA proves the sentence, and realizability extracts a program that finds a prime above $x$.

The typical use is to transfer a classical theorem of number theory to a constructive setting without rewriting its proof.
A trap is to expect this for every sentence: the theorem fails for $\forall \exists \forall$ sentences.

### L3 human

The theorem is a conservation result between a classical theory and its intuitionistic version.
The same pattern holds for other pairs, for example $\mathsf{PA}^\omega$ over $\mathsf{HA}^\omega$, and second-order arithmetic over its intuitionistic version.
In each case the proof combines a negative translation with a Friedman translation.
A stronger form comes from functional interpretations: the [[Dialectica interpretation|HZ17ES9PDY]] gives a term of system T, and [[proof mining|~7cf2af55]] uses such terms to extract explicit bounds.
The general theory of such results is the subject of [[conservation theorems|~fc5d3da7]].
