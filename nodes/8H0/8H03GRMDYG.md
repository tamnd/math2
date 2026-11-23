---
tag: 8H03GRMDYG
kind: concept
name: Interpretability between theories
aliases: [relative-interpretation, interpretability, weak-interpretability]
msc: ["03F25", "03F30", "03B10"]
topics: [8XY7JYZKFW]
audience: grad
uses: [92SWXST1ZM, WDVVEYD6AT, HYJ10AF6RT, CY1TXHF6KQ, VM8TQ70CVJ, 0QFT7Z76N5, 4PZM5GJTR5, 7CVJCQKY41, 3ANXZC3BEG, 2BB5BMQKCJ]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretability
    locator: Informal definition
  - url: https://en.wikipedia.org/wiki/Interpretation_(model_theory)
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Weak_interpretability
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Tolerant_sequence
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Cointerpretability
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Interpretability_logic
    locator: lead section
  - book: isbn:9780122384523
  - book: isbn:9780521857840
---

## Summary

Set theory has no symbol for $0$ or for the successor, yet it can do arithmetic: read $0$ as the empty set, the successor of $x$ as $x \cup \{x\}$, and "number" as "element of $\omega$".
Under this reading every axiom of Peano arithmetic becomes a theorem of ZF, and that is what it means for [[ZF to interpret PA|918F85S4NQ]].

In general, let $S$ and $T$ be [[first-order theories|92SWXST1ZM]].
An *interpretation* $I$ of $T$ in $S$ gives a domain [[formula|HYJ10AF6RT]] $\delta(x)$ of $S$ and a formula of $S$ for each symbol of $T$, with function symbols given by the formulas of their graphs.
It translates each formula $A$ of $T$ into a formula $A^I$ of $S$: replace each symbol by its formula, keep the connectives, and relativize each quantifier to $\delta$.
The conditions are that $S$ proves $\exists x \, \delta(x)$, that $S$ proves that each graph formula defines a total function on $\delta$, and that $S$ proves $\sigma^I$ for each axiom $\sigma$ of $T$.
Then $S$ *interprets* $T$, written $S \rhd T$; the [[formal definition|2BB5BMQKCJ]] gives the details.
An interpretation sends a contradiction of $T$ to a contradiction of $S$, so $S \rhd T$ gives the consistency of $T$ from the consistency of $S$.

## Motivation

Mathematicians build one kind of object inside another all the time.
The natural numbers are built as sets, the integers as pairs of natural numbers, and the hyperbolic plane inside the Euclidean plane.
Each construction uses only definitions, and each axiom of the new objects becomes a theorem about the old ones.
Interpretability is the exact form of this practice for first-order theories.

It compares theories that need not share a language, and it does so without choosing models.
It also gives the standard shape of a [[relative consistency proof|X3G0RG2GPZ]]: if $S$ interprets $T$, then a finitary argument turns a proof of $\bot$ in $T$ into a proof of $\bot$ in $S$.

Interpretability returns in two places later on.
For extensions of PA it is equivalent to a conservation property for $\Pi_1$ sentences, and so it sits next to the [[conservation theorems|TNZ995J8AP]].
Its laws over PA are the subject of the interpretability logics in [[provability and interpretability logics|3E7M66WW6Q]].

## Notation

We write $S \rhd T$, or $T \lhd S$, for "$S$ interprets $T$", and some books write $T \le S$ or $T \trianglelefteq S$.
For one interpretation $I$, we write $A^I$ or $A^\tau$ for the translation of $A$.
$\mathrm{Con}(T)$ is the arithmetic sentence "$T$ is consistent", built from a [[Gödel numbering|MFJXPAF0R0]] and a fixed recursive axiomatization of $T$.
For such $T$, $T \upharpoonright n$ is the finite theory of the first $n$ axioms in a fixed enumeration.
$\Sigma_1$ and $\Pi_1$ are classes of the [[arithmetical hierarchy|7CVJCQKY41]], and PA is [[Peano arithmetic|0QFT7Z76N5]].
Watch the direction of the symbol: in $S \rhd T$ the theory $S$ at the wide end does the work.

## Remarks

