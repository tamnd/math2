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

We prove the easy direction with one step of modus ponens, and the hard direction by putting $\varphi \to$ in front of every line of a derivation, by induction on the lines.
We work in the [[Hilbert system|1MGMQX43B8]] L with the axiom schemas A1, A2, A3 and the rule [[modus ponens|0Y0MQYST0M]] (MP).

**From right to left.** Assume $\Gamma \vdash \varphi \to \psi$.

1. Take a derivation of $\varphi \to \psi$ from $\Gamma$.
   It is also a derivation from $\Gamma \cup \{ \varphi \}$, since each member of $\Gamma$ is a member of $\Gamma \cup \{ \varphi \}$.
2. Add the line $\varphi$, which is a hypothesis in $\Gamma \cup \{ \varphi \}$.
3. Add the line $\psi$, by MP from the lines $\varphi$ and $\varphi \to \psi$.
4. The result is a derivation of $\psi$ from $\Gamma \cup \{ \varphi \}$, so $\Gamma \cup \{ \varphi \} \vdash \psi$.

**From left to right.** Let $\psi_1, \dots, \psi_n$ be a derivation from $\Gamma \cup \{ \varphi \}$ with $\psi_n = \psi$.
We prove by strong induction on $i$, for $i = 1, \dots, n$, that $\Gamma \vdash \varphi \to \psi_i$.
Fix $i$, and assume $\Gamma \vdash \varphi \to \psi_j$ for all $j < i$.
By the definition of a derivation, one of four cases holds for $\psi_i$.

1. Case 1: $\psi_i$ is an axiom of L.
   Then the following three lines form a derivation from $\Gamma$:
   $$\psi_i, \qquad \psi_i \to (\varphi \to \psi_i), \qquad \varphi \to \psi_i.$$
   The first line is an axiom, the second is an instance of A1, and the third follows by MP.
   So $\Gamma \vdash \varphi \to \psi_i$.
2. Case 2: $\psi_i \in \Gamma$.
   The same three lines form a derivation from $\Gamma$, with the first line now a hypothesis.
   So $\Gamma \vdash \varphi \to \psi_i$.
3. Case 3: $\psi_i$ is $\varphi$.
   We need $\Gamma \vdash \varphi \to \varphi$, and the following five lines derive it from no hypotheses:
   $$\begin{array}{rll} 1. & \varphi \to ((\varphi \to \varphi) \to \varphi) & \text{A1} \\ 2. & (\varphi \to ((\varphi \to \varphi) \to \varphi)) \to ((\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi)) & \text{A2} \\ 3. & (\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi) & \text{MP, lines 1 and 2} \\ 4. & \varphi \to (\varphi \to \varphi) & \text{A1} \\ 5. & \varphi \to \varphi & \text{MP, lines 4 and 3} \end{array}$$
   So $\Gamma \vdash \varphi \to \psi_i$.
4. Case 4: $\psi_i$ follows by MP from earlier lines $\psi_j$ and $\psi_k$, where $j, k < i$ and $\psi_k$ is the formula $\psi_j \to \psi_i$.
   By the induction hypothesis, $\Gamma \vdash \varphi \to \psi_j$ and $\Gamma \vdash \varphi \to (\psi_j \to \psi_i)$.
5. In Case 4 we use the instance of A2
   $$(\varphi \to (\psi_j \to \psi_i)) \to ((\varphi \to \psi_j) \to (\varphi \to \psi_i)).$$
   MP with $\Gamma \vdash \varphi \to (\psi_j \to \psi_i)$ gives $\Gamma \vdash (\varphi \to \psi_j) \to (\varphi \to \psi_i)$.
   MP with $\Gamma \vdash \varphi \to \psi_j$ then gives $\Gamma \vdash \varphi \to \psi_i$.
6. In each case $\Gamma \vdash \varphi \to \psi_i$, and this completes the induction.
   For $i = n$ we get $\Gamma \vdash \varphi \to \psi$.

This proves $\Gamma \cup \{ \varphi \} \vdash \psi$ if and only if $\Gamma \vdash \varphi \to \psi$.

## Idea

We move the hypothesis $\varphi$ in front of every line of the derivation, line by line.
A1 handles the lines that do not depend on $\varphi$, the fixed derivation of $\varphi \to \varphi$ handles the line $\varphi$ itself, and A2 carries the hypothesis through each step of MP.
The proof does not use A3, and it uses no theorem of L except $\varphi \to \varphi$, which it derives on the spot.

## Variants

The proof is an algorithm that turns a derivation from $\Gamma \cup \{ \varphi \}$ into a derivation from $\Gamma$.
Each line $\psi_i$ of the old derivation becomes at most five lines of the new one: five in Case 3, and three in the other cases.
So a derivation of $n$ lines becomes one of at most $5n$ lines.
The same induction proves the theorem for every Hilbert system whose only rule is MP and which derives all instances of A1 and A2.
For first-order logic with the rule of generalization, the induction has one more case, and it needs the condition that the generalized variable is not free in $\varphi$.
