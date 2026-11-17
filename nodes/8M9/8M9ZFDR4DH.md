---
tag: 8M9ZFDR4DH
kind: statement
role: theorem
name: Deduction theorem for predicate logic
aliases: [the-deduction-theorem-in-predicate-logic]
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
about: [N95HV0VWSM]
uses: [2B00FE6K5W, 9X08XK5RV2, 0ZNX6DQ3EJ]
sources:
  - wikipedia: en:480010@r1320842012
    locator: Deduction theorem, section The deduction theorem in predicate logic
    note: adopted
    mention: wikipedia://en/480010#Y3DL
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/Deduction_theorem
    locator: The deduction theorem in predicate logic
  - book: isbn:9781482237726
    locator: Chapter 2
  - book: isbn:9780122384523
    locator: Section 2.4
inventory: [TGSPJ68GEB]
---

## Statement

Let $\Gamma$ be a set of formulas of a first-order language, and let $\varphi$ and $\psi$ be formulas.
We use the two forms $\mathsf{H}$ and $\mathsf{H}_G$ of the [[Hilbert-style predicate calculus|2B00FE6K5W]].
In $\mathsf{H}_G$ generalization is a rule; in $\mathsf{H}$ the axioms are closed under generalization and modus ponens is the only rule.

1. In both systems, if $\Gamma \vdash \varphi \to \psi$, then $\Gamma \cup \{\varphi\} \vdash \psi$.
2. In $\mathsf{H}$, if $\Gamma \cup \{\varphi\} \vdash_{\mathsf{H}} \psi$, then $\Gamma \vdash_{\mathsf{H}} \varphi \to \psi$.
3. In $\mathsf{H}_G$, suppose that $\psi$ has a derivation from $\Gamma \cup \{\varphi\}$ in which the rule of generalization is never applied with a variable that is free in $\varphi$. Then $\Gamma \vdash_{\mathsf{H}_G} \varphi \to \psi$.

In particular, if $\varphi$ is a sentence, then in both systems $\Gamma \cup \{\varphi\} \vdash \psi$ holds if and only if $\Gamma \vdash \varphi \to \psi$.
The [[proof|GTRGQ7XZP7]] is an induction on derivations, as for the [[propositional deduction theorem|9X08XK5RV2]].

## Remarks

### Why each hypothesis is needed

The condition on generalization in part 3 cannot be dropped.
In $\mathsf{H}_G$ the rule of generalization gives $\{P(x)\} \vdash \forall x\, P(x)$, but $P(x) \to \forall x\, P(x)$ is not a theorem.
The [[counterexample|D3SW6V4R1B]] checks this with a structure of two elements.
Part 2 has no condition because $\mathsf{H}$ does not derive $\forall x\, P(x)$ from $P(x)$: the condition moves into the [[generalization theorem|VKSK35Y52Z]].

### Consequences

- If $\varphi_1, \dots, \varphi_n$ are sentences, then $\Gamma \cup \{\varphi_1, \dots, \varphi_n\} \vdash \psi$ if and only if $\Gamma \vdash \varphi_1 \to (\varphi_2 \to \cdots (\varphi_n \to \psi) \cdots)$. Apply the theorem $n$ times.
- A theory proves $\varphi \to \psi$ exactly when $\psi$ follows from the theory with the extra axiom $\varphi$, for each sentence $\varphi$. Mathematicians use this when they prove "if $\varphi$ then $\psi$" by assuming $\varphi$, as in a [[direct proof|0NTF6DMVAP]].
- For a sentence $\varphi$: if $\Gamma \cup \{\varphi\}$ derives a formula and its negation, then $\Gamma \vdash \neg \varphi$. The theorem gives $\Gamma \vdash \varphi \to \chi$ and $\Gamma \vdash \varphi \to \neg \chi$, and the tautology $(\varphi \to \chi) \to ((\varphi \to \neg \chi) \to \neg \varphi)$ finishes. This is [[proof by contradiction|0J0XBKG64S]] inside the calculus.
- The theorem reduces derivability from a finite set of sentences to derivability from the empty set: $\{\varphi_1, \dots, \varphi_n\} \vdash \psi$ if and only if $\vdash \varphi_1 \wedge \cdots \wedge \varphi_n \to \psi$.

### Converse

Part 1 is the converse of parts 2 and 3, and it holds with no condition.
A derivation of $\varphi \to \psi$ from $\Gamma$, followed by the line $\varphi$ and one step of [[modus ponens|0Y0MQYST0M]], is a derivation of $\psi$ from $\Gamma \cup \{\varphi\}$.

### Generalizations

- Mendelson states part 3 with a weaker condition: generalization may use a free variable of $\varphi$ when it is applied to a formula whose derivation does not use $\varphi$.
- In [[natural deduction|6KT3BJZ7D1]] the theorem is a rule, $\to$-introduction, and in the [[sequent calculus|W72CA3R9MP]] it is the rule $\to$R.
- In modal logic with the rule of necessitation (from $\varphi$, infer $\Box \varphi$), the same failure appears: $\{p\} \vdash \Box p$, but $p \to \Box p$ is not a theorem of the logic K.

## History

Herbrand proved a deduction theorem in his thesis of 1930.
The restricted form for systems with a rule of generalization is the one in Mendelson's textbook.

## Explanations

### L1 human

To prove "if it rains, then the street is wet", we assume that it rains and then show that the street is wet.
The deduction theorem says that the formal calculus allows this way of proving an "if ... then" statement.
In predicate logic there is one catch, about letters such as $x$ that stand for an unknown object.
If we assume "$x$ is even" and then use the assumption as if $x$ were every number, we get "every number is even".
The statement "if $x$ is even, then every number is even" is false for $x = 2$, so this use must be forbidden.

### L2 human

We derive $\forall x\, P(x) \to \forall x\, Q(x)$ from $\Gamma = \{\forall x\, (P(x) \to Q(x))\}$ in $\mathsf{H}_G$.

1. The [[derivation with the rule of generalization|C8ANFQQ843]] derives $\forall x\, Q(x)$ from $\Gamma \cup \{\forall x\, P(x)\}$.
2. Its only use of generalization is on $x$, in its last line.
3. The variable $x$ is not free in $\varphi = \forall x\, P(x)$, so the condition of part 3 holds.
4. Part 3 gives $\Gamma \vdash_{\mathsf{H}_G} \forall x\, P(x) \to \forall x\, Q(x)$.

The typical use is to find a derivation of $\varphi \to \psi$: assume $\varphi$, derive $\psi$, and discharge $\varphi$ with the theorem.
A trap is to discharge an assumption with a free variable after generalizing on that variable, as in $P(x)$, $\forall x\, P(x)$.

### L3 human

The theorem says that implication internalizes the consequence relation: $\varphi \to \psi$ is derivable exactly when $\psi$ is derivable from $\varphi$.
In a category of proofs this is the adjunction between the product with $\varphi$ and the exponential, the same law that gives currying in the lambda calculus and the [[Curry-Howard correspondence|A77FER1Q5H]].
The failure in $\mathsf{H}_G$ comes from a mismatch of two consequence relations: a free variable in a hypothesis is read universally, while in $\varphi \to \psi$ it is read for one fixed value.
Systems such as $\mathsf{H}$, [[natural deduction|6KT3BJZ7D1]] and the sequent calculus avoid the mismatch, and they put the condition on generalization into the generalization theorem or into an eigenvariable condition.
