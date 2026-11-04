---
tag: GJYYBPKQ32
kind: proof
name: Proof of Class existence theorem
proves: V5JFWF2SH8
sources:
  - wikipedia: en:528491@r1330985339
    locator: Von Neumann–Bernays–Gödel set theory, section Axiomatization of NBG > Class existence theorem
    note: adopted
    mention: wikipedia://en/528491#SNV3
    sections: [Proof]
---

## Proof

**Proof of the class existence theorem.thin** The proof starts by applying the transformation rules to the given formula to produce a transformed formula. Since this formula is equivalent to the given formula, the proof is completed by proving the class existence theorem for transformed formulas.

Gödel pointed out that the class existence theorem "is a metatheorem, that is, a theorem about the system \[NBG\], not in the system …" It is a theorem about NBG because it is proved in the metatheory by induction on NBG formulas. Also, its proof—instead of invoking finitely many NBG axioms—inductively describes how to use NBG axioms to construct a class satisfying a given formula. For every formula, this description can be turned into a constructive existence proof that is in NBG. Therefore, this metatheorem can generate the NBG proofs that replace uses of NBG's class existence theorem.

A recursive computer program succinctly captures the construction of a class from a given formula. The definition of this program does not depend on the proof of the class existence theorem. However, the proof is needed to prove that the class constructed by the program satisfies the given formula and is built using the axioms. This program is written in pseudocode that uses a Pascal-style case statement.

$$\begin{array}{l} \mathbf{function} \;\text{Class}(\phi, \,n) \\ \quad\begin{array}{rl} \mathbf{input}\!: \;\,&\phi \text{ is a transformed formula of the form } \phi(x_1, \ldots, x_n, Y_1, \ldots, Y_m); \\ &n \text{ specifies that a class of } n\text{-tuples is returned.} \\ \;\;\;\;\mathbf{output}\!: \;\,&\text{class } A \text{ of } n\text{-tuples satisfying } \\ &\,\forall x_1 \cdots \,\forall x_n [(x_1, \ldots , x_n) \in A \iff \phi(x_1, \ldots, x_n, Y_1, \ldots, Y_m)]. \end{array} \\ \mathbf{begin} \\ \quad \mathbf{case} \;\phi \;\mathbf{of} \\ \qquad \begin{alignedat}{2} x_i \in x_j: \;\;&\mathbf{return} \;\,E_{i,j,n}; &&\text{// } E_{i,j,n} \;\,= \{(x_1, \dots, x_n): x_i \in x_j\} \\ x_i \in Y_k: \;\;&\mathbf{return} \;\,E_{i,Y_k,n}; &&\text{// } E_{i,Y_k,n} = \{(x_1, \dots, x_{n}): x_i \in Y_k\} \\ \neg\psi: \;\;&\mathbf{return} \;\,\complement_{V^n}\text{Class}(\psi, \,n); &&\text{// } \complement_{V^n}\text{Class}(\psi, \,n) = V^n \setminus \text{Class}(\psi, \,n) \\ \psi_1 \land \psi_2: \;\;&\mathbf{return} \;\,\text{Class}(\psi_1, \,n) \cap \text{Class}(\psi_2, \,n);&& \\ \;\;\;\;\,\exists x_{n+1}(\psi): \;\;&\mathbf{return} \;\,Dom(\text{Class}(\psi, \,n+1)); &&\text{// } x_{n+1} \text{ is free in } \psi; \text{ Class}(\psi, \,n+1) \\ &\ &&\text{// returns a class of } (n+1)\text{-tuples} \end{alignedat} \\ \quad \mathbf{end} \\ \mathbf{end} \end{array}$$

Let $\phi$ be the formula of example 2. The function call $A = Class(\phi, 1)$ generates the class $A,$ which is compared below with $\phi.$ This shows that the construction of the class $A$ mirrors the construction of its defining formula $\phi.$

$$\begin{alignedat}{2} &\phi \;&&= \;\;\exists x_2\,(x_2 \!\in\! x_1 \land \;\;\neg\;\;\;\;\exists x_3\;(x_3 \!\in\! x_2)) \,\land \;\;\,\exists x_2\,(x_2 \!\in\! x_1 \land \;\;\,\exists x_3\,(x_3 \!\in\! x_2 \,\land\;\;\neg\;\;\;\;\exists x_4\;(x_4 \!\in\! x_3))) \\ &A \;&&= Dom\,(\;E_{2,1,2}\; \cap \;\complement_{V^2}\,Dom\,(\;E_{3,2,3}\;)) \,\cap\, Dom\,(\;E_{2,1,2}\;\cap \, Dom\,(\;\,E_{3,2,3}\; \cap \;\complement_{V^3}\,Dom\,(\;E_{4,3,4}\;))) \end{alignedat}$$
