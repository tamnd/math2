---
tag: FHZPY6GVPG
kind: proof
name: Proof that reduced products preserve Horn formulas by induction
msc: ["03C20"]
topics: [HZG1YP26AB]
audience: grad
proves: 8RRECJJM3G
uses: [F4WRD396PB, 84XXPH6XJ8, 15PF73BKY6, 0HTGB13FE2]
methods: [12MQ2NJ29A, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Reduced_product
    locator: lead section
---

## Proof

Write $\mathcal{P} = \prod_{i \in I} \mathcal{M}_i / F$ and $[\![ \varphi(a) ]\!] = \set{i \in I : \mathcal{M}_i \models \varphi(a(i))}$ for a tuple $a$ of elements of $\prod_{i \in I} M_i$.
We prove by [[structural induction|12MQ2NJ29A]] on Horn formulas $\varphi$ the claim: for every tuple $a$, if $[\![ \varphi(a) ]\!] \in F$, then $\mathcal{P} \models \varphi([a])$.

1. *Terms.* For a term $t$, the value $t^{\mathcal{P}}([a])$ is the class of the function $i \mapsto t^{\mathcal{M}_i}(a(i))$. This follows by induction on $t$ from clauses 1 and 3 of the [[definition|84XXPH6XJ8]].
2. *Atomic formulas.* By step 1, $t_1 = t_2$ holds in $\mathcal{P}$ at $[a]$ exactly when $[\![ t_1(a) = t_2(a) ]\!] \in F$. For $R(t_1, \dots, t_k)$ the same holds by clause 2. So for atomic $\alpha$: $\mathcal{P} \models \alpha([a])$ if and only if $[\![ \alpha(a) ]\!] \in F$.
3. *Basic Horn formulas, case $\lnot\alpha_1 \lor \dots \lor \lnot\alpha_m \lor \beta$ with $m \ge 1$.* The case $m = 0$ is step 2. Let $X = [\![ \varphi(a) ]\!] \in F$. If some $\alpha_k$ fails in $\mathcal{P}$ at $[a]$, then $\lnot\alpha_k$ holds and so does $\varphi$.
4. Otherwise every $\alpha_k$ holds in $\mathcal{P}$, so $Y_k = [\![ \alpha_k(a) ]\!] \in F$ by step 2. Then $Z = X \cap Y_1 \cap \dots \cap Y_m \in F$, because $F$ is closed under finite intersections.
5. For $i \in Z$ all $\alpha_k$ hold in $\mathcal{M}_i$, and the disjunction holds, so $\beta$ holds. So $[\![ \beta(a) ]\!] \supseteq Z$ lies in $F$, and $\mathcal{P} \models \beta([a])$ by step 2.
6. *Basic Horn formulas, case $\lnot\alpha_1 \lor \dots \lor \lnot\alpha_m$.* Suppose every $\alpha_k$ holds in $\mathcal{P}$. Then the set $Z$ of step 4 lies in $F$. For $i \in Z$ all $\alpha_k$ hold in $\mathcal{M}_i$, so the disjunction fails at $i$, although $i \in X$.
7. So $Z = \emptyset$, and $\emptyset \in F$, which a filter excludes. Hence some $\alpha_k$ fails in $\mathcal{P}$, and $\varphi$ holds there.
8. *Conjunction.* $[\![ (\varphi \land \psi)(a) ]\!] = [\![ \varphi(a) ]\!] \cap [\![ \psi(a) ]\!]$. If it lies in $F$, both larger sets lie in $F$, and the induction hypothesis gives $\varphi$ and $\psi$ in $\mathcal{P}$.
9. *Existential quantifier $\exists y \, \psi(a, y)$.* Let $X = [\![ \exists y \, \psi(a, y) ]\!] \in F$. For $i \in X$ choose $b(i) \in M_i$ with $\mathcal{M}_i \models \psi(a(i), b(i))$; for $i \notin X$ choose any $b(i) \in M_i$. This uses the [[axiom of choice|0HTGB13FE2]] and $M_i \neq \emptyset$.
10. Then $[\![ \psi(a, b) ]\!] \supseteq X$, so it lies in $F$. The induction hypothesis gives $\mathcal{P} \models \psi([a], [b])$, so $\mathcal{P} \models \exists y \, \psi([a], y)$.
11. *Universal quantifier $\forall y \, \psi(a, y)$.* Let $X = [\![ \forall y \, \psi(a, y) ]\!] \in F$, and let $[b]$ be any element of $\mathcal{P}$. For $i \in X$, $\mathcal{M}_i \models \psi(a(i), b(i))$, so $[\![ \psi(a, b) ]\!] \supseteq X$ lies in $F$.
12. The induction hypothesis gives $\mathcal{P} \models \psi([a], [b])$. Since $[b]$ was arbitrary, $\mathcal{P} \models \forall y \, \psi([a], y)$.

Steps 2 to 12 cover every way to build a Horn formula, so the claim holds for every Horn formula.
For a Horn sentence true in every factor, the truth set is $I \in F$, so the sentence holds in $\mathcal{P}$.

## Idea

Atomic facts pass to the reduced product exactly when they hold on a set in the filter.
A Horn formula has at most one positive conclusion in each basic part, so we never need to choose between two conclusions, and the closure of $F$ under intersections is enough.
Quantifiers are handled by choosing witnesses coordinate by coordinate.
Negation in general is not handled, and this is where a filter that is not an ultrafilter fails.

## Variants

For an ultrafilter the same induction also handles negation and disjunction, and it gives [[Łoś's theorem|AGYBSTD7BG]].
For finite index sets, step 9 needs no axiom of choice, since only finitely many choices are made.
