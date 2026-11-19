---
tag: 5F6H9XXMVN
kind: example
name: The strict conditional is not a variably strict conditional
msc: ["03B45"]
topics: [CQM9SRN8PM]
audience: research
not_instance_of:
  - target: ZGYG7WN7EC
    note: the strict conditional obeys strengthening of the antecedent, which fails for counterfactuals
uses: [ZGYG7WN7EC, 5JW54NP52K, PTQNQF2K3T]
sources:
  - url: https://en.wikipedia.org/wiki/Counterfactual_conditional
    locator: Strict conditional
---

## Example

The [[strict conditional|5JW54NP52K]] is $\varphi \prec \psi := \square(\varphi \to \psi)$, interpreted in a Kripke model $(W, R, V)$.
We show that it obeys strengthening of the antecedent, transitivity and contraposition.
So it cannot be the conditional of [[conditional logic|ZGYG7WN7EC]], where all three fail.

1. Strengthening. Let $w \models \square(\varphi \to \psi)$ and let $w R v$ with $v \models \varphi \wedge \chi$.
2. Then $v \models \varphi$ and $v \models \varphi \to \psi$, so $v \models \psi$. Hence $w \models \square((\varphi \wedge \chi) \to \psi)$.
3. Transitivity. Let $w \models \square(\varphi \to \psi)$ and $w \models \square(\psi \to \chi)$, and let $w R v$ with $v \models \varphi$.
4. Then $v \models \psi$ by the first premise, and $v \models \chi$ by the second. Hence $w \models \square(\varphi \to \chi)$.
5. Contraposition. At each $v$ with $w R v$, the formulas $\varphi \to \psi$ and $\neg\psi \to \neg\varphi$ have the same truth value.
6. So $\square(\varphi \to \psi)$ and $\square(\neg\psi \to \neg\varphi)$ have the same truth value at $w$.

In [[the three-world sphere model|PTQNQF2K3T]], $p > q$ holds and $(p \wedge r) > q$ fails.
By step 2, no strict conditional can take these two values.

## Remarks

The strict conditional checks $\varphi \to \psi$ on one fixed set of worlds, $R[w]$, for every antecedent.
A counterfactual checks it on a set that depends on $\varphi$: the closest $\varphi$-worlds.
This is why Lewis calls counterfactuals variably strict.
A sphere model with a single sphere $\$_w = \set{R[w]}$ gives back the strict conditional for antecedents that are possible at $w$.
Some authors keep a strict analysis and let the context change $R$ from one sentence to the next, which gives a dynamic strict conditional.

## Explanations

### L1 human

A strict "if" says: in every situation we consider, if the match is struck, it lights.
Then it also says: in every situation we consider, if the match is struck and wet, it lights.
The set of situations is the same in both sentences.
A counterfactual "if" looks at different situations for different "if" parts, so the second sentence can fail.

### L2 human

1. Take one Kripke world $w$ with $R[w] = \set{u, v}$, and $p, q, r$ as in the three-world model: $p, q$ true at $u$; $p, r$ true at $v$.
2. $\square(p \to q)$ fails at $w$, since $v$ has $p$ and not $q$.
3. So the strict conditional cannot make "if $p$ then $q$" true here, while the sphere model can.

The typical use of this comparison is to explain why counterfactuals need a semantics with an ordering of worlds.
A trap: the strict conditional is still non-material, since a false antecedent at $w$ does not make it true.
