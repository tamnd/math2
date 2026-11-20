---
tag: BZBJ6SP2M6
kind: proof
name: Proof of the isomorphism theorems for algebraizable logics
msc: ["03G27", "08C15"]
topics: [QYA4H5Y7VR]
audience: research
proves: 8ZFJ67HTWR
uses: [XADWEW9TNP, WRXEKT4NQS, DCSXXT4SER]
methods: [0NTF6DMVAP, TFQ1845T84, MKHVRNW68H]
sources:
  - book: isbn:9781848902077
---

## Proof

We prove parts 1, 3 and 4; part 2 is cited from Blok and Pigozzi.
By structurality, (A2) gives $\varphi \approx \psi \models_K E[\Delta(\varphi, \psi)]$ and back, for all formulas $\varphi, \psi$; we use this as (A2).

**Part 1.**

1. For a set $\Theta$ of equations let $\equiv_\Theta = \set{(\alpha, \beta) : \Theta \models_K \alpha \approx \beta}$. It is a congruence, since $\models_K$ is preserved by the operations.
2. For each $(\alpha, \beta) \notin {\equiv_\Theta}$ choose $A \in K$ and $h : \mathrm{Fm} \to A$ that satisfy $\Theta$ with $h(\alpha) \ne h(\beta)$. The product of these maps embeds $\mathrm{Fm}/{\equiv_\Theta}$ in a product of members of $K$, so $\mathrm{Fm}/{\equiv_\Theta} \in K$.
3. Let $T$ be a theory. By (A2) and (A1), $(\varphi, \psi) \in {\equiv_{E[T]}}$ iff $E[T] \models_K E[\Delta(\varphi, \psi)]$ iff $T \vdash \Delta(\varphi, \psi)$ iff $\Delta(\varphi, \psi) \subseteq T$. So $\theta_T = {\equiv_{E[T]}}$ is a $K$-congruence.
4. Let $\theta$ be a $K$-congruence and $T_\theta = \set{\varphi : E(\varphi) \subseteq \theta}$. If $T_\theta \vdash \varphi$, then $E[T_\theta] \models_K E(\varphi)$ by (A1). The quotient map into $\mathrm{Fm}/\theta \in K$ satisfies $E[T_\theta]$, so it satisfies $E(\varphi)$, and $\varphi \in T_\theta$. So $T_\theta$ is a theory.
5. $T_{\theta_T} = \set{\varphi : E[T] \models_K E(\varphi)} = T$ by step 3 and (A1).
6. $(\varphi, \psi) \in \theta_{T_\theta}$ iff $E[\Delta(\varphi, \psi)] \subseteq \theta$ iff $(\varphi, \psi) \in \theta$, by (A2) applied to the quotient map. So $\theta_{T_\theta} = \theta$.
7. Both maps preserve inclusion, so they are inverse lattice isomorphisms.

**Part 3.**

8. For a subquasivariety $K'$, the relation $\vdash_{K'}$ is structural and contains $\vdash$, since $K' \subseteq K$. It is finitary since $E$ is finite and $\models_{K'}$ is finitary for a quasivariety.
9. (A2) holds in $K'$, so $\Psi \models_{K'} \varepsilon \approx \delta$ iff $\Delta[\Psi] \vdash_{K'} \Delta(\varepsilon, \delta)$. So $\vdash_{K'}$ determines the quasi-identities of $K'$, and $K'$ itself. The map is injective and reverses order in both directions.
10. Let $\vdash'$ be a finitary extension, and let $K'$ be the class of $A \in K$ that satisfy the quasi-identities $\bigwedge E[\Gamma] \to \varepsilon \approx \delta$ for finite $\Gamma \vdash' \varphi$ and $\varepsilon \approx \delta$ in $E(\varphi)$. It is a subquasivariety, and $\vdash' \subseteq \vdash_{K'}$.
11. Let $E[\Gamma] \models_{K'} E(\varphi)$, and let $T$ be the $\vdash'$-theory of $\Gamma$; it is a $\vdash$-theory. Every homomorphism into $\mathrm{Fm}/\theta_T$ is the quotient map after a substitution $\sigma$. If it satisfies $E[\Gamma_0]$ with $\Gamma_0 \vdash' \psi$, then $\sigma[\Gamma_0] \subseteq T$ by step 5, so $\sigma(\psi) \in T$ and it satisfies $E(\psi)$. So $\mathrm{Fm}/\theta_T \in K'$.
12. The quotient map satisfies $E[\Gamma]$, so it satisfies $E(\varphi)$, and $\varphi \in T$ by step 5. So $\Gamma \vdash' \varphi$, and $\vdash' = {\vdash_{K'}}$.

**Part 4.** If $\vdash'$ is $\vdash$ plus a set $X$ of axioms closed under substitution, steps 10 to 12 give $K' = \set{A \in K : A \models E[X]}$.
Conversely, the class of $A \in K$ satisfying a set $\Psi$ of equations corresponds to $\vdash$ plus the axioms $\Delta[\sigma[\Psi]]$ for all substitutions $\sigma$.
Indeed, a homomorphism $h$ into $A \in K$ satisfies every substitution instance of $\Psi$ iff the subalgebra $h[\mathrm{Fm}] \in K$ satisfies $\Psi$, and (A2), (A1) turn these instances into the axioms.
$\blacksquare$

## Idea

The translations $E$ and $\Delta$ turn formulas into equations and back, and (A1) and (A2) say that nothing is lost.
So theories, which are sets of formulas closed under $\vdash$, become sets of equations closed under $\models_K$, which are $K$-congruences.
Extensions of $\vdash$ become stronger equational consequence relations, which are given by smaller quasivarieties.

## Variants

1. Part 1 holds for any logic and any $K$ closed under subalgebras and products, without finitarity.
2. One route to part 2 shows that the $K$-congruences of $\mathrm{Fm}$ are the Leibniz congruences of the theories, which depend only on $\vdash$; two quasivarieties with the same relative congruences on $\mathrm{Fm}$ have the same quasi-identities.
