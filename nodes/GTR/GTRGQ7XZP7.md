---
tag: GTRGQ7XZP7
kind: proof
name: Proof of the deduction theorem for predicate logic
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
proves: 8M9ZFDR4DH
uses: [2B00FE6K5W, 05006AJ7DZ, 0Y0MQYST0M]
methods: [12MQ2NJ29A, 0WCP0PVET6]
sources:
  - book: isbn:9781482237726
    locator: Chapter 2
  - url: https://en.wikipedia.org/wiki/Deduction_theorem
    locator: Proof of the deduction theorem
---

## Proof

Part 1 adds one step of modus ponens; for parts 2 and 3 we put "$\varphi \to$" in front of every line of a derivation and repair each step.
We use the axioms of $\mathsf{H}$ and $\mathsf{H}_G$ from the [[definition of the calculus|2B00FE6K5W]].
In $\mathsf{H}_G$ two of the propositional axioms are
$$\text{(A1)}\ \alpha \to (\beta \to \alpha), \qquad \text{(A2)}\ (\alpha \to (\beta \to \gamma)) \to ((\alpha \to \beta) \to (\alpha \to \gamma)).$$
In $\mathsf{H}$ every instance of A1 and A2 is a [[tautology|05006AJ7DZ]], and so an axiom of group 1.

**Part 1.**

1. Assume $\Gamma \vdash \varphi \to \psi$, and take a derivation of $\varphi \to \psi$ from $\Gamma$.
2. Add the line $\varphi$, which is a hypothesis of $\Gamma \cup \{ \varphi \}$.
3. Add the line $\psi$, by [[modus ponens|0Y0MQYST0M]] from the last two lines.
   The result is a derivation of $\psi$ from $\Gamma \cup \{ \varphi \}$.

**Parts 2 and 3.**
Let $\psi_1, \dots, \psi_n = \psi$ be a derivation from $\Gamma \cup \{ \varphi \}$.
In part 3, assume that generalization is never applied in it to a variable free in $\varphi$.
We show by strong induction on $i$ that $\Gamma \vdash \varphi \to \psi_i$.

4. Case $\psi_i$ is an axiom or a member of $\Gamma$.
   Then $\Gamma \vdash \psi_i$, and $\psi_i \to (\varphi \to \psi_i)$ is an instance of A1.
   Modus ponens gives $\Gamma \vdash \varphi \to \psi_i$.
5. Case $\psi_i = \varphi$.
   We must show $\vdash \varphi \to \varphi$, and five lines do it:
   $$\begin{array}{rll} \text{a.} & (\varphi \to ((\varphi \to \varphi) \to \varphi)) \to ((\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi)) & \text{A2} \\ \text{b.} & \varphi \to ((\varphi \to \varphi) \to \varphi) & \text{A1} \\ \text{c.} & (\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi) & \text{modus ponens, b and a} \\ \text{d.} & \varphi \to (\varphi \to \varphi) & \text{A1} \\ \text{e.} & \varphi \to \varphi & \text{modus ponens, d and c} \end{array}$$
6. Case $\psi_i$ follows by modus ponens from $\psi_j$ and $\psi_k = (\psi_j \to \psi_i)$, with $j, k < i$.
   By the induction hypothesis, $\Gamma \vdash \varphi \to \psi_j$ and $\Gamma \vdash \varphi \to (\psi_j \to \psi_i)$.
7. In the same case, A2 gives $(\varphi \to (\psi_j \to \psi_i)) \to ((\varphi \to \psi_j) \to (\varphi \to \psi_i))$.
   Modus ponens with the second result of step 6 gives $\Gamma \vdash (\varphi \to \psi_j) \to (\varphi \to \psi_i)$.
   Modus ponens with the first result gives $\Gamma \vdash \varphi \to \psi_i$.
8. In $\mathsf{H}$ these are all the cases, because modus ponens is the only rule.
   The case $i = n$ proves part 2.
9. In $\mathsf{H}_G$ there is one more case: $\psi_i = \forall x\, \psi_j$ follows by generalization from $\psi_j$, with $j < i$.
   By the induction hypothesis, $\Gamma \vdash_{\mathsf{H}_G} \varphi \to \psi_j$, and the rule of generalization gives $\Gamma \vdash_{\mathsf{H}_G} \forall x\,(\varphi \to \psi_j)$.
10. By the assumption of part 3, $x$ is not free in $\varphi$.
    So $\forall x\,(\varphi \to \psi_j) \to (\varphi \to \forall x\, \psi_j)$ is an axiom of $\mathsf{H}_G$.
11. Modus ponens with step 9 gives $\Gamma \vdash_{\mathsf{H}_G} \varphi \to \forall x\, \psi_j$, that is, $\Gamma \vdash_{\mathsf{H}_G} \varphi \to \psi_i$.
12. The case $i = n$ gives $\Gamma \vdash_{\mathsf{H}_G} \varphi \to \psi$, which proves part 3.

## Idea

We put "$\varphi \to$" in front of every line of the derivation and repair each step with a few extra lines.
Axioms and hypotheses use A1, the line $\varphi$ itself uses the five-line derivation of $\varphi \to \varphi$, and modus ponens uses A2.
A step of generalization on $x$ passes under "$\varphi \to$" by the axiom $\forall x\,(\varphi \to \psi) \to (\varphi \to \forall x\, \psi)$.
That axiom needs $x$ not free in $\varphi$, and this is exactly where the restriction of part 3 comes from.

## Variants

In $\mathsf{H}$, the cases can use tautologies directly.
For example, $\varphi \to \varphi$ is itself a tautology, so step 5 needs one line.
Each case then needs at most three lines, so the new derivation has at most three times as many lines as the old one.

A semantic proof for sentences uses [[soundness|4A84VHDTHV]] and [[completeness|WQ1ZE255SF]].
If every model of $\Gamma \cup \{ \varphi \}$ satisfies $\psi$, then every model of $\Gamma$ satisfies $\varphi \to \psi$.
This route is circular in most books, because their proof of completeness uses the deduction theorem.
