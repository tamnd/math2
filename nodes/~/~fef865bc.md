---
tag: ~fef865bc
kind: proof
name: Proof of Herbrand's theorem by cut elimination
msc: ["03F05", "03B10"]
topics: [FBWW4J1XWG]
audience: grad
proves: VZ21F10WRS
uses: [W72CA3R9MP, AYRZ98Y0NW, WQ1ZE255SF, 05006AJ7DZ, 6D3WA7N2W4]
methods: [0NTF6DMVAP, 0ASJVEFA9J, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand's_theorem
    locator: Proof sketch
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
    locator: lead section
---

## Proof

Let $\sigma$ be a signature without equality that has at least one constant symbol $c$.
Let $\psi$ be a quantifier-free formula whose free variables are among $x_1, \dots, x_n$.
We prove: if $\exists x_1 \cdots \exists x_n \, \psi$ is valid, then some disjunction $\psi(\bar t_1) \lor \cdots \lor \psi(\bar t_k)$ with $k \ge 1$ and closed terms is a [[tautology|05006AJ7DZ]].
The other direction is steps 4 to 7 of the [[proof by compactness|~e4acb6a6]], and it is repeated at the end.

Setup: the calculus.
We use the [[sequent calculus|W72CA3R9MP]] LK with the primitive symbols $\neg, \land, \lor, \to, \forall, \exists$.
A sequent is $\Gamma \Rightarrow \Delta$ with finite multisets $\Gamma$ and $\Delta$ of formulas.
The rules are the following, written as "premises / conclusion".

- Axiom: $A \Rightarrow A$ for atomic $A$.
- Weakening: $\Gamma \Rightarrow \Delta$ / $A, \Gamma \Rightarrow \Delta$, and $\Gamma \Rightarrow \Delta$ / $\Gamma \Rightarrow \Delta, A$.
- Contraction: $A, A, \Gamma \Rightarrow \Delta$ / $A, \Gamma \Rightarrow \Delta$, and $\Gamma \Rightarrow \Delta, A, A$ / $\Gamma \Rightarrow \Delta, A$.
- $\neg$L: $\Gamma \Rightarrow \Delta, A$ / $\neg A, \Gamma \Rightarrow \Delta$. $\neg$R: $A, \Gamma \Rightarrow \Delta$ / $\Gamma \Rightarrow \Delta, \neg A$.
- $\land$L: $A, B, \Gamma \Rightarrow \Delta$ / $A \land B, \Gamma \Rightarrow \Delta$. $\land$R: $\Gamma \Rightarrow \Delta, A$ and $\Gamma \Rightarrow \Delta, B$ / $\Gamma \Rightarrow \Delta, A \land B$.
- $\lor$L: $A, \Gamma \Rightarrow \Delta$ and $B, \Gamma \Rightarrow \Delta$ / $A \lor B, \Gamma \Rightarrow \Delta$. $\lor$R: $\Gamma \Rightarrow \Delta, A, B$ / $\Gamma \Rightarrow \Delta, A \lor B$.
- $\to$L: $\Gamma \Rightarrow \Delta, A$ and $B, \Gamma \Rightarrow \Delta$ / $A \to B, \Gamma \Rightarrow \Delta$. $\to$R: $A, \Gamma \Rightarrow \Delta, B$ / $\Gamma \Rightarrow \Delta, A \to B$.
- $\forall$L: $A^x_t, \Gamma \Rightarrow \Delta$ / $\forall x A, \Gamma \Rightarrow \Delta$. $\exists$R: $\Gamma \Rightarrow \Delta, A^x_t$ / $\Gamma \Rightarrow \Delta, \exists x A$. In both, $t$ is any term substitutable for $x$ in $A$.
- $\forall$R: $\Gamma \Rightarrow \Delta, A^x_a$ / $\Gamma \Rightarrow \Delta, \forall x A$. $\exists$L: $A^x_a, \Gamma \Rightarrow \Delta$ / $\exists x A, \Gamma \Rightarrow \Delta$. In both, the eigenvariable $a$ is not free in the conclusion.
- Cut: $\Gamma \Rightarrow \Delta, C$ and $C, \Gamma \Rightarrow \Delta$ / $\Gamma \Rightarrow \Delta$.

This form of the rules derives the same sequents without cut as Gentzen's form, because weakening and contraction turn each form of a rule into the other.
A sequent is valid when, in every structure and under every assignment to the variables, some member of $\Gamma$ is false or some member of $\Delta$ is true.
We use one fact (F): every valid sequent has a derivation in LK without cut.
It combines the completeness of LK, which follows from [[Gödel's completeness theorem|WQ1ZE255SF]], with the [[cut-elimination theorem|AYRZ98Y0NW]].

Setup: instances and tautological sequents.
For $1 \le j \le n$ and terms $u_1, \dots, u_{j-1}$, a partial instance of level $j$ is the formula $\exists x_j \cdots \exists x_n \, \psi(u_1, \dots, u_{j-1}, x_j, \dots, x_n)$.
The terms may contain variables, and they are substitutable, as the rule $\exists$R requires.
Its full instances are the quantifier-free formulas $\psi(u_1, \dots, u_{j-1}, s_j, \dots, s_n)$ for terms $s_j, \dots, s_n$.
The partial instance of level $1$ is $\exists \bar x \, \psi$ itself.
In a quantifier-free formula we read each atomic formula, with or without variables, as a propositional variable.
A sequent of quantifier-free formulas holds under a truth assignment $v$ when $v$ makes some member of $\Gamma$ false or some member of $\Delta$ true.
It is tautological when it holds under every truth assignment.

Part 1: the shape of a cut-free derivation.

1. Assume that $\exists \bar x \, \psi$ is valid. Then the sequent $\Rightarrow \exists \bar x \, \psi$ is valid, and by (F) it has a cut-free derivation $D$.
2. Say that a sequent has property (P) when every formula of its antecedent is quantifier-free, and every formula of its succedent is quantifier-free or a partial instance.
3. The end sequent $\Rightarrow \exists \bar x \, \psi$ has (P), since its succedent is the partial instance of level $1$.
4. We show: if the conclusion of a rule in $D$ has (P), then each premise has (P). Then every sequent of $D$ has (P), by [[induction|0ASJVEFA9J]] on the distance from the end sequent.
5. Weakening and contraction: each formula of a premise is a formula of the conclusion, on the same side.
6. $\neg$L, $\land$L, $\lor$L, $\to$L: the principal formula is in the antecedent of the conclusion, so it is quantifier-free, and so are its parts $A$ and $B$. In each premise these parts stand on a side where quantifier-free formulas are allowed.
7. $\neg$R, $\land$R, $\lor$R, $\to$R: the principal formula is in the succedent and does not begin with $\exists$. So it is not a partial instance, and it is quantifier-free. Its parts are quantifier-free, and (P) allows them on both sides.
8. $\forall$L and $\exists$L: the principal formula is in the antecedent and has a quantifier, against (P). So these rules do not occur in $D$.
9. $\forall$R: the principal formula $\forall x A$ is in the succedent, and it is neither quantifier-free nor a partial instance. So this rule does not occur in $D$.
10. $\exists$R: the principal formula is in the succedent, so it is a partial instance $\exists x_j \cdots \exists x_n \, \psi(u_1, \dots, u_{j-1}, x_j, \dots, x_n)$ with $x = x_j$. The premise contains it with $x_j$ replaced by a term $t$. For $j < n$ this is a partial instance of level $j + 1$, with $u_j = t$. For $j = n$ it is the full instance $\psi(u_1, \dots, u_{n-1}, t)$, which is quantifier-free.
11. Axioms have no premises, and cut does not occur in $D$. By steps 5 to 10, every sequent of $D$ has (P). In particular, $D$ has no eigenvariables, because $\forall$R and $\exists$L do not occur.

Part 2: replacing partial instances by finite sets of full instances.

12. Each sequent $S$ of $D$ can be written as $\Gamma \Rightarrow \Delta_0, E_1, \dots, E_m$, where $\Gamma$ and $\Delta_0$ are quantifier-free and $E_1, \dots, E_m$ are occurrences of partial instances. This uses step 11.
13. Claim (M): there are finite sets $I_1, \dots, I_m$, where $I_i$ consists of full instances of $E_i$, such that the sequent $\Gamma \Rightarrow \Delta_0, I_1, \dots, I_m$ is tautological. We prove (M) by induction on the height of the part of $D$ that ends in $S$.
14. A tool for the propositional rules (T): fix a truth assignment $v$, and assume all formulas involved are quantifier-free. If $v$ makes each premise hold, then $v$ makes the conclusion hold. We check this rule by rule in steps 15 to 19.
15. Weakening and contraction: the conclusion has the same set of formulas on each side as the premise, or more.
16. $\neg$L: if $v$ makes $\neg A$ and all of $\Gamma$ true, then $A$ is false, so the premise gives a true member of $\Delta$. $\neg$R: if $\Gamma$ is true and $\Delta$ is false, the premise makes $A$ false, so $\neg A$ is true.
17. $\land$L: a true $A \land B$ makes $A$ and $B$ true, and the premise applies. $\land$R: if $\Gamma$ is true and $\Delta$ is false, the premises make $A$ and $B$ true, so $A \land B$ is true.
18. $\lor$L: a true $A \lor B$ makes $A$ or $B$ true, and the matching premise applies. $\lor$R: the premise gives a true member of $\Delta$, or $A$ or $B$ is true.
19. $\to$L: let $A \to B$ and $\Gamma$ be true and $\Delta$ false. The first premise makes $A$ true, then $B$ is true, and the second premise gives a contradiction. $\to$R: if $\Gamma$ is true, $\Delta$ is false and $A$ is true, the premise makes $B$ true; so $A \to B$ is true.
20. Case of an axiom $A \Rightarrow A$: here $m = 0$, and the sequent is tautological, since $v$ makes $A$ false or true.
21. Case of weakening that adds a partial instance $E$: put $I = \emptyset$ for $E$, and keep the sets of the premise. The new sequent is the one of the premise.
22. Case of contraction of two occurrences of a partial instance $E$ with sets $I$ and $I'$: put $I \cup I'$ for $E$. The new sequent has the same formulas as the one of the premise, so it is tautological.
23. Case of any other rule except $\exists$R (a propositional rule, or weakening or contraction of a quantifier-free formula): by steps 6 and 7 the principal formula and its parts are quantifier-free. Each partial instance of the conclusion is a side formula, and it occurs in each premise.
24. For each such $E_i$, let $I_i$ be the union of its sets in the premises. Adding formulas to a tautological sequent keeps it tautological, so each premise stays tautological with the sets $I_i$.
25. Treat the formulas of the sets $I_i$ as extra side formulas of the rule. By (T), every $v$ that makes the premises hold makes the conclusion hold. So the conclusion with the sets $I_i$ is tautological.
26. Case of $\exists$R with principal formula $E$ of level $j < n$: the premise contains the partial instance $E'$ of level $j + 1$ from step 10, with a set $I$. Each full instance of $E'$ is a full instance of $E$, because $E'$ fixes one more term. Put $I$ for $E$. The new sequent is the one of the premise.
27. Case of $\exists$R with principal formula $E$ of level $n$: the premise contains the full instance $\psi(u_1, \dots, u_{n-1}, t)$ as a member of its $\Delta_0$. Put $I = \{\psi(u_1, \dots, u_{n-1}, t)\}$ for $E$. The new sequent is again the one of the premise.
28. By steps 20 to 27 and induction, (M) holds for every sequent of $D$.

Part 3: the Herbrand disjunction.

29. Apply (M) to the end sequent $\Rightarrow \exists \bar x \, \psi$. Here $\Gamma$ and $\Delta_0$ are empty and $m = 1$. We get a finite set $I = \{\psi(\bar s_1), \dots, \psi(\bar s_k)\}$ with $\Rightarrow I$ tautological.
30. We have $k \ge 1$, because the empty sequent $\Rightarrow$ holds under no truth assignment.
31. A sequent $\Rightarrow \delta_1, \dots, \delta_k$ holds under $v$ exactly when $v$ makes $\delta_1 \lor \cdots \lor \delta_k$ true. So $\delta = \psi(\bar s_1) \lor \cdots \lor \psi(\bar s_k)$ is a tautology.
32. The terms in $\bar s_i$ may contain free variables. For a quantifier-free formula $\chi$, let $\chi^c$ be the result of replacing every variable by the constant $c$. Let $\bar t_i$ be $\bar s_i$ with every variable replaced by $c$. Then $\delta^c = \psi(\bar t_1) \lor \cdots \lor \psi(\bar t_k)$, because the free variables of $\psi(\bar s_i)$ all lie in the terms $\bar s_i$.
33. Let $w$ be a truth assignment to the atomic sentences. Define $v(\alpha) = w(\alpha^c)$ for every atomic formula $\alpha$.
34. By induction on $\chi$, $\bar v(\chi) = \bar w(\chi^c)$ for every quantifier-free $\chi$: the atomic case is step 33, and the substitution commutes with the connectives.
35. So $\bar w(\delta^c) = \bar v(\delta) = T$ by step 31. Since $w$ was arbitrary, $\psi(\bar t_1) \lor \cdots \lor \psi(\bar t_k)$ is a tautology with closed terms $\bar t_i$.

The converse.

36. If $\psi(\bar t_1) \lor \cdots \lor \psi(\bar t_k)$ is a tautology, it is true in every structure $\mathcal{A}$, under the truth values that $\mathcal{A}$ gives to atomic sentences. So some $\psi(\bar t_i)$ is true in $\mathcal{A}$, and $\mathcal{A} \models \exists \bar x \, \psi$ with the witnesses $t_{i,1}^{\mathcal{A}}, \dots, t_{i,n}^{\mathcal{A}}$.

Steps 1 to 35 and step 36 prove Herbrand's theorem.

## Idea

In a cut-free derivation of $\Rightarrow \exists \bar x \, \psi$, every formula is a subformula of the end sequent in Gentzen's sense, so the only quantifier rules are applications of $\exists$R in the succedent.
Each $\exists$R inference chooses a term, and each $\exists$R on a formula of level $n$ produces one full instance.
Collecting these instances, with unions at contractions, turns the derivation into a propositional derivation of the Herbrand disjunction.
Free variables in the chosen terms are harmless, because replacing them by a constant keeps a tautology a tautology.

## Variants

- The proof gives a bound: the number $k$ of instances is at most the number of $\exists$R inferences on formulas of level $n$ in $D$. So the Herbrand complexity is at most the number of $\exists$R inferences of any cut-free derivation.
- Gentzen's midsequent theorem gives the same result for all prenex sentences: a cut-free derivation of a prenex sequent can be rearranged so that all quantifier inferences come below one quantifier-free sequent.
- The [[proof by compactness|~e4acb6a6]] is shorter, but it is not constructive. The proof here computes the terms from a cut-free derivation, and cut elimination is itself an algorithm.
