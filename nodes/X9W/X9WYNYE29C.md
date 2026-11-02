---
tag: X9WYNYE29C
kind: statement
role: theorem
name: Gödel's incompleteness theorems
msc: [03F40, 03F30]
uses: [3K1AKGXF8A, 0QFT7Z76N5, MFJXPAF0R0, 92SWXST1ZM, DKFGQTRYZE, TN9G24VABN, 655K8Y7VS8]
about: [92SWXST1ZM, 655K8Y7VS8]
sources:
  - url: https://en.wikipedia.org/wiki/Gödel's_incompleteness_theorems
same_as:
  wikidata: Q200787
  wikipedia: Gödel's incompleteness theorems
---

## Statement

Let $T$ be a consistent first-order [[theory|92SWXST1ZM]] in the language of arithmetic whose set of axioms is [[computably enumerable|TN9G24VABN]].

1. (First incompleteness theorem.) If $T$ contains [[Robinson arithmetic|3K1AKGXF8A]] $\mathsf{Q}$, then there is a [[sentence|DKFGQTRYZE]] $G$ such that $T \nvdash G$ and $T \nvdash \neg G$. So $T$ is not [[complete|655K8Y7VS8]].
2. (Second incompleteness theorem.) If $T$ contains the [[Peano axioms|0QFT7Z76N5]] $\mathsf{PA}$, then $T \nvdash \mathrm{Con}(T)$. Here $\mathrm{Prov}_T$ is the standard provability predicate of $T$ for a [[Gödel numbering|MFJXPAF0R0]], and $\mathrm{Con}(T)$ is $\neg \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$.

## Remarks

Proof idea for 1: by the [[diagonal lemma|3PRW76471J]] there is a sentence $G$ with $T \vdash G \leftrightarrow \neg \mathrm{Prov}_T(\ulcorner G \urcorner)$.
If $T \vdash G$, then $T \vdash \mathrm{Prov}_T(\ulcorner G \urcorner)$, and $T$ is inconsistent.
Gödel's argument that $T \nvdash \neg G$ used $\omega$-consistency; Rosser's variant of the sentence needs only consistency, which gives the form stated here.
Proof idea for 2: the argument for "if $T$ is consistent then $T \nvdash G$" can be carried out inside $T$, so $T \vdash \mathrm{Con}(T) \to G$; thus $T \vdash \mathrm{Con}(T)$ would give $T \vdash G$.

The hypotheses matter.
The theory of the true sentences of $\N$ is complete and consistent, but its axioms are not computably enumerable.
[[Presburger arithmetic|B66JYY3K58]], with addition but no multiplication, is consistent, computably axiomatized and complete.

## Explanations

### L1 human

The first theorem says that any reasonable list of axioms for arithmetic leaves some statements undecided: neither they nor their negations can be proved.
The second says that such a system cannot prove its own consistency.
So no single computer-checkable set of axioms captures all truths about the natural numbers.

### L2 human

The proofs turn statements about proofs into statements about numbers by a [[Gödel numbering|MFJXPAF0R0]], and then use the [[diagonal lemma|3PRW76471J]] to build a self-referential sentence.
The first theorem implies that every consistent computably axiomatized extension of $\mathsf{Q}$ is incomplete, and with more work that such theories are undecidable.
The second theorem ended the hope of Hilbert's program to prove the consistency of mathematics by finitary means within mathematics itself.
Concrete true statements unprovable in $\mathsf{PA}$ include [[Goodstein's theorem|XQMNJF241J]] and the [[Paris–Harrington theorem|509ZWA0R26]].
