---
tag: PY679V9MVR
kind: statement
role: theorem
name: Conservativity of Peano arithmetic over Heyting arithmetic for Pi-0-2 sentences
msc: ["03F25", "03F30", "03F55"]
topics: [8XY7JYZKFW]
audience: grad
uses: [0QFT7Z76N5, RXHJPVMPJH, 6CCK0TT69P, WC4TDGEWZR, N238J43XNE, Z22K35X95F, DC1X1S0DJE]
about: [6CCK0TT69P, CK8ZQRN183, TNZ995J8AP]
proofs: [ANXVZG97MG]
sources:
  - url: https://en.wikipedia.org/wiki/Friedman_translation
    locator: Application
  - url: https://en.wikipedia.org/wiki/Heyting_arithmetic
    locator: Conservativity
history:
  notes: "Harvey Friedman published the proof by the A-translation in 1978. Albert Dragalin found the same method independently."
---

## Statement

The theorem says that the excluded middle adds no new theorems of the form "for every $x$ there is a $y$ with a decidable property": classical and intuitionistic arithmetic prove the same such sentences.

Let PA be [[Peano arithmetic|0QFT7Z76N5]] and HA [[Heyting arithmetic|RXHJPVMPJH]], in the language $0, S, +, \cdot, =$.
Let $\varphi(x, y)$ be a quantifier-free formula whose free variables are among $x$ and $y$.

**Theorem.** If $\mathsf{PA} \vdash \forall x\, \exists y\, \varphi(x, y)$, then $\mathsf{HA} \vdash \forall x\, \exists y\, \varphi(x, y)$.

So PA is a $\Pi^0_2$-[[conservative extension|N238J43XNE]] of HA, for $\Pi^0_2$ sentences with a quantifier-free matrix.
The theorem holds with several variables $x_1, \dots, x_k$ in place of $x$, by the same proof.

## Remarks

### A first case

Euclid's theorem, "for every $x$ there is a prime $y > x$", has this form once "$y$ is prime" is written with bounded quantifiers or a primitive recursive symbol.
Suppose a proof in PA uses a proof by contradiction.
The [[Gödel-Gentzen theorem|WC4TDGEWZR]] turns it into an HA proof of
$$\neg \forall y\, \neg \varphi(x, y).$$
The [[A-translation|6CCK0TT69P]] with $A = \exists y\, \varphi(x, y)$ then turns that into an HA proof of $\exists y\, \varphi(x, y)$.
The [[proof|ANXVZG97MG]] carries out these two steps for every $\varphi$.

### Why each hypothesis is needed

The matrix must be decidable, and the quantifier prefix must be $\forall \exists$.
For $\Pi^0_3$ sentences the theorem fails: the [[Pi-0-3 non-example|HVHEKG9FA5]] gives a sentence $\forall x\, \exists y\, \forall z\, \psi$ that PA proves and HA does not.
For arbitrary formulas it fails too, since PA proves $\exists y\, T(x, x, y) \vee \neg \exists y\, T(x, x, y)$ with Kleene's predicate $T$, and HA does not.

The two theories must share their axioms.
The extension $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ proves the $\Pi^0_1$ sentence $\mathrm{Con}(\mathsf{PA})$, which HA does not prove, so it is not $\Pi^0_2$-conservative over HA.

### What it gives you

PA and HA have the same provably recursive functions: if PA proves that a program halts on every input, so does HA.
[[Markov's rule|Z22K35X95F]] holds for HA: if HA proves $\neg \neg \exists y\, \varphi(x, y)$ with $\varphi$ quantifier-free, then HA proves $\exists y\, \varphi(x, y)$.
With the existence property of HA, a closed $\Sigma^0_1$ theorem $\exists y\, \varphi(y)$ of PA has a numeral witness $n$ with $\mathsf{HA} \vdash \varphi(\overline{n})$.
With Kleene's realizability, every theorem $\forall x\, \exists y\, \varphi$ of PA has a computable witness function $f$ with $\varphi(x, f(x))$ true for all $x$.

### The converse

The converse holds, since HA is a part of PA.
So PA and HA prove exactly the same $\Pi^0_2$ sentences with a quantifier-free matrix.
For negative formulas, those without $\vee$ and $\exists$, the two theories also agree, by the [[negative translation|DC1X1S0DJE]].

### Generalizations

The same holds with function symbols for all primitive recursive functions, and then every $\Pi^0_2$ sentence is equivalent in HA to one of the form above.
It holds for arithmetic in all finite types, $\mathsf{PA}^\omega$ over $\mathsf{HA}^\omega$, by the same proof.
The [[Dialectica interpretation|HZ17ES9PDY]] gives a stronger form, in which the witness $y$ is a term of [[Gödel's system T|A4WR995XZP]] applied to $x$.

## History

Harvey Friedman published the proof by the A-translation in 1978.
Albert Dragalin found the same method independently.
The result also follows from Gödel's [[Dialectica interpretation|HZ17ES9PDY]] of 1958, but the A-translation gives a short proof inside HA.

## Explanations

### L1 human

Some mathematicians accept only proofs that avoid the law of excluded middle.
The theorem says that for a large class of statements this restriction loses nothing.
These are the statements "for every number $x$ there is a number $y$ with a property that a calculation can check".
For example, "for every $x$ there is a prime $y$ larger than $x$" has this form.
If such a statement has a classical proof in arithmetic, it also has an intuitionistic proof.

### L2 human

We trace the theorem for $\forall x\, \exists y\, (x < y \wedge \mathrm{Prime}(y))$, with $\mathrm{Prime}$ a primitive recursive predicate symbol.
Euclid's proof is by contradiction: if no prime exceeds $x$, then the prime factors of $x! + 1$ give a contradiction.
The negative translation turns this into an HA proof of $\neg \forall y\, \neg (x < y \wedge \mathrm{Prime}(y))$.
The A-translation with $A = \exists y\, (x < y \wedge \mathrm{Prime}(y))$ turns it into an HA proof of $A$.
Realizability then extracts a program that finds a prime above $x$, and the [[bound from Euclid's proof|S0GAFZK93F]] makes this program explicit.

The typical use is to move a classical theorem of number theory into a constructive setting without rewriting its proof.
Watch out: the theorem fails for $\forall \exists \forall$ sentences, so check the quantifier prefix before you use it.

### L3 human

The theorem is a [[conservation theorem|TNZ995J8AP]] between a classical theory and its intuitionistic version.
The same pattern holds for other pairs, for example $\mathsf{PA}^\omega$ over $\mathsf{HA}^\omega$ and classical second-order arithmetic over its intuitionistic version.
In each case the proof combines a negative translation with a Friedman translation.
Functional interpretations give more: the [[Dialectica interpretation|HZ17ES9PDY]] gives a term of system T for the witness, and [[proof mining|XR1JXQG1CD]] turns such terms into explicit bounds.
