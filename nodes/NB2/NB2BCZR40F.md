---
tag: NB2BCZR40F
kind: concept
name: Provability predicate
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
uses: [6M12VR1GT6, MFJXPAF0R0, 3K1AKGXF8A, 92SWXST1ZM]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section P
    note: adopted
    mention: wikipedia://en/76765067#O2L8
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Provability_predicate
    locator: lead section
  - book: isbn:9780521857840
inventory: [808MBHW2M1]
---

## Summary

The sentence $0 + 0 = 0$ has a three-line proof in Robinson arithmetic, and that proof has a code number $p$.
The formula $\exists y \, \mathrm{Prf}_{\mathsf{Q}}(y, \ulcorner 0 + 0 = 0 \urcorner)$ says "some number codes a proof of $0 + 0 = 0$", and $p$ makes it true.
A provability predicate is this formula with the sentence left open: a formula of arithmetic that says "the sentence with code $x$ is provable".

Exactly, let $T$ be a [[first-order theory|92SWXST1ZM]] in the language of arithmetic with a decidable set of axioms.
Let $\mathrm{Prf}_T(y, x)$ be a $\Sigma_1$ formula that represents in [[Robinson arithmetic|3K1AKGXF8A]] the relation "$y$ codes a proof in $T$ of the formula with code $x$", as [[arithmetization of syntax|6M12VR1GT6]] provides.
The provability predicate of $T$ is
$$\mathrm{Prov}_T(x) := \exists y \, \mathrm{Prf}_T(y, x).$$
For each sentence $\varphi$, the sentence $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$ is true in $\mathbb{N}$ exactly when $T \vdash \varphi$.

## Motivation

Gödel's plan was to imitate the liar sentence, "this sentence is false", with "true" replaced by "provable".
Truth cannot be expressed in arithmetic, but provability can, and the provability predicate is the formula that expresses it.
The proof relation $\mathrm{Prf}_T$ is decidable, so a formula can express it with only bounded searches.
The set of theorems is not decidable, and the unbounded quantifier $\exists y$ is exactly the step from "this is a proof" to "a proof exists".
That makes $\mathrm{Prov}_T$ a $\Sigma_1$ formula, and the [[Gödel sentence|X9WYNYE29C]], which denies its own provability, is $\Pi_1$.

## Notation

Gödel wrote $\mathrm{Bew}(x)$, from the German "beweisbar", which means provable (see [[Bew|BF017NCXF4]]).
Other books write $\mathrm{Pr}_T(x)$ or $\mathrm{Prov}_T(x)$.
Provability logic writes $\square_T \varphi$, or just $\square \varphi$, for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$, and the [[derivability conditions|F6H4STF9RG]] set up this shorthand.
The corner quotes $\ulcorner \varphi \urcorner$ stand for the numeral of the [[Gödel number|MFJXPAF0R0]] of $\varphi$.

## Remarks

### A first case

[[Robinson arithmetic proves that 0 + 0 = 0 is provable|SVMC76P884]] works out the opening example.
The proof of $0 + 0 = 0$ has a code $p$, the relation "$p$ codes a proof" is true and decidable, and representability gives $\mathsf{Q} \vdash \mathrm{Prf}_{\mathsf{Q}}(\underline{p}, \ulcorner 0 + 0 = 0 \urcorner)$.
One step of logic then gives $\mathsf{Q} \vdash \mathrm{Prov}_{\mathsf{Q}}(\ulcorner 0 + 0 = 0 \urcorner)$.
The same argument works for every theorem of every theory $T$ with a decidable axiom set: if $T \vdash \varphi$, then $\mathsf{Q} \vdash \mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
This is the first derivability condition.
For $\mathsf{PA}$, the predicate built from the [[decidable proof relation|QGR9FT4EHP]] is the standard one, used in the [[second incompleteness theorem|4PZM5GJTR5]].

### Proofs that are not proofs

The reverse direction fails.
From $T \vdash \mathrm{Prov}_T(\ulcorner \varphi \urcorner)$ we cannot conclude $T \vdash \varphi$ in general.
The theory $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is consistent, and it proves $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner)$, while it does not prove $0 = S0$.
In a model of it, the witness $y$ is a non-standard number that codes no real proof, as [[non-standard proofs in a model of PA + ¬Con(PA)|JP0RVCPF38]] shows.
The reverse direction does hold when $T$ is $\Sigma_1$-sound, that is, when every $\Sigma_1$ sentence that $T$ proves is true in $\mathbb{N}$.
See [[ω-consistency|4S29X1GTV4]] for the related condition that Gödel used.

