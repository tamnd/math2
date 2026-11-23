---
tag: DSQJ1RA71N
kind: statement
role: theorem
name: Spector's theorem on the Dialectica interpretation of analysis
msc: ["03F10", "03F35", "03F25"]
topics: [8XY7JYZKFW]
audience: research
uses: [8CCG6F2FAT, A4WR995XZP, ZREF8MTYNW, 6QFRG42QQR, WC4TDGEWZR, DC60FYCSPM, BWS0QMJJKT, WEMJBN339R]
about: [8CCG6F2FAT, HZ17ES9PDY]
proofs: [DZD5KXKN24]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Comprehension
  - url: https://en.wikipedia.org/wiki/Bar_recursion
    locator: lead section
history:
  first_stated: "Clifford Spector, 1962"
  notes: "Spector's paper 'Provably recursive functionals of analysis' appeared in 1962, after his death in 1961."
---

## Statement

Let $\mathsf{WE}\text{-}\mathsf{PA}^\omega$ be classical arithmetic in all finite types with the quantifier-free extensionality rule, and let $\mathsf{WE}\text{-}\mathsf{HA}^\omega$ be its intuitionistic version.
The types are built from $\mathbb{N}$ by $\sigma \to \tau$.
Let $\mathrm{AC}^0$ be the schema of countable choice in all types, $\forall n\, \exists x^\rho\, A(n, x) \to \exists f^{\mathbb{N} \to \rho}\, \forall n\, A(n, f\, n)$, for every formula $A$ and every type $\rho$.
Let T + BR be [[Gödel's system T|A4WR995XZP]] with the [[bar recursors|8CCG6F2FAT]] $\mathrm{BR}_{\rho, \tau}$ of all types and their defining equations.

**Theorem (Spector).**
Let $\varphi(n, m)$ be quantifier-free, with $n$ and $m$ of type $\mathbb{N}$.
If $\mathsf{WE}\text{-}\mathsf{PA}^\omega + \mathrm{AC}^0$ proves $\forall n\, \exists m\, \varphi(n, m)$, then there is a closed term $t : \mathbb{N} \to \mathbb{N}$ of T + BR such that $\mathsf{WE}\text{-}\mathsf{HA}^\omega$ with the equations of BR proves $\forall n\, \varphi(n, t\, n)$.

The theory $\mathsf{WE}\text{-}\mathsf{PA}^\omega + \mathrm{AC}^0$ contains classical [[second-order arithmetic|DC60FYCSPM]], with sets of numbers read as their characteristic functions.
For a formula $C(n)$, excluded middle gives $\forall n\, \exists k\, (k = 0 \leftrightarrow C(n))$.
Then $\mathrm{AC}^0$ gives an $f$ with $\forall n\, (f\, n = 0 \leftrightarrow C(n))$, and that is [[comprehension|BWS0QMJJKT]] for $C$.

## Remarks

### Why the hypotheses are needed

The conclusion must be $\Pi^0_2$ with $\varphi$ quantifier-free.
For a theorem $\forall x\, \exists y\, \forall z\, \psi$ a computable witness for $y$ may not exist, as the [[halting formula|7RFM1XPJQV]] shows.

Bar recursion is needed, since T alone does not suffice.
Analysis proves that every term of T normalizes, so the evaluation function of T is provably total in analysis, and no term of T defines it.

### Consequences

Every provably recursive function of classical second-order arithmetic is defined by a closed term of type $\mathbb{N} \to \mathbb{N}$ of T + BR.
For example, analysis proves that every Goodstein sequence reaches $0$, so a term of T + BR computes the number of steps.

The theorem also gives Spector's consistency argument.
If analysis proved $0 = 1$, then the theorem for $\forall n\, \exists m\, (0 = 1)$ would give a proof of $0 = 1$ in $\mathsf{WE}\text{-}\mathsf{HA}^\omega$ with the equations of BR.
So the consistency of analysis reduces to the consistency of that theory, as Gödel reduced the consistency of PA to that of T.

### Generalizations

The theorem extends to the schema of [[dependent choice|WEMJBN339R]] in all types, and we do not prove this extension.
The variables $n$ and $m$ can have any finite types, with a term $t$ of the type $\sigma \to \tau$ when $n : \sigma$ and $m : \tau$.
Kohlenbach's monotone interpretation gives majorants of $t$ in T + BR, and these are the basis of [[proof mining|XR1JXQG1CD]] in analysis.

## History

Spector proved the theorem in a paper published in 1962, after his death in 1961.
It extended Gödel's 1958 [[Dialectica interpretation|HZ17ES9PDY]] of arithmetic to classical analysis.
Later work replaced Spector's bar recursion by other forms, such as modified bar recursion, and studied the models of bar recursion.

## Explanations

### L1 human

The theorem says that each "for every $n$ there is an $m$" proved in classical analysis comes with a program that computes $m$ from $n$.
The program is written in a language that has one new kind of loop, bar recursion.
That loop keeps going until a test says the data collected are enough, and the test always passes in the end.
For example, from a proof in analysis that every Goodstein sequence reaches $0$, the method gives a program that computes the number of steps.

### L2 human

We trace the steps of the proof for a theorem $\forall n\, \exists m\, \varphi(n, m)$ of analysis.

1. The negative translation gives an intuitionistic proof of $\forall n\, \neg \neg \exists m\, \varphi(n, m)$ from the translated axioms.
2. The translated choice axiom follows from choice and the double negation shift.
3. The Dialectica interpretation turns the proof into terms, and bar recursion supplies the terms for the double negation shift.
4. The interpretation of $\neg \neg \exists m\, \varphi$ is $\exists m\, \neg \neg \varphi$, so the term gives $m$ from $n$.

The typical use is to see that the only extra ingredient beyond Gödel's interpretation of PA is the double negation shift.
Watch out: the Dialectica interpretation of $\mathrm{AC}^0$ itself is easy, and the hard case is the negative translation of $\mathrm{AC}^0$.

### L3 human

Spector's theorem carries out Hilbert's program for analysis in a relative form, since it reduces consistency to the well-foundedness of bar recursion, a principle whose justification goes beyond analysis.
The double negation shift is the classical content of countable choice, and bar recursion is its computational content.
Modern versions use products of selection functions or modified bar recursion, and they connect classical choice with backward induction in games and with continuation monads.