### A first interpretation

We check two axioms of PA under the reading of the Summary, arguing in ZF.
The axiom $\forall x \, \lnot (S(x) = 0)$ translates to
$$\forall x \, \bigl(x \in \omega \to x \cup \{x\} \ne \emptyset\bigr).$$
This holds because $x \in x \cup \{x\}$, so $x \cup \{x\}$ has an element.

An instance of induction for a formula $A$ translates to "if $A^I(\emptyset)$ and $A^I(x) \to A^I(x \cup \{x\})$ for all $x \in \omega$, then $A^I(n)$ for all $n \in \omega$".
Separation gives the set $X = \{n \in \omega : A^I(n)\}$, the hypotheses say that $X$ contains $\emptyset$ and is closed under successor, and $\omega$ is the least such set, so $X = \omega$.
Check: we used one instance of Separation for each formula $A$, which is exactly what a schema needs.
The [[full verification|918F85S4NQ]] treats the other axioms and defines $+$ and $\cdot$ by recursion on $\omega$.

### Consistency, not truth

If $S \rhd T$ and $S$ is consistent, then $T$ is consistent.
The reason is that the translation of a derivation of $\bot$ in $T$ is a derivation of $\bot^I = \bot$ in $S$, since an interpretation sends theorems to theorems.
Most relative consistency proofs have this shape, for example the [[consistency of hyperbolic geometry relative to Euclidean geometry|PVW9DJASNJ]].

An interpretation does not preserve truth.
Feferman showed that [[PA interprets PA plus the inconsistency of PA|H34RWH89JJ]], a consistent theory whose new axiom $\lnot \mathrm{Con}(\mathsf{PA})$ is false.
In the standard model the interpretation defines a non-standard model, in which a non-standard number plays the part of a proof of $0 = 1$.

### Interpretability is not conservation

The two notions answer different questions.
$T$ is *conservative* over $S$ for a class of sentences when $T$ extends $S$ and proves no new sentences of that class, as in [[conservative extension|N238J43XNE]].
An interpretation needs no common language and asks only that the axioms of $T$ be translated into theorems of $S$.

For extensions of PA the two meet at one level, by the Orey-Hájek characterization.
Let $S$ and $T$ be consistent [[recursively axiomatized|3ANXZC3BEG]] extensions of PA in the language of PA.
Then three conditions are equivalent.

1. $S \rhd T$.
2. Every $\Pi_1$ sentence that $T$ proves is provable in $S$.
3. $S \vdash \mathrm{Con}(T \upharpoonright n)$ for every $n$.

So an interpretation of $T$ in $S$ gives $\Pi_1$-conservation and nothing more.
For example, $\mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA})$ is interpretable in PA, and yet it proves the $\Sigma_1$ sentence $\lnot \mathrm{Con}(\mathsf{PA})$, which PA does not prove.
In the other direction, $\mathsf{ACA}_0$ is conservative over PA for arithmetic sentences.
That is a statement about all arithmetic theorems, which no interpretation alone can give, and the [[conservation theorems|TNZ995J8AP]] prove it by other means.

### Global, local and weak interpretability

The relation $S \rhd T$ is *global* interpretability: one translation works for all axioms of $T$.
$T$ is *locally* interpretable in $S$ when each finite subtheory of $T$ is interpretable in $S$, possibly by a different translation for each one.
Global implies local, since one translation serves every finite subtheory.
Orey's compactness theorem gives the converse when $S$ is a recursively axiomatized extension of PA in the language of PA and $T$ is recursively axiomatized.

