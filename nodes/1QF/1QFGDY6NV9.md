---
tag: 1QFGDY6NV9
kind: proof
name: Proof of Peirce's law
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
proves: GMSZ75D5WE
uses: [H31CS3HK5P, 05RSK4Q657, 1MGMQX43B8, 9X08XK5RV2, Y060MF2NZ7]
methods: [0WCP0PVET6, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Peirce%27s_law
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Proof

We split on the truth value of $\varphi$ for the tautology, and we carry out the same split inside L with the law of proof by cases.
Let $\varphi$ and $\psi$ be formulas, and write $\pi$ for $((\varphi \to \psi) \to \varphi) \to \varphi$.

**Part 1: $\pi$ is a tautology.** Let $v$ be a [[truth assignment|H31CS3HK5P]].
We use the [[truth table|05RSK4Q657]] of $\to$: $a \to b$ has the value $0$ exactly when $a = 1$ and $b = 0$.

1. Case $v(\varphi) = 1$.
   The consequent of $\pi$ is $\varphi$, so $v(\pi) = v((\varphi \to \psi) \to \varphi) \to 1 = 1$.
2. Case $v(\varphi) = 0$.
   Then $v(\varphi \to \psi) = 0 \to v(\psi) = 1$, so $v((\varphi \to \psi) \to \varphi) = 1 \to 0 = 0$, and $v(\pi) = 0 \to 0 = 1$.
3. In both cases $v(\pi) = 1$.
   Since $v$ was arbitrary, $\pi$ is a tautology.

**Part 2: $\vdash \pi$ in L.** We write $\eta$ for the hypothesis $(\varphi \to \psi) \to \varphi$.
We use the [[deduction theorem|9X08XK5RV2]] (DT) and the laws T1, T4 and T8 of the [[basic theorems of L|Y060MF2NZ7]].

1. The following lines form a derivation from $\{ \eta, \ \neg \varphi \}$:
   $$\begin{array}{rll} 1. & (\varphi \to \psi) \to \varphi & \text{hypothesis } \eta \\ 2. & \neg \varphi & \text{hypothesis} \\ 3. & \neg \varphi \to (\varphi \to \psi) & \text{T4} \\ 4. & \varphi \to \psi & \text{MP, lines 2 and 3} \\ 5. & \varphi & \text{MP, lines 4 and 1} \end{array}$$
   So $\{ \eta, \ \neg \varphi \} \vdash \varphi$.
2. By DT, $\{ \eta \} \vdash \neg \varphi \to \varphi$.
3. By T1, $\vdash \varphi \to \varphi$.
4. By T8 with $\varphi$ in the place of $\psi$, $\vdash (\varphi \to \varphi) \to ((\neg \varphi \to \varphi) \to \varphi)$.
5. Modus ponens with steps 3 and 4 gives $\vdash (\neg \varphi \to \varphi) \to \varphi$.
6. Modus ponens with steps 2 and 5 gives $\{ \eta \} \vdash \varphi$.
7. By DT, $\vdash \eta \to \varphi$, that is, $\vdash ((\varphi \to \psi) \to \varphi) \to \varphi$.

This proves both parts of Peirce's law.

## Idea

The semantic part is a case split on the value of $\varphi$: if $\varphi$ is false, the antecedent $(\varphi \to \psi) \to \varphi$ is false.
The derivation follows the same split inside L.
Under the hypothesis $\eta$, the case $\neg \varphi$ leads to $\varphi$ through $\varphi \to \psi$, and the case $\varphi$ leads to $\varphi$ at once.
Then T8, proof by cases on $\varphi$ and $\neg \varphi$, gives $\varphi$.

## Variants

Part 2 also follows from Part 1 and the [[completeness theorem for propositional logic|81ZNY1XKYJ]], since every tautology in $\neg$ and $\to$ is a theorem of L.
That route gives no explicit derivation, and it uses a much deeper theorem.
In the [[implicational propositional calculus|ZMVBAY7ZZD]], Peirce's law is an axiom, so it needs no proof there; its role is to make that system complete.
