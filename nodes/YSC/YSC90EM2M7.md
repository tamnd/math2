---
tag: YSC90EM2M7
kind: example
name: True arithmetic is not recursively axiomatizable
msc: ["03D35", "03F40"]
topics: [FBWW4J1XWG]
audience: grad
not_instance_of:
  - target: 3ANXZC3BEG
    note: true arithmetic is complete and consistent, and the first incompleteness theorem shows that no decidable set of sentences has exactly its theorems
uses: [3ANXZC3BEG, X9WYNYE29C, 3K1AKGXF8A, 655K8Y7VS8, TN9G24VABN, PPGD5KW8JC]
sources:
  - url: https://en.wikipedia.org/wiki/True_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: lead section
---

## Example

The set of all true sentences about $+$ and $\cdot$ on the natural numbers answers every question, but no computer-checkable list of axioms proves exactly these sentences.
Let $L_A = \{ 0, S, +, \cdot \}$ and $\mathfrak{N} = (\mathbb{N}, 0, S, +, \cdot)$.
True arithmetic is the theory $\mathrm{TA} = \operatorname{Th}(\mathfrak{N})$, the set of all $L_A$-sentences true in $\mathfrak{N}$.
We show that $\mathrm{TA}$ is not a [[recursively axiomatizable theory|3ANXZC3BEG]]: no decidable set $\Sigma$ of sentences has $\operatorname{Thm}(\Sigma) = \operatorname{Thm}(\mathrm{TA})$.

1. $\mathrm{TA}$ is closed under derivation.
   If $\mathrm{TA} \vdash \sigma$, then $\sigma$ is true in the model $\mathfrak{N}$ of $\mathrm{TA}$, by the [[soundness theorem|AVD7T7J063]].
   So $\operatorname{Thm}(\mathrm{TA}) = \mathrm{TA}$.
2. $\mathrm{TA}$ is [[complete|655K8Y7VS8]].
   For each sentence $\sigma$, either $\sigma$ or $\neg \sigma$ is true in $\mathfrak{N}$, so one of them lies in $\mathrm{TA}$.
3. Suppose, for a contradiction, that $\Sigma$ is a decidable set of sentences with $\operatorname{Thm}(\Sigma) = \mathrm{TA}$.
4. $\Sigma$ is consistent, because all its theorems are true in $\mathfrak{N}$, and a sentence and its negation are not both true there.
5. $\Sigma$ is [[computably enumerable|TN9G24VABN]], because every [[computable set|PPGD5KW8JC]] is computably enumerable.
6. $\Sigma$ proves every axiom of [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$, because each such axiom is true in $\mathfrak{N}$ and so lies in $\mathrm{TA} = \operatorname{Thm}(\Sigma)$.
7. By steps 4, 5 and 6, the [[first incompleteness theorem|X9WYNYE29C]] applies to $\Sigma$.
   It gives a sentence $G$ with $\Sigma \nvdash G$ and $\Sigma \nvdash \neg G$.
8. By step 2, $G$ or $\neg G$ lies in $\mathrm{TA} = \operatorname{Thm}(\Sigma)$, which contradicts step 7.
9. So no such $\Sigma$ exists, and $\mathrm{TA}$ is not recursively axiomatizable.

## Remarks

Completeness alone does not make a theory decidable.
A complete theory is decidable when it is also recursively axiomatizable, and $\mathrm{TA}$ is not.

$\mathrm{TA}$ is not even computably enumerable.
If it were, [[Craig's theorem on axiomatizability|6AN62NQ8AN]] would give it a decidable set of axioms, against step 9.
By [[Tarski's undefinability theorem|YRV6SYK2BY]], $\mathrm{TA}$ is not even definable by a formula of $L_A$.

The picture changes when we drop multiplication.
The theory of $(\mathbb{N}, 0, 1, +)$ is [[Presburger arithmetic|4W0E9G7PPV]], which is complete, recursively axiomatizable and decidable.
The incompleteness theorem does not apply there, because the axioms of $\mathsf{Q}$ mention multiplication.

The example [[true arithmetic taken as a set of axioms|9BW1F5B5GA]] uses the same argument to show that $\mathrm{TA}$ itself is not a decidable set.
The result here is stronger: no decidable set at all has the same theorems as $\mathrm{TA}$.

## Explanations

### L1 human

True arithmetic is the collection of all true statements about whole numbers with addition and multiplication.
It answers every question, since for each statement either it or its opposite is true.
One might hope for a list of axioms, checkable by a computer, from which exactly these true statements follow.
Gödel's theorem says that this is impossible: every checkable list that proves only true statements leaves some true statement unproved.

### L2 human

We compare true arithmetic with the axioms of [[Peano arithmetic|4HDC97G2E9]].
The axioms of $\mathsf{PA}$ are true in $\mathfrak{N}$, so $\operatorname{Thm}(\mathsf{PA}) \subseteq \mathrm{TA}$.
The axioms of $\mathsf{PA}$ form a decidable set, so steps 4 to 7 apply to $\Sigma = \mathsf{PA}$ and give a sentence $G$ that $\mathsf{PA}$ neither proves nor refutes.
One of $G$ and $\neg G$ is true in $\mathfrak{N}$, so it lies in $\mathrm{TA}$ but not in $\operatorname{Thm}(\mathsf{PA})$.
So $\operatorname{Thm}(\mathsf{PA})$ is a proper subset of $\mathrm{TA}$.
If we add the missing sentence to $\mathsf{PA}$, we get a new decidable axiom set, and the argument starts again with a new sentence.

The typical use is to separate two properties of a theory: completeness and recursive axiomatizability.
Watch out: the result does not say that some sentences of $\mathrm{TA}$ have no proof from $\mathrm{TA}$, since each one is its own proof; it says that $\mathrm{TA}$ is not a decidable set of axioms and has no decidable replacement.
