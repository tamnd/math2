---
tag: ST0ZHXSKFG
kind: proof
name: Proof of the truth lemma for canonical models
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
proves: NM4CB7QAYT
uses: [JS8W7PA6JK, TVE4F04KME, NGHWZ9Y7ZV, SC0BSJ3GT6, 12MQ2NJ29A, 0ASJVEFA9J]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Canonical models
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds, chapter on completeness and canonical models
---

## Proof

We prove the five parts of [[the truth lemma|NM4CB7QAYT]] in order: first we build worlds, then successors, and then we check truth by induction on formulas.

We use three facts about a maximal $\Lambda$-consistent set $\Gamma$, each of which follows from consistency and maximality.
First, $\Lambda \subseteq \Gamma$.
Second, for each $\varphi$, exactly one of $\varphi$ and $\neg\varphi$ lies in $\Gamma$.
Third, $\Gamma$ is closed under modus ponens.
Together they give $\varphi \to \psi \in \Gamma$ if and only if $\varphi \notin \Gamma$ or $\psi \in \Gamma$.

### Part 1: Lindenbaum's lemma

1. The language is countable, so we list all formulas as $\psi_0, \psi_1, \psi_2, \dots$.
   Let $\Gamma$ be $\Lambda$-consistent and put $\Gamma_0 = \Gamma$.
2. Put $\Gamma_{n+1} = \Gamma_n \cup \{ \psi_n \}$ if this set is $\Lambda$-consistent, and $\Gamma_{n+1} = \Gamma_n \cup \{ \neg\psi_n \}$ otherwise.
3. Each $\Gamma_{n+1}$ is consistent, by [[induction|0ASJVEFA9J]] on $n$.
   If both choices were inconsistent, there would be conjunctions $\alpha$ and $\beta$ of members of $\Gamma_n$ with $\Lambda \vdash \neg(\alpha \wedge \psi_n)$ and $\Lambda \vdash \neg(\beta \wedge \neg\psi_n)$.
   These two theorems give $\Lambda \vdash \neg(\alpha \wedge \beta)$ by propositional logic, so $\Gamma_n$ would be inconsistent.
4. Let $\Gamma^+ = \bigcup_n \Gamma_n$.
   A finite subset of $\Gamma^+$ lies in some $\Gamma_n$, so $\Gamma^+$ is consistent.
5. For each $n$, one of $\psi_n$ and $\neg\psi_n$ lies in $\Gamma^+$, so no proper extension of $\Gamma^+$ is consistent.
   So $\Gamma^+$ is maximal consistent and contains $\Gamma$.

### Part 2: the box lemma

6. Let $\{ \varphi : \square\varphi \in \Gamma \} \subseteq \Delta$ and $\varphi \in \Delta$, and suppose that $\lozenge\varphi \notin \Gamma$.
   Then $\neg\lozenge\varphi \in \Gamma$, and $\Lambda \vdash \neg\lozenge\varphi \to \square\neg\varphi$ by the duality of [[K|JS8W7PA6JK]].
7. So $\square\neg\varphi \in \Gamma$, hence $\neg\varphi \in \Delta$, which contradicts $\varphi \in \Delta$ and the consistency of $\Delta$.
   So $\lozenge\varphi \in \Gamma$.
8. Conversely, let $\{ \lozenge\varphi : \varphi \in \Delta \} \subseteq \Gamma$ and $\square\varphi \in \Gamma$, and suppose that $\varphi \notin \Delta$.
   Then $\neg\varphi \in \Delta$, so $\lozenge\neg\varphi \in \Gamma$.
9. By duality, $\lozenge\neg\varphi$ is equivalent in $\Lambda$ to $\neg\square\varphi$, so $\neg\square\varphi \in \Gamma$, which contradicts $\square\varphi \in \Gamma$.
   So $\varphi \in \Delta$.

### Part 3: the existence lemma

10. Let $\lozenge\varphi \in \Gamma$ and put $\Delta_0 = \{ \varphi \} \cup \{ \psi : \square\psi \in \Gamma \}$.
    We show that $\Delta_0$ is $\Lambda$-consistent.
