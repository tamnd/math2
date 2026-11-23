---
tag: DFP1N4WTF9
kind: proof
name: Proof of the compactness theorem from the completeness theorem
msc: ["03C07", "03B10"]
topics: [FBWW4J1XWG]
audience: ug2
proves: 1NR3HAWG9D
uses: [G0DTR159RN, WQ1ZE255SF, AVD7T7J063, DCR0S91GYY, VM8TQ70CVJ, QN7M1JCGT9, MVCH6N9SNW]
methods: [0J0XBKG64S, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: Proofs
  - book: isbn:9780122384523
    locator: Section 2.5
---

## Proof

We use that a derivation is finite, so a contradiction derived from $\Gamma$ uses only finitely many members of $\Gamma$.
Derivability $\vdash$ is in the Hilbert system $H$ of the [[soundness theorem|AVD7T7J063]].
A set is [[consistent|VM8TQ70CVJ]] when it derives no pair $\psi$, $\neg \psi$.

**Parts 1 and 3.**

1. Let $\Gamma$ be [[satisfiable|QN7M1JCGT9]], with a [[model|MVCH6N9SNW]] $\mathcal{A}$.
   Every finite $\Gamma_0 \subseteq \Gamma$ has the model $\mathcal{A}$, so $\Gamma$ is finitely satisfiable.
2. Conversely, let $\Gamma$ be finitely satisfiable, and suppose that $\Gamma$ is not consistent.
   Then $\Gamma \vdash \psi$ and $\Gamma \vdash \neg \psi$ for some formula $\psi$.
3. The two derivations are finite lists, so together they use a finite set $\Gamma_0 \subseteq \Gamma$.
   Then $\Gamma_0 \vdash \psi$ and $\Gamma_0 \vdash \neg \psi$, so $\Gamma_0$ is inconsistent.
4. The set $\Gamma_0$ has a model, by the hypothesis of step 2.
   By the soundness theorem, a set with a model is consistent, so $\Gamma_0$ is consistent.
   This contradicts step 3.
5. So $\Gamma$ is consistent.
   The [[model existence theorem|G0DTR159RN]] gives a model of $\Gamma$ with at most $|L| + \aleph_0$ elements.
   This proves parts 1 and 3.

**Part 2.**

6. If $\Gamma_0 \subseteq \Gamma$ and $\Gamma_0 \models \varphi$, then every model of $\Gamma$ is a model of $\Gamma_0$, so it satisfies $\varphi$.
   Hence $\Gamma \models \varphi$.
7. Conversely, let $\Gamma \models \varphi$.
   By [[Gödel's completeness theorem|WQ1ZE255SF]], $\Gamma \vdash \varphi$.
8. The derivation uses a finite $\Gamma_0 \subseteq \Gamma$, so $\Gamma_0 \vdash \varphi$.
   By the soundness theorem, $\Gamma_0 \models \varphi$.

## Idea

A proof is a finite object, so it can only cite finitely many hypotheses.
If every finite part of $\Gamma$ has a model, soundness says that no finite part is contradictory, and so $\Gamma$ itself is not contradictory.
The model existence theorem then turns "not contradictory" into "has a model".
All the hard work is inside the model existence theorem; compactness is the short corollary.

## Variants

Part 2 also follows from part 1 with no further proof theory.
We have $\Gamma \models \varphi$ if and only if $\Gamma \cup \{ \neg \varphi \}$ has no model.
Apply part 1 to $\Gamma \cup \{ \neg \varphi \}$: it has no model exactly when some finite part $\Gamma_0 \cup \{ \neg \varphi \}$ has no model, that is, when $\Gamma_0 \models \varphi$.

The [[proof by ultraproducts|22TWAHBVWT]] avoids proof systems, but it gives no bound on the size of the model.
For a countable $L$, the present proof needs no axiom of choice, because the model existence theorem for countable $L$ builds its maximal consistent set by the [[enumeration proof of Lindenbaum's lemma|DCR0S91GYY]].
