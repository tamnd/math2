---
tag: 6K76NTAEVF
kind: proof
name: Proof of the deduction theorem
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
proves: 9X08XK5RV2
uses: [1MGMQX43B8, 0Y0MQYST0M]
methods: [0KMVFSHFGZ, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Deduction_theorem
    locator: Proof of the deduction theorem
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Proof

We work in the [[Hilbert system|1MGMQX43B8]] L with the axiom schemas A1, A2, A3 and the rule [[modus ponens|0Y0MQYST0M]] (MP).
We prove the two directions separately.

**From right to left.** Assume $\Gamma \vdash \varphi \to \psi$.

1. Take a derivation of $\varphi \to \psi$ from $\Gamma$. It is also a derivation from $\Gamma \cup \set{\varphi}$, since each member of $\Gamma$ is a member of $\Gamma \cup \set{\varphi}$.
2. Add the line $\varphi$, which is a hypothesis in $\Gamma \cup \set{\varphi}$.
3. Add the line $\psi$, by MP from the lines $\varphi$ and $\varphi \to \psi$.
4. The result is a derivation of $\psi$ from $\Gamma \cup \set{\varphi}$, so $\Gamma \cup \set{\varphi} \vdash \psi$.

**From left to right.** Let $\psi_1, \dots, \psi_n$ be a derivation from $\Gamma \cup \set{\varphi}$ with $\psi_n = \psi$.
We prove by strong induction on $i$, for $i = 1, \dots, n$, that $\Gamma \vdash \varphi \to \psi_i$.
Fix $i$, and assume $\Gamma \vdash \varphi \to \psi_j$ for all $j < i$.
By the definition of a derivation, one of four cases holds for $\psi_i$.

5. Case 1: $\psi_i$ is an axiom of L. Then $\psi_i$ is a line of a derivation from $\Gamma$. The formula $\psi_i \to (\varphi \to \psi_i)$ is an instance of A1. MP gives $\varphi \to \psi_i$, so $\Gamma \vdash \varphi \to \psi_i$.
6. Case 2: $\psi_i \in \Gamma$. Then $\psi_i$ is a hypothesis in a derivation from $\Gamma$, and the rest is as in Case 1.
7. Case 3: $\psi_i = \varphi$. We need $\Gamma \vdash \varphi \to \varphi$, and we give a derivation of it from no hypotheses.
8. Its first line is $\varphi \to ((\varphi \to \varphi) \to \varphi)$, an instance of A1 with $\psi := \varphi \to \varphi$.
9. Its second line is $(\varphi \to ((\varphi \to \varphi) \to \varphi)) \to ((\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi))$, an instance of A2 with $\psi := \varphi \to \varphi$ and $\chi := \varphi$.
10. Its third line is $(\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi)$, by MP from the first two lines.
11. Its fourth line is $\varphi \to (\varphi \to \varphi)$, an instance of A1 with $\psi := \varphi$.
12. Its fifth line is $\varphi \to \varphi$, by MP from the fourth and third lines. So $\Gamma \vdash \varphi \to \psi_i$ in Case 3.
13. Case 4: $\psi_i$ follows by MP from earlier lines $\psi_j$ and $\psi_k$, where $j, k < i$ and $\psi_k$ is the formula $\psi_j \to \psi_i$.
14. By the induction hypothesis, $\Gamma \vdash \varphi \to \psi_j$ and $\Gamma \vdash \varphi \to (\psi_j \to \psi_i)$.
15. The formula $(\varphi \to (\psi_j \to \psi_i)) \to ((\varphi \to \psi_j) \to (\varphi \to \psi_i))$ is an instance of A2.
16. MP with step 14 gives $\Gamma \vdash (\varphi \to \psi_j) \to (\varphi \to \psi_i)$.
17. MP with the other part of step 14 gives $\Gamma \vdash \varphi \to \psi_i$.
18. In each case $\Gamma \vdash \varphi \to \psi_i$. This completes the induction.
19. For $i = n$ we get $\Gamma \vdash \varphi \to \psi$.

This proves $\Gamma \cup \set{\varphi} \vdash \psi$ if and only if $\Gamma \vdash \varphi \to \psi$.

## Idea

We move the hypothesis $\varphi$ in front of every line of the derivation, line by line.
A1 handles the lines that do not depend on $\varphi$, the fixed derivation of $\varphi \to \varphi$ handles the line $\varphi$, and A2 passes the hypothesis through each step of MP.
The proof does not use A3, and it does not use any theorem of L except $\varphi \to \varphi$, which it derives itself.

## Variants

The proof is an algorithm that turns a derivation from $\Gamma \cup \set{\varphi}$ into a derivation from $\Gamma$.
Each line $\psi_i$ of the old derivation becomes at most five lines of the new one: five in Case 3, and three in the other cases.
So a derivation of $n$ lines becomes one of at most $5n$ lines.
The same induction proves the theorem for every Hilbert system whose only rule is MP and which derives all instances of A1 and A2.
For first-order logic with the rule of generalization, the induction has one more case, and it needs the condition that the generalized variable is not free in $\varphi$.
