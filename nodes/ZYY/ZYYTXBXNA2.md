---
tag: ZYYTXBXNA2
kind: example
name: The converse Barcan formula and increasing domains
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [9PYDNBA5X4]
uses: [9PYDNBA5X4, D2H3S12V7X, G989VP2NGP]
sources:
  - url: https://en.wikipedia.org/wiki/Barcan_formula
    locator: Converse Barcan formula
---

## Example

The converse Barcan formula is $\square \forall x \varphi \to \forall x \square \varphi$, one of the two schemata on the page [[Barcan formula|9PYDNBA5X4]].
We derive it in $\mathsf{QK}$, and then we check on two models that its truth depends on whether domains increase.

The derivation uses instantiation, the [[necessitation rule|G989VP2NGP]], the axiom K and generalization.

1. $\vdash \forall x \varphi \to \varphi$, by instantiation of $x$ by itself.
2. $\vdash \square (\forall x \varphi \to \varphi)$, by necessitation.
3. $\vdash \square \forall x \varphi \to \square \varphi$, by K and modus ponens.
4. $\vdash \forall x \, (\square \forall x \varphi \to \square \varphi)$, by generalization.
5. $\vdash \square \forall x \varphi \to \forall x \square \varphi$, by the axiom $\forall x (A \to B) \to (A \to \forall x B)$, since $x$ is not free in $\square \forall x \varphi$.

The first model has increasing domains.
Let $W = \{w, v\}$, $R = \{(w, v)\}$, $D(w) = \{1\}$, $D(v) = \{1, 2\}$, and $I(P, w) = \emptyset$, $I(P, v) = \{1, 2\}$.

6. The only pair of $R$ is $(w, v)$, and $D(w) = \{1\} \subseteq \{1, 2\} = D(v)$. So the domains increase.
7. At $w$: $\square \forall x P x$ needs $\forall x P x$ at $v$, and $D(v) = \{1, 2\} \subseteq I(P, v)$. So the antecedent holds at $w$.
8. At $w$: $\forall x \square P x$ needs $\square P x$ under $x \mapsto 1$ only, since $D(w) = \{1\}$. At $v$, $1 \in I(P, v)$. So the consequent holds at $w$.
9. At $v$ there are no successors, so both $\square$-formulas hold, and the instance holds at $v$.

The second model has a shrinking domain.
Let $W = \{w, v\}$, $R = \{(w, v)\}$, $D(w) = \{1, 2\}$, $D(v) = \{1\}$, and $I(P, u) = D(u)$ for $u \in W$.

10. $w R v$ and $D(w) = \{1, 2\} \not\subseteq \{1\} = D(v)$. So the domains do not increase.
11. At $w$: $\square \forall x P x$ needs $\forall x P x$ at $v$, and $D(v) = \{1\} = I(P, v)$. So the antecedent holds at $w$.
12. At $w$: $\forall x \square P x$ needs $\square P x$ under $x \mapsto 2$, since $2 \in D(w)$. At $v$, $2 \notin I(P, v)$. So the consequent fails at $w$.
13. By steps 11 and 12, the instance $\square \forall x P x \to \forall x \square P x$ fails at $w$.

## Remarks

Steps 1 to 5 use no modal axiom beyond K, so every quantified normal modal logic with the classical quantifier rules proves the converse Barcan formula.
Step 13 shows that these rules are not sound for the second model, under the semantics with assignments into $U$.
The object $2$ exists at $w$ and is gone at $v$, and the antecedent says nothing about it at $v$.
This is the general pattern of the frame condition: the converse Barcan formula is valid on a frame with domains exactly when no object disappears along $R$.
If in the second model we add $2$ to $D(v)$, the domains increase, and with $I(P, u) = D(u)$ both sides hold at $w$.

## Explanations

### L1 human

The converse Barcan formula says: if in every possible future everything is $P$, then each thing that exists now is $P$ in every future.
This can fail when something that exists now does not exist in some future.
In the second model the object $2$ exists now, but not in the future $v$.
So "everything in $v$ is $P$" says nothing about $2$, and $2$ is not $P$ there.

### L2 human

We check step 12 again with the other object.

1. Under $x \mapsto 1$, $\square P x$ at $w$ needs $1 \in I(P, v)$.
2. $I(P, v) = D(v) = \{1\}$, so $1 \in I(P, v)$, and $\square P x$ holds under $x \mapsto 1$.
3. So the failure of $\forall x \square P x$ at $w$ comes only from the object $2$, the object that disappears.

The typical use of the derivation is to see that the classical quantifier rules force increasing domains.
A trap: the derivation of CBF uses K and necessitation only, while BF needs a further axiom; the two schemata are not symmetric in this way.
