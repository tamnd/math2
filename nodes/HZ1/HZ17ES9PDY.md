---
tag: HZ17ES9PDY
kind: concept
name: Dialectica interpretation
msc: ["03F10", "03F25", "03F50"]
topics: [8XY7JYZKFW]
audience: grad
uses: [CK8ZQRN183, RXHJPVMPJH, 5NVA2JRHPV, ZREF8MTYNW, A4WR995XZP, HGJVM49PA4]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Formula translation
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Proof translation (soundness)
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Characterisation principles
same_as:
  wikidata: Q5270518
  wikipedia: Dialectica interpretation
---

## Summary

The Dialectica interpretation is Gödel's translation of [[Heyting arithmetic|CK8ZQRN183]] into [[Gödel's system T|A4WR995XZP]], the quantifier-free theory of [[primitive recursive|5NVA2JRHPV]] functionals of finite type.
To each formula $A$ it assigns a formula $A^D = \exists x\, \forall y\, A_D(x, y)$, where $x$ and $y$ are tuples of variables of finite type and $A_D$ is quantifier-free; the [[definition|ZREF8MTYNW]] gives the clauses.
The soundness theorem says: if HA proves $A$, then a tuple $t$ of terms of T satisfies $\mathsf{T} \vdash A_D(t, y)$.
The idea matters because it reads off computable witnesses and bounds from proofs, and, after a [[double-negation translation|HGJVM49PA4]], it reduces the consistency of PA to that of T.

## Motivation

Hilbert's program asked for consistency proofs by finitary means.
Gentzen's proof for PA used induction up to $\varepsilon_0$, a principle about ordinals.
Gödel looked for a different extension of finitary reasoning: computation with functions of higher type, but no quantifiers over them.
A proof of $\forall n\, \exists m\, \varphi(n, m)$ should give a function $f$ with $\varphi(n, f(n))$.
For nested quantifiers, such as $\forall n\, \exists m\, \forall k\, \psi$, a witness is no longer computable in general; the interpretation then asks for a functional that defeats each counterexample function.
The translation $A \mapsto A^D$ makes this precise for every formula, by moving all quantifiers to the front with Skolem functions of higher type.

## Notation

We write $A^D = \exists x\, \forall y\, A_D(x, y)$; the tuple $x$ is the witness and the tuple $y$ the counterexample, or challenge.
We write $0$ for the type of natural numbers and $\sigma \to \tau$ for the function types of system T.
$\mathsf{HA}^\omega$ is Heyting arithmetic in all finite types, and $\mathsf{PA}^\omega$ its classical version.
AC is the axiom of choice in all finite types, MP is Markov's principle for quantifier-free formulas, and $\mathrm{IP}_\forall$ is independence of premise for universal premises.

## Remarks

### Examples

