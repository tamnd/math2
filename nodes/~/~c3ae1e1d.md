---
tag: ~c3ae1e1d
kind: proof
name: Proof of the Kripke completeness of GL
msc: ["03B45", "03F45"]
topics: [3E7M66WW6Q]
audience: research
proves: ~d95bfe82
uses: [61THBNS8WE, QQ6PZFGGB3, ~7b1fea34, NGHWZ9Y7ZV, G989VP2NGP, 0GJZW9JFZQ, 0DQPNJNPYK, 60FNZ35H6R, SC0BSJ3GT6]
methods: [0NTF6DMVAP, 0J0XBKG64S, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Proof

We prove $1 \Rightarrow 2 \Rightarrow 3 \Rightarrow 4 \Rightarrow 1$ for the items of the [[Kripke completeness of GL|~d95bfe82]].
We write $\Gamma \vdash \psi$ for $\mathsf{GL} \vdash \bigwedge \Gamma' \to \psi$ for some finite $\Gamma' \subseteq \Gamma$, and a set $\Gamma$ is consistent when $\Gamma \nvdash \bot$.

Part A: $1 \Rightarrow 2$ (soundness).

1. Let $(W, R)$ be transitive and conversely well-founded. Every tautology and the axiom $\mathrm{K}$ are valid on every frame. Löb's axiom is valid on $(W, R)$ by part 3 of [[Löb's axiom in provability logic|QQ6PZFGGB3]].
2. Modus ponens, the [[necessitation rule|G989VP2NGP]] and uniform substitution preserve validity on a fixed frame. For substitution, a valuation of the substituted formulas is a valuation of the variables.
3. By induction on the length of a derivation, every theorem of $\mathsf{GL}$ is valid on $(W, R)$.

Part B: $2 \Rightarrow 3$.

4. Let $(W, R)$ be finite, transitive and irreflexive, and let $X \subseteq W$ be nonempty. We show by contradiction that $X$ has an $R$-maximal element.
5. Assume not. Choose $x_0 \in X$, and for each $k$ choose $x_{k+1} \in X$ with $x_k R x_{k+1}$. Since $W$ is finite, $x_i = x_j$ for some $i < j$.
6. By [[transitivity|0GJZW9JFZQ]], $x_i R x_{i+1} R \cdots R x_j$ gives $x_i R x_j$, that is, $x_i R x_i$. This contradicts irreflexivity.
7. So $R$ is conversely [[well-founded|0DQPNJNPYK]], and $(W, R)$ is one of the frames of item 2. Hence item 2 implies item 3.

Part C: $3 \Rightarrow 4$.

8. Every frame in item 4 is a finite transitive irreflexive frame, so item 3 implies item 4.

Part D: $4 \Rightarrow 1$, by contraposition.
Assume $\mathsf{GL} \nvdash \varphi$.
Let $\mathrm{Sub}(\varphi)$ be the set of subformulas of $\varphi$, with $n$ elements, and let $\Sigma = \mathrm{Sub}(\varphi) \cup \set{\neg \psi : \psi \in \mathrm{Sub}(\varphi)}$.

