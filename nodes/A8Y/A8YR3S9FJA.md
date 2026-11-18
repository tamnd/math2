---
tag: A8YR3S9FJA
kind: proof
name: Proof of Kamp's theorem by separation
msc: ["03B44", "03C07"]
topics: [CQM9SRN8PM]
audience: research
proves: CQ0QCQK5JT
uses: [8XB117FKKV, 086QKPF0A6, 0FRXBVVR03]
methods: [0ASJVEFA9J, 0WCP0PVET6]
sources:
  - book: isbn:9780198537694
    locator: Gabbay, Hodkinson and Reynolds, Temporal Logic, volume 1
  - url: https://en.wikipedia.org/wiki/Kamp%27s_theorem
    locator: section Other expressive completeness results
---

## Proof

We prove [[Kamp's theorem|CQ0QCQK5JT]] from Gabbay's separation theorem, which we cite without proof.
Fix the class $\mathcal{K}$ of Dedekind complete linear orders, and work with all finite sets of unary predicates at once.
A $\mathrm{TL}(U, S)$ formula is *pure future* if it is a Boolean combination of formulas $A \, U \, B$ in which $A$ and $B$ contain no $S$.
It is *pure past* if it is a Boolean combination of formulas $A \, S \, B$ in which $A$ and $B$ contain no $U$.

1. Separation theorem, cited. Over $\mathcal{K}$, every $\mathrm{TL}(U, S)$ formula is equivalent to a Boolean combination of atoms, pure past formulas and pure future formulas.
2. Locality lemma. A pure future formula $C$ has the same truth value at $t$ in two structures on the same order that agree at all points $u > t$.
3. Proof of step 2. In $A \, U \, B$ at $t$ the clause only looks at points $u > t$ and $v$ with $t < v < u$. By induction on $A$ and $B$, which contain only $U$, their values at such points depend only on points after $t$.
4. Likewise, a pure past formula at $t$ depends only on the points $u < t$, and an atom at $t$ only on $t$.
5. Main claim. For every $\mathrm{FOMLO}$ formula $\varphi(x)$ with at most one free variable $x$, there is a $\mathrm{TL}(U, S)$ formula equivalent to it over $\mathcal{K}$. We prove it by induction on the quantifier depth $d$ of $\varphi$.
6. Normal form. Rename bound variables so that $x$ is never bound. Then $\varphi(x)$ is a Boolean combination of atomic formulas in $x$ alone and of formulas $\exists y\,\psi(x, y)$. Here $\psi$ has depth at most $d - 1$.
7. Atomic formulas in $x$ alone. $P(x)$ becomes $p$, $x = x$ becomes $\top$, and $x < x$ becomes $\bot$. Boolean combinations are kept.
8. Base case. For $d = 0$, step 6 has no quantified formulas, and step 7 gives the translation.
9. Induction step. It remains to treat $\theta(x) = \exists y\,\psi(x, y)$. In $\psi$, the variable $x$ occurs only in atoms $P(x)$, $x = x$, $x < x$, $x = z$, $x < z$ and $z < x$, where $z$ is another variable.
10. Removing $P(x)$. Let $P_1, \dots, P_k$ be the predicates. For each sign vector $\sigma \in \set{0, 1}^k$, let $\psi_\sigma$ be $\psi$ with each $P_i(x)$ replaced by $\top$ if $\sigma_i = 1$ and by $\bot$ otherwise. Also replace $x = x$ by $\top$ and $x < x$ by $\bot$.
11. Then $\theta(x)$ is equivalent to the disjunction over $\sigma$ of $\big(\bigwedge_{\sigma_i = 1} P_i(x) \wedge \bigwedge_{\sigma_i = 0} \neg P_i(x)\big) \wedge \exists y\,\psi_\sigma(x, y)$. This is a case split on the values of $P_i$ at $x$.
12. Removing the order atoms with $x$. Add three new unary predicates $Q_<$, $Q_=$, $Q_>$, with temporal atoms $q_<$, $q_=$, $q_>$. In $\psi_\sigma$ replace $z < x$ by $Q_<(z)$, $x = z$ and $z = x$ by $Q_=(z)$, and $x < z$ by $Q_>(z)$. Call the result $\chi_\sigma(y)$.
13. For a structure $\mathcal{M}$ and a point $t$, let $\mathcal{M}_t$ be $\mathcal{M}$ with $Q_<$, $Q_=$, $Q_>$ interpreted as $\set{u : u < t}$, $\set{t}$ and $\set{u : u > t}$.
14. By induction on the subformulas of $\psi_\sigma$, under every assignment to the other variables, and for every $u$: $\mathcal{M} \models \psi_\sigma(t, u)$ if and only if $\mathcal{M}_t \models \chi_\sigma(u)$. The atoms agree by step 13, and $x$ does not occur in $\chi_\sigma$.
15. $\chi_\sigma(y)$ has one free variable and depth at most $d - 1$. By the induction hypothesis, for the larger set of predicates, there is a $\mathrm{TL}(U, S)$ formula $A_\sigma$ equivalent to it over $\mathcal{K}$.
16. Now $\mathcal{M}_t \models \exists y\,\chi_\sigma(y)$ if and only if $A_\sigma$ holds at some point $u$, and $u < t$ or $u = t$ or $u > t$.
17. So step 16 holds if and only if $B_\sigma = (\top \, S \, A_\sigma) \vee A_\sigma \vee (\top \, U \, A_\sigma)$ is true at $t$ in $\mathcal{M}_t$.
18. By the separation theorem of step 1, $B_\sigma$ is equivalent over $\mathcal{K}$ to a Boolean combination of pure past formulas $C_j$, atoms and pure future formulas $D_l$.
19. Substitution. In each $C_j$ replace $q_<$ by $\top$ and $q_=$, $q_>$ by $\bot$, giving $C_j'$. In each $D_l$ replace $q_>$ by $\top$ and $q_<$, $q_=$ by $\bot$, giving $D_l'$. Replace the atom $q_=$ by $\top$ and $q_<$, $q_>$ by $\bot$.
20. Correctness of step 19. In $\mathcal{M}_t$, every point $u < t$ has $Q_<$ true and the others false. By step 4, $C_j$ at $t$ in $\mathcal{M}_t$ has the same value as $C_j'$ at $t$ in $\mathcal{M}_t$. As $C_j'$ mentions no new predicate, this is its value in $\mathcal{M}$.
21. The same argument with step 2 handles the $D_l$, and at $t$ itself only $Q_=$ is true.
22. Let $E_\sigma$ be the result of step 19. It mentions only the original predicates, and $E_\sigma$ is true at $t$ in $\mathcal{M}$ if and only if $\mathcal{M} \models \exists y\,\psi_\sigma(t, y)$, by steps 14 to 21.
23. By step 11, $\theta(x)$ is equivalent to the disjunction over $\sigma$ of $\big(\bigwedge_{\sigma_i = 1} p_i \wedge \bigwedge_{\sigma_i = 0} \neg p_i\big) \wedge E_\sigma$. This completes the induction.
24. The translation of each step does not depend on the order in $\mathcal{K}$. This gives the uniformity claimed in the theorem.

## Idea

A quantifier over points is the only thing that temporal logic lacks.
Split the quantified point into the cases "before now", "now" and "after now", and mark these regions with three new predicates.
The induction hypothesis gives a temporal formula, and separation splits it into parts that each see only one region.
In each part the new predicates are constant, so they can be replaced by $\top$ or $\bot$.

## Variants

1. Rabinovich (2014) gives a short self-contained proof.
2. For $(\mathbb{N}, <)$ and future formulas evaluated at $0$, Gabbay, Pnueli, Shelah and Stavi gave a proof in 1980.