- For $A = \forall n\, \exists m\, (n < m)$, the interpretation is $A^D = \exists f\, \forall n\, (n < f n)$, and the term $\lambda n.\, S\, n$ is a witness.
- [[Markov's principle is interpreted by the identity|9YVRTGXKZF]]: the formula $\neg \neg \exists y\, \varphi(y) \to \exists y\, \varphi(y)$ with $\varphi$ quantifier-free has a witness in T.
- [[The contraction axiom for a universal formula|XWHF8SMTEF]]: the witness for $A \to A \wedge A$ uses a definition by cases on the quantifier-free matrix.
- An implication $\forall y\, \varphi(y) \to \forall z\, \psi(z)$ with quantifier-free $\varphi$ and $\psi$ asks for a functional $Y$ with $\varphi(Y z) \to \psi(z)$: from each $z$ that might fail, find a $y$ that fails too.
- Via the negative translation, a theorem $\forall n\, \exists m\, \varphi(n, m)$ of PA, with $\varphi$ quantifier-free, gives a closed term $t$ of type $1$ with $\mathsf{T} \vdash \varphi(n, t\, n)$.

### Non-examples

- [[Excluded middle for the halting problem|9NTJJMPZ29]]: $\forall n\, (\exists k\, P(n, k) \vee \neg \exists k\, P(n, k))$ has no witness in T. The condition that fails: the witness would decide the halting problem.
- Full extensionality in all finite types. The condition that fails: Howard showed that its interpretation has no witness in T, so the interpretation uses a weakly extensional theory.
- A direct interpretation of PA without the negative translation. The condition that fails: excluded middle is not interpreted, as the halting example shows.

### Basic properties

- [[Soundness|6QFRG42QQR]]: HA proves $A$ only if T proves $A_D(t, y)$ for some terms $t$. The same holds for $\mathsf{HA}^\omega + \mathrm{AC} + \mathrm{MP} + \mathrm{IP}_\forall$.
- Characterization: $\mathsf{HA}^\omega + \mathrm{AC} + \mathrm{MP} + \mathrm{IP}_\forall$ proves $A \leftrightarrow A^D$ for every formula $A$.
- For quantifier-free $A$, $A^D$ is $A$ itself, with empty tuples.
- Every type-1 function given by the interpretation is definable in T, so it is $\alpha$-recursive for some $\alpha < \varepsilon_0$.
- The interpretation of an implication $A \to B$ needs a decision of the matrix of $A$, so it needs that quantifier-free formulas are decidable.

### History

Gödel published the interpretation in 1958, in the journal Dialectica, which gave it its name.
Spector extended it to classical analysis by [[bar recursion|8CCG6F2FAT]] in 1962.
Kreisel used it, together with the [[no-counterexample interpretation|4BCD1EM542]], to extract bounds from proofs, and Kohlenbach developed this into [[proof mining|XR1JXQG1CD]].

### Common errors

- To apply the interpretation to a classical proof directly. Classical proofs must first go through a negative translation.
- To think that the witness $x$ depends only on the parameters. In an implication, the witness $f$ in $A_D(x, f x v)$ also depends on the challenge $v$ of the conclusion.
- To think that the interpretation needs no decidability. The contraction axiom $A \to A \wedge A$ needs a definition by cases on $A_D$.

## Explanations

### L1 human

The interpretation reads each statement as a game between two players.
One player chooses $x$, the other answers with $y$, and the first wins if the simple condition $A_D(x, y)$ holds.
A proof of the statement gives a winning strategy, written as a program built from [[primitive recursion|5NVA2JRHPV]] in higher types.
For example, a proof of $\forall n\, \exists m\, (m > n)$ yields the program $n \mapsto n + 1$.
In this way, numbers and bounds can be read off from proofs.

### L2 human

We interpret the formula $B = \forall n\, \exists m\, (n < m) \to \exists k\, (5 < k)$.

1. The premise has $\exists f\, \forall n\, (n < f n)$: the witness is $f$, and the challenge is $n$.
2. The conclusion has $\exists k\, (5 < k)$: the witness is $k$, and there is no challenge.
3. By the clause for $\to$, $B^D$ asks for a functional $U$ (from $f$ to $k$) and a functional $Y$ (from $f$ to $n$) with $f(Y f) > Y f \to U f > 5$.
4. The terms $U f = f(5)$ and $Y f = 5$ work: if $f(5) > 5$, then $U f > 5$.

The typical use is to read off a witness, here $f(5)$, from a proof that uses a lemma, here the premise.
A trap is to forget the backward part $Y$: the conclusion needs the premise only at the point $5$, and $Y$ names this point.

### L3 human

The interpretation is a functional interpretation: formulas become types of witnesses and challenges, and proofs become terms.
In categorical terms, de Paiva's Dialectica categories model it, and they are models of linear logic; this explains the role of contraction.
Variants include Shoenfield's interpretation of classical arithmetic, Diller and Nahm's variant, the monotone interpretation of Kohlenbach and the bounded functional interpretation of Ferreira and Oliva.
With bar recursion it interprets classical analysis, and its monotone form underlies [[proof mining|XR1JXQG1CD]] in analysis.
Composed with the negative translation, it shows that PA and HA prove the same $\Pi^0_2$ sentences, a result that [[Friedman's A-translation|6CCK0TT69P]] also gives.