9. An atom is a consistent set $\Gamma \subseteq \Sigma$ such that $\psi \in \Gamma$ or $\neg \psi \in \Gamma$ for every $\psi \in \mathrm{Sub}(\varphi)$. By consistency, not both are in $\Gamma$.
10. Closure of atoms. If $\psi \in \mathrm{Sub}(\varphi)$ and $\Gamma \vdash \psi$, then $\psi \in \Gamma$. Otherwise $\neg \psi \in \Gamma$, and $\Gamma$ is inconsistent.
11. Atoms and connectives. Let $\psi \to \chi \in \mathrm{Sub}(\varphi)$. Then $\psi \to \chi \in \Gamma$ if and only if $\psi \notin \Gamma$ or $\chi \in \Gamma$. Both directions follow from step 10 and the tautologies $\psi \wedge (\psi \to \chi) \to \chi$, $\neg \psi \to (\psi \to \chi)$ and $\chi \to (\psi \to \chi)$.
12. Also $\bot \notin \Gamma$, since $\Gamma$ is consistent.
13. Finite [[Lindenbaum lemma|SC0BSJ3GT6]]: every consistent $\Delta_0 \subseteq \Sigma$ is contained in an atom. List $\mathrm{Sub}(\varphi)$ as $\psi_1, \dots, \psi_n$, and at stage $k$ add $\psi_k$ or $\neg \psi_k$. One of the two keeps consistency, since $\Delta \vdash \neg \psi_k$ and $\Delta \vdash \neg \neg \psi_k$ give $\Delta \vdash \bot$.
14. Let $W$ be the set of atoms. An atom is fixed by the set of $k$ with $\psi_k \in \Gamma$, so $W$ has at most $2^n$ elements.
15. Since $\mathsf{GL} \nvdash \varphi$, the set $\set{\neg \varphi}$ is consistent. By step 13 it is contained in an atom $\Gamma_0$, so $W$ is nonempty and $\varphi \notin \Gamma_0$.
16. Define $\Gamma R \Delta$ when (a) for every $\square \chi \in \Gamma$, both $\chi \in \Delta$ and $\square \chi \in \Delta$, and (b) some $\square \chi \in \Delta$ has $\square \chi \notin \Gamma$.
17. $R$ is irreflexive, since (b) fails for $\Delta = \Gamma$.
18. $R$ is transitive. Let $\Gamma R \Delta$ and $\Delta R \Theta$. Condition (a) for $\Gamma$ and $\Theta$ follows from (a) twice, since $\square \chi \in \Gamma$ gives $\square \chi \in \Delta$, then $\chi, \square \chi \in \Theta$.
19. For (b), take $\square \chi \in \Delta$ with $\square \chi \notin \Gamma$. By (a) for $\Delta R \Theta$, $\square \chi \in \Theta$. So (b) holds for $\Gamma$ and $\Theta$.
20. Let $V(p) = \set{\Gamma \in W : p \in \Gamma}$ for each variable $p$ of $\varphi$, and let $M = (W, R, V)$.
21. Truth lemma: for every $\psi \in \mathrm{Sub}(\varphi)$ and $\Gamma \in W$, $M, \Gamma \models \psi$ if and only if $\psi \in \Gamma$. We use [[structural induction|12MQ2NJ29A]] on $\psi$.
22. For a variable this is the definition of $V$. For $\bot$ it is step 12. For $\psi \to \chi$ it is step 11 and the induction hypothesis.
23. Case $\square \psi$, direction from right to left. Let $\square \psi \in \Gamma$ and $\Gamma R \Delta$. By (a), $\psi \in \Delta$, so $\Delta \models \psi$ by the induction hypothesis. Hence $\Gamma \models \square \psi$.
24. Case $\square \psi$, direction from left to right, by contraposition. Let $\square \psi \notin \Gamma$, and let $\Delta_0 = \set{\chi, \square \chi : \square \chi \in \Gamma} \cup \set{\square \psi, \neg \psi}$. Then $\Delta_0 \subseteq \Sigma$.
25. We show that $\Delta_0$ is consistent, by contradiction. Let $B$ be the conjunction of the formulas $\chi \wedge \square \chi$ with $\square \chi \in \Gamma$, and $B = \top$ when there are none. If $\Delta_0$ is inconsistent, then $\mathsf{GL} \vdash B \wedge \square \psi \to \psi$, that is, $\mathsf{GL} \vdash B \to (\square \psi \to \psi)$.
26. Rule (RM) of [[the proof of the properties of Löb's axiom|~7b1fea34]] gives $\mathsf{GL} \vdash \square B \to \square(\square \psi \to \psi)$. With Löb's axiom, $\mathsf{GL} \vdash \square B \to \square \psi$.
27. In $\mathsf{K}$, $\square$ commutes with finite conjunctions, so $\square B$ is equivalent to the conjunction of the $\square \chi \wedge \square \square \chi$. By axiom 4 (part 1 of [[Löb's axiom in provability logic|QQ6PZFGGB3]]), $\square \chi \to \square \square \chi$. So $\mathsf{GL} \vdash \bigwedge \set{\square \chi : \square \chi \in \Gamma} \to \square B$.
28. Steps 26 and 27 give $\Gamma \vdash \square \psi$. By step 10, $\square \psi \in \Gamma$, against step 24. So $\Delta_0$ is consistent.
29. By step 13, $\Delta_0$ is contained in an atom $\Delta$. Condition (a) holds by the first part of $\Delta_0$. Condition (b) holds since $\square \psi \in \Delta$ and $\square \psi \notin \Gamma$. So $\Gamma R \Delta$.
30. Since $\neg \psi \in \Delta$, $\psi \notin \Delta$, so $\Delta \not\models \psi$ by the induction hypothesis. Hence $\Gamma \not\models \square \psi$. This ends the truth lemma.
31. By steps 15 and 30, $\Gamma_0 \not\models \varphi$. By steps 14, 17 and 18, $(W, R)$ is a transitive irreflexive frame with at most $2^n$ worlds. So $\varphi$ is not valid on a frame of item 4.

Steps 3, 7, 8 and 31 close the cycle of implications.

## Idea

Soundness is the frame condition of Löb's axiom.
For completeness, the canonical model of $\mathsf{GL}$ fails, so we take maximal consistent sets only inside the finite set $\Sigma$.
Condition (b) makes the relation irreflexive: each step to a successor adds a new boxed formula.
The only place where Löb's axiom enters is step 26: the extra hypothesis $\square \psi$ in $\Delta_0$ is allowed because $\mathrm{L}$ turns "$\square \psi \to \psi$ follows from the boxed facts" into "$\square \psi$ follows from them".

## Variants

1. Chain bound. By (a) and (b), the set of boxed formulas of an atom grows strictly along $R$. So every $R$-chain in $M$ has at most $m + 1$ worlds, where $m$ is the number of boxed subformulas of $\varphi$. This bound gives the PSPACE upper bound for $\mathsf{GL}$.
2. Trees. Unravel the generated submodel of $\Gamma_0$ into the tree of its finite $R$-paths. The result is a finite transitive irreflexive tree that refutes $\varphi$ at its root, once $R$ on paths is taken as the transitive "proper initial segment" relation.
