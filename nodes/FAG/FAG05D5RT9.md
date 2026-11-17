---
tag: FAG05D5RT9
kind: proof
name: Proof of Lyndon's interpolation theorem
msc: ["03C40", "03F05", "03B10"]
topics: [FBWW4J1XWG]
audience: research
proves: BRDT1BT7WW
uses: [W72CA3R9MP, AYRZ98Y0NW, WQ1ZE255SF, 983GZBQYT4, DKFGQTRYZE, 1HK0VYWTV7, E2CBFNAVZY]
methods: [0ASJVEFA9J, 12MQ2NJ29A, 0WCP0PVET6]
sources:
  - wikipedia: en:2056790@r1321826961
    locator: Craig interpolation, section Proof of Craig's interpolation theorem
    note: adopted
    mention: wikipedia://en/2056790#6M9Y
    sections: [Proof]
  - arxiv: 2510.03822v1
    locator: Section 2, Theorem 2.5, and the remark on equality at the start of Section 2
  - doi: 10.2140/pjm.1959.9.129
    locator: Section 1, Introduction, and Section 5, Interpolation theorem
---

## Proof

The proof has three parts.
Part A is Maehara's method on cut-free sequent derivations, and it proves the theorem for relational signatures and sentences without equality.
Part B, the case of relational signatures with equality, is cited and not proved here.
Part C reduces function and constant symbols to Part B, and it is proved in full.
We use the polarity sets $\operatorname{Pos}$ and $\operatorname{Neg}$ of the [[statement|BRDT1BT7WW]], and we extend them to finite multisets by $\operatorname{Pos}(\Gamma) = \bigcup_{\gamma \in \Gamma} \operatorname{Pos}(\gamma)$, and likewise for $\operatorname{Neg}$.
We write $\operatorname{FV}(\Gamma)$ for the set of variables free in some member of $\Gamma$.

### Part A: relational signatures without equality

Let $\sigma$ be a signature with relation symbols only, and work with formulas without equality.
Then every term is a variable.
For the interpolants we allow two more atomic formulas, $\top$ (true) and $\bot$ (false), which contain no relation symbol.

