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

We use the axioms of $\mathsf{H}$ and $\mathsf{H}_G$ from the [[definition of the calculus|2B00FE6K5W]].
In $\mathsf{H}_G$ the propositional axioms are (A1) $\alpha \to (\beta \to \alpha)$ and (A2) $(\alpha \to (\beta \to \gamma)) \to ((\alpha \to \beta) \to (\alpha \to \gamma))$, among others.
In $\mathsf{H}$ every instance of A1 and A2 is a [[tautology|05006AJ7DZ]], and so an axiom of group 1.

**Part 1.**

1. Assume $\Gamma \vdash \varphi \to \psi$, and take a derivation of $\varphi \to \psi$ from $\Gamma$.
2. Add the line $\varphi$, which is a hypothesis of $\Gamma \cup \{\varphi\}$.
3. Add the line $\psi$, by [[modus ponens|0Y0MQYST0M]] from the last two lines. The result is a derivation of $\psi$ from $\Gamma \cup \{\varphi\}$.

**Parts 2 and 3.**
Let $\psi_1, \dots, \psi_n = \psi$ be a derivation from $\Gamma \cup \{\varphi\}$.
In part 3, assume that generalization is never applied in it with a variable free in $\varphi$.
We show by strong induction on $i$ that $\Gamma \vdash \varphi \to \psi_i$.

4. Case $\psi_i$ is an axiom or a member of $\Gamma$. Then $\Gamma \vdash \psi_i$ with a one-line derivation.
5. The formula $\psi_i \to (\varphi \to \psi_i)$ is an instance of A1. Modus ponens gives $\Gamma \vdash \varphi \to \psi_i$.
6. Case $\psi_i = \varphi$. We derive $\varphi \to \varphi$ from no hypotheses, in steps 7 to 11.
7. $(\varphi \to ((\varphi \to \varphi) \to \varphi)) \to ((\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi))$ is an instance of A2.
8. $\varphi \to ((\varphi \to \varphi) \to \varphi)$ is an instance of A1.
9. Modus ponens from steps 8 and 7 gives $(\varphi \to (\varphi \to \varphi)) \to (\varphi \to \varphi)$.
10. $\varphi \to (\varphi \to \varphi)$ is an instance of A1.
11. Modus ponens from steps 10 and 9 gives $\varphi \to \varphi$. So $\Gamma \vdash \varphi \to \psi_i$.
12. Case $\psi_i$ follows by modus ponens from $\psi_j$ and $\psi_k = (\psi_j \to \psi_i)$, with $j, k < i$.
13. By the induction hypothesis, $\Gamma \vdash \varphi \to \psi_j$ and $\Gamma \vdash \varphi \to (\psi_j \to \psi_i)$.
14. The formula $(\varphi \to (\psi_j \to \psi_i)) \to ((\varphi \to \psi_j) \to (\varphi \to \psi_i))$ is an instance of A2.
15. Modus ponens with the second part of step 13 gives $\Gamma \vdash (\varphi \to \psi_j) \to (\varphi \to \psi_i)$.
16. Modus ponens with the first part of step 13 gives $\Gamma \vdash \varphi \to \psi_i$.
17. In $\mathsf{H}$ these are all the cases, because modus ponens is the only rule. This proves part 2.
18. In $\mathsf{H}_G$ there is one more case: $\psi_i = \forall x\, \psi_j$ follows by generalization from $\psi_j$, with $j < i$.
19. By the induction hypothesis, $\Gamma \vdash_{\mathsf{H}_G} \varphi \to \psi_j$.
20. The rule of generalization in a derivation from $\Gamma$ gives $\Gamma \vdash_{\mathsf{H}_G} \forall x\, (\varphi \to \psi_j)$.
21. By the assumption of part 3, $x$ is not free in $\varphi$.
22. So $\forall x\, (\varphi \to \psi_j) \to (\varphi \to \forall x\, \psi_j)$ is an axiom of $\mathsf{H}_G$.
23. Modus ponens from steps 20 and 22 gives $\Gamma \vdash_{\mathsf{H}_G} \varphi \to \forall x\, \psi_j$, that is, $\Gamma \vdash_{\mathsf{H}_G} \varphi \to \psi_i$.
24. The case $i = n$ gives $\Gamma \vdash \varphi \to \psi$. This proves part 3.

## Idea

We put "$\varphi \to$" in front of every line of the derivation and repair each step with a few extra lines.
Axioms and hypotheses use A1, the line $\varphi$ uses a derivation of $\varphi \to \varphi$, and modus ponens uses A2.
A step of generalization on $x$ passes under "$\varphi \to$" by the axiom $\forall x\, (\varphi \to \psi) \to (\varphi \to \forall x\, \psi)$, and this needs $x$ not free in $\varphi$.

## Variants

- In $\mathsf{H}$, the steps 4 to 16 can use tautologies directly: $\varphi \to \varphi$ is itself a tautology, so step 6 needs one line.
- A semantic proof for sentences uses [[soundness|4A84VHDTHV]] and [[completeness|WQ1ZE255SF]]. If every model of $\Gamma \cup \{\varphi\}$ satisfies $\psi$, then every model of $\Gamma$ satisfies $\varphi \to \psi$. This argument depends on the completeness theorem, whose proof uses the deduction theorem.
- The proof gives an explicit bound: the new derivation has at most five lines for each line of the old one.
