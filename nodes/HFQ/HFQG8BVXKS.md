---
tag: HFQG8BVXKS
kind: proof
name: Proof of the generalization theorem
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
proves: VKSK35Y52Z
uses: [2B00FE6K5W, NCDZ969V7X, 05006AJ7DZ]
methods: [12MQ2NJ29A, 0WCP0PVET6]
sources:
  - book: isbn:9780122384523
    locator: Section 2.4
---

## Proof

We use the axiom groups 1 to 6 of the [[definition of the calculus|2B00FE6K5W]].

**Part 1.**
Assume that $x$ is not free in any member of $\Gamma$.
Let $\varphi_1, \dots, \varphi_n$ be a deduction of $\varphi$ from $\Gamma$.
We show by strong induction on $i$ that $\Gamma \vdash \forall x\, \varphi_i$ for each $i$.
Fix $i$ and assume the claim for all $j < i$.
There are three cases.

1. Case $\varphi_i$ is a logical axiom. Then $\varphi_i$ is a generalization of a formula of groups 1 to 6.
2. So $\forall x\, \varphi_i$ is also a generalization of the same formula, and it is a logical axiom. Its one-line deduction gives $\Gamma \vdash \forall x\, \varphi_i$.
3. Case $\varphi_i \in \Gamma$. By the hypothesis, $x$ is not free in $\varphi_i$.
4. So $\varphi_i \to \forall x\, \varphi_i$ is a logical axiom of group 4.
5. Modus ponens with $\varphi_i \in \Gamma$ gives $\Gamma \vdash \forall x\, \varphi_i$.
6. Case $\varphi_i$ follows by modus ponens from $\varphi_j$ and $\varphi_k = (\varphi_j \to \varphi_i)$, with $j, k < i$.
7. By the induction hypothesis, $\Gamma \vdash \forall x\, \varphi_j$ and $\Gamma \vdash \forall x\, (\varphi_j \to \varphi_i)$.
8. The formula $\forall x\, (\varphi_j \to \varphi_i) \to (\forall x\, \varphi_j \to \forall x\, \varphi_i)$ is a logical axiom of group 3.
9. Modus ponens with step 7 gives $\Gamma \vdash \forall x\, \varphi_j \to \forall x\, \varphi_i$.
10. Modus ponens with $\Gamma \vdash \forall x\, \varphi_j$ gives $\Gamma \vdash \forall x\, \varphi_i$.
11. The case $i = n$ gives $\Gamma \vdash \forall x\, \varphi$, which proves part 1.

**Part 2.**
Assume that $c$ does not occur in any member of $\Gamma$, and let $\alpha_1, \dots, \alpha_n$ be a deduction of $\varphi$ from $\Gamma$.
For a formula or term $\theta$, write $\theta'$ for the result of replacing each occurrence of $c$ in $\theta$ by $y$.

12. Choose a variable $y$ that occurs in none of $\alpha_1, \dots, \alpha_n$. One exists because the deduction uses finitely many symbols. Then $y$ does not occur in $\varphi = \alpha_n$.
13. We show that $\alpha_1', \dots, \alpha_n'$ is a deduction of $\varphi'$ from $\Gamma$. We check each line, in steps 14 to 23.
14. If $\alpha_i \in \Gamma$, then $c$ does not occur in $\alpha_i$, so $\alpha_i' = \alpha_i \in \Gamma$.
15. If $\alpha_i$ follows by modus ponens from $\alpha_j$ and $\alpha_j \to \alpha_i$, then $(\alpha_j \to \alpha_i)' = \alpha_j' \to \alpha_i'$, so $\alpha_i'$ follows by modus ponens from $\alpha_j'$ and $(\alpha_j \to \alpha_i)'$.
16. Let $\alpha_i = \forall x_1 \cdots \forall x_m\, \theta$ be a logical axiom, with $\theta$ in one of groups 1 to 6. Each $x_k$ differs from $y$, because $y$ does not occur in $\alpha_i$.
17. So $\alpha_i' = \forall x_1 \cdots \forall x_m\, \theta'$, and it suffices to show that $\theta'$ is in the same group as $\theta$.
18. Group 1. Let $v$ be a truth assignment to the prime formulas of $\theta'$. Define $u(A) = v(A')$ for each prime formula $A$ of $\theta$. Replacing $c$ commutes with $\neg$ and $\to$, so $\theta$ under $u$ and $\theta'$ under $v$ get the same value, by induction on $\theta$. That value is true, because $\theta$ is a [[tautology|05006AJ7DZ]].
19. Group 2. Here $\theta = \forall x\, \psi \to \psi[t/x]$ with $t$ substitutable for $x$ in $\psi$, and $x \neq y$. The replacement acts on $c$ and the substitution acts on free $x$, so $(\psi[t/x])' = \psi'[t'/x]$.
20. The term $t'$ is substitutable for $x$ in $\psi'$. Its variables are those of $t$, which no quantifier captures because $t$ is substitutable, and possibly $y$, which no quantifier captures because $\forall y$ does not occur in $\psi$. So $\theta' = \forall x\, \psi' \to \psi'[t'/x]$ is in group 2.
21. Group 3. $\theta'$ is $\forall x\, (\psi' \to \chi') \to (\forall x\, \psi' \to \forall x\, \chi')$, which is in group 3.
22. Group 4. $\theta = \psi \to \forall x\, \psi$ with $x$ not free in $\psi$. Since $x \neq y$, the variable $x$ is not free in $\psi'$, so $\theta' = \psi' \to \forall x\, \psi'$ is in group 4.
23. Groups 5 and 6. Replacing $c$ by $y$ in an atomic formula gives an atomic formula, and the variables named in the schema differ from $y$. So $\theta'$ is again in group 5 or group 6.
24. Steps 14 to 23 show that $\alpha_1', \dots, \alpha_n'$ is a deduction of $\varphi'$ from $\Gamma$.
25. Let $\Gamma_0$ be the set of members of $\Gamma$ that occur in this deduction. It is a deduction from $\Gamma_0$, so $\Gamma_0 \vdash \varphi'$.
26. The variable $y$ does not occur in any member of $\Gamma_0$, by the choice of $y$ in step 12.
27. Part 1 applied to $\Gamma_0$ and $y$ gives $\Gamma_0 \vdash \forall y\, \varphi'$.
28. Every deduction from $\Gamma_0$ is a deduction from $\Gamma$, so $\Gamma \vdash \forall y\, \varphi'$. This is $\Gamma \vdash \forall y\, \varphi_{c \mapsto y}$, which proves part 2.

## Idea

Part 1 puts $\forall x$ in front of every line of a deduction and repairs each step.
Axioms stay axioms because the axioms are closed under generalization, hypotheses get $\forall x$ from group 4, and modus ponens passes under $\forall x$ by group 3.
Part 2 replaces the constant $c$ by a fresh variable in the whole deduction, checks that each axiom stays an axiom, and then applies part 1.

## Variants

- In Mendelson's variant $\mathsf{H}_G$, part 1 needs no proof, because generalization is a rule. Part 2 is proved there by the same replacement of $c$ by a fresh variable, followed by the rule.
- A semantic proof of part 1 uses [[soundness|4A84VHDTHV]] and [[completeness|WQ1ZE255SF]]. If every structure and assignment that satisfy $\Gamma$ satisfy $\varphi$, then changing the value of $x$ keeps $\Gamma$ true, because $x$ is not free in $\Gamma$, and so it keeps $\varphi$ true. This proof is not used in practice, because the proof of completeness uses the generalization theorem.