11. If it is not, there are $\psi_1, \dots, \psi_n$ with $\square\psi_i \in \Gamma$ and $\Lambda \vdash (\psi_1 \wedge \dots \wedge \psi_n) \to \neg\varphi$.
12. Necessitation and axiom $\mathrm{K}$ of the normal logic $\Lambda$ give $\Lambda \vdash (\square\psi_1 \wedge \dots \wedge \square\psi_n) \to \square\neg\varphi$.
    This is the one step that uses normality.
    Since $\Gamma$ contains each $\square\psi_i$ and all of $\Lambda$, it contains $\square\neg\varphi$.
13. But $\square\neg\varphi$ is equivalent in $\Lambda$ to $\neg\lozenge\varphi$, and $\lozenge\varphi \in \Gamma$, so $\Gamma$ would be inconsistent.
14. By part 1, $\Delta_0$ extends to a maximal consistent $\Delta$.
    Then $\varphi \in \Delta$ and $\{ \psi : \square\psi \in \Gamma \} \subseteq \Delta$, that is, $\Gamma R^\Lambda \Delta$.

### Part 4: the truth lemma

15. We use [[structural induction|12MQ2NJ29A]] on $\varphi$, for all $\Gamma$ at once.
    For a variable $p$, $\Gamma \models p$ holds iff $\Gamma \in V^\Lambda(p)$ iff $p \in \Gamma$, by the definition of $V^\Lambda$.
16. For $\bot$, the formula is false at $\Gamma$, and $\bot \notin \Gamma$ since $\Gamma$ is consistent.
17. For $\varphi \to \psi$, $\Gamma \models \varphi \to \psi$ holds iff $\varphi \notin \Gamma$ or $\psi \in \Gamma$, by the induction hypothesis, iff $\varphi \to \psi \in \Gamma$, by the facts above.
18. For $\square\varphi$, let first $\square\varphi \in \Gamma$ and $\Gamma R^\Lambda \Delta$.
    Then $\varphi \in \Delta$ by the definition of $R^\Lambda$, so $\Delta \models \varphi$ by the induction hypothesis, and $\Gamma \models \square\varphi$.
19. Now let $\square\varphi \notin \Gamma$.
    Then $\neg\square\varphi \in \Gamma$, so $\lozenge\neg\varphi \in \Gamma$ by duality.
20. Part 3 gives $\Delta$ with $\Gamma R^\Lambda \Delta$ and $\neg\varphi \in \Delta$.
    Then $\varphi \notin \Delta$, so $\Delta \not\models \varphi$ by the induction hypothesis, and $\Gamma \not\models \square\varphi$.

### Part 5: the canonical model theorem

21. Let $\Sigma$ be $\Lambda$-consistent.
    By part 1 it lies in some $\Gamma \in W^\Lambda$, and by part 4 every member of $\Sigma$ is true at $\Gamma$.
22. If $\Lambda \vdash \varphi$, then $\varphi$ lies in every maximal consistent set, so $\varphi$ is true in $\mathfrak{M}^\Lambda$ by part 4.
    If $\Lambda \nvdash \varphi$, then $\{ \neg\varphi \}$ is consistent, so $\varphi$ is false at some world by step 21.

## Idea

Lindenbaum's lemma makes worlds, and the existence lemma makes successors.
The existence lemma is the one place where the modal axioms enter: necessitation and axiom $\mathrm{K}$ turn an inconsistency below the box into an inconsistency at $\Gamma$.
The truth lemma is then an induction on formulas, and its box case calls the existence lemma.

## Variants

For an uncountable set of variables, part 1 uses [[Zorn's lemma|04RXTQA5ZA]] on the consistent supersets of $\Gamma$ instead of an enumeration.

If all sets are restricted to a finite set $\Sigma$ closed under subformulas and single negations, the same steps give a finite model, which is a form of [[filtration|6ZZSHAKG5F]].

In the algebraic proof, part 1 is the ultrafilter theorem for the Lindenbaum algebra, and part 3 represents the operator $\lozenge$ of that algebra by a relation.
