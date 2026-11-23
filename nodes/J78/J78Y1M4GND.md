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

A consequence relation is an abstract relation "$\varphi$ follows from $\Gamma$" that obeys the three rules every reasonable notion of following obeys.

Let $L$ be a set, whose elements we call formulas.
A consequence relation on $L$ is a relation ${\vdash} \subseteq \mathcal{P}(L) \times L$ such that, for all $\Gamma, \Delta \subseteq L$ and all $\varphi \in L$, the following hold.

1. (R) Reflexivity: if $\varphi \in \Gamma$, then $\Gamma \vdash \varphi$.
2. (M) Monotonicity: if $\Gamma \vdash \varphi$ and $\Gamma \subseteq \Delta$, then $\Delta \vdash \varphi$.
3. (C) Cut: if $\Gamma \vdash \psi$ for every $\psi \in \Delta$ and $\Gamma \cup \Delta \vdash \varphi$, then $\Gamma \vdash \varphi$.

The consequence operator of $\vdash$ is the map $\mathrm{Cn} \colon \mathcal{P}(L) \to \mathcal{P}(L)$ given by
$$\mathrm{Cn}(\Gamma) = \{ \varphi \in L : \Gamma \vdash \varphi \}.$$
The relation is finitary when $\Gamma \vdash \varphi$ implies $\Gamma_0 \vdash \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$.

Suppose that $L$ is the set of [[formulas|HYJ10AF6RT]] built from propositional variables by connectives.
A substitution $\sigma$ maps variables to formulas, and it extends to all formulas by replacing each variable $p$ by $\sigma(p)$.
The relation is structural when $\Gamma \vdash \varphi$ implies $\sigma[\Gamma] \vdash \sigma(\varphi)$ for every substitution $\sigma$.

A theory is any set $T \subseteq L$, and its members are its axioms.
A theory $T$ is deductively closed when $\mathrm{Cn}(T) = T$, that is, when $T \vdash \varphi$ implies $\varphi \in T$.

## Notation

We write $\Gamma, \varphi \vdash \psi$ for $\Gamma \cup \{ \varphi \} \vdash \psi$, and $\varphi_1, \dots, \varphi_n \vdash \psi$ for $\{ \varphi_1, \dots, \varphi_n \} \vdash \psi$.
We write $\vdash \varphi$ for $\emptyset \vdash \varphi$, and $\Gamma \nvdash \varphi$ when $\Gamma \vdash \varphi$ fails.
Books usually write $\models$ for a relation given by a semantics and $\vdash$ for one given by a proof system, and the definition covers both.
Following Tarski, some authors work only with the operator, written $C$ or $\mathrm{Cn}$.
The pair $(L, \vdash)$ is also called a deductive system or an abstract logic, and many authors require it to be structural.

## Remarks

### Why each condition is there

Reflexivity says that an assumption follows from any list that contains it, which is the least we can ask.
Monotonicity says that extra assumptions never destroy a conclusion.
It holds for proofs, because a proof need not use every assumption, and for truth in models, because more assumptions mean fewer models.
Cut says that proved lemmas can be used as extra assumptions without gaining anything new.
It holds for proofs because we can paste the proof of each lemma into the main proof.

A small consequence relation on three formulas is built in the L2 explanation below.
For a relation that fails a condition, let $L$ be the propositional formulas, and let $\Gamma \vdash_1 \varphi$ hold when $\varphi \in \Gamma$ or $\varphi$ follows from two members of $\Gamma$ by one use of modus ponens.
Then $p, p \to q, q \to r \vdash_1 q$ and $p, p \to q, q \to r, q \vdash_1 r$, but $p, p \to q, q \to r \nvdash_1 r$.
So one-step consequence satisfies (R) and (M) and fails cut.
The concept page [[consequence relation|FCXHSC6Z4R]] gives more examples and non-examples.

### Two other forms of cut

Given (R) and (M), cut is equivalent to transitivity (T): if $\Gamma \vdash \psi$ for every $\psi \in \Delta$ and $\Delta \vdash \varphi$, then $\Gamma \vdash \varphi$.
For (C) to (T), monotonicity turns $\Delta \vdash \varphi$ into $\Gamma \cup \Delta \vdash \varphi$, and then (C) applies.
For (T) to (C), reflexivity gives $\Gamma \vdash \chi$ for each $\chi \in \Gamma$, so $\Gamma$ yields every member of $\Gamma \cup \Delta$, and (T) applies.

