---
tag: 5TR5B71JGM
kind: proof
name: Proof of the Skolem normal form theorem
msc: ["03B10", "03C07"]
topics: [PSRDJXRW53]
audience: ug2
proves: Q5H7C57VNH
uses: [GCPQGMJYEV, EZ8NCHN7SJ, CS82V969DE, NCDZ969V7X, 983GZBQYT4, 2RBQPV02AS, 0HTGB13FE2, B37TYWXS74]
methods: [0ASJVEFA9J, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
    locator: lead section
---

## Proof

We first prove both parts for a single Skolemization step, and then chain the steps by induction on the number of existential quantifiers in the prefix.

Let $\varphi = \forall x_1 \cdots \forall x_k \, \exists y \, \chi$ be a prenex $\sigma$-sentence with distinct prefix variables, where $\chi$ is prenex.
Let $f$ be a $k$-ary function symbol not in $\sigma$, a constant symbol when $k = 0$.
Let $\varphi' = \forall x_1 \cdots \forall x_k \, \chi[f(x_1, \dots, x_k)/y]$, a sentence over $\sigma' = \sigma \cup \{ f \}$.
Write $\bar{x}$ for $x_1, \dots, x_k$, and $\bar{a}$ for a tuple $a_1, \dots, a_k$ of elements.

1. The term $f(\bar{x})$ is [[substitutable|NCDZ969V7X]] for $y$ in $\chi$.
   Reason: the quantifiers of $\chi$ bind variables different from $x_1, \dots, x_k$, because the prefix variables of $\varphi$ are distinct.
2. Let $\mathcal{N}$ be a $\sigma'$-[[structure|983GZBQYT4]] and let $s$ be an assignment with $s(x_i) = a_i$.
   Then $\mathcal{N} \models \chi[f(\bar{x})/y][s]$ holds exactly when $\mathcal{N} \models \chi[s(y \mid f^{\mathcal{N}}(\bar{a}))]$.
   Reason: step 1 and the substitution lemma of [[structures, satisfaction and truth|NJDME6F845]].
3. Claim (a): if $\mathcal{N} \models \varphi'$, then $\mathcal{N} \models \varphi$.
   Let $\bar{a}$ be any tuple.
   Since $\mathcal{N} \models \varphi'$, the formula $\chi[f(\bar{x})/y]$ holds at $\bar{a}$.
4. By step 2, $\chi$ holds at $\bar{a}$ with $y$ given the value $b = f^{\mathcal{N}}(\bar{a})$.
   So $\exists y \, \chi$ holds at $\bar{a}$, by the clause for $\exists$ of [[satisfaction|2RBQPV02AS]].
5. This holds for every $\bar{a}$, so $\mathcal{N} \models \forall \bar{x} \, \exists y \, \chi$, that is, $\mathcal{N} \models \varphi$.
   This proves claim (a).
6. Claim (b): if a $\sigma$-structure $\mathcal{M}$ satisfies $\varphi$, then some expansion $\mathcal{M}'$ of $\mathcal{M}$ to $\sigma'$ satisfies $\varphi'$.
   For each $\bar{a} \in M^k$, let $W(\bar{a})$ be the set of $b \in M$ such that $\chi$ holds in $\mathcal{M}$ at $\bar{a}$ with $y = b$.
7. Each $W(\bar{a})$ is nonempty.
   Reason: $\mathcal{M} \models \varphi$, so $\exists y \, \chi$ holds at every $\bar{a}$.
8. By the [[axiom of choice|0HTGB13FE2]], there is a function $F \colon M^k \to M$ with $F(\bar{a}) \in W(\bar{a})$ for every $\bar{a}$.
   For $k = 0$, the set $M^0$ has one element, and one choice suffices.
9. Let $\mathcal{M}'$ be $\mathcal{M}$ with $f$ interpreted as $F$.
   The formula $\chi$ does not contain $f$, so it has the same truth value in $\mathcal{M}$ and in $\mathcal{M}'$ under every assignment.
   Reason: the truth of a formula depends only on the interpretations of the symbols in it.
10. For each $\bar{a}$, $\chi$ holds in $\mathcal{M}'$ at $\bar{a}$ with $y = F(\bar{a}) = f^{\mathcal{M}'}(\bar{a})$, by steps 8 and 9.
    By step 2, $\chi[f(\bar{x})/y]$ holds in $\mathcal{M}'$ at $\bar{a}$.
11. So $\mathcal{M}' \models \varphi'$.
    This proves claim (b).
12. The sentence $\varphi'$ is again prenex with distinct prefix variables, and its prefix has one $\exists$ fewer than that of $\varphi$.
    Reason: the substitution changes only the matrix, and the prefix of $\varphi'$ is $\forall \bar{x}$ followed by the prefix of $\chi$.
13. Let $\varphi = \varphi_0, \varphi_1, \dots, \varphi_m = \varphi^S$ be the sentences of the repeated Skolemization, over $\sigma = \sigma_0 \subseteq \sigma_1 \subseteq \dots \subseteq \sigma_m = \sigma^S$.
    Here $m$ is the number of $\exists$ in the prefix of $\varphi$, by step 12.
14. Part 1.
    Let $\mathcal{N} \models \varphi_m$.
    By claim (a) and [[induction|0ASJVEFA9J]] downwards from $j = m$, the reduct of $\mathcal{N}$ to $\sigma_j$ satisfies $\varphi_j$ for each $j$.
    Reason: the truth of a $\sigma_j$-sentence does not change when we pass to the reduct to $\sigma_j$.
    For $j = 0$ this is part 1.
15. Part 2.
    Let $\mathcal{M} \models \varphi_0$.
    By claim (b) and induction upwards on $j$, there are expansions $\mathcal{M}_j$ of $\mathcal{M}$ to $\sigma_j$ with $\mathcal{M}_j \models \varphi_j$.
    For $j = m$ this is part 2, and $\mathcal{M}_m$ has the domain $M$.
16. Part 3.
    If $\varphi^S$ has a model, then it is a model of $\varphi$, by part 1.
    If $\varphi$ has a model $\mathcal{M}$, then $\mathcal{M}_m$ is a model of $\varphi^S$, by part 2.
    So $\varphi$ and $\varphi^S$ are [[equisatisfiable|B37TYWXS74]].

## Idea

A sentence $\forall \bar{x} \, \exists y \, \chi$ says that a witness $y$ exists for each $\bar{x}$.
A Skolem function names one witness for each $\bar{x}$, and the axiom of choice picks it.
The new sentence implies the old one, because the named witness is a witness.
Each step removes one $\exists$, so finitely many steps reach a universal sentence.

## Variants

All the existential quantifiers can be Skolemized at once.
The function for each $\exists y$ takes as arguments the universal variables to the left of $\exists y$, and the result is the same up to the names of the symbols.

For a countable $\mathcal{M}$, fix an enumeration of $M$ and let $F(\bar{a})$ be the first element of $W(\bar{a})$.
This avoids the axiom of choice in step 8.

Part 3 alone needs no choice when $\sigma$ is countable.
If $\varphi$ has a model, then it is consistent, and the proof of the completeness theorem gives a countable model, to which the enumeration argument applies.
