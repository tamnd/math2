---
tag: DGQRT1BVJ3
kind: example
name: Uniform reflection over PRA proves the induction schema
msc: ["03F30", "03F40"]
topics: [HXHHWY3328]
audience: research
instance_of: [NB485KFXKV]
uses: [NB485KFXKV, 5NVA2JRHPV, NB2BCZR40F, 6M12VR1GT6, MPSCREYC3M, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_principle
    locator: For arithmetic
---

## Example

Let $\mathsf{PRA}$ be primitive recursive arithmetic as a first-order theory.
Its language has a function symbol for each [[primitive recursive function|5NVA2JRHPV]], its axioms are the axioms for $0$ and $S$, the defining equations of these functions, and the induction schema for formulas without quantifiers.
In this language, let $\mathsf{PA}$ mean $\mathsf{PRA}$ plus the induction schema for all formulas.
The uniform [[reflection principle|NB485KFXKV]] $\mathrm{RFN}(\mathsf{PRA})$ is the schema of the sentences
$$\forall y \, \forall z \, \bigl(\mathrm{Prov}_{\mathsf{PRA}}(\ulcorner \psi(\dot{y}, \dot{z}) \urcorner) \to \psi(y, z)\bigr),$$
one for each formula $\psi(y, z)$, where $z$ may stand for a list $z_1, \ldots, z_k$ of variables.
We show that $\mathsf{PRA} + \mathrm{RFN}(\mathsf{PRA})$ proves every instance of the induction schema, so it contains $\mathsf{PA}$.
This is the easy half of the Kreisel-Lévy theorem.

Fix a formula $\varphi(x, z)$ and put
$$\psi(y, z) := \bigl(\varphi(0, z) \wedge \forall x \, (\varphi(x, z) \to \varphi(Sx, z))\bigr) \to \varphi(y, z).$$

1. Fix numbers $n$ and $m$, and write $A$ for the antecedent $\varphi(0, \underline{m}) \wedge \forall x \, (\varphi(x, \underline{m}) \to \varphi(Sx, \underline{m}))$. We describe a proof of $\psi(\underline{n}, \underline{m})$ in pure first-order logic.
2. From the hypothesis $A$ we get $\varphi(0, \underline{m})$, by the rule for $\wedge$.
3. From $A$ we get $\forall x \, (\varphi(x, \underline{m}) \to \varphi(Sx, \underline{m}))$, and by instantiation with $x := \underline{k}$ we get $\varphi(\underline{k}, \underline{m}) \to \varphi(\underline{k+1}, \underline{m})$ for each $k < n$. Here $S\underline{k}$ is the numeral $\underline{k+1}$.
4. Starting from step 2, $n$ uses of modus ponens with the formulas of step 3 give $\varphi(\underline{n}, \underline{m})$.
5. The deduction theorem turns steps 2 to 4 into a proof of $A \to \varphi(\underline{n}, \underline{m})$, which is $\psi(\underline{n}, \underline{m})$.
6. The construction of steps 1 to 5 is uniform: there is a primitive recursive function $p$ such that $p(n, m)$ is the code of this proof. The reason is that the proof is built by a recursion on $n$ from syntactic operations that are primitive recursive, by the [[arithmetization of syntax|6M12VR1GT6]].
7. A proof in pure logic is also a proof in $\mathsf{PRA}$. So for all $n$, $m$ the number $p(n, m)$ codes a $\mathsf{PRA}$-proof of $\psi(\underline{n}, \underline{m})$.
8. The statement of step 7 is a quantifier-free formula of the language of $\mathsf{PRA}$ in the variables $n$, $m$, and $\mathsf{PRA}$ proves it by quantifier-free induction on $n$. This verification is a routine part of the arithmetization of syntax inside $\mathsf{PRA}$, and we do not write it out. So $\mathsf{PRA} \vdash \forall y \, \forall z \, \mathrm{Prov}_{\mathsf{PRA}}(\ulcorner \psi(\dot{y}, \dot{z}) \urcorner)$.
9. The instance of $\mathrm{RFN}(\mathsf{PRA})$ for $\psi$ and step 8 give, by modus ponens under the quantifiers, $\forall y \, \forall z \, \psi(y, z)$.
10. The variable $y$ does not occur in the antecedent of $\psi$. So $\forall y \, \psi(y, z)$ is logically equivalent to $\bigl(\varphi(0, z) \wedge \forall x \, (\varphi(x, z) \to \varphi(Sx, z))\bigr) \to \forall y \, \varphi(y, z)$.
11. With step 9, this gives the instance of the induction schema for $\varphi$, with all parameters $z$ universally quantified.

Since $\varphi$ was arbitrary, $\mathsf{PRA} + \mathrm{RFN}(\mathsf{PRA})$ proves every axiom of $\mathsf{PA}$.

## Remarks

The example uses the uniform principle in an essential way.
For each single $n$ the sentence $\psi(\underline{n}, \underline{m})$ is already provable, by steps 1 to 5, so local reflection for these sentences adds nothing; the gain is the passage from all $n$ to $\forall y$.
The converse inclusion, that $\mathsf{PA}$ proves each instance of $\mathrm{RFN}(\mathsf{PRA})$, is the hard half of the Kreisel-Lévy theorem of 1968.
One standard proof uses a cut elimination argument to bound the complexity of the formulas in a $\mathsf{PRA}$-proof, and then a [[partial truth predicate|Y2MF1EZAM7]] for that complexity, with induction on the length of the proof inside $\mathsf{PA}$.
Together, the two halves show that $\mathsf{PA}$ and $\mathsf{PRA} + \mathrm{RFN}(\mathsf{PRA})$ have the same theorems.
If we replace $\mathsf{PRA}$ by $\mathsf{PA}$ in the example, we obtain $\mathsf{PA} + \mathrm{RFN}(\mathsf{PA})$, a proper extension of $\mathsf{PA}$, since it proves $\mathrm{Con}(\mathsf{PA})$.

## Explanations

### L1 human

Induction is the rule "if a property holds for $0$, and passes from each number to the next, then it holds for all numbers".
For one fixed number, such as $5$, no rule is needed: we pass from $0$ to $1$, from $1$ to $2$, and so on, five times.
These short arguments can be written down by a simple program, one argument for each number.
A weak theory can check that the program always writes a correct proof.
The uniform reflection principle then says "whatever this theory proves, for every number, is true for every number".
Together this gives induction for the property.

### L2 human

We take $\varphi(x) := (x + 0 = x)$, with no parameters, and $n = 2$.

1. The antecedent $A$ is $0 + 0 = 0 \wedge \forall x \, (x + 0 = x \to Sx + 0 = Sx)$.
2. From $A$ we get $0 + 0 = 0$.
3. From $A$ and the instances $x := 0$ and $x := S0$ we get $0 + 0 = 0 \to S0 + 0 = S0$ and $S0 + 0 = S0 \to SS0 + 0 = SS0$.
4. Two uses of modus ponens give $SS0 + 0 = SS0$, so $A \to SS0 + 0 = SS0$ is proved.
5. The proof for $n$ has $n$ uses of modus ponens, so a program that writes it for each $n$ is a simple loop.

The typical use is to show that a strong theory is equivalent to a weak one plus reflection, as $\mathsf{PA}$ is to $\mathsf{PRA}$ plus uniform reflection.
A trap: the proofs of step 4 grow with $n$, so no single proof of fixed length covers all $n$, and the passage to $\forall y$ really needs the reflection principle.
