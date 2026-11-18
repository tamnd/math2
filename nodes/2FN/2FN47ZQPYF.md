---
tag: 2FN47ZQPYF
kind: proof
name: Proof of Sahlqvist's theorem
msc: ["03B45", "03C95"]
topics: [SPQVNPZDTB]
audience: research
proves: S4SSDMETJM
uses: [3RYBWYPJVD, YW6YGBMVQY, NGHWZ9Y7ZV, 6W9MEGN982, SC0BSJ3GT6, TVE4F04KME, NM4CB7QAYT]
methods: [0NTF6DMVAP, 12MQ2NJ29A, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Sahlqvist_formula
    locator: Definition
  - url: https://en.wikipedia.org/wiki/General_frame
    locator: Completeness
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Canonical models
---

## Proof

We write $\mathrm{ST}_x$ for the [[standard translation|YW6YGBMVQY]], and $\mathfrak{F}, w \Vdash \chi$ when $\chi$ is true at $w$ under every valuation on $\mathfrak{F}$.
So $\mathfrak{F}, w \Vdash \chi$ if and only if $\mathfrak{F} \models \forall \bar{P} \, \mathrm{ST}_x(\chi)[w]$, where $\bar{P}$ lists the predicates of the variables of $\chi$.
For $k \geq 0$, let $R^0(y, u)$ be $y = u$ and $R^{k+1}(y, u)$ be $\exists v \, (R(y, v) \wedge R^k(v, u))$.
Then $\mathrm{ST}_y(\square^k p)$ is equivalent to $\forall u \, (R^k(y, u) \to P(u))$, by induction on $k$.

Part A: monotonicity.

1. Let $\psi$ be positive, and let $V \subseteq V'$ mean $V(p) \subseteq V'(p)$ for every $p$. Claim: if $V \subseteq V'$ and $(W, R, V), u \models \psi$, then $(W, R, V'), u \models \psi$.
2. We prove the claim by structural induction on $\psi$. For a variable it is $V(p) \subseteq V'(p)$. For $\top$ and $\bot$ the truth value does not depend on $V$.
3. The clauses for $\wedge$, $\vee$, $\square$ and $\lozenge$ only combine truth values of subformulas with "and", "or", "for all successors" and "for some successor". Each of these preserves the passage from $V$ to $V'$ given by the induction hypothesis.
4. So $\mathrm{ST}_x(\psi)$ is upward monotone in each $P$. For a negative formula $\nu = \neg \pi$, the formula $\neg \mathrm{ST}_y(\nu)$ is $\mathrm{ST}_y(\pi)$, which is also upward monotone.

Part B: local correspondence for a Sahlqvist implication without $\vee$ in the antecedent.