### Formulas that define the same set

The predicate depends on the formula that presents the axioms, not only on the set of theorems.
The [[Rosser provability predicate|Z0H1KA8ZHT]] defines the same set in $\mathbb{N}$ when $T$ is consistent, but it adds the clause "and no shorter proof of the negation exists".
$T$ proves the consistency statement built from it, so it cannot satisfy all three derivability conditions, since those conditions give the second incompleteness theorem.
In the same way, for consistent $T \supseteq \mathsf{PA}$, the formula $\mathrm{Prov}_T(x) \wedge \mathrm{Con}(T)$ defines the set of theorems in $\mathbb{N}$.
Yet $T$ proves none of its instances, since each instance implies $\mathrm{Con}(T)$, so the first derivability condition fails.
Feferman's work makes this sensitivity exact, and the [[consistency statement|4NBAX3VRQ7]] page returns to it.

### Not a truth predicate

Provability is not truth.
A formula $\mathrm{Tr}(x)$ with $\mathrm{Tr}(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ for every sentence $\varphi$ would be a truth predicate.
By [[Tarski's undefinability theorem|YRV6SYK2BY]], no formula of arithmetic is one.
The provability predicate escapes this limit because it does not satisfy those equivalences.

### Watch out

Do not read $T \vdash \mathrm{Prov}_T(\ulcorner \varphi \urcorner)$ as $T \vdash \varphi$.
The example $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ above separates them, with $\varphi$ the sentence $0 = S0$.
Do not treat $\mathrm{Prov}_T$ as decidable either.
Only $\mathrm{Prf}_T$ is decidable, and the quantifier $\exists y$ has no bound, because proofs can be much longer than the sentences they prove.

### History

Gödel's 1931 paper defined the formula $\mathrm{Bew}(x)$ as the last step of its list of arithmetized notions.
Hilbert and Bernays isolated the properties of the predicate that the second incompleteness theorem uses, in the second volume of their Grundlagen der Mathematik (1939), and Löb gave the simpler form of these conditions in 1955.
Feferman showed in 1960 how the second theorem depends on the formula that defines the axioms.

### Try it

Is $\mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$ true in $\mathbb{N}$ when $T = \mathsf{PA}$?
No: it is true in $\mathbb{N}$ only if $\mathsf{PA}$ proves $0 = S0$, and $\mathsf{PA}$ has the model $\mathbb{N}$, in which $0 = S0$ is false.

Which class is $\neg \mathrm{Prov}_T(x)$ in?
It is $\neg \exists y \, \mathrm{Prf}_T(y, x)$, which is equivalent to $\forall y \, \neg \mathrm{Prf}_T(y, x)$, a $\Pi_1$ formula.

## Explanations

### L1 human

A provability predicate is a formula of arithmetic that says "this statement has a proof".
It speaks through code numbers: "there is a number that codes a proof of the statement with code $n$".
The statement $0 + 0 = 0$ has a short proof, so the formula holds for its code.
To confirm the formula for a statement that has a proof, you only need to find the proof.
To confirm that a statement has no proof, no finite search is enough, since the proof might be very long.

### L2 human

We use the predicate to build the [[Gödel sentence|X9WYNYE29C]] of $\mathsf{PA}$.
The [[diagonal lemma|3PRW76471J]] applied to the formula $\neg \mathrm{Prov}_{\mathsf{PA}}(x)$ gives a sentence $G$ with
$$\mathsf{PA} \vdash G \leftrightarrow \neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner G \urcorner).$$
Suppose $\mathsf{PA} \vdash G$.
The first derivability condition gives $\mathsf{PA} \vdash \mathrm{Prov}_{\mathsf{PA}}(\ulcorner G \urcorner)$, and the equivalence gives $\mathsf{PA} \vdash \neg G$, so $\mathsf{PA}$ would be inconsistent.
So $\mathsf{PA}$ does not prove $G$, and this is the typical use: a formula about provability, put into a fixed point, yields an unprovable sentence.

### L3 human

The provability predicate is a $\Sigma_1$ definition of a computably enumerable set that is not decidable.
Its behavior inside $T$ is the subject of [[provability logic|WJK0YA4GP2]].
For the standard predicate of $\mathsf{PA}$, Solovay's theorem says that the modal logic GL describes exactly the schemes that $\mathsf{PA}$ proves about it.
Rosser's and Feferman's predicates define the same set in $\mathbb{N}$ but obey other modal laws.
The idea extends to interpretability predicates and to stronger notions such as $\omega$-provability, which lead to the polymodal logic GLP.
