---
tag: 4ZW3M0NSXN
kind: example
name: Modus ponens for the multiplicative implication of BI
msc: ["03B47"]
topics: [98QF5J4W16]
audience: research
instance_of: [5JKHNK7AR5]
uses: [F0R5WTBN8Y, J7F9HPATG5]
sources:
  - url: https://en.wikipedia.org/wiki/Bunched_logic
    locator: Foundations
---

## Example

In every resource model of [[the definition|F0R5WTBN8Y]], the formula $A \ast (A \mathrel{-\!\!*} B)$ entails $B$.

1. Let $r \models A \ast (A \mathrel{-\!\!*} B)$.
2. By the clause for $\ast$, there are $s$ and $t$ with $s \models A$, $t \models A \mathrel{-\!\!*} B$ and $s \bullet t \sqsubseteq r$.
3. By the clause for $\mathrel{-\!\!*}$ with the resource $s$, we get $t \bullet s \models B$.
4. $t \bullet s = s \bullet t$, since the monoid is commutative.
5. $s \bullet t \sqsubseteq r$, so $r \models B$ by persistence, remark 1 of the definition.

## Remarks

The converse fails: $B$ does not entail $A \ast (A \mathrel{-\!\!*} B)$.
In [[the model on the natural numbers|J7F9HPATG5]], let $V(p) = \{1\}$ and $V(q) = \{0\}$.
Then $0 \models q$, but $0 \models p \ast (p \mathrel{-\!\!*} q)$ would need $t + 1 = 0$ for some $t$, which is impossible.
The Wikipedia article states the law $A \ast B \vdash C$ if and only if $A \vdash B \mathrel{-\!\!*} C$.
This example is the semantic form of that law for $A \mathrel{-\!\!*} B \vdash A \mathrel{-\!\!*} B$, together with the commutativity of $\ast$.

## Explanations

### L1 human

If we have a resource for $A$, and separately a machine that turns any resource for $A$ into one for $B$, then together we have a resource for $B$.

### L2 human

We use the model of [[the example on the natural numbers|J7F9HPATG5]] with $V(p) = \{1\}$ and $V(q) = \{2\}$, and we look at $p \wedge (p \mathrel{-\!\!*} q)$.

1. $1 \models p$.
2. $1 \models p \mathrel{-\!\!*} q$, since $1 + 1 = 2$ and $2 \models q$.
3. So $1 \models p \wedge (p \mathrel{-\!\!*} q)$.
4. But $1 \not\models q$, since $V(q) = \{2\}$.

The typical use of the law with $\ast$ is to apply a stored implication to a separate resource.
A trap: with $\wedge$ in place of $\ast$, the law fails, as the steps above show, since the same resource is used twice.