5. Let $\chi = \varphi \to \psi$, with $\psi$ positive and $\varphi$ built from $\top$, $\bot$, boxed atoms and negative formulas with $\wedge$ and $\lozenge$. If $\bot$ occurs in $\varphi$, then $\varphi$ is equivalent to $\bot$, because $\wedge$ and $\lozenge$ send $\bot$ to $\bot$. Then $\chi$ is valid on every frame, and $c_\chi(x)$ is $x = x$. So assume that $\bot$ does not occur in $\varphi$.
6. Claim: $\mathrm{ST}_x(\varphi)$ is equivalent to $\exists \bar{y} \, (\mathrm{REL} \wedge \mathrm{BOX} \wedge \mathrm{NEG})$. Here $\mathrm{REL}$ is a conjunction of atoms $R(y_i, y_j)$ or $R(x, y_j)$, $\mathrm{BOX}$ is a conjunction of formulas $\mathrm{ST}_{y_i}(\square^{k_i} p_i)$, and $\mathrm{NEG}$ is a conjunction of formulas $\mathrm{ST}_{y_i}(\nu_i)$ with $\nu_i$ negative. The variable $x$ may occur among the $y_i$ in $\mathrm{BOX}$ and $\mathrm{NEG}$.
7. Proof of the claim by induction on $\varphi$. A boxed atom or a negative formula at $x$ is its own normal form, and $\top$ gives empty conjunctions.
8. For $\varphi_1 \wedge \varphi_2$, rename the bound variables of the two normal forms apart. Then $\exists \bar{y}_1 A_1 \wedge \exists \bar{y}_2 A_2$ is equivalent to $\exists \bar{y}_1 \bar{y}_2 \, (A_1 \wedge A_2)$.
9. For $\lozenge \varphi_1$, $\mathrm{ST}_x(\lozenge \varphi_1) = \exists y \, (R(x, y) \wedge \mathrm{ST}_y(\varphi_1))$. Insert the normal form of $\mathrm{ST}_y(\varphi_1)$ and move its quantifiers $\exists \bar{y}_1$ to the front, which is allowed since $\bar{y}_1$ does not contain $x$ or $y$.
10. So $\mathfrak{F}, w \Vdash \chi$ if and only if $\mathfrak{F} \models \forall \bar{P} \, \forall \bar{y} \, (\mathrm{REL} \wedge \mathrm{BOX} \to \mathrm{POS})[w]$, with $\mathrm{POS} = \mathrm{ST}_x(\psi) \vee \neg \mathrm{NEG}$. This is prenex rewriting of $\exists \bar{y} \, (\cdots) \to \mathrm{ST}_x(\psi)$.
11. By step 4, $\mathrm{POS}$ is a disjunction of upward monotone formulas, so it is upward monotone in each $P$.
12. Minimal valuation. For each variable $p$, let $\sigma_p(u)$ be the disjunction of the formulas $R^{k_i}(y_i, u)$ over the conjuncts $\mathrm{ST}_{y_i}(\square^{k_i} p)$ of $\mathrm{BOX}$ with $p_i = p$. If there is no such conjunct, let $\sigma_p(u)$ be $u \neq u$.
13. Define $c_\chi(x) = \forall \bar{y} \, (\mathrm{REL} \to \mathrm{POS}[\sigma_p / P])$, where each atom $P(t)$ is replaced by $\sigma_p(t)$. This is a first-order formula in $R$ and $=$, and it is computed from $\chi$ by steps 6 to 12.
14. From second order to first order. Assume $\mathfrak{F}, w \Vdash \chi$, and let $\bar{y}$ satisfy $\mathrm{REL}$. Take the valuation $V_\sigma(p) = \set{u : \mathfrak{F} \models \sigma_p(u)}$ for these values of $\bar{y}$.
15. Under $V_\sigma$, each conjunct $\forall u \, (R^{k_i}(y_i, u) \to P_i(u))$ of $\mathrm{BOX}$ holds, because $R^{k_i}(y_i, u)$ is a disjunct of $\sigma_{p_i}(u)$. By step 10, $\mathrm{POS}$ holds under $V_\sigma$, which is $\mathrm{POS}[\sigma_p / P]$. So $\mathfrak{F} \models c_\chi[w]$.
16. From first order to second order. Assume $\mathfrak{F} \models c_\chi[w]$. Let $V$ be any valuation and let $\bar{y}$ satisfy $\mathrm{REL} \wedge \mathrm{BOX}$ under $V$.
17. $\mathrm{BOX}$ under $V$ says that every $u$ with $R^{k_i}(y_i, u)$ lies in $V(p_i)$. So $V_\sigma(p) \subseteq V(p)$ for every $p$, by the definition of $\sigma_p$.
18. By $c_\chi$, $\mathrm{POS}$ holds under $V_\sigma$. By step 11 and step 17, $\mathrm{POS}$ holds under $V$.
19. So the formula of step 10 holds at $w$ for every valuation, and $\mathfrak{F}, w \Vdash \chi$. This proves item 1 for these implications.

Part C: local correspondence for all Sahlqvist formulas.

