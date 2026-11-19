---
tag: V7MTF4P01E
kind: definition
name: Minimal logic
msc: ["03B20"]
topics: [38EQ20GR7M]
audience: grad
defines: 3MBG95617E
uses: [52XCYMK0WW, 1MGMQX43B8, 0Y0MQYST0M, 5GTQ69W47T]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_logic
    locator: Syntax and axiomatization
  - url: https://en.wikipedia.org/wiki/Minimal_logic
    locator: Relation to intuitionistic logic
---

## Definition

The formulas of minimal logic are built from propositional variables and a constant $\bot$ with $\wedge$, $\vee$ and $\to$.
The negation $\neg\varphi$ abbreviates $\varphi \to \bot$.
*Minimal logic* $\mathsf{ML}$ is the set of formulas derivable in the [[Hilbert system|1MGMQX43B8]] with axioms 1 to 6 of [[intuitionistic logic|52XCYMK0WW]] and the rule of [[modus ponens|0Y0MQYST0M]].
These axioms are the following schemes.

1. $\varphi \to (\psi \to \varphi)$.
2. $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$.
3. $\varphi \wedge \psi \to \varphi$ and $\varphi \wedge \psi \to \psi$.
4. $\varphi \to (\psi \to \varphi \wedge \psi)$.
5. $\varphi \to \varphi \vee \psi$ and $\psi \to \varphi \vee \psi$.
6. $(\varphi \to \chi) \to ((\psi \to \chi) \to (\varphi \vee \psi \to \chi))$.

No axiom mentions $\bot$, so $\bot$ is an atom with no special rule.

## Notation

$\mathsf{ML}$ is also written $\mathsf{MPC}$ or $\mathsf{J}$, and $\vdash_{\mathsf{m}}$ is derivability in it.
A *minimal Kripke model* is a [[Kripke model for intuitionistic logic|5GTQ69W47T]] with one more up-set $F$, and $w \Vdash \bot$ means $w \in F$.

## Remarks

1. $\mathsf{IPC}$ is $\mathsf{ML}$ plus the scheme $\bot \to \varphi$. In natural deduction, $\mathsf{ML}$ is $\mathrm{NJ}$ without the rule "from $\bot$ infer $\varphi$".
2. The deduction theorem holds for $\mathsf{ML}$, since its proof uses only axioms 1 and 2.
3. Relation to $\mathsf{IPC}$. Let $X_\varphi$ be the conjunction of $\bot \to p$ over the variables $p$ of $\varphi$. Then $\mathsf{IPC} \vdash \varphi$ if and only if $\mathsf{ML} \vdash X_\varphi \to \varphi$. The proof is in the steps below.
4. Soundness and completeness: $\mathsf{ML} \vdash \varphi$ if and only if $\varphi$ is true at every world of every minimal Kripke model. It follows from the [[Kripke completeness of intuitionistic logic|480TCT5CJ9]] applied to $\varphi[f/\bot]$, with $f$ a new variable. A cut-free $\mathrm{LJ}$ derivation of a formula without $\bot$ uses no rule for $\bot$, so $\mathsf{ML} \vdash \varphi$ if and only if $\mathsf{IPC} \vdash \varphi[f/\bot]$.
5. Example: the instance $\bot \to (p \to \bot)$ of axiom 1 is $\bot \to \neg p$, so every negation follows from $\bot$.
6. Non-example: $\bot \to p$ is not derivable; see [[ex falso is not a theorem of minimal logic|T2SXPH67RQ]].

Proof of remark 3.

1. Assume $\mathsf{ML} \vdash X_\varphi \to \varphi$. Each conjunct of $X_\varphi$ is an $\mathsf{IPC}$ axiom, so $\mathsf{IPC} \vdash \varphi$.
2. Conversely, let $D$ be an $\mathsf{IPC}$ derivation of $\varphi$. Replace every variable of $D$ that is not in $\varphi$ by $\bot$.
3. Axiom instances stay axiom instances, and modus ponens steps stay correct. So the result is an $\mathsf{IPC}$ derivation of $\varphi$ in the variables of $\varphi$.
4. Claim: $\mathsf{ML} \vdash X_\varphi \to (\bot \to \chi)$ for every $\chi$ in the variables of $\varphi$. We use induction on $\chi$.
5. For $\chi = p$, the formula $\bot \to p$ is a conjunct of $X_\varphi$. For $\chi = \bot$, $\bot \to \bot$ is derivable.
6. For $\chi = \chi_1 \wedge \chi_2$, combine the two induction hypotheses with axiom 4. For $\chi = \chi_1 \vee \chi_2$, use axiom 5.
7. For $\chi = \chi_1 \to \chi_2$, from $\bot \to \chi_2$ and axiom 1 we get $\bot \to (\chi_1 \to \chi_2)$.
8. So under the hypothesis $X_\varphi$, each axiom instance $\bot \to \chi$ in the derivation of step 3 is derivable in $\mathsf{ML}$.
9. Hence $X_\varphi \vdash_{\mathsf{m}} \varphi$, and the deduction theorem gives $\mathsf{ML} \vdash X_\varphi \to \varphi$.

Negative formulas.
A formula is *negative* if it is built from $\bot$ and negated variables $\neg p$ by $\wedge$ and $\to$.
For negative $\varphi$, $\mathsf{IPC} \vdash \varphi$ if and only if $\mathsf{ML} \vdash \varphi$.

1. One direction holds since $\mathsf{ML} \subseteq \mathsf{IPC}$.
2. Let $\mathsf{ML} \nvdash \varphi$. By remark 4, a minimal Kripke model with up-sets $V(p)$ and $F$ refutes $\varphi$ at a world $w$.
3. Put $V'(p) := V(p) \cup F$. This is again an up-set, and $\bot \to p$ is now true at every world.
4. A world forces $\neg p$ under $V'$ if and only if no later world is in $V(p) \setminus F$. The same holds under $V$.
5. So $\neg p$ has the same truth set under $V$ and $V'$. By induction on $\wedge$ and $\to$, so does every negative formula.
6. Hence the new model refutes $X_\varphi \to \varphi$ at $w$, so $\mathsf{ML} \nvdash X_\varphi \to \varphi$ by soundness. Remark 3 gives $\mathsf{IPC} \nvdash \varphi$.

## Explanations

### L1 human

Minimal logic uses six of the seven axiom schemes of intuitionistic logic.
The missing scheme says that a contradiction implies every statement.
So in minimal logic, the symbol for contradiction is just a letter with no rule attached.
For example, "if $\bot$ then $p$" can not be derived, but "if $p$ then $p$" can.

### L2 human

We derive $(p \to q) \to (\neg q \to \neg p)$ in natural deduction for $\mathsf{ML}$.

1. Assume $p \to q$, assume $\neg q$, and assume $p$.
2. From $p$ and $p \to q$, get $q$.
3. From $q$ and $\neg q$, that is, $q \to \bot$, get $\bot$.
4. Discharge $p$, and get $\neg p$.
5. Discharge $\neg q$ and then $p \to q$.

The typical use of the definition is to sort negation laws into those that need ex falso and those that do not.
A trap: one may not treat $\bot$ as "false" in a truth table for $\mathsf{ML}$, since the two-valued table with $\bot = 0$ validates $\bot \to p$.
