---
tag: ~c2ea41cc
kind: proof
name: Proof of Gödel's completeness theorem from the model existence theorem
msc: ["03B10", "03C07"]
topics: [FBWW4J1XWG]
audience: ug2
proves: WQ1ZE255SF
uses: [G0DTR159RN, ~bc83b0fa, ~65534b28, ~331f6430, DKFGQTRYZE, MVCH6N9SNW, 2RBQPV02AS]
methods: [0J0XBKG64S, 0BB5TPGQ1N]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem
    locator: Model existence theorem
  - book: isbn:9780122384523
    locator: Section 2.5
  - url: https://builds.openlogicproject.org/
    locator: The Completeness Theorem
---

## Proof

We use the [[model existence theorem|G0DTR159RN]], proved by the [[Henkin construction|~65534b28]], and fact (P5) of the [[enumeration proof of Lindenbaum's lemma|~bc83b0fa]].

Strong form.

1. Let $\Gamma$ be a set of [[sentences|DKFGQTRYZE]] and $\varphi$ a sentence, with $\Gamma \models \varphi$.
2. Suppose that $\Gamma \cup \set{\neg \varphi}$ is consistent.
3. The model existence theorem gives a [[model|MVCH6N9SNW]] $\mathcal{A}$ of $\Gamma \cup \set{\neg \varphi}$.
4. $\mathcal{A}$ is a model of $\Gamma$, so $\mathcal{A} \models \varphi$ by step 1.
5. Also $\mathcal{A} \models \neg \varphi$, so $\mathcal{A} \not\models \varphi$ by the clause for $\neg$. This contradicts step 4.
6. Hence $\Gamma \cup \set{\neg \varphi}$ is inconsistent.
7. By (P5), $\Gamma \vdash \varphi$. This proves the strong form.

Weak form.

8. A valid sentence $\varphi$ satisfies $\emptyset \models \varphi$. Step 7 with $\Gamma = \emptyset$ gives $\vdash \varphi$.

Formulas with free variables.

9. Let $\Gamma$ be a set of sentences and $\varphi$ a formula with free variables $x_1, \dots, x_k$, with $\Gamma \models \varphi$.
10. Let $\mathcal{A}$ be a model of $\Gamma$. By step 9, $\mathcal{A} \models \varphi[s]$ for every assignment $s$. By the clause for $\forall$, $\mathcal{A} \models \forall x_1 \cdots \forall x_k \, \varphi$.
11. So $\Gamma \models \forall x_1 \cdots \forall x_k \, \varphi$, and step 7 gives $\Gamma \vdash \forall x_1 \cdots \forall x_k \, \varphi$.
12. Each $x_i$ is substitutable for itself, so $\forall x_i \, \alpha \to \alpha$ is an axiom of group 2. With MP $k$ times, $\Gamma \vdash \varphi$.

## Idea

Completeness says that a sentence that is not provable is not a consequence.
If $\Gamma \nvdash \varphi$, then $\Gamma$ together with $\neg \varphi$ is consistent, and a consistent set has a model.
That model satisfies $\Gamma$ and fails $\varphi$, so $\varphi$ is not a consequence of $\Gamma$.
All the work lies in the model existence theorem.

## Variants

- [[Gödel's original proof|~5f72fbfc]] reduces to prenex sentences of the form $\forall \bar x \, \exists \bar y \, \psi$ and uses propositional completeness with a compactness argument.
- Tableau proof: build a systematic tableau for $\Gamma \cup \set{\neg \varphi}$. If it does not close, an infinite open branch is a Hintikka set, and its terms form a model. If it closes, the closed tableau is a derivation.
- Algebraic proof: Rasiowa and Sikorski find an ultrafilter of the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] that respects the infinite joins which the quantifiers define, for a countable language.
- For the cut-free [[sequent calculus|W72CA3R9MP]], a failed proof search gives a countermodel. This proves completeness without cut, and so [[cut elimination|AYRZ98Y0NW]].