$T$ is *weakly interpretable* in $S$ when $T$ is interpretable in some [[consistent|VM8TQ70CVJ]] extension of $S$ in the language of $S$.
For consistent recursively axiomatized extensions of PA in the language of PA, this holds exactly when $S$ together with all $\Pi_1$ theorems of $T$ is consistent.
From left to right, a consistent $S' \supseteq S$ with $S' \rhd T$ proves every $\Pi_1$ theorem of $T$, by the step from 1 to 2.
From right to left, $S$ plus the $\Pi_1$ theorems of $T$ is consistent, recursively axiomatizable by [[Craig's theorem|6AN62NQ8AN]], and interprets $T$ by the step from 2 to 1.

### Tolerance, cointerpretability and Orey sentences

Japaridze extended weak interpretability to *tolerance* of finite sequences.
A sequence $T_1, \dots, T_n$ is tolerant when some consistent extensions $S_1, \dots, S_n$ of $T_1, \dots, T_n$ have $S_i \rhd S_{i+1}$ for each $i < n$.
For $n = 2$ this says that $T_2$ is weakly interpretable in $T_1$.
He also introduced a dual relation: $T$ is *cointerpretable* in $S$ when a translation $\tau$ of the language of $S$ into that of $T$ has $S \vdash A$ whenever $T \vdash A^\tau$.
For theories that contain PA it corresponds to $\Sigma_1$-conservativity, as interpretability corresponds to $\Pi_1$-conservativity.

A sentence $\sigma$ is an *Orey sentence* for $T$ when $T \rhd T + \sigma$ and $T \rhd T + \lnot \sigma$.
For consistent $T$ such a $\sigma$ is independent of $T$, since both extensions are then consistent.
For a consistent recursively axiomatized extension $T$ of PA in the language of PA, no $\Pi_1$ sentence $\sigma$ is an Orey sentence.
Indeed $T \rhd T + \sigma$ gives $T \vdash \sigma$ by $\Pi_1$-conservation, so $T + \lnot \sigma$ is inconsistent and not interpretable in $T$.
The same argument with $\lnot \sigma$ excludes $\Sigma_1$ sentences.

### More examples and non-examples

Each construction below defines a domain and the symbols, and proves the translated axioms.
Euclidean plane geometry interprets hyperbolic plane geometry, with the open unit disk as domain and its chords as lines, as in the [[Beltrami-Klein model|PVW9DJASNJ]].
PA interprets ZF with the axiom of infinity replaced by its negation, by Ackermann's coding: $x \in y$ means that the binary digit of $y$ at place $x$ is $1$.
For example $5 = 2^0 + 2^2$ codes the set $\{0, 2\}$.
ZF interprets ZFC plus the generalized continuum hypothesis, with Gödel's constructible universe as domain, as in the [[consistency proof of the axiom of choice|J3F0KBH6JT]].

On the other side, [[PA does not interpret PA plus the consistency of PA|NN7696NJR6]], because condition 2 above fails for the $\Pi_1$ sentence $\mathrm{Con}(\mathsf{PA})$.
PA does not interpret ZF either.
ZF proves that $\omega$ is a model of PA, so it proves the translation of $\mathrm{Con}(\mathsf{PA})$ and interprets $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$.
So $\mathsf{PA} \rhd \mathsf{ZF}$ would give $\mathsf{PA} \rhd \mathsf{PA} + \mathrm{Con}(\mathsf{PA})$ by transitivity.
Finally, the theory of a set with exactly two elements does not interpret the theory of an infinite set: a domain of $k$-tuples in a two-element model has at most $2^k$ elements.

### The rules you can use

Interpretability is reflexive, by the identity translation, and transitive.
If $I$ interprets $S$ in $R$ and $J$ interprets $T$ in $S$, the composite has domain $\delta_I(x) \land \delta_J(x)^I$ and translates each symbol $P$ of $T$ by $(\varphi^J_P)^I$.
If $S \rhd T$ by $I$ and $T \vdash \sigma$, then $S \vdash \sigma^I$; the [[formal definition|2BB5BMQKCJ]] proves this lemma.

If $S$ is a recursively axiomatized extension of PA, $T$ is recursively axiomatized and $S \vdash \mathrm{Con}(T)$, then $S \rhd T$.
This is the arithmetized completeness theorem, which goes back to Hilbert and Bernays.
The converse fails: PA interprets $\mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA})$ but does not prove its consistency, since that consistency implies $\mathrm{Con}(\mathsf{PA})$.

### Watch out

The first slip is to read $S \rhd T$ the wrong way round.
$S$ does the work, so $S$ is at least as strong as $T$ in consistency strength.

