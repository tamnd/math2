---
tag: DX0KPMH4QZ
kind: concept
name: True arithmetic
aliases: [ta, theory-of-the-standard-model, complete-theory-of-arithmetic]
msc: ["03F30", "03F40"]
topics: [QHCRN4JVG0]
audience: grad
uses: [D8SD54M5PN, HACXBCM7SS, MFJXPAF0R0, 4A84VHDTHV, 4W0E9G7PPV, 92SWXST1ZM, 655K8Y7VS8, YRV6SYK2BY, NYJX5QXX1T, 60P2XWY5QX, P5N2ND3VCG, 7CVJCQKY41, 3ANXZC3BEG, X9WYNYE29C, 1QWN5CV4CG]
sources:
  - url: https://en.wikipedia.org/wiki/True_arithmetic
    locator: Definition
  - url: https://en.wikipedia.org/wiki/True_arithmetic
    locator: Arithmetic undefinability
  - url: https://en.wikipedia.org/wiki/True_arithmetic
    locator: Computability properties
  - url: https://en.wikipedia.org/wiki/True_arithmetic
    locator: Model-theoretic properties
same_as:
  wikipedia: True arithmetic
---

## Summary

The sentence $\mathrm{Con}(\mathsf{PA})$ says that no number codes a proof of $0 = S0$ from the axioms of [[Peano arithmetic|HACXBCM7SS]].
It is true in the standard model $\mathfrak{N}$, but $\mathsf{PA}$ does not prove it.
True arithmetic contains it anyway, together with every other true sentence.

