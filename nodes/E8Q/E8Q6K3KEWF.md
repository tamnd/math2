---
tag: E8Q6K3KEWF
kind: proof
name: Proof of Takeuti's conjecture by semi-valuations
msc: ["03F05", "03B15"]
topics: [XTTKZTYDSD]
audience: research
proves: W560YMCPA3
methods: [0BB5TPGQ1N, 0ASJVEFA9J]
uses: [W72CA3R9MP, H31CS3HK5P, AYRZ98Y0NW, WGWBBVE8GX, AVD7T7J063, SVNYKTGQ48]
sources:
  - url: https://en.wikipedia.org/wiki/Takeuti%27s_conjecture
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Method_of_analytic_tableaux
    locator: lead section
---

## Proof

We prove the contrapositive: if $\Gamma \vdash \Delta$ has no cut-free derivation in $\mathrm{LK}^2$, then it has no derivation at all, and we cite one lemma, the extension of semi-valuations.

### Setup

We use the calculus $\mathrm{LK}^2$ and the abstracts of the [[statement|W560YMCPA3]].
We take $\neg$, $\to$, $\forall x$ and $\forall X$ as the logical symbols, and the other symbols are abbreviations.
Formulas may contain free variables.

A *semi-valuation* is a partial map $V$ from formulas to $\{ \mathrm{t}, \mathrm{f} \}$ with the following conditions.
If $V(\neg A) = \mathrm{t}$ then $V(A) = \mathrm{f}$, and if $V(\neg A) = \mathrm{f}$ then $V(A) = \mathrm{t}$.
If $V(A \to B) = \mathrm{t}$ then $V(A) = \mathrm{f}$ or $V(B) = \mathrm{t}$, and if $V(A \to B) = \mathrm{f}$ then $V(A) = \mathrm{t}$ and $V(B) = \mathrm{f}$.
If $V(\forall x \, A) = \mathrm{t}$ then $V(A[s/x]) = \mathrm{t}$ for every term $s$, and if $V(\forall x \, A) = \mathrm{f}$ then $V(A[y/x]) = \mathrm{f}$ for some variable $y$.
If $V(\forall X \, A) = \mathrm{t}$ then $V(A[T/X]) = \mathrm{t}$ for every abstract $T$, and if $V(\forall X \, A) = \mathrm{f}$ then $V(A[Y/X]) = \mathrm{f}$ for some variable $Y$.

A *valuation* is a semi-valuation that is defined on every formula, like a [[truth valuation|H31CS3HK5P]] of propositional logic.
A sequent $\Gamma' \vdash \Delta'$ is *true under* $W$ if $W(C) = \mathrm{f}$ for some $C$ in $\Gamma'$ or $W(D) = \mathrm{t}$ for some $D$ in $\Delta'$.
A *substitution* $\sigma$ replaces the free first-order variables by terms and the free second-order variables by abstracts.

### A failed search gives a semi-valuation

1. Assume that $\Gamma \vdash \Delta$ has no cut-free derivation.
2. Build the search tree of $\Gamma \vdash \Delta$, as for [[analytic tableaux|WGWBBVE8GX]], with root $\Gamma \vdash \Delta$.
   Above each sequent, apply one cut-free rule backwards, in a fixed fair order, and keep the principal formula in the premise, so that each formula stays in all later sequents of the branch.
3. Fairness means that each formula on a branch is treated infinitely often.
   Each time a formula $\forall X \, A$ on the left is treated, the next abstract in a fixed list of all abstracts is used, and first-order terms are used in the same way, while on the right a new variable is used.
4. A branch stops when its last sequent has a formula on both sides, since such a sequent has a cut-free derivation from an axiom $A \vdash A$ by weakening.
5. If every branch stops, the tree is finite by König's lemma, because each sequent has at most two premises.
   Then the tree is a cut-free derivation of $\Gamma \vdash \Delta$, against step 1.
6. So some branch $B$ never stops.
   Define $V(A) = \mathrm{t}$ when $A$ is on the left of a sequent of $B$, and $V(A) = \mathrm{f}$ when $A$ is on the right of a sequent of $B$.
7. The map $V$ is well defined: if $A$ were on the left of one sequent and on the right of another, both occurrences would be in the later sequent, by step 2, and $B$ would stop, by step 4.
8. The map $V$ is a semi-valuation, by fairness.
   For example, if $\forall X \, A$ is on the left of $B$, then for each abstract $T$ the formula $A[T/X]$ appears on the left of a later sequent of $B$.
