---
tag: 8Y7VESEXNG
kind: proof
name: Proof of the fixed point axiom, induction rule and reachability for common knowledge
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
proves: 8K0CMPQXXB
uses: [RRRHWH9F6Y, 05J9NWX07X, ERG3KAQWYF]
methods: [0ASJVEFA9J, 0NTF6DMVAP]
sources:
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 2
  - url: https://en.wikipedia.org/wiki/Common_knowledge_(logic)
    locator: section Modal logic (syntactic characterization)
---

## Proof

We use the notation of [[the theorem|8K0CMPQXXB]].
Write $R_G(w) = \set{v : w R_G v}$ for the $R_G$-successors of $w$.

Lemma A: $M, w \models E_G\chi$ iff $\chi$ holds at every $v \in R_G(w)$.

1. $E_G\chi$ is $\bigwedge_{a \in G} K_a\chi$. So it holds at $w$ iff $\chi$ holds at every $R_a$-successor of $w$, for every $a \in G$.
2. The union of these successor sets over $a \in G$ is $R_G(w)$. This proves Lemma A.

Lemma B: for $k \ge 1$, $M, w \models E_G^k\varphi$ iff $\varphi$ holds at every $v$ reachable from $w$ in exactly $k$ steps of $R_G$.

3. For $k = 1$ this is Lemma A with $\chi = \varphi$.
4. Let it hold for $k$. By Lemma A with $\chi = E_G^k\varphi$, $E_G^{k+1}\varphi$ holds at $w$ iff $E_G^k\varphi$ holds at every $v \in R_G(w)$.
5. By the induction hypothesis, this says $\varphi$ holds at every world $k$ steps from some $v \in R_G(w)$.
6. These are exactly the worlds $k + 1$ steps from $w$. This proves Lemma B.

Part 1, reachability.

7. By definition, $C_G\varphi$ holds at $w$ iff $E_G^k\varphi$ holds at $w$ for all $k \ge 1$.
8. By Lemma B, this says $\varphi$ holds at every world reachable in $k$ steps, for every $k \ge 1$.
9. Those worlds are exactly the $v$ with $w R_G^+ v$. This proves part 1.

Part 2, the fixed point axiom.

10. Let $C_G\varphi$ hold at $w$, and let $v \in R_G(w)$. Then $w R_G^+ v$, so $\varphi$ holds at $v$ by part 1.
11. If $v R_G^+ u$, then $w R_G^+ u$, since one step to $v$ followed by a path from $v$ is a path from $w$.
12. So $\varphi$ holds at every $u$ with $v R_G^+ u$, and $C_G\varphi$ holds at $v$ by part 1.
13. Thus $\varphi \wedge C_G\varphi$ holds on $R_G(w)$, and $E_G(\varphi \wedge C_G\varphi)$ holds at $w$ by Lemma A.
14. Conversely, let $E_G(\varphi \wedge C_G\varphi)$ hold at $w$, and let $w R_G^+ u$. Take a path from $w$ to $u$, with first step $v \in R_G(w)$.
15. By Lemma A, $\varphi \wedge C_G\varphi$ holds at $v$.
16. If $u = v$ along a one-step path, $\varphi$ holds at $u$. Otherwise $v R_G^+ u$, and $\varphi$ holds at $u$ by part 1 at $v$.
17. So $\varphi$ holds at every $u$ with $w R_G^+ u$, and $C_G\varphi$ holds at $w$ by part 1. This proves part 2.

Part 4, the greatest post-fixed point.

18. Let $X = [\![C_G\varphi]\!]$. By Lemma A, $f(Y)$ is the truth set of $E_G(\varphi \wedge \chi)$ whenever $Y = [\![\chi]\!]$.
19. So part 2 says $X = f(X)$. In particular $X \subseteq f(X)$.
20. Let $Y \subseteq f(Y)$. We show by induction on $k \ge 1$: if $w \in Y$ and $v$ is $k$ steps from $w$, then $v \in [\![\varphi]\!] \cap Y$.
21. For $k = 1$: $w \in f(Y)$, so every $v \in R_G(w)$ lies in $[\![\varphi]\!] \cap Y$, by the definition of $f$.
22. For $k + 1$: the path passes a world $v'$ that is $k$ steps from $w$, followed by one step to $v$.
23. By the induction hypothesis $v' \in Y$. By the case $k = 1$ at $v'$, we get $v \in [\![\varphi]\!] \cap Y$.
24. So every $w \in Y$ has $\varphi$ at all $R_G^+$-successors. By part 1, $Y \subseteq X$.
25. Hence $X$ is the largest $Y$ with $Y \subseteq f(Y)$. This proves part 4.

Part 3, the induction rule.

26. Let $\psi \to E_G(\varphi \wedge \psi)$ be true at every world. By step 18, this says $[\![\psi]\!] \subseteq f([\![\psi]\!])$.
27. By step 24 with $Y = [\![\psi]\!]$, we get $[\![\psi]\!] \subseteq [\![C_G\varphi]\!]$.
28. So $\psi \to C_G\varphi$ is true at every world. This proves part 3.

## Idea

Each $E_G$ is one step along the union of the agents' relations, so $E_G^k$ is $k$ steps.
Common knowledge is all path lengths at once, that is, the transitive closure.
A path splits as a first step plus a shorter path, which is the fixed point axiom.
The induction rule is induction on path length.

## Variants

1. Algebraic proof. The map $f$ preserves arbitrary intersections, so its greatest fixed point is $\bigcap_{k \ge 1} f^k(W)$.
   By induction on $k$, $f^k(W)$ is the truth set of $E_G\varphi \wedge \cdots \wedge E_G^k\varphi$.
   So the greatest fixed point is $[\![C_G\varphi]\!]$ directly from the definition.
2. Syntactic proof: in the axiom system, $C_G\varphi \to E_G^k\varphi$ follows from the fixed point axiom by induction on $k$, and the induction rule is proved sound as in step 26.