True arithmetic $\mathrm{TA}$, also written $\mathrm{Th}(\mathfrak{N})$, is the set of all sentences of the [[language of arithmetic|D8SD54M5PN]] $L_A$ that are true in $\mathfrak{N}$.
It is a [[complete theory|655K8Y7VS8]]: for every sentence $\sigma$, exactly one of $\sigma$ and $\neg \sigma$ belongs to it.
It is not definable in $\mathfrak{N}$ by any formula of $L_A$, by [[Tarski's undefinability theorem|YRV6SYK2BY]], so it lies above every level of the [[arithmetical hierarchy|7CVJCQKY41]].
Its [[Turing degree|P5N2ND3VCG]] is $\mathbf{0}^{(\omega)}$, the degree of the $\omega$-th [[Turing jump|60P2XWY5QX]] of the empty set.
In particular it is not [[recursively axiomatizable|3ANXZC3BEG]], which is a form of Gödel's [[first incompleteness theorem|X9WYNYE29C]].

## Motivation

A theory such as $\mathsf{PA}$ is a list of axioms, and it proves some of the true sentences.
True arithmetic is the target such theories aim at: it contains every true sentence, whether or not a proof system reaches it.
Comparing a theory with $\mathrm{TA}$ measures how incomplete it is.
The theorems of $\mathsf{PA}$ form a proper subset of $\mathrm{TA}$, and the difference contains $\mathrm{Con}(\mathsf{PA})$ and Goodstein's theorem.
In model theory, $\mathrm{TA}$ is the theory of the structures that look exactly like $\mathfrak{N}$ to first-order logic, the structures elementarily equivalent to $\mathfrak{N}$.

## Notation

We write $\mathrm{TA}$ or $\mathrm{Th}(\mathfrak{N})$; other books write $\mathrm{Th}(\mathbb{N}, 0, S, +, \cdot)$ or $\mathrm{Th}(\mathcal{N})$.
Via a [[Gödel numbering|MFJXPAF0R0]], $\mathrm{TA}$ is also the set of numbers below.

$$\{ \ulcorner \sigma \urcorner : \mathfrak{N} \models \sigma \} \subseteq \mathbb{N}$$

The set of true $\Sigma_n$ sentences is written $\mathrm{TA} \cap \Sigma_n$ or $\mathrm{Tr}_{\Sigma_n}$.

## Remarks

### Two true sentences that PA misses

Every theorem of $\mathsf{PA}$ belongs to $\mathrm{TA}$, because $\mathfrak{N}$ is a model of $\mathsf{PA}$.
The converse fails, and two sentences show it.

The first is $\mathrm{Con}(\mathsf{PA})$.
Every axiom of $\mathsf{PA}$ is true in $\mathfrak{N}$, so every theorem is true, and the false sentence $0 = S0$ is not a theorem.
So no number codes a proof of $0 = S0$, and $\mathrm{Con}(\mathsf{PA})$ holds in $\mathfrak{N}$, as [[the consistency example|EQR2AMD0GQ]] checks.
The second incompleteness theorem says that $\mathsf{PA}$ does not prove it.

The second is Goodstein's theorem, a $\Pi_2$ sentence about bases and subtraction with no mention of proofs.
It is true, by an argument with ordinals below $\varepsilon_0$, and Kirby and Paris showed in 1982 that $\mathsf{PA}$ does not prove it, as [[the Goodstein example|C2F2D75YSA]] explains.

[[True arithmetic taken as a set of axioms|9BW1F5B5GA]] gives a proof system whose theorems are exactly $\mathrm{TA}$, and it is not an effective formal system.

### What is not true arithmetic

Let $M$ be a model of $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$.
Its complete theory $\mathrm{Th}(M)$ contains the false sentence $\neg \mathrm{Con}(\mathsf{PA})$, so it is not $\mathrm{TA}$, by [[the model of the inconsistency statement|WZZ3VC4BVS]].
$\mathsf{PA}$ itself is not $\mathrm{TA}$, since it is incomplete and $\mathrm{TA}$ is complete.
[[Presburger arithmetic|4W0E9G7PPV]], the theory of $(\mathbb{N}, 0, S, +)$, is a complete theory of the natural numbers too.
It is not $\mathrm{TA}$: it lives in a smaller language without multiplication, and it is decidable.

### Basic properties

$\mathrm{TA}$ is consistent, because $\mathfrak{N}$ is a model of it.
It is complete, because each sentence is either true or false in $\mathfrak{N}$.
It is deductively closed: if $\mathrm{TA} \vdash \sigma$, then $\mathfrak{N} \models \sigma$ by [[soundness|4A84VHDTHV]], so $\sigma \in \mathrm{TA}$.

It is not recursively axiomatizable.
A recursive set of axioms with consequences $\mathrm{TA}$ would make $\mathrm{TA}$ computably enumerable.
A complete theory that is computably enumerable is decidable: to decide $\sigma$, enumerate theorems until $\sigma$ or $\neg \sigma$ appears.
But $\mathrm{TA}$ is not decidable, as the next remark shows.

### How complex truth is

No formula $\tau(x)$ of $L_A$ satisfies $\mathfrak{N} \models \tau(\ulcorner \sigma \urcorner) \leftrightarrow \sigma$ for all sentences $\sigma$, by Tarski's theorem.
So $\mathrm{TA}$ is not $\Sigma^0_n$ for any $n$.
Each piece is simpler.
For each $n \ge 1$, the set $\mathrm{TA} \cap \Sigma_n$ is $\Sigma^0_n$, and every $\Sigma^0_n$ set is many-one reducible to it.
Applying [[Post's theorem|NYJX5QXX1T]] uniformly in $n$ gives $\mathrm{TA} \equiv_T \emptyset^{(\omega)}$.

### Models of true arithmetic

Every model of $\mathrm{TA}$ is elementarily equivalent to $\mathfrak{N}$, and $\mathfrak{N}$ embeds in it as an initial segment.
By compactness, $\mathrm{TA}$ has [[nonstandard models|1QWN5CV4CG]].
It has $2^{\aleph_0}$ countable models up to isomorphism.
So a complete theory fixes which sentences are true, not which structure satisfies them.

### History

Gödel's incompleteness theorem of 1931 implies that no recursively axiomatized theory extending $\mathsf{Q}$ has exactly the theorems of $\mathrm{TA}$.
Tarski proved in the 1930s that arithmetic truth is not arithmetically definable.
Skolem gave the first construction of a nonstandard model of true arithmetic.

### Watch out

A complete theory need not be decidable.
Completeness together with a recursive axiomatization gives decidability, and $\mathrm{TA}$ has no recursive axiomatization.
Do not confuse $\mathrm{TA}$ with $\mathsf{PA}$ either: $\mathsf{PA}$ has a recursive set of axioms, while $\mathrm{TA}$ is a set of true sentences given by no effective rule.
A nonstandard model of $\mathsf{PA}$ may or may not satisfy $\mathrm{TA}$; the model of $\neg \mathrm{Con}(\mathsf{PA})$ above does not.

### Try it

Write the twin prime conjecture as a sentence $\tau$ of $L_A$, and decide which of $\tau$ and $\neg \tau$ lies in $\mathrm{TA}$.
Answer: one form is $\forall x \, \exists p \, (x < p \land \mathrm{Pr}(p) \land \mathrm{Pr}(p + \overline{2}))$, with $\mathrm{Pr}$ the $\Delta_0$ formula for primality, a $\Pi_2$ sentence.
Exactly one of $\tau$ and $\neg \tau$ lies in $\mathrm{TA}$, by completeness, but which one is an open problem.
Membership in $\mathrm{TA}$ is a fact about $\mathfrak{N}$, not something we can always compute.

## Explanations

### L1 human

True arithmetic is the collection of all statements about whole numbers that are true.
It contains easy facts such as $2 + 2 = 4$, deep theorems such as Fermat's last theorem, and statements no one has proved yet, if they are true.
Gödel showed that no computer-checkable list of axioms proves exactly these statements.
So true arithmetic is a well-defined collection that no proof system captures.

### L2 human

We see why $\mathrm{TA}$ climbs the whole arithmetical hierarchy.

1. The sentence $\exists x \, (x \cdot x = \overline{49})$ is $\Sigma_1$, and a search confirms it, here at $x = 7$.
2. A $\Pi_1$ sentence $\forall x \, \varphi(x)$ with $\varphi$ in $\Delta_0$ can be refuted by a search, but not confirmed by one.
3. A $\Sigma_2$ sentence $\exists x \, \forall y \, \varphi(x, y)$ needs the answers to infinitely many $\Pi_1$ questions.
4. Each extra quantifier alternation needs one more Turing jump, and deciding all of $\mathrm{TA}$ needs all finite jumps at once, which is $\emptyset^{(\omega)}$.

The typical use is as the strongest possible theory in $L_A$ when one asks whether a statement is "true but unprovable".
Watch out: "true" does not mean "true in every model of $\mathsf{PA}$".
The sentences true in every model of $\mathsf{PA}$ are the theorems of $\mathsf{PA}$, by the completeness theorem.

### L3 human

The second-order Peano axioms determine $\mathfrak{N}$ up to isomorphism, while its complete first-order theory $\mathrm{TA}$ has nonstandard models.
So $\mathrm{TA}$ shows exactly what first-order logic loses.
Its models are the models of arithmetic that are elementarily equivalent to $\mathfrak{N}$, and they are the usual setting for results on end extensions and on the structure of nonstandard models.
In computability theory, $\mathrm{TA}$ has degree $\mathbf{0}^{(\omega)}$, and the arithmetical sets are exactly the sets computable in some finite jump $\mathbf{0}^{(n)}$.
The theory of the standard model of second-order arithmetic is not definable in second-order arithmetic, by the same undefinability argument.
