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

Let $\mathsf{WE}\text{-}\mathsf{PA}^\omega$ be classical arithmetic in all finite types, with the quantifier-free extensionality rule, and $\mathsf{WE}\text{-}\mathsf{HA}^\omega$ its intuitionistic version.
Let $\mathrm{AC}^0$ be the schema of countable choice in all types: $\forall n\, \exists x^\rho\, A(n, x) \to \exists f^{0 \to \rho}\, \forall n\, A(n, f\, n)$, for every formula $A$ and every type $\rho$.
Let T + BR be [[Gödel's system T|A4WR995XZP]] with the [[bar recursors|8CCG6F2FAT]] $\mathrm{BR}_{\rho, \tau}$ of all types and their defining equations.

**Theorem (Spector).**
Let $\varphi(n, m)$ be quantifier-free, with $n$ and $m$ of type $0$.
If $\mathsf{WE}\text{-}\mathsf{PA}^\omega + \mathrm{AC}^0$ proves $\forall n\, \exists m\, \varphi(n, m)$, then there is a closed term $t : 0 \to 0$ of T + BR such that $\mathsf{WE}\text{-}\mathsf{HA}^\omega$ with the equations of BR proves $\forall n\, \varphi(n, t\, n)$.

The theory $\mathsf{WE}\text{-}\mathsf{PA}^\omega + \mathrm{AC}^0$ contains classical [[second-order arithmetic|DC60FYCSPM]], with sets of numbers read as their characteristic functions.
Indeed, for a formula $C(n)$, excluded middle gives $\forall n\, \exists k\, (k = 0 \leftrightarrow C(n))$, and $\mathrm{AC}^0$ gives $f$ with $\forall n\, (f\, n = 0 \leftrightarrow C(n))$: this is [[comprehension|BWS0QMJJKT]].

## Remarks

### Why each hypothesis is needed

- The conclusion must be $\Pi^0_2$ with $\varphi$ quantifier-free. For $\forall x\, \exists y\, \forall z\, \psi$ a computable witness for $y$ may not exist, as the [[halting formula|7RFM1XPJQV]] shows.
- Bar recursion is needed: analysis proves the totality of functions, such as the number of steps of Goodstein sequences, that grow faster than every function defined in T.
- The verifying theory needs the equations of BR. The proof checks the interpretation of the double negation shift by these equations alone, with no induction over bars.

### Consequences

- Every provably recursive function of classical second-order arithmetic is defined by a closed term of type $0 \to 0$ of T + BR.
- A model of T + BR, such as the continuous functionals, gives a consistency proof of analysis relative to the existence of bar recursion. This is the sense in which Spector extended Gödel's consistency argument.

### Converse

The theorem gives one inclusion between the provably recursive functions of analysis and the type-1 functions of T + BR.
The converse inclusion is a different question, and it is not part of this theorem.

### Generalizations

- The theorem extends to the schema of [[dependent choice|WEMJBN339R]] in all types, with the same proof method; we do not prove this extension.
- The variables $n$ and $m$ can have any finite types, with a term $t$ of the type of $n \to m$.
- Kohlenbach's monotone interpretation gives majorants of $t$ in T + BR, and these are the basis of [[proof mining|XR1JXQG1CD]] in analysis.

## History

Spector proved the theorem in a paper published in 1962, after his death in 1961.
It extended Gödel's 1958 [[Dialectica interpretation|HZ17ES9PDY]] of arithmetic to classical analysis.
Later work replaced Spector's bar recursion by other forms, such as modified bar recursion, and studied the models of bar recursion.

## Explanations

### L1 human

The theorem says that each "for every $n$ there is an $m$" proved in classical analysis comes with a program that computes $m$ from $n$.
The program is written in a language that has one new kind of loop, bar recursion.
That loop keeps going until a test says the data collected are enough, and the test always passes in the end.
For example, from a proof in analysis that every Goodstein sequence reaches $0$, the method gives a term of T + BR that computes the number of steps.

### L2 human

We trace the steps of the proof for a theorem $\forall n\, \exists m\, \varphi(n, m)$ of analysis.

1. The negative translation gives an intuitionistic proof of $\forall n\, \neg \neg \exists m\, \varphi(n, m)$ from the translated axioms.
2. The translated choice axiom follows from choice and the double negation shift.
3. The Dialectica interpretation turns the proof into terms, and bar recursion supplies the terms for the double negation shift.
4. The interpretation of $\neg \neg \exists m\, \varphi$ is $\exists m\, \neg \neg \varphi$, so the term gives $m$ from $n$.

The typical use is to see that the only extra ingredient beyond Gödel's interpretation of PA is the double negation shift.
A trap is to apply the Dialectica interpretation to $\mathrm{AC}^0$ without the negative translation step; the translated axiom is the hard case.

### L3 human

Spector's theorem is a realization of Hilbert's program for analysis in a relativized form: consistency is reduced to the well-foundedness of bar recursion, a principle whose justification goes beyond analysis.
The double negation shift is the classical content of countable choice, and bar recursion is its computational content.
Modern versions use products of selection functions or modified bar recursion, and they connect classical choice with backward induction in games and with continuation monads.