For a finitary relation with (R) and (M), cut follows from its one-formula case: if $\Gamma \vdash \psi$ and $\Gamma, \psi \vdash \varphi$, then $\Gamma \vdash \varphi$.
Suppose $\Gamma \vdash \psi$ for $\psi \in \Delta$ and $\Gamma \cup \Delta \vdash \varphi$.
Finiteness and (M) give $\Gamma, \psi_1, \dots, \psi_n \vdash \varphi$ for some $\psi_1, \dots, \psi_n \in \Delta$.
By (M), $\Gamma, \psi_1, \dots, \psi_{n-1} \vdash \psi_n$, so the one-formula cut removes $\psi_n$.
After $n$ such steps we reach $\Gamma \vdash \varphi$.

### Consequence relations are closure operators

A [[closure operator|17FVAN6HXX]] on $\mathcal{P}(L)$ is a map $C$ with $X \subseteq C(X)$, with $C(X) \subseteq C(Y)$ when $X \subseteq Y$, and with $C(C(X)) = C(X)$.
The map ${\vdash} \mapsto \mathrm{Cn}$ is a bijection from consequence relations on $L$ onto closure operators on $\mathcal{P}(L)$.
Its inverse sends $C$ to the relation with $\Gamma \vdash_C \varphi$ exactly when $\varphi \in C(\Gamma)$.

1. Reflexivity gives $\Gamma \subseteq \mathrm{Cn}(\Gamma)$, and monotonicity makes $\mathrm{Cn}$ monotone.
2. For idempotence, put $\Delta = \mathrm{Cn}(\Gamma)$ and let $\Delta \vdash \varphi$.
   Then $\Gamma \vdash \psi$ for every $\psi \in \Delta$, and $\Gamma \cup \Delta \vdash \varphi$ by (M), so cut gives $\Gamma \vdash \varphi$.
3. Conversely, $\vdash_C$ satisfies (R) because $\Gamma \subseteq C(\Gamma)$, and (M) because $C$ is monotone.
4. For cut, let $\Delta \subseteq C(\Gamma)$ and $\varphi \in C(\Gamma \cup \Delta)$.
   Since $\Gamma \cup \Delta \subseteq C(\Gamma)$, we get $C(\Gamma \cup \Delta) \subseteq C(C(\Gamma)) = C(\Gamma)$.
5. The two maps are inverse, since $\varphi \in \mathrm{Cn}(\Gamma)$ says exactly $\Gamma \vdash \varphi$.

### The lattice of closed theories

Under this bijection the deductively closed theories are the closed sets of $\mathrm{Cn}$.
An intersection of closed theories $T_i$ is closed, because $\mathrm{Cn}(\bigcap_i T_i) \subseteq \mathrm{Cn}(T_i) = T_i$ for each $i$.
So the closed theories form a complete lattice.
They also determine the relation: $\Gamma \vdash \varphi$ holds exactly when $\varphi$ lies in every closed theory that contains $\Gamma$, because $\mathrm{Cn}(\Gamma)$ is the least such theory.
The relation is finitary exactly when $\mathrm{Cn}$ is algebraic, that is, when $\mathrm{Cn}(\Gamma)$ is the union of the sets $\mathrm{Cn}(\Gamma_0)$ for finite $\Gamma_0 \subseteq \Gamma$.

### Where consequence relations come from

Let $K$ be a class of models with a relation "$\mathcal{M}$ satisfies $\varphi$".
Put $\Gamma \models_K \varphi$ when every $\mathcal{M} \in K$ that satisfies all of $\Gamma$ satisfies $\varphi$.
This is a consequence relation: (R) and (M) hold by the definition, and for (C) a model of $\Gamma$ satisfies all of $\Delta$, hence all of $\Gamma \cup \Delta$, hence $\varphi$.
[[Logical consequence|1HK0VYWTV7]] is the case of all valuations or all structures, as in [[classical propositional consequence|5X683DYC8S]].
Every consequence relation arises this way: take as models the closed theories, and let $T$ satisfy $\varphi$ when $\varphi \in T$.

