---
tag: DX0KPMH4QZ
kind: concept
name: True arithmetic
aliases: [ta, theory-of-the-standard-model, complete-theory-of-arithmetic]
msc: ["03F30", "03F40"]
topics: [QHCRN4JVG0]
audience: grad
uses: [D8SD54M5PN, HACXBCM7SS, MFJXPAF0R0, 4A84VHDTHV, B66JYY3K58, 92SWXST1ZM, 655K8Y7VS8, YRV6SYK2BY, NYJX5QXX1T, 60P2XWY5QX, P5N2ND3VCG, 7CVJCQKY41, 3ANXZC3BEG, X9WYNYE29C, 1QWN5CV4CG]
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

True arithmetic $\mathrm{TA}$, also written $\mathrm{Th}(\mathfrak{N})$, is the set of all sentences of the [[language of arithmetic|D8SD54M5PN]] $L_A$ that are true in the standard model $\mathfrak{N}$.
It is a [[complete theory|655K8Y7VS8]]: for every sentence $\sigma$, exactly one of $\sigma$ and $\neg \sigma$ belongs to it.
It is not definable in $\mathfrak{N}$ by any formula of $L_A$, by [[Tarski's undefinability theorem|YRV6SYK2BY]], so it lies above every level of the [[arithmetical hierarchy|7CVJCQKY41]].
Its [[Turing degree|P5N2ND3VCG]] is $\mathbf{0}^{(\omega)}$, the degree of the $\omega$-th [[Turing jump|60P2XWY5QX]] of the empty set.
In particular it is not [[recursively axiomatizable|3ANXZC3BEG]], which is a form of Gödel's [[first incompleteness theorem|X9WYNYE29C]].

## Motivation

A theory such as [[Peano arithmetic|HACXBCM7SS]] is a list of axioms, and it proves some true sentences.
True arithmetic is the target that such theories aim at: it contains every true sentence, whether or not any proof system reaches it.
Comparing a theory with $\mathrm{TA}$ measures its incompleteness: $\mathsf{PA}$ is a proper subset of $\mathrm{TA}$, and the difference contains $\mathrm{Con}(\mathsf{PA})$ and Goodstein's theorem.
As a theory, $\mathrm{TA}$ is the natural object for model theory of arithmetic, since its models are exactly the structures elementarily equivalent to $\mathfrak{N}$.

## Notation

We write $\mathrm{TA}$ or $\mathrm{Th}(\mathfrak{N})$; other books write $\mathrm{Th}(\N, 0, S, +, \cdot)$ or $\mathrm{Th}(\mathcal{N})$.
Via a [[Gödel numbering|MFJXPAF0R0]], $\mathrm{TA}$ is also the set $\set{\ulcorner \sigma \urcorner : \mathfrak{N} \models \sigma} \subseteq \N$.
The intersection of $\mathrm{TA}$ with the $\Sigma_n$ sentences is written $\mathrm{TA} \cap \Sigma_n$ or $\mathrm{Tr}_{\Sigma_n}$.

## Remarks

### Examples

- Every theorem of $\mathsf{PA}$ belongs to $\mathrm{TA}$, because $\mathfrak{N}$ is a model of $\mathsf{PA}$.
- Goodstein's theorem belongs to $\mathrm{TA}$ but is not a theorem of $\mathsf{PA}$; [[this example|C2F2D75YSA]] explains both facts.
- $\mathrm{Con}(\mathsf{PA})$ belongs to $\mathrm{TA}$; [[this example|EQR2AMD0GQ]] checks it.
- [[True arithmetic taken as a set of axioms|9BW1F5B5GA]] gives a proof system whose theorems are exactly $\mathrm{TA}$, and shows that it is not an effective formal system.

### Non-examples

- For a model $M$ of $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$, the complete theory $\mathrm{Th}(M)$ is not $\mathrm{TA}$; [[this non-example|WZZ3VC4BVS]] gives the argument.
- $\mathsf{PA}$ is not $\mathrm{TA}$: it is incomplete, while $\mathrm{TA}$ is complete.
- The theory of $(\N, 0, S, +)$, [[Presburger arithmetic|B66JYY3K58]], is a complete theory of the natural numbers, but it is decidable and in a smaller language; it is not $\mathrm{TA}$.

### Basic properties

- Consistent and complete. $\mathfrak{N}$ is a model, so $\mathrm{TA}$ is consistent; each $\sigma$ is true or false in $\mathfrak{N}$, so $\mathrm{TA}$ is complete.
- Deductively closed. If $\mathrm{TA} \vdash \sigma$, then $\mathfrak{N} \models \sigma$ by [[soundness|4A84VHDTHV]], so $\sigma \in \mathrm{TA}$.
- Undefinability. No formula $\tau(x)$ of $L_A$ satisfies $\mathfrak{N} \models \tau(\ulcorner \sigma \urcorner) \leftrightarrow \sigma$ for all sentences $\sigma$. So $\mathrm{TA}$ is not $\Sigma^0_n$ for any $n$.
- Partial truth. For each $n \ge 1$, the set $\mathrm{TA} \cap \Sigma_n$ is $\Sigma^0_n$, and it is complete for $\Sigma^0_n$ sets under many-one reduction.
- Degree. By [[Post's theorem|NYJX5QXX1T]], applied uniformly in $n$, $\mathrm{TA} \equiv_T \emptyset^{(\omega)}$.
- Not recursively axiomatizable. A recursive axiom set $A$ with consequences $\mathrm{TA}$ would make $\mathrm{TA}$ computably enumerable. A complete computably enumerable theory is decidable, and $\mathrm{TA}$ is not decidable.
- Models. Every model of $\mathrm{TA}$ is elementarily equivalent to $\mathfrak{N}$, and $\mathfrak{N}$ embeds as an initial segment. By compactness $\mathrm{TA}$ has [[nonstandard models|1QWN5CV4CG]]. It has $2^{\aleph_0}$ countable models up to isomorphism.

### History

Gödel's incompleteness theorem of 1931 implies that no recursively axiomatized theory extending $\mathsf{Q}$ has exactly the theorems of $\mathrm{TA}$.
Tarski proved that arithmetic truth is not arithmetically definable, which gives the undefinability property above.
Skolem gave the first construction of a nonstandard model of true arithmetic.

### Common errors

- To think that a complete theory is decidable. Completeness plus a recursive axiomatization gives decidability; $\mathrm{TA}$ has no recursive axiomatization.
- To confuse $\mathrm{TA}$ with $\mathsf{PA}$. $\mathsf{PA}$ is a recursive set of axioms; $\mathrm{TA}$ is a set of true sentences, not given by any effective rule.
- To think that every model of $\mathrm{TA}$ is $\mathfrak{N}$. Completeness fixes the sentences, not the model; nonstandard models of $\mathrm{TA}$ exist.
- To think that a nonstandard model of $\mathsf{PA}$ must satisfy $\mathrm{TA}$. Some do and some do not, as the non-example shows.

## Explanations

### L1 human

True arithmetic is the collection of all statements about whole numbers that are true.
It contains easy facts such as $2 + 2 = 4$, deep theorems such as Fermat's last theorem, and statements no one has proved yet, if they are true.
Gödel showed that no computer-checkable list of axioms proves exactly these statements.
So true arithmetic is a well-defined collection that no proof system captures.

### L2 human

We see why $\mathrm{TA}$ climbs the whole arithmetical hierarchy.

1. The sentence $\exists x \, (x \cdot x = \overline{49})$ is $\Sigma_1$; its truth can be confirmed by a search, here at $x = 7$.
2. A $\Pi_1$ sentence $\forall x \, \varphi(x)$ with $\varphi$ in $\Delta_0$ can be refuted by a search, but not confirmed by one.
3. A $\Sigma_2$ sentence $\exists x \, \forall y \, \varphi(x, y)$ needs the answers to infinitely many $\Pi_1$ questions.
4. Each extra quantifier alternation needs one more Turing jump. Deciding all of $\mathrm{TA}$ needs all finite jumps at once, which is $\emptyset^{(\omega)}$.

The typical use is as the strongest possible theory in $L_A$ when one asks whether a statement is "true but unprovable".
A trap is to identify "true" with "true in every model of $\mathsf{PA}$"; the second notion gives the theorems of $\mathsf{PA}$, by the completeness theorem.

### L3 human

The second-order Peano axioms determine $\mathfrak{N}$ up to isomorphism, while its complete first-order theory $\mathrm{TA}$ has nonstandard models.
So $\mathrm{TA}$ shows exactly what first-order logic loses.
Its models are the models of arithmetic that are elementarily equivalent to $\mathfrak{N}$, and they are the usual setting for results on end extensions and on the structure of nonstandard models.
In computability theory, $\mathrm{TA}$ has degree $\mathbf{0}^{(\omega)}$, and the arithmetical sets are exactly the sets computable in some finite jump $\mathbf{0}^{(n)}$.
The second-order analogue, the theory of the standard model of second-order arithmetic, is not definable in second-order arithmetic, by the same undefinability argument.
