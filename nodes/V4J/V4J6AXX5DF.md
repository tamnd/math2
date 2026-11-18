---
tag: V4J6AXX5DF
kind: proof
name: Proof of soundness of normal modal logics
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
proves: E87G6ZTMTN
uses: [JS8W7PA6JK, 6BQ71KQ6QT, 05006AJ7DZ, 12MQ2NJ29A]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Proof

We prove part 1 of [[soundness of normal modal logics|E87G6ZTMTN]], that $\operatorname{Log}(\mathsf{C})$ satisfies the five properties of a [[normal modal logic|JS8W7PA6JK]].
Then we derive part 2.
It suffices to show each property for the set $\operatorname{Log}(\mathfrak{F})$ of formulas valid on one frame $\mathfrak{F} = (W, R)$, since an intersection of normal logics is normal.

1. Tautologies. Let $\varphi = \tau^\sigma$ with $\tau$ a [[tautology|05006AJ7DZ]]. At a world $w$ of a model on $\mathfrak{F}$, the clauses for $\bot$ and $\to$ are the classical truth tables.
2. So $\varphi$ has at $w$ the truth value that $\tau$ gets when each variable $q$ of $\tau$ takes the value of $\sigma(q)$ at $w$. This value is "true", since $\tau$ is a tautology.
3. Axiom $\mathrm{K}$. Let $\mathfrak{M}$ be a model on $\mathfrak{F}$, and let $w \models \square(p \to q)$ and $w \models \square p$.
4. Let $w R v$. Then $v \models p \to q$ and $v \models p$, by the clause for $\square$.
5. So $v \models q$ by the clause for $\to$. As $v$ was any successor of $w$, we get $w \models \square q$.
6. Modus ponens. Let $\varphi$ and $\varphi \to \psi$ be valid on $\mathfrak{F}$. At each world of each model on $\mathfrak{F}$ both are true, so $\psi$ is true there.
7. Necessitation. Let $\varphi$ be valid on $\mathfrak{F}$, let $\mathfrak{M}$ be a model on $\mathfrak{F}$, and let $w \in W$.
8. Every successor $v$ of $w$ satisfies $\varphi$, since $\varphi$ is true at every world of $\mathfrak{M}$. So $w \models \square\varphi$.
9. Substitution, the lemma. Let $\sigma$ be a substitution and $\mathfrak{M} = (W, R, V)$. Define $V^\sigma(p) = [\![\sigma(p)]\!]^{\mathfrak{M}}$ and $\mathfrak{M}^\sigma = (W, R, V^\sigma)$.
10. We claim $\mathfrak{M}, w \models \chi^\sigma$ if and only if $\mathfrak{M}^\sigma, w \models \chi$, for every formula $\chi$ and world $w$. We use [[structural induction|12MQ2NJ29A]] on $\chi$.
11. For $\chi = p$: $\mathfrak{M}, w \models \sigma(p)$ if and only if $w \in V^\sigma(p)$, by the definition of $V^\sigma$. For $\chi = \bot$ both sides are false.
12. For $\chi = \alpha \to \beta$: $\chi^\sigma = \alpha^\sigma \to \beta^\sigma$, and the claim follows from the induction hypothesis for $\alpha$ and $\beta$ at $w$.
13. For $\chi = \square\alpha$: $\chi^\sigma = \square(\alpha^\sigma)$. Both sides say that every successor $v$ of $w$ satisfies $\alpha^\sigma$ in $\mathfrak{M}$, or $\alpha$ in $\mathfrak{M}^\sigma$. These agree by the induction hypothesis at $v$.
14. Substitution, the conclusion. Let $\varphi$ be valid on $\mathfrak{F}$. For a model $\mathfrak{M}$ on $\mathfrak{F}$, the model $\mathfrak{M}^\sigma$ is also on $\mathfrak{F}$, so $\varphi$ is true at every world of $\mathfrak{M}^\sigma$.
15. By the lemma, $\varphi^\sigma$ is true at every world of $\mathfrak{M}$. So $\varphi^\sigma$ is valid on $\mathfrak{F}$.
16. Steps 1 to 15 show that $\operatorname{Log}(\mathfrak{F})$ is normal, and $\operatorname{Log}(\mathsf{C}) = \bigcap_{\mathfrak{F} \in \mathsf{C}} \operatorname{Log}(\mathfrak{F})$ is normal. This is part 1.
17. For part 2, let each formula of $\Gamma$ be valid on every frame of $\mathsf{C}$. Then $\Gamma \subseteq \operatorname{Log}(\mathsf{C})$.
18. By part 1, $\operatorname{Log}(\mathsf{C})$ is a normal logic that contains $\Gamma$. Since $\mathsf{K}\Gamma$ is the smallest such logic, $\mathsf{K}\Gamma \subseteq \operatorname{Log}(\mathsf{C})$.

## Idea

Each axiom is true at every world, and each rule turns formulas valid on the frame into formulas valid on the frame.
Necessitation needs validity at all worlds, not truth at one world, and substitution needs validity under all valuations.
This is why the right notion is validity on a frame.

## Variants

1. For a Hilbert system, the same steps give an induction on the length of a derivation. Each line of a derivation in $\mathsf{K}\Gamma$ is valid on every frame of $\mathsf{C}$.
2. An algebraic version: the complex algebra of a frame is a modal algebra. Every normal logic is sound for the modal algebras that validate its axioms.