20. Disjunctions in the antecedent. Every Sahlqvist antecedent is equivalent to a disjunction $\varphi_1 \vee \cdots \vee \varphi_m$ of antecedents without $\vee$, because $\lozenge$ and $\wedge$ distribute over $\vee$. Then $\varphi \to \psi$ is equivalent to $\bigwedge_j (\varphi_j \to \psi)$.
21. Conjunctions. $\mathfrak{F}, w \Vdash \chi_1 \wedge \chi_2$ if and only if $\mathfrak{F}, w \Vdash \chi_1$ and $\mathfrak{F}, w \Vdash \chi_2$. So $c_{\chi_1 \wedge \chi_2} = c_{\chi_1} \wedge c_{\chi_2}$.
22. Boxes. $\mathfrak{F}, w \Vdash \square \chi_1$ if and only if $\mathfrak{F}, v \Vdash \chi_1$ for every $v$ with $w R v$, since a valuation that refutes $\chi_1$ at a successor $v$ refutes $\square \chi_1$ at $w$. So $c_{\square \chi_1}(x) = \forall y \, (R(x, y) \to c_{\chi_1}(y))$.
23. Disjunctions without shared variables. Assume $\mathfrak{F}, w \not\Vdash \chi_1$ and $\mathfrak{F}, w \not\Vdash \chi_2$, by valuations $V_1$ and $V_2$. Since the variables are disjoint, one valuation agrees with $V_1$ on the variables of $\chi_1$ and with $V_2$ on those of $\chi_2$, and it refutes $\chi_1 \vee \chi_2$. So $c_{\chi_1 \vee \chi_2} = c_{\chi_1} \vee c_{\chi_2}$.
24. By induction on the construction of Sahlqvist formulas, steps 19 to 23 give item 1.

Part D: canonicity, as a structure with cited lemmas.

25. A general frame $(W, R, A)$ is descriptive when it is differentiated, tight and compact; see [[general and descriptive frames|6W9MEGN982]]. On a descriptive frame, the closed sets are the intersections of admissible sets.
26. Cited: for a normal logic $\Lambda$, the canonical general frame, whose admissible sets are the sets $\set{\Gamma : \varphi \in \Gamma}$, is descriptive. Its underlying Kripke frame is the canonical frame of $\Lambda$. Every formula of $\Lambda$ is valid on the canonical general frame, by the truth lemma.
27. Cited: on a descriptive frame, every single point is closed, and if $C$ is closed, then $\set{u : y R^k u}$ and $R^{-1}[C]$ are closed. So the minimal valuations $V_\sigma$ of step 14 take closed values.
28. Cited (Esakia's lemma): on a descriptive frame, $R^{-1}[\bigcap_i C_i] = \bigcap_i R^{-1}[C_i]$ for every downward directed family of closed sets $C_i$.
29. Cited (intersection lemma): by step 28, if a positive formula is evaluated under a closed valuation, its truth set is the intersection of its truth sets under the admissible valuations above it.
30. From steps 27 to 29, a Sahlqvist formula that is valid on a descriptive frame under all admissible valuations is valid under all minimal valuations $V_\sigma$. By Part B, which only uses minimal valuations, it is valid on the underlying Kripke frame. This property is called d-persistence.
31. Let $\chi \in \Lambda$. By step 26, $\chi$ is valid on the canonical general frame. By step 30, it is valid on the canonical frame. This proves item 2.

Part E: completeness.

32. Let $\Lambda = \mathsf{K} \oplus \Sigma$, and let $\Gamma$ be $\Lambda$-consistent. By [[Lindenbaum's lemma|SC0BSJ3GT6]] and the [[truth lemma|NM4CB7QAYT]], $\Gamma$ is satisfied at a world of the [[canonical model|TVE4F04KME]] of $\Lambda$.
33. By item 2, the canonical frame validates every $\chi \in \Sigma$, so by item 1 it satisfies every $\forall x \, c_\chi(x)$. This proves item 3.

## Idea

Frame validity is a universal second-order statement.
The shape of a Sahlqvist antecedent lets one pull its diamonds out as first-order quantifiers and read off the smallest valuation that makes the boxed atoms true.
The consequent is monotone, so checking that smallest valuation is enough, and the second-order quantifiers disappear.
For canonicity, the smallest valuations are closed sets in descriptive frames, and Esakia's lemma moves validity from admissible to closed valuations.

## Variants

Sambin and Vaccaro gave the topological proof of canonicity outlined in Part D.
The algebraic proof shows that Sahlqvist inequalities are preserved by canonical extensions of modal algebras, using the same continuity of $\lozenge$ on closed elements.
The algorithms SQEMA and ALBA replace Parts B and C by rewrite rules based on Ackermann's lemma, which eliminates a second-order quantifier under a monotonicity condition.