Derivability in a [[formal system|439M8B4DY2]] is a finitary consequence relation, because derivations are finite, as in [[the Hilbert system example|1H0WHK62VP]].
A proof system is sound for a semantics when ${\vdash} \subseteq {\models}$, and complete for it (in the sense of a proof system and a semantics) when the two relations are equal.
For first-order logic the equality is [[Gödel's completeness theorem|WQ1ZE255SF]], and by the [[compactness theorem|1NR3HAWG9D]] classical semantic consequence is finitary, as it must be.

### Structural and multiple-conclusion relations

Classical consequence is structural: a substitution instance of a valid argument is valid.
The relation with $\Gamma \vdash \varphi$ when $\varphi \in \Gamma$ or $\varphi = p$, for a fixed variable $p$, is a finitary consequence relation that is not structural.
Its operator is $\Gamma \mapsto \Gamma \cup \{ p \}$, so $\vdash p$ holds, but the substitution $p \mapsto q$ would give $\vdash q$, which fails.
Abstract algebraic logic takes a logic to be a structural consequence relation on a formula algebra; see [[algebraic logic|QYA4H5Y7VR]].

A multiple-conclusion relation $\Gamma \vdash \Delta$ reads "if all of $\Gamma$ hold, then some member of $\Delta$ holds".
Its conditions are overlap ($\Gamma \vdash \Delta$ when $\Gamma \cap \Delta \neq \emptyset$), dilution (enlarging either side keeps $\vdash$) and cut, which in the finitary case reads: if $\Gamma \vdash \Delta, \psi$ and $\Gamma, \psi \vdash \Delta$, then $\Gamma \vdash \Delta$.
Classically $p \vee q \models p, q$ holds, while neither $p \vee q \models p$ nor $p \vee q \models q$ holds.
These relations match the sequents $\Gamma \Rightarrow \Delta$ of the classical [[sequent calculus|W72CA3R9MP]].

### Watch out

Many inference relations in use are not consequence relations.
The [[closed-world assumption|W4QZGRCDPA]] and probabilistic inference keep reflexivity but fail monotonicity, and they are studied as non-monotonic logic.
[[Substructural logics|98QF5J4W16]] weaken the conditions at the level of sequents, where $\Gamma$ is a list or a multiset.
Before you call a relation a consequence relation, check all three conditions, and monotonicity first.

## Explanations

### L1 human

A consequence relation says which statements follow from which.
Three rules hold for any reasonable notion of "follows".
A statement follows from any list that contains it.
Adding more assumptions never destroys a conclusion.
If some facts follow from our assumptions, we may use them as extra assumptions without getting anything new.
For example, "$x$ is even" follows from "$x = 2$", and "$x + 1$ is odd" follows from "$x = 2$" and "$x$ is even", so "$x + 1$ is odd" already follows from "$x = 2$" alone.

### L2 human

We build a consequence relation from a closure operator and watch the theorem at work.
Let $L = \{ p, q, r \}$, and define
$$\mathrm{Cn}(X) = \begin{cases} X \cup \{ r \} & \text{if } \{ p, q \} \subseteq X, \\ X & \text{otherwise.} \end{cases}$$

1. $\mathrm{Cn}$ is extensive by its definition.
2. It is monotone, because $\{ p, q \} \subseteq X \subseteq Y$ implies $\{ p, q \} \subseteq Y$.
3. It is idempotent: if $\{ p, q \} \subseteq X$, then $\mathrm{Cn}(X)$ already contains $r$, and a second application adds nothing.
4. The matching relation has $p, q \vdash r$, while $p \nvdash r$ and $q \nvdash r$.
5. Of the $8$ subsets of $L$, only $\{ p, q \}$ fails to be closed, so there are $7$ closed theories.
6. The least closed theory that contains $\{ p, q \}$ is $\{ p, q, r \} = \mathrm{Cn}(\{ p, q \})$, as the theorem predicts.

The typical use of the abstract definition is to prove a fact once for many logics, such as the Lindenbaum lemma for finitary relations in [[abstract logical systems|RQXV7PM2WT]].

### L3 human

The theorem on closure operators puts logic inside lattice theory: the theories of a logic form a closure system, and an algebraic one when the relation is finitary.
In abstract algebraic logic a logic is a structural consequence relation, and its algebraic counterpart is studied through the Leibniz operator and classes of logical matrices; see [[algebraic logic|QYA4H5Y7VR]].
In proof theory the three conditions become the structural rules of Gentzen's sequent calculus: reflexivity is the identity axiom, monotonicity is weakening, and (C) is the cut rule.
Dropping weakening or contraction leads to substructural logics, where the relation is no longer a closure operator on sets.
[[Abstract logical systems|RQXV7PM2WT]] add a semantics to the relation, and in an institution each signature carries its own consequence relation.
