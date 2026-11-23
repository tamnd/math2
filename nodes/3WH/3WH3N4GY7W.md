---
tag: 3WH3N4GY7W
kind: proof
name: Proof of the Gödel-Gentzen translation theorem
msc: ["03F25", "03F55", "03B20"]
topics: [8XY7JYZKFW]
audience: grad
proves: WC4TDGEWZR
uses: [QEZR7PZ2DD, PAQ4ZX2TX1, NCDZ969V7X, RXHJPVMPJH, 0QFT7Z76N5]
methods: [12MQ2NJ29A, 0WCP0PVET6, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: First-order logic
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: Results
  - book: isbn:9781447145578
---

## Proof

We show that every translated formula is stable under $\neg \neg$, and then translate an NK derivation rule by rule into an NJ derivation.
We use the rules of [[natural deduction|PAQ4ZX2TX1]] and the clauses of the [[negative translation|QEZR7PZ2DD]] $A \mapsto A^N$.
Recall that $\neg B$ is $B \to \bot$, and that NJ is NK without RAA.

### Lemma 1: substitution

1. The formulas $A$ and $A^N$ have the same free variables, since each clause adds only $\neg$, $\wedge$ and $\bot$.
2. The clauses add no quantifiers, so a term $t$ is substitutable for $x$ in $A^N$ whenever it is substitutable for $x$ in $A$.
3. We have $(A[t/x])^N = A^N[t/x]$, by induction on $A$, because each clause commutes with [[substitution|NCDZ969V7X]].

### Lemma 2: two facts of NJ

1. Fact (a): $\vdash_i \neg \neg \neg B \to \neg B$.
   Assume $\neg \neg \neg B$ and $B$.
2. Under the extra assumption $\neg B$, ${\to}\mathrm{E}$ with $B$ gives $\bot$, and ${\to}\mathrm{I}$ discharges $\neg B$ and gives $\neg \neg B$.
3. Then ${\to}\mathrm{E}$ with $\neg \neg \neg B$ gives $\bot$, and ${\to}\mathrm{I}$ discharges $B$ and gives $\neg B$.
4. Fact (b): if $\vdash_i X \to Y$, then $\vdash_i \neg \neg X \to \neg \neg Y$.
   Assume $\neg \neg X$ and $\neg Y$.
5. Under the extra assumption $X$, the derivation of $X \to Y$ gives $Y$, and $\neg Y$ gives $\bot$.
6. The rule ${\to}\mathrm{I}$ discharges $X$ and gives $\neg X$, and $\neg \neg X$ then gives $\bot$.
7. The rule ${\to}\mathrm{I}$ discharges $\neg Y$ and gives $\neg \neg Y$, and a last ${\to}\mathrm{I}$ discharges $\neg \neg X$.

### Lemma 3: stability

For every formula $A$ we show $\vdash_i \neg \neg A^N \to A^N$, by induction on $A$.

1. Case $\bot$: assume $\neg \neg \bot$.
   The derivation $[\bot]^u$ followed by ${\to}\mathrm{I}^u$ gives $\neg \bot$, so ${\to}\mathrm{E}$ gives $\bot$.
2. Case $P$ atomic, $P \ne \bot$: $P^N = \neg \neg P$, and $\neg \neg \neg \neg P \to \neg \neg P$ is fact (a) with $B = \neg P$.
3. Cases $A \vee B$ and $\exists x\, A$: the translation has the form $\neg C$, and $\neg \neg \neg C \to \neg C$ is fact (a).
4. Case $A \wedge B$: ${\wedge}\mathrm{E}$ gives $\vdash_i A^N \wedge B^N \to A^N$, so fact (b) gives $\neg \neg (A^N \wedge B^N) \to \neg \neg A^N$.
   The induction hypothesis turns $\neg \neg A^N$ into $A^N$, in the same way we get $B^N$, and ${\wedge}\mathrm{I}$ gives $A^N \wedge B^N$.
5. Case $A \to B$: assume $\neg \neg (A^N \to B^N)$ and $A^N$, and also $\neg B^N$ and $A^N \to B^N$.
   Then ${\to}\mathrm{E}$ gives $B^N$, and $\neg B^N$ gives $\bot$.
6. Discharging $A^N \to B^N$ gives $\neg (A^N \to B^N)$, the first assumption gives $\bot$, and discharging $\neg B^N$ gives $\neg \neg B^N$.
   The induction hypothesis gives $B^N$, and ${\to}\mathrm{I}$ discharges $A^N$.
7. Case $\forall x\, A$: ${\forall}\mathrm{E}$ gives $\vdash_i \forall x\, A^N \to A^N$, so fact (b) gives $\neg \neg \forall x\, A^N \to \neg \neg A^N$.
8. Assume $\neg \neg \forall x\, A^N$, so the induction hypothesis gives $A^N$.
   The variable $x$ is not free in this only open assumption, so ${\forall}\mathrm{I}$ gives $\forall x\, A^N$.

### Main claim: the rules for the connectives

The claim is that if NK derives $A$ with open assumptions in $\Delta$, then NJ derives $A^N$ with open assumptions in $\Delta^N$.
We use induction on the NK derivation, with one case for its last rule.

1. An assumption $A$ becomes the one-node derivation $A^N$, with $A^N \in \Delta^N$.
2. For ${\wedge}\mathrm{I}$, ${\wedge}\mathrm{E}$, ${\to}\mathrm{I}$ and ${\to}\mathrm{E}$, the translation commutes with $\wedge$ and $\to$, so we apply the same rule to the translated derivations.
3. For ${\bot}\mathrm{E}$, induction gives a derivation of $\bot^N = \bot$, and ${\bot}\mathrm{E}$ in NJ gives $A^N$.
4. For RAA, the premise derives $\bot$ from $\Delta \cup \{ \neg A \}$, and $(\neg A)^N = \neg A^N$.
   Induction gives an NJ derivation of $\bot$ from $\Delta^N \cup \{ \neg A^N \}$, then ${\to}\mathrm{I}$ gives $\neg \neg A^N$, and Lemma 3 gives $A^N$.
5. For ${\vee}\mathrm{I}$ from $A$, induction gives $A^N$.
   Assume $\neg A^N \wedge \neg B^N$, so ${\wedge}\mathrm{E}$ gives $\neg A^N$ and ${\to}\mathrm{E}$ gives $\bot$, and ${\to}\mathrm{I}$ gives $(A \vee B)^N$.
   The rule ${\vee}\mathrm{I}$ from $B$ is the same with the other conjunct.
6. For ${\vee}\mathrm{E}$, induction gives $\neg (\neg A^N \wedge \neg B^N)$, a derivation of $C^N$ from $A^N$, and one from $B^N$.
   Assume $\neg C^N$, so the assumption $A^N$ gives $C^N$ and then $\bot$, and ${\to}\mathrm{I}$ gives $\neg A^N$.
7. In the same way we get $\neg B^N$, and then ${\wedge}\mathrm{I}$ and the first premise give $\bot$.
   Discharging $\neg C^N$ gives $\neg \neg C^N$, and Lemma 3 gives $C^N$.

### Main claim: the rules for quantifiers and equality

1. For ${\forall}\mathrm{I}$, induction and Lemma 1 give a derivation of $(A[y/x])^N = A^N[y/x]$.
   By Lemma 1, $y$ is not free in $\forall x\, A^N$ or in $\Delta^N$, so ${\forall}\mathrm{I}$ gives $\forall x\, A^N$.
2. For ${\forall}\mathrm{E}$, the rule turns $\forall x\, A^N$ into $A^N[t/x]$, which is $(A[t/x])^N$ by Lemma 1.
3. For ${\exists}\mathrm{I}$, induction gives $A^N[t/x]$.
   Assume $\forall x\, \neg A^N$, so ${\forall}\mathrm{E}$ and ${\to}\mathrm{E}$ give $\bot$, and ${\to}\mathrm{I}$ gives $\neg \forall x\, \neg A^N = (\exists x\, A)^N$.
4. For ${\exists}\mathrm{E}$, induction gives $\neg \forall x\, \neg A^N$ and a derivation of $C^N$ from $A^N[y/x]$ and $\Delta^N$.
   Assume $\neg C^N$, so the assumption $A^N[y/x]$ gives $\bot$, and ${\to}\mathrm{I}$ gives $\neg A^N[y/x]$.
5. The eigenvariable $y$ is not free in $C$, $\exists x\, A$ or $\Delta$, so by Lemma 1 it is not free in $\neg C^N$, $\forall x\, \neg A^N$ or $\Delta^N$.
   So ${\forall}\mathrm{I}$ gives $\forall x\, \neg A^N$, the first premise gives $\bot$, and Lemma 3 applied to $\neg \neg C^N$ gives $C^N$.
6. For ${=}\mathrm{I}$, we need $\neg \neg (t = t)$.
   Assume $\neg (t = t)$, then ${=}\mathrm{I}$ and ${\to}\mathrm{E}$ give $\bot$, and ${\to}\mathrm{I}$ gives the claim.
7. For ${=}\mathrm{E}$, induction gives $\neg \neg (s = t)$ and $\varphi^N[s/x]$.
   Assume $\neg \varphi^N[t/x]$, and under the assumption $s = t$ use ${=}\mathrm{E}$ to get $\varphi^N[t/x]$ and then $\bot$, so $\neg (s = t)$.
8. With $\neg \neg (s = t)$ we get $\bot$, so ${\to}\mathrm{I}$ gives $\neg \neg \varphi^N[t/x]$.
   Lemma 3 gives $\varphi^N[t/x]$, which is $(\varphi[t/x])^N$ by Lemma 1.

### Parts 1 and 3 of the theorem

1. If $\Gamma \vdash_c A$, the main claim with some $\Delta \subseteq \Gamma$ gives $\Gamma^N \vdash_i A^N$.
2. For the converse, NK proves $A \leftrightarrow A^N$ for every $A$, by induction on $A$.
   The induction uses $\neg \neg P \leftrightarrow P$, $A \vee B \leftrightarrow \neg (\neg A \wedge \neg B)$ and $\exists x\, A \leftrightarrow \neg \forall x\, \neg A$, which hold in NK.
3. An NJ derivation of $A^N$ from $\Gamma^N$ is an NK derivation.
   Replacing each open assumption $B^N$ by an NK derivation of $B^N$ from $B$, and then deriving $A$ from $A^N$, gives $\Gamma \vdash_c A$.
4. For part 3, if PA proves $\bot$, then part 2 below gives $\mathsf{HA} \vdash \bot^N$, and $\bot^N = \bot$.
   If HA proves $\bot$, so does PA, because every NJ derivation is an NK derivation.

### Part 2 of the theorem

1. [[Heyting arithmetic|RXHJPVMPJH]] proves $x = y \vee \neg x = y$ by induction, so it proves $s = t \vee \neg s = t$ for all terms $s$ and $t$.
2. Hence HA proves $\neg \neg (s = t) \to s = t$: in the case $\neg s = t$, the premise gives $\bot$, and ${\bot}\mathrm{E}$ gives $s = t$.
   With $P \to \neg \neg P$ from NJ, HA proves $P \leftrightarrow P^N$ for every atomic $P$.
3. By induction on $C$, if $C$ has no $\vee$ and no $\exists$, then HA proves $C \leftrightarrow C^N$, because the clauses for $\wedge$, $\to$ and $\forall$ commute with the connectives.
4. In the usual axiomatization, the axioms of [[PA|0QFT7Z76N5]] other than induction have no $\vee$ and no $\exists$, so HA proves their translations.
5. By Lemma 1, the translation of the induction axiom for $\varphi$ is the induction axiom for $\varphi^N$:
   $$\varphi^N(0) \wedge \forall x\, (\varphi^N(x) \to \varphi^N(S x)) \to \forall x\, \varphi^N(x).$$
6. Let $\mathsf{PA} \vdash A$.
   Then $\Gamma \vdash_c A$ for finitely many axioms $\Gamma$ of PA, part 1 gives $\Gamma^N \vdash_i A^N$, and HA proves every formula of $\Gamma^N$ by steps 4 and 5, so $\mathsf{HA} \vdash A^N$.
7. Conversely, if $\mathsf{HA} \vdash A^N$, then $\mathsf{PA} \vdash A^N$, and $\mathsf{PA} \vdash A$ by step 2 of parts 1 and 3.

This proves the three parts of the [[Gödel-Gentzen translation theorem|WC4TDGEWZR]].

## Idea

A classical proof differs from an intuitionistic one only in the rule RAA, which concludes $A$ from a refutation of $\neg A$.
After the translation every formula is stable, that is, $\neg \neg A^N$ implies $A^N$, so RAA becomes an intuitionistic step.
The rules for $\vee$ and $\exists$ are simulated by their negative forms, and their elimination rules use stability once more.
In arithmetic the induction axioms translate into induction axioms, so the argument carries over from logic to PA and HA.

## Variants

Kolmogorov's translation gives a proof in which stability is immediate, because every subformula starts with $\neg \neg$, at the cost of a longer case for each rule.
With a Hilbert system, one checks instead that the translations of the logical axioms are intuitionistically provable and that modus ponens and generalization preserve the translation.
In the sequent calculus, a classical sequent $\Gamma \Rightarrow \Delta$ goes to the intuitionistic sequent $\Gamma^N, \neg \Delta^N \Rightarrow \bot$, and each rule is checked on its own.
For arithmetic alone one can drop the double negations on atoms from the start, since HA decides equations, and then step 2 of part 2 is not needed.
