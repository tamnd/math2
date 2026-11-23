---
tag: 6F5F3GN6SJ
kind: proof
name: Proof of Lindenbaum's lemma by Zorn's lemma
msc: ["03B10", "03C07", "03E25"]
topics: [FBWW4J1XWG]
audience: ug2
proves: SC0BSJ3GT6
uses: [DCR0S91GYY, VM8TQ70CVJ, 04RXTQA5ZA, DKFGQTRYZE]
methods: [0J0XBKG64S, JZQVJ9XT63]
sources:
  - url: https://en.wikipedia.org/wiki/Lindenbaum%27s_lemma
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Zorn%27s_lemma
    locator: lead section
---

## Proof

We apply Zorn's lemma to the consistent extensions of $\Gamma$, and then show that a maximal one decides every sentence.
Let $L$ be any first-order language, and let $\Gamma$ be a consistent set of [[sentences|DKFGQTRYZE]] of $L$.
We use the facts (P1), (P2) and (P5) from step (a) of the [[proof by enumeration|DCR0S91GYY]], which hold for every $L$.

1. Let $\mathcal{P}$ be the set of all [[consistent|VM8TQ70CVJ]] sets of sentences of $L$ that contain $\Gamma$, ordered by inclusion.
2. The set $\mathcal{P}$ is not empty, because $\Gamma \in \mathcal{P}$.
3. Let $\mathcal{C} \subseteq \mathcal{P}$ be a chain, that is, for all $X, Y \in \mathcal{C}$ we have $X \subseteq Y$ or $Y \subseteq X$.
   We find an upper bound of $\mathcal{C}$ in $\mathcal{P}$.
4. If $\mathcal{C}$ is empty, then $\Gamma$ is an upper bound.
5. If $\mathcal{C}$ is not empty, we put $U = \bigcup \mathcal{C}$.
   Then $U$ contains $\Gamma$, and $X \subseteq U$ for every $X \in \mathcal{C}$.
6. Suppose $U \vdash \psi$ and $U \vdash \neg \psi$.
   By (P1) the two derivations use a finite set $\{ \gamma_1, \dots, \gamma_k \} \subseteq U$, with $\gamma_i \in X_i \in \mathcal{C}$.
7. The sets $X_1, \dots, X_k$ lie in a chain, so one of them, say $X_j$, contains all the others.
   When $k = 0$, we take any member of $\mathcal{C}$ as $X_j$.
8. Then $\{ \gamma_1, \dots, \gamma_k \} \subseteq X_j$, and (P2) gives $X_j \vdash \psi$ and $X_j \vdash \neg \psi$, which contradicts $X_j \in \mathcal{P}$.
   So $U$ is consistent, and $U \in \mathcal{P}$ is an upper bound of $\mathcal{C}$.
9. Every chain in $\mathcal{P}$ has an upper bound in $\mathcal{P}$, so [[Zorn's lemma|04RXTQA5ZA]] gives a maximal element $\Delta$ of $\mathcal{P}$.
10. The set $\Delta$ is consistent and contains $\Gamma$, since $\Delta \in \mathcal{P}$.
11. Let $\sigma$ be a sentence of $L$, and suppose $\sigma \notin \Delta$ and $\neg \sigma \notin \Delta$.
12. The sets $\Delta \cup \{ \sigma \}$ and $\Delta \cup \{ \neg \sigma \}$ contain $\Gamma$ and are strictly larger than $\Delta$.
    By the maximality of $\Delta$ in $\mathcal{P}$, neither lies in $\mathcal{P}$, so both are inconsistent.
13. By (P5), $\Delta \vdash \neg \sigma$ and $\Delta \vdash \sigma$, so $\Delta$ is inconsistent, which contradicts step 10.
14. Hence $\sigma \in \Delta$ or $\neg \sigma \in \Delta$ for every sentence $\sigma$, and $\Delta$ is a maximal consistent set that contains $\Gamma$.
15. The properties 1 to 5 of the lemma follow as in step (c) of the proof by enumeration, which does not use the countability of $L$.

## Idea

The consistent extensions of $\Gamma$ form a partial order, and every chain in it has a consistent union, because a contradiction uses only finitely many sentences.
That is exactly the hypothesis of Zorn's lemma, so a maximal consistent extension exists.
Maximal here means "no consistent set is larger", and fact (P5) turns that into "every sentence or its negation is already inside".

## Variants

Instead of Zorn's lemma, we can well-order the sentences as $(\sigma_\alpha)_{\alpha < \kappa}$ and decide them in this order, with unions at limit ordinals.
This uses the well-ordering theorem, which is equivalent to Zorn's lemma.
A third route goes through algebra.
The consistent sets that contain $\Gamma$ give proper filters of the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]], and the ultrafilter lemma gives an ultrafilter above the filter of $\Gamma$.
This route needs only the [[Boolean prime ideal theorem|STPBXBKSZP]], which is strictly weaker than the axiom of choice over ZF.
