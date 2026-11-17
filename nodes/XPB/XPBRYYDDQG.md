---
tag: XPBRYYDDQG
kind: proof
name: Proof of the derivability conditions by formalized Σ1-completeness
msc: ["03F40"]
topics: [HXHHWY3328]
audience: grad
proves: F6H4STF9RG
uses: [NB2BCZR40F, 6M12VR1GT6, MPSCREYC3M, TT8MXRTVBM]
methods: [0NTF6DMVAP, 0ASJVEFA9J, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Bernays_provability_conditions
    locator: lead section
  - book: isbn:9780521857840
---

## Proof

We write $\square \varphi$ for $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$, as in the statement.
For a formula $\varphi(x)$, we write $\square \varphi(\dot{x})$ for the formula $\mathrm{Prov}_T(\mathrm{sub}(\ulcorner \varphi \urcorner, \mathrm{num}(x)))$.
It says "$\varphi$ applied to the numeral of $x$ is provable", with $x$ free.
D2 and the outline of D3 use facts about codes that $\mathsf{PA}$ proves by induction; we state these facts and do not write out their proofs.

Proof of D1.

1. Assume $T \vdash \varphi$, and let $p$ be the code of a proof of $\varphi$ in $T$.
2. The relation $\mathrm{Prf}_T(p, \# \varphi)$ is true, by the choice of $p$.
3. By the representability theorem of [[arithmetization of syntax|6M12VR1GT6]], $\mathsf{Q} \vdash \mathrm{Prf}_T(\underline{p}, \ulcorner \varphi \urcorner)$.
4. By the rule for $\exists$, $\mathsf{Q} \vdash \square \varphi$. Since $T \supseteq \mathsf{Q}$, $T \vdash \square \varphi$.

Proof of D2.

5. Let $c(y, z, x)$ be the primitive recursive function that writes the lines of $y$, then the lines of $z$, then the formula with code $x$.
6. If $y$ codes a proof of $\varphi \to \psi$ and $z$ codes a proof of $\varphi$, then $c(y, z, \# \psi)$ codes a proof of $\psi$. Each old line keeps its reason, and the new last line follows by modus ponens.
7. $\mathsf{PA}$ proves the formal version: $\forall y \, \forall z \, (\mathrm{Prf}_T(y, \ulcorner \varphi \to \psi \urcorner) \wedge \mathrm{Prf}_T(z, \ulcorner \varphi \urcorner) \to \mathrm{Prf}_T(c(y, z, \ulcorner \psi \urcorner), \ulcorner \psi \urcorner))$. The proof is induction on the length of $y$ and $z$, which formalizes step 6.
8. From step 7, the logical rules for $\exists$ give $\mathsf{PA} \vdash \square (\varphi \to \psi) \to (\square \varphi \to \square \psi)$, so $T$ proves D2.
9. The same argument with free variables gives $\mathsf{PA} \vdash \forall x \, (\square (\varphi(\dot{x}) \to \psi(\dot{x})) \to (\square \varphi(\dot{x}) \to \square \psi(\dot{x})))$.

Formalized $\Sigma_1$-completeness, outline.
We show: for each $\Sigma_1$ formula $\sigma(\vec{x})$, $\mathsf{PA} \vdash \sigma(\vec{x}) \to \square \sigma(\dot{\vec{x}})$.
The proof is an induction on the build of $\sigma$ from atomic formulas, negated atomic formulas, $\wedge$, $\vee$, bounded $\forall$ and $\exists$.

10. Special case for terms. We prove $\mathsf{PA} \vdash \forall x \, \forall y \, \square (\dot{x} + \dot{y} = (x + y)^{\boldsymbol{\cdot}})$ by induction on $y$ in $\mathsf{PA}$.
11. Base $y = 0$. The sentence $\forall v \, (v + 0 = v)$ is axiom 4 of [[Robinson arithmetic|TT8MXRTVBM]], so D1 gives $\square \forall v \, (v + 0 = v)$.
12. The instance $\forall v \, (v + 0 = v) \to \dot{x} + 0 = \dot{x}$ is a logical axiom for each $x$. $\mathsf{PA}$ proves that its code is an axiom code, so $\mathsf{PA} \vdash \forall x \, \square (\forall v \, (v + 0 = v) \to \dot{x} + 0 = \dot{x})$.
13. By steps 11 and 12 and step 9, $\mathsf{PA} \vdash \forall x \, \square (\dot{x} + 0 = \dot{x})$. Since $\mathrm{num}(0)$ is the code of the term $0$ and $x + 0 = x$, this is the base case.
14. Step $y \to y + 1$. Assume $\square (\dot{x} + \dot{y} = (x + y)^{\boldsymbol{\cdot}})$. By $\mathrm{num}(y + 1) = $ the code of $S$ followed by $\mathrm{num}(y)$, the numeral of $y + 1$ is the term $S \dot{y}$.
15. As in steps 11 to 13, axiom 5 of $\mathsf{Q}$ gives $\square (\dot{x} + S \dot{y} = S (\dot{x} + \dot{y}))$.
16. The equality axiom $a = b \to S a = S b$ and step 9 turn the assumption of step 14 into $\square (S(\dot{x} + \dot{y}) = S (x + y)^{\boldsymbol{\cdot}})$.
17. The term $S (x + y)^{\boldsymbol{\cdot}}$ is the numeral of $x + y + 1$, by the definition of $\mathrm{num}$. The transitivity of equality and step 9 combine steps 15 and 16 into $\square (\dot{x} + (y + 1)^{\boldsymbol{\cdot}} = (x + (y + 1))^{\boldsymbol{\cdot}})$.
18. The formula $\square (\dot{x} + \dot{y} = (x + y)^{\boldsymbol{\cdot}})$ is $\Sigma_1$, and $\mathsf{PA}$ has induction for it. So steps 13 and 17 give the claim of step 10.
19. In the same way, $\mathsf{PA}$ proves $\square (t(\dot{\vec{x}}) = (t(\vec{x}))^{\boldsymbol{\cdot}})$ for every term $t$, by induction on $t$, with a similar lemma for $\cdot$.
20. Atomic case $s = t$: if $s(\vec{x}) = t(\vec{x})$, step 19 for $s$ and $t$, symmetry and transitivity give $\square (s(\dot{\vec{x}}) = t(\dot{\vec{x}}))$.
21. Negated atomic case: $\mathsf{PA}$ proves $\forall m \, \forall n \, (m \ne n \to \square (\dot{m} \ne \dot{n}))$ by induction, from axioms 1 and 2 of $\mathsf{Q}$; combined with step 19 this gives the case $s \ne t$.
22. The cases $\wedge$, $\vee$ and $\exists$ follow from the induction hypothesis, step 9 and the logical axioms for these connectives.
23. The case $\forall z \le t$ uses induction on the bound, with the theorem $\mathsf{PA} \vdash \forall k \, \forall z \, (z \le S k \leftrightarrow z \le k \vee z = S k)$.
24. This ends the outline: $\mathsf{PA} \vdash \sigma(\vec{x}) \to \square \sigma(\dot{\vec{x}})$ for every $\Sigma_1$ formula $\sigma$.

Proof of D3.

25. For a sentence $\varphi$, the sentence $\square \varphi$ is $\Sigma_1$, because $\mathrm{Prf}_T$ is $\Sigma_1$ and $\mathrm{Prov}_T$ adds one $\exists$.
26. Formalized $\Sigma_1$-completeness for $\sigma = \square \varphi$ gives $\mathsf{PA} \vdash \square \varphi \to \square \square \varphi$.
27. Since $T \supseteq \mathsf{PA}$, $T \vdash \square \varphi \to \square \square \varphi$. This is D3, and the proof is complete up to the facts of steps 7, 12 and 19 to 23, which are routine inductions in $\mathsf{PA}$.

## Idea

D1 is representability: a real proof is a number, and $\mathsf{Q}$ checks it.
D2 is modus ponens on codes: two proofs joined with one more line give a proof.
D3 is D1 carried out inside $T$, and this needs $T$ to prove, with free variables, that true $\Sigma_1$ statements are provable.
That formalized completeness is an induction on formulas, which needs induction in $T$.

## Variants

For $T \supseteq \mathsf{I}\Sigma_1$ the same outline works, because every induction in steps 18 to 23 is on a $\Sigma_1$ formula.
Another route first reduces each $\Sigma_1$ formula, provably in $\mathsf{PA}$, to the form $\exists \vec{y} \, (s = t)$, by the theorem of Matiyasevich, Robinson, Davis and Putnam.
Then only the atomic case, step 20, and the $\exists$ case are needed, at the price of a deep theorem about Diophantine sets.
