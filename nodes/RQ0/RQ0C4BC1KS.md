---
tag: RQ0C4BC1KS
kind: proof
name: Proof of algebraic completeness by the Lindenbaum algebra
msc: ["03B20", "06D20", "03G10"]
topics: [38EQ20GR7M]
audience: grad
proves: JM1XJXWZYH
uses: [NG943XNQWH, 52XCYMK0WW, 9X08XK5RV2, MGCVQXXQJH, 5083DHSK82]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Heyting_algebra
    locator: Heyting algebras as applied to intuitionistic logic
---

## Proof

We use the axioms 1 to 7 of [[the Hilbert system for IPC|52XCYMK0WW]].
In a Heyting algebra, $x \leq y \to z$ if and only if $x \wedge y \leq z$.
So $x \to y = 1$ if and only if $x \leq y$.

Part A: soundness.

1. Let $v$ be a valuation. Write $a, b, c$ for the values of $\varphi, \psi, \chi$.
2. Axiom 1: $a \wedge b \leq a$, so $a \leq b \to a$, and $v = 1$.
3. Axiom 2: put $x = a \to (b \to c)$ and $y = a \to b$. Then $a \wedge y \leq b$ and $a \wedge x \leq b \to c$.
4. So $a \wedge x \wedge y \leq b \wedge (b \to c) \leq c$. Hence $x \leq y \to (a \to c)$, and axiom 2 gets value $1$.
5. Axioms 3, 4 and 5: $a \wedge b \leq a$, $a \wedge b \leq a \wedge b$ and $a \leq a \vee b$.
6. Axiom 6: a Heyting algebra is distributive. So $(a \vee b) \wedge (a \to c) \wedge (b \to c) \leq (a \wedge (a \to c)) \vee (b \wedge (b \to c)) \leq c$.
7. Axiom 7: $0 \leq a$.
8. Modus ponens: if $a = 1$ and $a \to b = 1$, then $1 = a \leq b$.
9. By induction on derivations, every theorem gets value $1$. This proves item 1.

Part B: the Lindenbaum algebra.

10. Put $\varphi \equiv \psi$ if $\mathsf{IPC} \vdash \varphi \to \psi$ and $\mathsf{IPC} \vdash \psi \to \varphi$. Order the classes by $[\varphi] \leq [\psi]$ if $\mathsf{IPC} \vdash \varphi \to \psi$.
11. This is a well-defined partial order, since $\vdash \varphi \to \varphi$ and implication is transitive in $\mathsf{IPC}$.
12. By axioms 3 and 4, $[\varphi \wedge \psi]$ is the meet. By axioms 5 and 6, $[\varphi \vee \psi]$ is the join.
13. By axiom 7, $[\bot]$ is the least element. Every theorem $\top$ gives the greatest element $[\top]$, by axiom 1.
14. By the [[deduction theorem|9X08XK5RV2]], $\vdash \chi \to (\varphi \to \psi)$ if and only if $\vdash \chi \wedge \varphi \to \psi$. So $[\varphi \to \psi]$ is the relative pseudocomplement.
15. The operations are well defined on classes, by step 14 and the monotonicity of $\wedge$, $\vee$ and $\to$ in $\mathsf{IPC}$. So the Lindenbaum algebra $\mathcal{L}$ is a Heyting algebra.
16. Let $v_0(p) = [p]$. By induction on $\varphi$, $v_0(\varphi) = [\varphi]$.
17. Freeness: let $H$ be a Heyting algebra and $f$ a map from variables to $H$, with extension $v_f$. Put $h([\varphi]) = v_f(\varphi)$.
18. By step 9, $\vdash \varphi \to \psi$ gives $v_f(\varphi) \leq v_f(\psi)$. So $h$ is well defined and preserves order.
19. $h$ preserves the operations, by the clauses of $v_f$. It sends $[p]$ to $f(p)$.
20. The classes $[p]$ generate $\mathcal{L}$, so $h$ is the only such homomorphism. This proves item 2.

Part C: completeness.

21. Let $\varphi$ be valid in $\mathcal{L}$. Then $[\varphi] = v_0(\varphi) = [\top]$.
22. So $\vdash \top \to \varphi$, and modus ponens gives $\vdash \varphi$. This proves item 3.

Part D: logics and varieties.

23. Let $L$ be a superintuitionistic logic. Validity of $\varphi$ in $H$ is the equation $\varphi \approx 1$, where $1$ is the term $\bot \to \bot$.
24. So $\mathbf{V}(L)$ is defined by equations. It is closed under homomorphic images, subalgebras and products, so it is a variety.
25. The inclusion $L \subseteq \mathrm{Log}(\mathbf{V}(L))$ holds by definition. For the converse, form the Lindenbaum algebra $\mathcal{L}_L$ of $L$ as in steps 10 to 15, with $\vdash_L$ in place of $\vdash$.
26. Steps 10 to 15 use only theorems of $\mathsf{IPC}$ and modus ponens, so $\mathcal{L}_L$ is a Heyting algebra.
27. A valuation $v$ in $\mathcal{L}_L$ has the form $v(p) = [\sigma(p)]$ for a substitution $\sigma$. By induction, $v(\psi) = [\sigma(\psi)]$.
28. For $\psi \in L$, closure under substitution gives $\sigma(\psi) \in L$, so $v(\psi) = 1$. Hence $\mathcal{L}_L \in \mathbf{V}(L)$.
29. If $\varphi \notin L$, then $v_0(\varphi) = [\varphi] \neq 1$ in $\mathcal{L}_L$. So $\varphi \notin \mathrm{Log}(\mathbf{V}(L))$. This proves item 4.
30. Let $K$ be a variety. $\mathrm{Log}(K)$ contains $\mathsf{IPC}$ by step 9 and is closed under modus ponens by step 8.
31. It is closed under substitution: a valuation composed with a substitution is again a valuation.
32. By [[Birkhoff's theorem|5083DHSK82]], cited here, $K$ is the class of models of a set $E$ of equations $s \approx t$.
33. In a Heyting algebra, $s = t$ if and only if $(s \to t) \wedge (t \to s) = 1$. So $K$ is defined by the formulas $(s \to t) \wedge (t \to s)$.
34. These formulas lie in $\mathrm{Log}(K)$. So $\mathbf{V}(\mathrm{Log}(K)) \subseteq K$, and the inclusion $K \subseteq \mathbf{V}(\mathrm{Log}(K))$ is direct. This proves item 5.
35. Both maps reverse inclusion, and by items 4 and 5 they are inverse to each other. So they are lattice anti-isomorphisms. This proves item 6.

## Idea

Soundness checks that each axiom gets the top value, using the adjunction between $\wedge$ and $\to$.
For completeness, the formulas themselves, modulo provable equivalence, form a Heyting algebra.
In it, the valuation that sends each variable to its own class gives each formula its own class.
So a formula valid there is provably equivalent to $\top$.

## Variants

1. Completeness also follows from [[Kripke completeness|480TCT5CJ9]]: the up-sets of a Kripke frame form a Heyting algebra, and Kripke validity is validity in this algebra.
2. The same proof works for every superintuitionistic logic, as in Part D.
