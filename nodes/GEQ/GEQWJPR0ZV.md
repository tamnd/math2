---
tag: GEQWJPR0ZV
kind: example
name: A derivation that uses Peirce's law in the implicational calculus
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
illustrates: [ZMVBAY7ZZD, GMSZ75D5WE]
uses: [ZMVBAY7ZZD, GMSZ75D5WE, 9X08XK5RV2, 0Y0MQYST0M, NG943XNQWH]
sources:
  - url: https://en.wikipedia.org/wiki/Peirce%27s_law
    locator: Using Peirce's law with the deduction theorem
  - url: https://en.wikipedia.org/wiki/Implicational_propositional_calculus
    locator: Axiom system
---

## Example

Let $p$ and $q$ be propositional variables.
We derive $((p \to q) \to q) \to ((q \to p) \to p)$ in the [[implicational propositional calculus|ZMVBAY7ZZD]], with the axioms K, S, [[Peirce's law|GMSZ75D5WE]] and [[modus ponens|0Y0MQYST0M]].
Since $(p \to q) \to q$ expresses $p \lor q$, the formula says that $p \lor q$ implies $q \lor p$.
The [[deduction theorem|9X08XK5RV2]] holds in this system, since its proof uses only K, S and modus ponens.

1. Let $\Gamma = \set{(p \to q) \to q, \; q \to p}$. From $\Gamma \cup \set{p \to q}$ we derive $p$: the hypotheses $p \to q$ and $(p \to q) \to q$ give $q$ by modus ponens, and then $q$ and $q \to p$ give $p$.
2. The deduction theorem, applied to step 1, gives $\Gamma \vdash (p \to q) \to p$.
3. The formula $((p \to q) \to p) \to p$ is an instance of Peirce's law, so $\Gamma \vdash ((p \to q) \to p) \to p$.
4. Modus ponens with steps 2 and 3 gives $\Gamma \vdash p$.
5. The deduction theorem, used twice, gives $\vdash ((p \to q) \to q) \to ((q \to p) \to p)$.

## Remarks

Peirce's law is needed here: the formula is not derivable from K and S alone.
In the three-element [[Heyting algebra|NG943XNQWH]] $0 < \tfrac12 < 1$, with $a \to b = 1$ when $a \le b$ and $a \to b = b$ otherwise, K and S always take the value $1$ and modus ponens preserves the value $1$.
Take $p = \tfrac12$ and $q = 0$: then $(p \to q) \to q = 0 \to 0 = 1$, $q \to p = 1$, and the formula takes the value $1 \to (1 \to \tfrac12) = \tfrac12$.

The pattern of the derivation is general: to derive $\varphi$, derive $(\varphi \to \psi) \to \varphi$ for some $\psi$, and then apply Peirce's law.
So Peirce's law lets us assume $\varphi \to \psi$ while we prove $\varphi$, which is a form of proof by contradiction without negation.
With $q$ and $p$ exchanged, the same steps give the converse implication, so the two forms of disjunction are equivalent in the system.

## Explanations

### L1 human

We want to show: if "$p$ or $q$" holds, then "$q$ or $p$" holds, written with "if ... then" only.
The trick is Peirce's law: to prove $p$, it is enough to prove $p$ under the extra assumption "$p$ implies $q$".
Under that assumption the given facts produce $q$ and then $p$.
So $p$ follows, and the law gives the result.

### L2 human

We check the formula of the example by its truth table, as the soundness theorem predicts.

1. If $p = 1$, the consequent $(q \to p) \to p$ is $1$, so the formula is $1$.
2. If $p = 0$ and $q = 1$, then $q \to p = 0$, so $(q \to p) \to p = 1$, and the formula is $1$.
3. If $p = 0$ and $q = 0$, then $p \to q = 1$ and $(p \to q) \to q = 0$, so the formula is $1$ because its antecedent is $0$.

The typical use of Peirce's law in derivations is exactly step 3 of the example: the last step that turns $(\varphi \to \psi) \to \varphi$ into $\varphi$.
A trap is to use the deduction theorem in a direction it does not give: from $\Gamma \vdash (p \to q) \to p$ we may not conclude $\Gamma \vdash p$ without Peirce's law.
