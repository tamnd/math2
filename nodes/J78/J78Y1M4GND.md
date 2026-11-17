---
tag: J78Y1M4GND
kind: definition
name: Consequence relation
aliases: [consequence-operator, tarski-consequence-relation]
msc: ["03B22"]
topics: [H8QZY0RZXZ]
audience: grad
defines: FCXHSC6Z4R
uses: [1HK0VYWTV7, 17FVAN6HXX, 439M8B4DY2, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Consequence_relation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Closure_operator
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Structural_rule
    locator: lead section
---

## Definition

Let $L$ be a set, whose elements we call formulas.
A consequence relation on $L$ is a relation ${\vdash} \subseteq \mathcal{P}(L) \times L$ between sets of formulas and formulas such that, for all $\Gamma, \Delta \subseteq L$ and all $\varphi \in L$:

- (R) reflexivity: if $\varphi \in \Gamma$, then $\Gamma \vdash \varphi$;
- (M) monotonicity: if $\Gamma \vdash \varphi$ and $\Gamma \subseteq \Delta$, then $\Delta \vdash \varphi$;
- (C) cut: if $\Gamma \vdash \psi$ for every $\psi \in \Delta$ and $\Gamma \cup \Delta \vdash \varphi$, then $\Gamma \vdash \varphi$.

The consequence operator of $\vdash$ is the map $\mathrm{Cn} \colon \mathcal{P}(L) \to \mathcal{P}(L)$ with $\mathrm{Cn}(\Gamma) = \set{\varphi \in L : \Gamma \vdash \varphi}$.

A consequence relation is finitary when $\Gamma \vdash \varphi$ implies $\Gamma_0 \vdash \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$.

When $L$ is the set of [[formulas|HYJ10AF6RT]] built from propositional variables by connectives, a substitution $\sigma$ is a map from variables to formulas, extended to all formulas by replacing each variable $p$ by $\sigma(p)$.
A consequence relation on such an $L$ is structural when $\Gamma \vdash \varphi$ implies $\sigma[\Gamma] \vdash \sigma(\varphi)$ for every substitution $\sigma$.

A theory is any set $T \subseteq L$.
A theory $T$ is deductively closed when $\mathrm{Cn}(T) = T$, that is, when $T \vdash \varphi$ implies $\varphi \in T$.

## Notation

- $\Gamma, \varphi \vdash \psi$ abbreviates $\Gamma \cup \set{\varphi} \vdash \psi$, and $\varphi_1, \dots, \varphi_n \vdash \psi$ abbreviates $\set{\varphi_1, \dots, \varphi_n} \vdash \psi$.
- $\vdash \varphi$ abbreviates $\emptyset \vdash \varphi$, and $\Gamma \nvdash \varphi$ says that $\Gamma \vdash \varphi$ fails.
- Semantic consequence relations are usually written $\models$, and relations given by a proof system are written $\vdash$; the definition covers both.
- Some authors write $C$ or $\mathrm{Cn}$ for the operator and work only with it, following Tarski.
- The pair $(L, \vdash)$ is often called a deductive system or an abstract logic, and many authors define it only for structural relations.

## Remarks

### Equivalent forms of cut

Given (R) and (M), cut (C) is equivalent to transitivity (T): if $\Gamma \vdash \psi$ for every $\psi \in \Delta$ and $\Delta \vdash \varphi$, then $\Gamma \vdash \varphi$.

1. (C) implies (T): from $\Delta \vdash \varphi$, monotonicity gives $\Gamma \cup \Delta \vdash \varphi$, and (C) gives $\Gamma \vdash \varphi$.
2. (T) implies (C): assume $\Gamma \vdash \psi$ for $\psi \in \Delta$ and $\Gamma \cup \Delta \vdash \varphi$. Every $\chi \in \Gamma$ satisfies $\Gamma \vdash \chi$ by (R), so $\Gamma$ yields every formula of $\Gamma \cup \Delta$, and (T) gives $\Gamma \vdash \varphi$.

For a finitary relation that satisfies (R) and (M), cut follows from its one-formula case: if $\Gamma \vdash \psi$ and $\Gamma, \psi \vdash \varphi$, then $\Gamma \vdash \varphi$.

3. Assume $\Gamma \vdash \psi$ for $\psi \in \Delta$ and $\Gamma \cup \Delta \vdash \varphi$.
4. By finiteness and (M), $\Gamma \cup \set{\psi_1, \dots, \psi_n} \vdash \varphi$ for some $\psi_1, \dots, \psi_n \in \Delta$.
5. By (M), $\Gamma \cup \set{\psi_1, \dots, \psi_{n-1}} \vdash \psi_n$, and the one-formula cut removes $\psi_n$.
6. Repeating step 5 $n$ times gives $\Gamma \vdash \varphi$.

### Consequence relations and closure operators

A [[closure operator|17FVAN6HXX]] on $\mathcal{P}(L)$ is a map $C$ with $X \subseteq C(X)$, with $C(X) \subseteq C(Y)$ whenever $X \subseteq Y$, and with $C(C(X)) = C(X)$.

Theorem: the map ${\vdash} \mapsto \mathrm{Cn}$ is a bijection from consequence relations on $L$ to closure operators on $\mathcal{P}(L)$, whose inverse sends $C$ to the relation $\Gamma \vdash_C \varphi \iff \varphi \in C(\Gamma)$.

Proof.

1. Let $\vdash$ be a consequence relation. Then $\Gamma \subseteq \mathrm{Cn}(\Gamma)$ by (R), and $\mathrm{Cn}$ is monotone by (M).
2. $\mathrm{Cn}(\Gamma) \subseteq \mathrm{Cn}(\mathrm{Cn}(\Gamma))$ by step 1. For the converse, let $\mathrm{Cn}(\Gamma) \vdash \varphi$ and put $\Delta = \mathrm{Cn}(\Gamma)$.
3. Then $\Gamma \vdash \psi$ for every $\psi \in \Delta$, and $\Gamma \cup \Delta \vdash \varphi$ by (M). Cut gives $\Gamma \vdash \varphi$, so $\mathrm{Cn}$ is idempotent.
4. Let $C$ be a closure operator. Then $\vdash_C$ satisfies (R) because $\Gamma \subseteq C(\Gamma)$, and (M) because $C$ is monotone.
5. For cut, assume $\Delta \subseteq C(\Gamma)$ and $\varphi \in C(\Gamma \cup \Delta)$. Since $\Gamma \cup \Delta \subseteq C(\Gamma)$, monotonicity and idempotence give $C(\Gamma \cup \Delta) \subseteq C(C(\Gamma)) = C(\Gamma)$, so $\varphi \in C(\Gamma)$.
6. The two maps are inverse to each other, since $\varphi \in \mathrm{Cn}(\Gamma)$ holds exactly when $\Gamma \vdash \varphi$.

Under this bijection the deductively closed theories are the closed sets of $\mathrm{Cn}$.
They are closed under arbitrary intersections, since $\mathrm{Cn}(\bigcap_i T_i) \subseteq \mathrm{Cn}(T_i) = T_i$ for each $i$, so they form a complete lattice.
They determine the relation: $\Gamma \vdash \varphi$ holds exactly when $\varphi$ belongs to every deductively closed theory that contains $\Gamma$, because $\mathrm{Cn}(\Gamma)$ is the least such theory.
The relation is finitary exactly when $\mathrm{Cn}$ is algebraic, that is, $\mathrm{Cn}(\Gamma) = \bigcup \set{\mathrm{Cn}(\Gamma_0) : \Gamma_0 \subseteq \Gamma \text{ finite}}$.

### Semantic and syntactic consequence

Let $K$ be any class of models, with a relation "$\mathcal{M}$ satisfies $\varphi$" for $\mathcal{M} \in K$ and $\varphi \in L$.
Put $\Gamma \models_K \varphi$ when every $\mathcal{M} \in K$ that satisfies all formulas of $\Gamma$ satisfies $\varphi$.
Then $\models_K$ is a consequence relation.
(R) and (M) are immediate, and for (C), a model of $\Gamma$ satisfies each $\psi \in \Delta$, hence all of $\Gamma \cup \Delta$, hence $\varphi$.
[[Logical consequence|1HK0VYWTV7]] of classical logic is the case where $K$ is the class of all valuations or all structures, as in the [[propositional example|5X683DYC8S]].

Every consequence relation arises in this way.
Take for $K$ the deductively closed theories, and let $T$ satisfy $\varphi$ when $\varphi \in T$; by the previous subsection, $\models_K$ is the given relation.

Derivability in a [[formal system|439M8B4DY2]] is also a consequence relation, and it is finitary because derivations are finite, as in the [[Hilbert example|1H0WHK62VP]].
A proof system is sound for a semantic relation when ${\vdash} \subseteq {\models}$, and complete when the two relations are equal; for first-order logic this equality is [[Gödel's completeness theorem|WQ1ZE255SF]].
By the [[compactness theorem|1NR3HAWG9D]], classical semantic consequence is finitary, which is what completeness for a finitary proof system requires.

### Structural relations

Classical consequence is structural: a substitution instance of a valid argument is valid.
The relation with $\Gamma \vdash \varphi$ when $\varphi \in \Gamma$ or $\varphi = p$, for a fixed variable $p$, is a finitary consequence relation that is not structural.
Its operator is $\Gamma \mapsto \Gamma \cup \set{p}$; we have $\vdash p$, but the substitution $p \mapsto q$ does not give $\vdash q$.
Structural consequence relations are the subject of abstract algebraic logic, where a logic is identified with a structural consequence relation on a formula algebra; see [[algebraic logic|QYA4H5Y7VR]].

### Multiple conclusions

A multiple-conclusion consequence relation is a relation $\Gamma \vdash \Delta$ between two sets of formulas, read "if all of $\Gamma$ hold, then some formula of $\Delta$ holds".
Its conditions are overlap ($\Gamma \vdash \Delta$ when $\Gamma \cap \Delta \neq \emptyset$), dilution (enlarging either side preserves $\vdash$) and a cut condition, which in the finitary case reads: if $\Gamma \vdash \Delta, \psi$ and $\Gamma, \psi \vdash \Delta$, then $\Gamma \vdash \Delta$.
In classical logic $p \vee q \models p, q$ holds, while neither $p \vee q \models p$ nor $p \vee q \models q$ holds; single conclusions cannot express this fact directly.
These relations match the sequents $\Gamma \Rightarrow \Delta$ of the classical [[sequent calculus|W72CA3R9MP]].

### Non-monotonic inference

Inference relations used in artificial intelligence, such as the [[closed-world assumption|W4QZGRCDPA]], satisfy reflexivity but fail monotonicity: new information can remove a conclusion.
They are not consequence relations in the sense above, and they are studied under the name non-monotonic logic.
Substructural logics drop or weaken other conditions, but at the level of sequents; see [[substructural logics|98QF5J4W16]].

## Explanations

### L1 human

A consequence relation says which statements follow from which.
Three rules hold for any reasonable notion of "follows".
A statement follows from any list that contains it.
Adding more assumptions never destroys a conclusion.
And if some facts follow from our assumptions, we may use those facts as extra assumptions without getting anything new.
For example, from "$x = 2$" follows "$x$ is even", and from "$x = 2$" and "$x$ is even" follows "$x + 1$ is odd", so "$x + 1$ is odd" already follows from "$x = 2$" alone.

### L2 human

We build a small consequence relation from a closure operator and check the theorem in this case.

1. Let $L = \set{p, q, r}$, and let $\mathrm{Cn}(X) = X \cup \set{r}$ when $\set{p, q} \subseteq X$, and $\mathrm{Cn}(X) = X$ otherwise.
2. $\mathrm{Cn}$ is extensive by definition, and monotone because $\set{p, q} \subseteq X \subseteq Y$ implies $\set{p, q} \subseteq Y$.
3. It is idempotent: if $\set{p, q} \subseteq X$, then $\mathrm{Cn}(X)$ contains $r$, and applying $\mathrm{Cn}$ again adds nothing.
4. The relation is $X \vdash \varphi$ iff $\varphi \in X$, or $\varphi = r$ and $p, q \in X$. So $p, q \vdash r$, while $p \nvdash r$ and $q \nvdash r$.
5. The closed sets are the subsets $X$ with $r \in X$ or $\set{p, q} \not\subseteq X$. There are seven: $\emptyset$, $\set{p}$, $\set{q}$, $\set{r}$, $\set{p, r}$, $\set{q, r}$, $\set{p, q, r}$.
6. The set $\set{p, q}$ is not closed, and the least closed set that contains it is $\set{p, q, r} = \mathrm{Cn}(\set{p, q})$, as the theorem predicts.

The typical use of the definition is to prove facts about many logics at once, such as the [[Lindenbaum lemma|RQXV7PM2WT]] for finitary relations.
A trap is to call any inference relation a consequence relation: probabilistic and default inference usually fail monotonicity.

### L3 human

The definition goes back to Tarski's consequence operators, and the theorem above identifies them with closure operators, so the theories of a logic form a closure system, a complete lattice of subsets.
In abstract algebraic logic, a logic is a structural consequence relation, and its algebraic counterpart is studied through the Leibniz operator and through classes of matrices; see [[algebraic logic|QYA4H5Y7VR]].

In proof theory the three conditions appear as the structural rules of Gentzen's sequent calculus: reflexivity as the identity axiom, monotonicity as weakening, and the condition (C) as the cut rule.
Dropping weakening or contraction leads to [[substructural logics|98QF5J4W16]], where $\Gamma$ is a multiset or a list and the relation is no longer determined by a closure operator on sets.
The notion is the core of [[abstract logical systems|RQXV7PM2WT]], where a logic is a consequence relation together with a semantics, and in an institution each signature carries its own consequence relation.