Setup: the calculus.
We use the [[sequent calculus|W72CA3R9MP]] LK with exactly the rules listed in the [[proof of Herbrand's theorem by cut elimination|~fef865bc]].
These are the axioms $A \Rightarrow A$ for atomic $A$, weakening, contraction, two rules for each of $\neg, \land, \lor, \to, \forall, \exists$, and cut.
A sequent $\Gamma \Rightarrow \Delta$ is valid when, in every [[structure|983GZBQYT4]] $\mathcal{A}$ and under every assignment $s$, some member of $\Gamma$ is false or some member of $\Delta$ is true.
Fact (F): every valid sequent has a derivation in LK without cut.
It combines the completeness of LK, which follows from [[Gödel's completeness theorem|WQ1ZE255SF]], with the [[cut-elimination theorem|AYRZ98Y0NW]].
We also use the substitution lemma: if $y$ is substitutable for $x$ in $A$, then $\mathcal{A} \models A^x_y[s]$ if and only if $\mathcal{A} \models A[s(x \mid s(y))]$.

Setup: split sequents and interpolants.
A split of $\Gamma \Rightarrow \Delta$ is a way to write $\Gamma$ as the multiset union $\Gamma_1, \Gamma_2$ and $\Delta$ as $\Delta_1, \Delta_2$.
We write it $[\Gamma_1 ; \Delta_1 \parallel \Gamma_2 ; \Delta_2]$, and we call $\Gamma_1, \Delta_1$ the left part and $\Gamma_2, \Delta_2$ the right part.
Put

- $L^+ = \operatorname{Pos}(\Gamma_1) \cup \operatorname{Neg}(\Delta_1)$ and $L^- = \operatorname{Neg}(\Gamma_1) \cup \operatorname{Pos}(\Delta_1)$;
- $R^+ = \operatorname{Pos}(\Delta_2) \cup \operatorname{Neg}(\Gamma_2)$ and $R^- = \operatorname{Neg}(\Delta_2) \cup \operatorname{Pos}(\Gamma_2)$.

An interpolant of the split is a formula $\theta$, possibly with $\top$ and $\bot$, such that

- (I1) $\Gamma_1 \Rightarrow \Delta_1, \theta$ is valid;
- (I2) $\theta, \Gamma_2 \Rightarrow \Delta_2$ is valid;
- (I3) $\operatorname{Pos}(\theta) \subseteq L^+ \cap R^+$ and $\operatorname{Neg}(\theta) \subseteq L^- \cap R^-$;
- (I4) $\operatorname{FV}(\theta) \subseteq \operatorname{FV}(\Gamma_1, \Delta_1) \cap \operatorname{FV}(\Gamma_2, \Delta_2)$.

Maehara's lemma: if $\Gamma \Rightarrow \Delta$ has a cut-free derivation, then every split of $\Gamma \Rightarrow \Delta$ has an interpolant.
We prove it by [[induction|0ASJVEFA9J]] on the derivation.
Given a split of the conclusion of a rule, we split each premise by keeping every context formula in its part and putting each auxiliary formula in the part of the principal formula.
For contraction, both copies go to the part of the contracted formula.

1. Polarity bookkeeping. For the propositional rules, $\operatorname{Pos}(\neg A) = \operatorname{Neg}(A)$, $\operatorname{Pos}(A \to B) = \operatorname{Neg}(A) \cup \operatorname{Pos}(B)$ and $\operatorname{Neg}(A \to B) = \operatorname{Pos}(A) \cup \operatorname{Neg}(B)$; for $\land$ and $\lor$ the sets are unions. For the quantifier rules, $\operatorname{Pos}(A^x_y) = \operatorname{Pos}(A) = \operatorname{Pos}(\forall x A) = \operatorname{Pos}(\exists x A)$, and likewise for $\operatorname{Neg}$, since renaming a variable changes no relation symbol.
2. From step 1, with the split chosen above, the sets $L^+, L^-, R^+, R^-$ of each premise are contained in the same sets of the conclusion. For example, in $\neg$L with $\neg A$ in $\Gamma_1$, the premise has $A$ in $\Delta_1$, and $\operatorname{Neg}(A) = \operatorname{Pos}(\neg A)$, $\operatorname{Pos}(A) = \operatorname{Neg}(\neg A)$. So (I3) for a premise implies (I3) for the conclusion, for the same $\theta$.
3. For every rule except $\forall$L and $\exists$R, the free variables of each premise part are free in the same part of the conclusion, apart from the eigenvariable of $\forall$R and $\exists$L. So (I4) passes down in all other cases.
4. Axiom $R \bar u \Rightarrow R \bar u$, with $A = R \bar u$. There are four splits. If $A$ is in $\Gamma_1$ and in $\Delta_1$, take $\theta = \bot$. If $A$ is in $\Gamma_2$ and in $\Delta_2$, take $\theta = \top$.
5. If $A$ is in $\Gamma_1$ and in $\Delta_2$, take $\theta = A$. Then (I1) is $A \Rightarrow A$ and (I2) is $A \Rightarrow A$. Also $R \in \operatorname{Pos}(\Gamma_1) \subseteq L^+$ and $R \in \operatorname{Pos}(\Delta_2) \subseteq R^+$, and $\operatorname{FV}(A)$ lies in both parts.
6. If $A$ is in $\Gamma_2$ and in $\Delta_1$, take $\theta = \neg A$. Then (I1) is $\Rightarrow A, \neg A$ and (I2) is $\neg A, A \Rightarrow$, both valid. Also $\operatorname{Neg}(\neg A) = \{R\}$, with $R \in \operatorname{Pos}(\Delta_1) \subseteq L^-$ and $R \in \operatorname{Pos}(\Gamma_2) \subseteq R^-$.
7. Weakening and contraction. Keep the interpolant $\theta$ of the premise. Weakening adds a formula to one side of (I1) or (I2), which keeps validity. Contraction removes a copy of a formula that is still present, and a sequent with one copy is valid exactly when the sequent with two copies is valid.
8. One-premise propositional rules: $\neg$L, $\neg$R, $\land$L, $\lor$R, $\to$R. Keep $\theta$. If the principal formula is in the left part, (I2) is unchanged, and (I1) for the conclusion follows from (I1) for the premise by the same rule, which is sound. If it is in the right part, (I1) is unchanged, and (I2) follows by the same rule. Steps 2 and 3 give (I3) and (I4).
9. Two-premise rules: $\land$R, $\lor$L, $\to$L. Let $\theta_1$ and $\theta_2$ be interpolants of the two premises. If the principal formula is in the left part, take $\theta = \theta_1 \lor \theta_2$. If it is in the right part, take $\theta = \theta_1 \land \theta_2$.
10. Case $\land$R with $A \land B$ in $\Delta_1$. The premises are $[\Gamma_1 ; \Delta_1, A \parallel \Gamma_2 ; \Delta_2]$ and $[\Gamma_1 ; \Delta_1, B \parallel \Gamma_2 ; \Delta_2]$. From $\Gamma_1 \Rightarrow \Delta_1, A, \theta_1$ and $\Gamma_1 \Rightarrow \Delta_1, B, \theta_2$ we get $\Gamma_1 \Rightarrow \Delta_1, A \land B, \theta_1 \lor \theta_2$. From $\theta_1, \Gamma_2 \Rightarrow \Delta_2$ and $\theta_2, \Gamma_2 \Rightarrow \Delta_2$ we get $\theta_1 \lor \theta_2, \Gamma_2 \Rightarrow \Delta_2$.
11. Case $\land$R with $A \land B$ in $\Delta_2$. From $\Gamma_1 \Rightarrow \Delta_1, \theta_1$ and $\Gamma_1 \Rightarrow \Delta_1, \theta_2$ we get $\Gamma_1 \Rightarrow \Delta_1, \theta_1 \land \theta_2$. From $\theta_1, \Gamma_2 \Rightarrow \Delta_2, A$ and $\theta_2, \Gamma_2 \Rightarrow \Delta_2, B$ we get $\theta_1 \land \theta_2, \Gamma_2 \Rightarrow \Delta_2, A \land B$.
12. Case $\to$L with $A \to B$ in $\Gamma_1$. Under an assignment that makes $\Gamma_1$ and $A \to B$ true, $\Delta_1$ false and $\theta_1 \lor \theta_2$ false, the first premise $\Gamma_1 \Rightarrow \Delta_1, A, \theta_1$ makes $A$ true, and the second premise $B, \Gamma_1 \Rightarrow \Delta_1, \theta_2$ makes $B$ false. This contradicts the truth of $A \to B$, so (I1) holds. (I2) follows as in step 10.
13. The cases $\to$L in $\Gamma_2$, and $\lor$L in either part, are checked in the same way, by [[cases|0WCP0PVET6]] on the truth values. In all two-premise cases, $\operatorname{Pos}(\theta) = \operatorname{Pos}(\theta_1) \cup \operatorname{Pos}(\theta_2)$ and $\operatorname{Neg}(\theta) = \operatorname{Neg}(\theta_1) \cup \operatorname{Neg}(\theta_2)$, and $\operatorname{FV}(\theta) = \operatorname{FV}(\theta_1) \cup \operatorname{FV}(\theta_2)$, so steps 2 and 3 give (I3) and (I4).
14. Rules $\forall$R and $\exists$L, with eigenvariable $a$. Say the principal formula is in the left part; the other case is symmetric. The right part of the premise is the right part of the conclusion, in which $a$ is not free. By (I4) for the premise, $a$ is not free in $\theta$. Keep $\theta$.
15. For $\forall$R with $\forall x A$ in $\Delta_1$, we check (I1). Take $\mathcal{A}$ and $s$ with $\Gamma_1$ true, $\Delta_1$ false and $\theta$ false. For each $b$ in the universe, the assignment $s(a \mid b)$ gives the same truth values to $\Gamma_1, \Delta_1, \theta$, since $a$ is not free in them.
16. So the premise makes $A^x_a$ true under $s(a \mid b)$, and the substitution lemma gives $\mathcal{A} \models A[s(x \mid b)]$, since $a$ is not free in $\forall x A$. So $\forall x A$ is true under $s$. The case $\exists$L is the same with signs reversed.
17. Rules $\forall$L and $\exists$R, with the term $y$, a variable. The polarity sets do not change, by step 1. Let $\theta$ be the interpolant of the premise. If $y$ is free in the conclusion part that contains the principal formula, or $y$ is not free in $\theta$, keep $\theta$: (I1), (I2) follow by the same rule, and (I4) holds.
18. Otherwise $y$ is free in $\theta$ but not free in the part of the conclusion with the principal formula. By (I4) for the premise, $y$ is free in the other part, which is the same in premise and conclusion.
19. If the principal formula is in the left part, take $\forall y \, \theta$. If it is in the right part, take $\exists y \, \theta$. In both cases (I3) holds since quantifiers do not change signs, and (I4) holds since $y$ is removed.
20. Case $\forall$L with $\forall x A$ in $\Gamma_1$, and $\theta' = \forall y \, \theta$. For (I1), take $\mathcal{A}, s$ with $\Gamma_1$ and $\forall x A$ true and $\Delta_1$ false. For each $b$, the assignment $s(y \mid b)$ gives the same values to $\Gamma_1, \forall x A, \Delta_1$, since $y$ is not free in them. Under $s(y \mid b)$, $A^x_y$ is true by the substitution lemma, so the premise gives $\theta$ true. So $\forall y \, \theta$ is true under $s$. For (I2), $\forall y \, \theta \models \theta$, so $\theta, \Gamma_2 \Rightarrow \Delta_2$ gives $\forall y \, \theta, \Gamma_2 \Rightarrow \Delta_2$.
21. Case $\forall$L with $\forall x A$ in $\Gamma_2$, and $\theta' = \exists y \, \theta$. (I1) holds since $\theta \models \exists y \, \theta$. For (I2), take $\mathcal{A}, s$ with $\exists y \, \theta$, $\forall x A$ and $\Gamma_2$ true. Choose $b$ with $\theta$ true under $s(y \mid b)$. Under $s(y \mid b)$, the formulas $\forall x A$, $\Gamma_2$, $\Delta_2$ keep their values, $A^x_y$ is true, and the premise $\theta, A^x_y, \Gamma_2 \Rightarrow \Delta_2$ makes some member of $\Delta_2$ true. So some member of $\Delta_2$ is true under $s$.
22. The two cases of $\exists$R are dual. With $\exists x A$ in $\Delta_1$, take $\forall y \, \theta$: if $\Gamma_1$ is true and $\Delta_1$, $\exists x A$ are false under $s$, then under each $s(y \mid b)$ the formula $A^x_y$ is false, so $\theta$ is true. With $\exists x A$ in $\Delta_2$, take $\exists y \, \theta$: a witness $b$ for $\theta$ makes $\Gamma_2$ false, or $\Delta_2$ true, or $A^x_y$ true under $s(y \mid b)$, and the last gives $\exists x A$ true under $s$.
23. The calculus has no other rules, since the derivation has no cut. This proves Maehara's lemma.
24. End of Part A. Let $\varphi \models \psi$, for sentences without equality over $\sigma$. Then $\varphi \Rightarrow \psi$ is valid, and by (F) it has a cut-free derivation. Apply Maehara's lemma to the split $[\varphi ; \emptyset \parallel \emptyset ; \psi]$.
25. Here $L^+ = \operatorname{Pos}(\varphi)$, $L^- = \operatorname{Neg}(\varphi)$, $R^+ = \operatorname{Pos}(\psi)$, $R^- = \operatorname{Neg}(\psi)$. So the interpolant $\theta$ satisfies $\varphi \models \theta$, $\theta \models \psi$, and properties 2 and 3 of the statement. By (I4), $\theta$ has no free variables.
26. To remove $\top$ and $\bot$, replace $\top$ by $\forall x \, (x = x)$ and $\bot$ by $\neg \forall x \, (x = x)$. This keeps the truth values and adds no relation symbol of $\sigma$. The statement allows equality in $\theta$; in logic without equality one keeps $\top$ and $\bot$ instead.

### Part B: relational signatures with equality (cited)

The theorem holds for relational signatures when $\varphi$ and $\psi$ may contain $=$.
This case is not proved here.
Ten Cate and Comer state that all results of their Section 2, among them Theorem 2.5, hold with and without equality, with $=$ outside the sign conditions.
Lyndon (1959, Section 1) writes that the theorem takes the same form whether or not identity is admitted with suitable axioms, and his proof in Sections 4 and 5 is model-theoretic.
Part A does not give it directly.
If one treats $=$ as a relation symbol $E$ and adds the equality axioms, the axioms $E x y \land P x \to P y$ put each relation symbol $P$ with both signs on one side, and properties 2 and 3 are lost.

### Part C: function and constant symbols

Let $\sigma$ have function and constant symbols, and let $\varphi \models \psi$ for $\sigma$-sentences, with or without $=$.
A constant symbol counts as a $0$-ary function symbol.
For each $m$-ary function symbol $f$, let $G_f$ be a new $(m+1)$-ary relation symbol, and let $\sigma^*$ be the relational signature with the relation symbols of $\sigma$ and the symbols $G_f$.

27. For a term $t$ and a variable $y$ not in $t$, define a formula $D(t, y)$ by recursion on $t$. For a variable $x$, $D(x, y)$ is $y = x$. For $t = f t_1 \cdots t_m$, $D(t, y)$ is $\exists y_1 \cdots \exists y_m \, (D(t_1, y_1) \land \cdots \land D(t_m, y_m) \land G_f y_1 \cdots y_m y)$, with new variables $y_i$.
28. Translate each $\sigma$-formula $\chi$ into a $\sigma^*$-formula $\chi^*$. An atomic $R t_1 \cdots t_m$ becomes $\exists y_1 \cdots \exists y_m \, (D(t_1, y_1) \land \cdots \land D(t_m, y_m) \land R y_1 \cdots y_m)$. An atomic $t_1 = t_2$ becomes $\exists y_1 \exists y_2 \, (D(t_1, y_1) \land D(t_2, y_2) \land y_1 = y_2)$. The translation commutes with $\neg, \land, \lor, \to, \forall, \exists$.
29. Each relation symbol $R$ of $\sigma$ occurs in the translation of $R \bar t$ once, with the same sign as $R \bar t$. So $\chi^*$ has the same sets $\operatorname{Pos}$ and $\operatorname{Neg}$ as $\chi$, when we restrict them to the relation symbols of $\sigma$.
30. For a $\sigma$-structure $\mathcal{A}$, let $\mathcal{A}^*$ be the $\sigma^*$-structure with the same universe and relations, where $G_f$ is the graph $\{(\bar a, b) : f^{\mathcal{A}}(\bar a) = b\}$. By [[structural induction|12MQ2NJ29A]] on $t$, $\mathcal{A}^* \models D(t, y)[s]$ if and only if $s(y)$ is the value of $t$ in $\mathcal{A}$ under $s$. Then, by structural induction on $\chi$, $\mathcal{A}^* \models \chi^*[s]$ if and only if $\mathcal{A} \models \chi[s]$.
31. For each $f$, let $\mathrm{Fun}_f$ be the sentence $\forall \bar x \, \exists y \, (G_f \bar x y \land \forall z \, (G_f \bar x z \to z = y))$. It says that $G_f$ is the graph of a function. Let $F_\varphi$ be the conjunction of $\mathrm{Fun}_f$ over the function symbols $f$ of $\varphi$, and define $F_\psi$ in the same way.
32. Claim: $\varphi^* \land F_\varphi \models F_\psi \to \psi^*$. Let $\mathcal{M}$ be a $\sigma^*$-structure with $\mathcal{M} \models \varphi^* \land F_\varphi \land F_\psi$. For each $f$ in $\varphi$ or $\psi$, $G_f^{\mathcal{M}}$ is the graph of a function, and we let $f^{\mathcal{A}}$ be that function. Interpret the other function symbols arbitrarily, which is possible since the universe is nonempty. This gives a $\sigma$-structure $\mathcal{A}$.
33. The proof of step 30 uses $G_f$ only for the $f$ that occur in $\chi$. So $\mathcal{M} \models \chi^*$ if and only if $\mathcal{A} \models \chi$, for $\chi = \varphi$ and $\chi = \psi$. From $\mathcal{M} \models \varphi^*$ we get $\mathcal{A} \models \varphi$, so $\mathcal{A} \models \psi$, so $\mathcal{M} \models \psi^*$. This proves the claim.
34. Apply Part B to the $\sigma^*$-sentences $\alpha = \varphi^* \land F_\varphi$ and $\beta = F_\psi \to \psi^*$. It gives a $\sigma^*$-sentence $\theta^*$ with $\alpha \models \theta^* \models \beta$ and the sign conditions for the relation symbols of $\sigma^*$.
35. For a relation symbol $R$ of $\sigma$, the sentences $F_\varphi$ and $F_\psi$ do not contain $R$, and $\psi^*$ is on the right of $\to$ in $\beta$. By step 29, $R \in \operatorname{Pos}(\alpha)$ if and only if $R \in \operatorname{Pos}(\varphi)$, and $R \in \operatorname{Pos}(\beta)$ if and only if $R \in \operatorname{Pos}(\psi)$, and likewise for $\operatorname{Neg}$. So $\theta^*$ satisfies properties 2 and 3 for the relation symbols of $\sigma$.
36. The symbol $G_f$ occurs in $\alpha$ only if $f$ occurs in $\varphi$, and in $\beta$ only if $f$ occurs in $\psi$. A symbol of $\theta^*$ occurs with some sign, so it occurs in $\alpha$ and in $\beta$ by Part B. So if $G_f$ occurs in $\theta^*$, then $f$ occurs in $\varphi$ and in $\psi$.
37. Let $\theta$ be $\theta^*$ with each atomic formula $G_f u_1 \cdots u_m v$ replaced by $f u_1 \cdots u_m = v$. The signs of the relation symbols of $\sigma$ do not change, and every function symbol of $\theta$ occurs in $\varphi$ and in $\psi$, by step 36. For every $\sigma$-structure $\mathcal{A}$, the atomic formulas $G_f \bar u v$ in $\mathcal{A}^*$ and $f \bar u = v$ in $\mathcal{A}$ have the same truth value, so $\mathcal{A}^* \models \theta^*$ if and only if $\mathcal{A} \models \theta$.
38. We show $\varphi \models \theta$. Let $\mathcal{A} \models \varphi$. By step 30, $\mathcal{A}^* \models \varphi^*$, and $\mathcal{A}^* \models F_\varphi$ since each $G_f$ is a graph. So $\mathcal{A}^* \models \theta^*$, and $\mathcal{A} \models \theta$ by step 37.
39. We show $\theta \models \psi$. Let $\mathcal{A} \models \theta$. By step 37, $\mathcal{A}^* \models \theta^*$, so $\mathcal{A}^* \models \beta$. Since $\mathcal{A}^* \models F_\psi$, we get $\mathcal{A}^* \models \psi^*$, and $\mathcal{A} \models \psi$ by step 30.

Steps 24 to 26, with Part B for equality and steps 27 to 39 for function symbols, prove the theorem.

## Idea

Cut elimination gives a derivation of $\varphi \Rightarrow \psi$ in which every formula is a subformula instance of $\varphi$ or $\psi$.
Maehara's method splits each sequent of the derivation into a part that comes from $\varphi$ and a part that comes from $\psi$, and builds an interpolant for each sequent from the leaves down.
A relation symbol enters the interpolant only at an axiom $A \Rightarrow A$ whose two copies of $A$ lie in different parts, and the sign it gets there is the sign that $A$ has in both parts.
Disjunction, conjunction and quantifiers never change a sign, so the signs found at the axioms survive to the end.
This is the proof of the [[Craig interpolation theorem|E2CBFNAVZY]] with the signs tracked.

## Variants

- Lyndon's published proof (1959, Sections 4 and 5) does not use a calculus. It works with models, through a "Main Theorem" that Lyndon describes as a substitute for the results of Herbrand and Gentzen.
- Ten Cate and Comer (Section 6) prove Craig interpolation for function-free sentences without equality with a tableau calculus, by an induction on the closed tableau. The same bookkeeping of signs gives the Lyndon version.
- The propositional case is Part A without the quantifier steps 14 to 22. It gives Lyndon interpolation for [[propositional formulas|TRS2HY57EG]], with propositional variables in place of relation symbols.
