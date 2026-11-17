---
tag: WFBG5RAG36
kind: proof
name: Proof of the soundness theorem by induction on derivations
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
proves: XD629S54CS
uses: [1MGMQX43B8, H31CS3HK5P, 0Y0MQYST0M, 05006AJ7DZ, 1HK0VYWTV7, VM8TQ70CVJ, QN7M1JCGT9]
methods: [0KMVFSHFGZ, 0WCP0PVET6, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Soundness
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Proof

We use the fixed notation: $v$ is a [[truth assignment|H31CS3HK5P]], and $v(\varphi)$ is the value of the formula $\varphi$ under $v$.
Recall that $\Gamma \vdash \varphi$ means derivability in the [[Hilbert system|1MGMQX43B8]] $L$, and $\Gamma \models \varphi$ means [[logical consequence|1HK0VYWTV7]].

1. By the definition of the valuation, $v(\neg \alpha) = 1 - v(\alpha)$, and $v(\alpha \to \beta) = 0$ exactly when $v(\alpha) = 1$ and $v(\beta) = 0$.
2. Every instance of (A1) is a [[tautology|05006AJ7DZ]]. Suppose $v(\varphi \to (\psi \to \varphi)) = 0$. By step 1, $v(\varphi) = 1$ and $v(\psi \to \varphi) = 0$, so $v(\varphi) = 0$, a contradiction.
3. Every instance of (A2) is a tautology. Suppose $v$ makes it false. By step 1, $v(\varphi \to (\psi \to \chi)) = 1$ and $v((\varphi \to \psi) \to (\varphi \to \chi)) = 0$.
4. The second fact of step 3 gives $v(\varphi \to \psi) = 1$ and $v(\varphi \to \chi) = 0$, so $v(\varphi) = 1$ and $v(\chi) = 0$ by step 1.
5. From $v(\varphi) = 1$ and $v(\varphi \to \psi) = 1$, step 1 gives $v(\psi) = 1$. Then $v(\psi \to \chi) = 0$, so $v(\varphi \to (\psi \to \chi)) = 0$. This contradicts step 3.
6. Every instance of (A3) is a tautology. Suppose $v$ makes it false. By step 1, $v(\neg \psi \to \neg \varphi) = 1$, $v(\neg \psi \to \varphi) = 1$ and $v(\psi) = 0$.
7. Then $v(\neg \psi) = 1$. The first fact of step 6 gives $v(\neg \varphi) = 1$, so $v(\varphi) = 0$. The second fact gives $v(\varphi) = 1$. This is a contradiction.
8. [[Modus ponens|0Y0MQYST0M]] preserves truth: if $v(\alpha) = 1$ and $v(\alpha \to \beta) = 1$, then $v(\beta) = 1$ by step 1.
9. Now let $\Gamma \vdash \varphi$, with a derivation $\varphi_1, \dots, \varphi_n = \varphi$ from $\Gamma$. Let $v$ be a truth assignment with $v(\gamma) = 1$ for every $\gamma \in \Gamma$.
10. We show $v(\varphi_i) = 1$ for $i = 1, \dots, n$ by [[strong induction|0KMVFSHFGZ]] on $i$. Assume $v(\varphi_j) = 1$ for all $j < i$.
11. Case 1: $\varphi_i$ is an axiom. Then $v(\varphi_i) = 1$ by steps 2 to 7.
12. Case 2: $\varphi_i \in \Gamma$. Then $v(\varphi_i) = 1$ by the choice of $v$ in step 9.
13. Case 3: $\varphi_i$ comes by MP from $\varphi_j$ and $\varphi_k = (\varphi_j \to \varphi_i)$ with $j, k < i$. The induction hypothesis gives $v(\varphi_j) = v(\varphi_k) = 1$, so $v(\varphi_i) = 1$ by step 8.
14. The three cases cover every line of a derivation. So $v(\varphi) = v(\varphi_n) = 1$.
15. The assignment $v$ was any model of $\Gamma$. Hence $\Gamma \models \varphi$, which is part 1 of the statement.
16. Take $\Gamma = \emptyset$. Then $\vdash \varphi$ gives $\models \varphi$, so every theorem of $L$ is a tautology.
17. Suppose $\vdash \varphi$ and $\vdash \neg \varphi$. Fix any truth assignment $v$. Step 16 gives $v(\varphi) = 1$ and $v(\neg \varphi) = 1$, which contradicts step 1. So $L$ is [[consistent|VM8TQ70CVJ]], which is part 2.
18. Let $\Gamma$ be [[satisfiable|QN7M1JCGT9]] by $v$, and suppose $\Gamma \vdash \varphi$ and $\Gamma \vdash \neg \varphi$. Steps 9 to 15 give $v(\varphi) = 1$ and $v(\neg \varphi) = 1$, again a contradiction. So $\Gamma$ is consistent, which is part 3.

## Idea

Fix one truth assignment that makes the hypotheses true.
The axioms are true under it because they are tautologies, and modus ponens keeps truth.
So truth passes from line to line along the derivation, and the last line is true.

## Variants

- Closure form: the set $T_v = \set{\alpha : v(\alpha) = 1}$ contains $\Gamma$ and the axioms and is closed under MP. The set of formulas derivable from $\Gamma$ is the smallest such set, so it lies inside $T_v$.
- Truth table form: steps 2 to 7 can be replaced by full truth tables in the values of $\varphi, \psi, \chi$: 4 rows for (A1) and (A3), and 8 rows for (A2).
- Algebraic form: replace $\set{0, 1}$ by any Boolean algebra $B$. The axioms take the top value under every map from $P$ to $B$, and MP keeps the top value, so the same induction works.
