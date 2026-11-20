---
tag: J7F9HPATG5
kind: example
name: A resource model on the natural numbers
msc: ["03B47"]
topics: [98QF5J4W16]
audience: research
instance_of: [5JKHNK7AR5]
uses: [F0R5WTBN8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Bunched_logic
    locator: Foundations, Truth-functional semantics
---

## Example

Take $M = \mathbb{N}$ with $\bullet = +$, $e = 0$, and equality as the order $\sqsubseteq$.
This is a resource model in the sense of [[the definition|F0R5WTBN8Y]], with $V(p) = V(q) = \{1\}$ and $V(u) = \{3\}$.

1. $(\mathbb{N}, +, 0)$ is a commutative monoid, and equality is a preorder.
2. If $r = r'$, then $r + s = r' + s$, so property 2 of the definition holds.
3. Every subset of $\mathbb{N}$ is an upper set for equality, so $V$ is allowed.
4. $r \models p \ast q$ if and only if $s + t = r$ for some $s \in V(p)$ and $t \in V(q)$, that is, $r = 2$.
5. $2 \models p \ast q$ but $2 \not\models p$, so $p \ast q$ does not entail $p$: the comma has no weakening.
6. $1 \models p$ but $1 \not\models p \ast p$, by step 4 with $q$ replaced by $p$: the comma has no contraction.
7. $1 \models p \wedge q$ but $1 \not\models p \ast q$, and $2 \models p \ast q$ but $2 \not\models p \wedge q$.
8. $r \models I$ if and only if $r = 0$, since $e = 0$ and the order is equality.
9. $r \models p \mathrel{-\!\!*} u$ if and only if $r + 1 = 3$, since $1$ is the only resource that forces $p$; that is, $r = 2$.

## Remarks

The model shows that $\ast$ and $\wedge$ are different connectives, although both are conjunctions.
Step 9 shows the resource reading of $\mathrel{-\!\!*}$: the resource $2$ needs one more unit for $p$ to reach $u$.

## Explanations

### L1 human

Here a resource is a number of coins.
Two coins can be split into one coin and one coin, but one coin cannot be split into two coins.

### L2 human

We check $p \ast (p \mathrel{-\!\!*} u)$ at the resource $3$.

1. $1 \models p$, since $V(p) = \{1\}$.
2. $2 \models p \mathrel{-\!\!*} u$, by step 9 of the example.
3. $1 + 2 = 3$, so $3 \models p \ast (p \mathrel{-\!\!*} u)$ by the clause for $\ast$.
4. $3 \models u$, since $V(u) = \{3\}$.

The typical use of this model is to separate formulas that differ only in the choice of $\ast$ or $\wedge$.
A trap: with the usual order $\leq$ in place of equality, $V(p) = \{1\}$ is not an upper set, so the model would not be allowed.