The second slip is to treat an interpretation as a proof of truth or of conservation.
PA interprets $\mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA})$, which is false in $\mathbb{N}$ and proves a $\Sigma_1$ sentence that PA does not prove.

The third slip is to check the translated axioms in one model of $S$ only.
Each translated axiom must be a theorem of $S$, so it must hold in every model of $S$.
A reading of PA in ZF that works in one model of ZF but fails in another is not an interpretation.

### History

Tarski introduced interpretability and weak interpretability in the 1953 book *Undecidable Theories*, written with Mostowski and Robinson, as a tool for proving undecidability.
Feferman showed in 1960, in "Arithmetization of metamathematics in a general setting", that PA interprets $\mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA})$.
Orey proved the compactness theorem, and the characterization by $\Pi_1$-conservativity carries the names of Orey and Hájek.
Japaridze introduced tolerance and cointerpretability in the early 1990s.

### Try it

First, does $\mathsf{ZF} \rhd \mathsf{PA}$ imply that ZF is conservative over PA?
No: the two theories have different languages, so the question needs a translation, and ZF proves the translation of $\mathrm{Con}(\mathsf{PA})$, which PA does not prove.

Second, let $\pi$ be a $\Pi_1$ sentence that PA does not prove.
Is $\mathsf{PA} + \pi$ interpretable in PA?
No: $\mathsf{PA} + \pi$ proves the $\Pi_1$ sentence $\pi$, so condition 2 of the Orey-Hájek characterization fails.

## Explanations

### L1 human

Suppose that one language has a word that another language lacks.
A translator can still express it with a phrase of the second language.
An interpretation does the same for mathematical theories: it translates each basic word of one theory into a phrase of another theory.
The translation must turn each basic rule of the first theory into a fact that the second theory can prove.
For example, set theory can speak about the numbers $0$, $1$ and $2$ as the sets $\{\}$, $\{0\}$ and $\{0, 1\}$.
Then a contradiction in arithmetic would give a contradiction in set theory.

### L2 human

We interpret in PA the theory $T$ of an equivalence relation $E$ with exactly two classes, both infinite.
Take the domain $\delta(x) := (x = x)$, and translate $E(x, y)$ as "$x + y$ is even":
$$\varphi_E(x, y) := \exists z \, (x + y = z + z).$$
Reflexivity holds with $z := x$, and symmetry holds because PA proves $x + y = y + x$.
For transitivity, let $x + y = 2a$ and $y + z = 2b$.
Then $x + z + 2y = 2a + 2b$, so $y \le a + b$ and $x + z = 2((a + b) - y)$.

The numbers $0$ and $1$ are not equivalent, because $z + z$ is $0$ or at least $2$.
Every $x$ is equivalent to $0$ or to $1$, because PA proves by [[induction|0ASJVEFA9J]] that each number is even or odd.
Each class has at least $k$ elements, namely $x, x + 2, \dots, x + 2(k - 1)$.
So PA proves every translated axiom, and since PA is consistent, $T$ is consistent.
The trap is to check only that the axioms hold in $\mathbb{N}$: what counts is that each translated axiom is a theorem of PA.

### L3 human

Interpretability is a preorder on theories, and its equivalence classes are the degrees of interpretability.
Theories that interpret each other are *mutually interpretable*, and *bi-interpretability* asks in addition that the two composite interpretations be definably isomorphic to the identity.
For single structures the same idea is a definable quotient of a definable set of tuples, as in [[interpretations and imaginaries|SZRM3N6BXW]].
An interpretation of $T$ in $S$ induces a map from the models of $S$ to the models of $T$, $\mathcal{M} \mapsto \mathcal{M}^I$.

For extensions of PA the Orey-Hájek characterization measures degrees of interpretability by $\Pi_1$ sentences such as consistency statements.
The modal logic ILM describes exactly the schematic laws of $p \rhd q$ over PA, read as "$\mathsf{PA} + q$ is interpretable in $\mathsf{PA} + p$", as GL does for provability; see [[provability and interpretability logics|3E7M66WW6Q]].
Conservation theorems compare theories by their theorems, interpretations by their translations, and [[Herbrand analysis|MESZ87G9ET]] reaches conservation by a third, proof-theoretic route.
