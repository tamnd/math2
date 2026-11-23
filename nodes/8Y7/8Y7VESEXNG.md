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

We show that $E_G^k$ is truth along paths of length $k$, and then read off the four parts from the structure of paths.
We use the notation of [[the theorem|8K0CMPQXXB]], and we write $R_G(w) = \{v : w R_G v\}$.

Lemma A: $M, w \models E_G \chi$ if and only if $\chi$ holds at every $v \in R_G(w)$.

1. $E_G \chi$ is $\bigwedge_{a \in G} K_a \chi$, so it holds at $w$ exactly when $\chi$ holds at every $R_a$-successor of $w$ for every $a \in G$.
2. The union of these successor sets over $a \in G$ is $R_G(w)$, which proves Lemma A.

Lemma B: for $k \ge 1$, $M, w \models E_G^k \varphi$ if and only if $\varphi$ holds at every world reachable from $w$ in exactly $k$ steps of $R_G$.

3. For $k = 1$ this is Lemma A with $\chi = \varphi$.
4. Assume Lemma B for $k$.
   By Lemma A with $\chi = E_G^k \varphi$, the formula $E_G^{k+1} \varphi$ holds at $w$ exactly when $E_G^k \varphi$ holds at every $v \in R_G(w)$.
5. By the induction hypothesis, that says $\varphi$ holds at every world $k$ steps from some $v \in R_G(w)$, and these are exactly the worlds $k + 1$ steps from $w$.

Part 1, reachability.

6. By definition, $C_G \varphi$ holds at $w$ exactly when $E_G^k \varphi$ holds at $w$ for all $k \ge 1$.
7. By Lemma B, that says $\varphi$ holds at every world reachable in $k$ steps for every $k \ge 1$, that is, at every $v$ with $w R_G^+ v$.

Part 2, the fixed point axiom.

8. Let $C_G \varphi$ hold at $w$, and let $v \in R_G(w)$.
   Then $w R_G^+ v$, so $\varphi$ holds at $v$ by part 1.
9. If $v R_G^+ u$, then $w R_G^+ u$, because one step to $v$ followed by a path from $v$ is a path from $w$.
   So $\varphi$ holds at every such $u$, and $C_G \varphi$ holds at $v$ by part 1.
10. Thus $\varphi \wedge C_G \varphi$ holds on $R_G(w)$, and $E_G (\varphi \wedge C_G \varphi)$ holds at $w$ by Lemma A.
11. Conversely, let $E_G (\varphi \wedge C_G \varphi)$ hold at $w$, let $w R_G^+ u$, and let $v \in R_G(w)$ be the first step of a path from $w$ to $u$.
    By Lemma A, $\varphi \wedge C_G \varphi$ holds at $v$.
12. If the path has one step, then $u = v$ and $\varphi$ holds at $u$.
    Otherwise $v R_G^+ u$, and $\varphi$ holds at $u$ by part 1 applied at $v$.
13. So $\varphi$ holds at every $u$ with $w R_G^+ u$, and $C_G \varphi$ holds at $w$ by part 1.

Part 4, the greatest post-fixed point.

14. Let $X = [\![C_G \varphi]\!]$.
    By Lemma A, if $Y = [\![\chi]\!]$, then $f(Y)$ is the truth set of $E_G (\varphi \wedge \chi)$.
15. So part 2 says $X = f(X)$, and in particular $X \subseteq f(X)$.
16. Let $Y \subseteq f(Y)$.
    We show by induction on $k \ge 1$ that if $w \in Y$ and $v$ is $k$ steps from $w$, then $v \in [\![\varphi]\!] \cap Y$.
17. For $k = 1$, we have $w \in f(Y)$, so every $v \in R_G(w)$ lies in $[\![\varphi]\!] \cap Y$ by the definition of $f$.
18. For $k + 1$, the path passes a world $v'$ that is $k$ steps from $w$ and then takes one step to $v$.
    By the induction hypothesis $v' \in Y$, and the case $k = 1$ at $v'$ gives $v \in [\![\varphi]\!] \cap Y$.
19. So every $w \in Y$ has $\varphi$ at all its $R_G^+$-successors, and part 1 gives $Y \subseteq X$.
    Hence $X$ is the largest $Y$ with $Y \subseteq f(Y)$.

Part 3, the induction rule.

20. Let $\psi \to E_G (\varphi \wedge \psi)$ be true at every world.
    By step 14, this says $[\![\psi]\!] \subseteq f([\![\psi]\!])$.
21. Step 19 with $Y = [\![\psi]\!]$ gives $[\![\psi]\!] \subseteq [\![C_G \varphi]\!]$, so $\psi \to C_G \varphi$ is true at every world.

This proves all four parts of the theorem.

## Idea

Each $E_G$ is one step along the union of the agents' relations, so $E_G^k$ is truth at the end of every path of length $k$.
Common knowledge asks for all lengths at once, which is the transitive closure.
A path is a first step followed by a shorter path, and that split is the fixed point axiom.
The induction rule is induction on the length of the path.

## Variants

There is an algebraic proof of part 4.
The map $f$ preserves arbitrary intersections, so its greatest fixed point is $\bigcap_{k \ge 1} f^k(W)$.
By induction on $k$, the set $f^k(W)$ is the truth set of $E_G \varphi \wedge \cdots \wedge E_G^k \varphi$, because $E_G$ distributes over conjunction.
So the greatest fixed point is $[\![C_G \varphi]\!]$, straight from the definition.

There is also a syntactic route inside the axiom system.
There $C_G \varphi \to E_G^k \varphi$ follows from the fixed point axiom by induction on $k$, and the soundness of the induction rule is proved as in step 20.