9. Extension lemma (cited: Tait 1966 for second-order logic, after Schütte; Takahashi 1967 and Prawitz 1968 for higher-order logic): every semi-valuation $V$ extends to a valuation $W$.
   We do not reprove this lemma, which is the non-constructive part of the proof.

### Every derivable sequent is true under the valuation

10. Claim: for every derivable sequent $\Gamma' \vdash \Delta'$ of $\mathrm{LK}^2$, with or without cut, and every substitution $\sigma$, the sequent $\sigma\Gamma' \vdash \sigma\Delta'$ is true under $W$.
    We prove it by induction on the derivation, in steps 11 to 15.
11. An axiom $A \vdash A$ is true, because $W(\sigma A)$ is $\mathrm{t}$ or $\mathrm{f}$.
    The structural rules keep truth, because they only add, copy or move formulas.
12. Cut has premises $\Gamma_1 \vdash \Delta_1, A$ and $A, \Gamma_2 \vdash \Delta_2$.
    If $W(\sigma A) = \mathrm{t}$, the second premise is true through a formula of $\sigma\Gamma_2$ or $\sigma\Delta_2$, and if $W(\sigma A) = \mathrm{f}$, the first premise is true through a formula of $\sigma\Gamma_1$ or $\sigma\Delta_1$, so the conclusion is true.
13. The propositional rules and the rules for $\forall x$ follow from the conditions on $W$, as in the [[soundness theorem|AVD7T7J063]].
    Since $W$ is total, each condition is an equivalence: for example, if all $W(A[T/X])$ are $\mathrm{t}$, then $W(\forall X \, A) = \mathrm{f}$ is impossible, so $W(\forall X \, A) = \mathrm{t}$.
14. For $(\forall^2 \mathrm{L})$, if the premise is true through $\sigma(A[T/X]) = (\sigma A)[\sigma T/X]$, this formula is false.
    Then $W(\sigma \forall X \, A) = \mathrm{f}$ by the condition for $\forall X$, and the conclusion is true.
15. For $(\forall^2 \mathrm{R})$ with the variable $Y$, assume that the conclusion is false under $\sigma$, let $T$ be any abstract, and let $\sigma'$ be $\sigma$ with $Y \mapsto T$.
    Since $Y$ is not free in $\Gamma'$, $\Delta'$ or $\forall X \, A$, the premise under $\sigma'$ is true only through $(\sigma A)[T/X]$.
    So $W((\sigma A)[T/X]) = \mathrm{t}$ for every $T$, and $W(\sigma \forall X \, A) = \mathrm{t}$ by step 13, against the assumption.

### The end of the proof

16. Apply the claim to $\Gamma \vdash \Delta$ with the identity substitution.
    By step 6, every formula of $\Gamma$ has $V$-value $\mathrm{t}$ and every formula of $\Delta$ has $V$-value $\mathrm{f}$, because $\Gamma \vdash \Delta$ is the first sequent of $B$.
    Since $W$ extends $V$, the sequent $\Gamma \vdash \Delta$ is not true under $W$.
17. So $\Gamma \vdash \Delta$ has no derivation in $\mathrm{LK}^2$, by step 10.
    This proves the contrapositive, so every derivable sequent has a cut-free derivation.

## Idea

A failed search for a cut-free proof leaves an infinite branch, and the branch describes a partial counter-model.
The cited extension lemma completes it to a total valuation that respects all instances of comprehension.
Every rule of $\mathrm{LK}^2$, including cut, is sound for such a valuation, so the sequent cannot have any derivation.
All the strength of the theorem lies in the extension lemma.

## Variants

Girard's proof uses strong normalization of [[System F|SVNYKTGQ48]] with reducibility candidates.
It works on natural deduction for second-order intuitionistic logic, and the candidates quantify over sets of terms in the same impredicative way as the valuations here.

Takeuti proved cut elimination for fragments of his calculus by syntactic reductions measured with ordinal diagrams, the method of his consistency proof for $\Pi^1_1$-comprehension.
Such proofs work only for fragments, because a full proof with an ordinal bound would need an ordinal analysis of second-order arithmetic.
