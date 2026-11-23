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

To prove $\varphi(\underline{3})$ from $\varphi(0)$ and the step $\forall x \, (\varphi(x) \to \varphi(Sx))$, no induction is needed: three uses of modus ponens carry $\varphi$ from $0$ to $1$, to $2$ and to $3$.
Every single case of induction is a finite proof of this kind.
Uniform reflection is the principle that collects all these finite proofs into one universal statement, and so it gives the full induction schema.

Let $\mathsf{PRA}$ be [[primitive recursive arithmetic|WCXH72T8D8]] as a first-order theory.
Its language has a function symbol for each [[primitive recursive function|5NVA2JRHPV]].
Its axioms are the axioms for $0$ and $S$, the defining equations of these functions, and induction for formulas without quantifiers.
In this language, let $\mathsf{PA}$ mean $\mathsf{PRA}$ plus induction for all formulas.
The uniform [[reflection principle|NB485KFXKV]] $\mathrm{RFN}(\mathsf{PRA})$ is the schema of the sentences
$$\forall y \, \forall z \, \bigl(\mathrm{Prov}_{\mathsf{PRA}}(\ulcorner \psi(\dot{y}, \dot{z}) \urcorner) \to \psi(y, z)\bigr),$$
one for each formula $\psi(y, z)$, where $z$ may be a list of variables.
We show that $\mathsf{PRA} + \mathrm{RFN}(\mathsf{PRA})$ proves every instance of induction, so it contains $\mathsf{PA}$.

Fix a formula $\varphi(x, z)$ and put
$$\psi(y, z) := \bigl(\varphi(0, z) \wedge \forall x \, (\varphi(x, z) \to \varphi(Sx, z))\bigr) \to \varphi(y, z).$$

1. Fix numbers $n$ and $m$, and write $A$ for the antecedent $\varphi(0, \underline{m}) \wedge \forall x \, (\varphi(x, \underline{m}) \to \varphi(Sx, \underline{m}))$.
   We describe a proof of $\psi(\underline{n}, \underline{m})$ in pure first-order logic.
2. From the hypothesis $A$ we get $\varphi(0, \underline{m})$, by the rule for $\wedge$.
3. From $A$ we also get $\varphi(\underline{k}, \underline{m}) \to \varphi(\underline{k+1}, \underline{m})$ for each $k < n$, by instantiating $x := \underline{k}$.
   Here $S\underline{k}$ is the numeral $\underline{k+1}$.
4. Starting from step 2, $n$ uses of modus ponens with the formulas of step 3 give $\varphi(\underline{n}, \underline{m})$.
5. The deduction theorem turns steps 2 to 4 into a proof of $A \to \varphi(\underline{n}, \underline{m})$, which is $\psi(\underline{n}, \underline{m})$.
6. The construction is uniform: a primitive recursive function $p$ gives the code $p(n, m)$ of this proof.
   The proof is built by a recursion on $n$ from syntactic operations that are primitive recursive, by the [[arithmetization of syntax|6M12VR1GT6]].
7. A proof in pure logic is also a $\mathsf{PRA}$-proof, so $p(n, m)$ codes a $\mathsf{PRA}$-proof of $\psi(\underline{n}, \underline{m})$ for all $n$ and $m$.
8. The statement of step 7 is a quantifier-free formula in the variables $n$ and $m$, and $\mathsf{PRA}$ proves it by quantifier-free induction on $n$.
   This check is a routine part of the arithmetization of syntax inside $\mathsf{PRA}$, and we do not write it out.
   So $\mathsf{PRA} \vdash \forall y \, \forall z \, \mathrm{Prov}_{\mathsf{PRA}}(\ulcorner \psi(\dot{y}, \dot{z}) \urcorner)$.
9. The instance of $\mathrm{RFN}(\mathsf{PRA})$ for $\psi$ and step 8 give $\forall y \, \forall z \, \psi(y, z)$, by modus ponens under the quantifiers.
10. The variable $y$ does not occur in the antecedent of $\psi$.
    So $\forall y \, \psi(y, z)$ is logically equivalent to $\bigl(\varphi(0, z) \wedge \forall x \, (\varphi(x, z) \to \varphi(Sx, z))\bigr) \to \forall y \, \varphi(y, z)$.
11. With step 9, this is the instance of induction for $\varphi$, with all parameters $z$ universally quantified.

Since $\varphi$ was arbitrary, $\mathsf{PRA} + \mathrm{RFN}(\mathsf{PRA})$ proves every axiom of $\mathsf{PA}$.

## Remarks

The uniform principle is essential here.
For each single $n$ the sentence $\psi(\underline{n}, \underline{m})$ is already provable by steps 1 to 5, so local reflection for these sentences adds nothing.
The gain is the step from "for each $n$, a proof" to "$\forall y$", and only the uniform principle makes it.

The converse inclusion, that $\mathsf{PA}$ proves each instance of $\mathrm{RFN}(\mathsf{PRA})$, is the hard half of the Kreisel-Lévy theorem of 1968.
One standard proof bounds the complexity of the formulas in a $\mathsf{PRA}$-proof by cut elimination, and then uses a [[partial truth predicate|Y2MF1EZAM7]] for that complexity, with induction on the proof inside $\mathsf{PA}$.
Together the two halves show that $\mathsf{PA}$ and $\mathsf{PRA} + \mathrm{RFN}(\mathsf{PRA})$ have the same theorems.

If we replace $\mathsf{PRA}$ by $\mathsf{PA}$, the same steps show that $\mathsf{PA} + \mathrm{RFN}(\mathsf{PA})$ contains $\mathsf{PA}$.
That theory is a proper extension of $\mathsf{PA}$, since it proves $\mathrm{Con}(\mathsf{PA})$.

## Explanations

### L1 human

Induction is the rule "if a property holds for $0$ and passes from each number to the next, it holds for all numbers".
For one fixed number, such as $5$, no rule is needed: we pass from $0$ to $1$, then to $2$, and so on, five times.
A simple program can write these short arguments, one for each number.
A weak theory can check that the program always writes a correct proof.
Uniform reflection then says "whatever this theory proves for every number is true for every number".
Together this gives induction for the property.

### L2 human

Take $\varphi(x) := (0 + x = x)$, with no parameters, and $n = 2$.
The antecedent $A$ is $0 + 0 = 0 \wedge \forall x \, (0 + x = x \to 0 + Sx = Sx)$.
From $A$ we get $0 + 0 = 0$.
Instantiating at $x := 0$ and at $x := S0$ gives
$$0 + 0 = 0 \to 0 + S0 = S0, \qquad 0 + S0 = S0 \to 0 + SS0 = SS0.$$
Two uses of modus ponens give $0 + SS0 = SS0$, so $A \to 0 + SS0 = SS0$ is proved.
The proof for $n$ has $n$ uses of modus ponens, so the program that writes it is a simple loop.
This is the typical use: a strong theory is shown equivalent to a weak theory plus reflection.
Watch out: these proofs grow with $n$, so no single proof of fixed length covers all $n$, and the step to $\forall y$ really needs reflection.
