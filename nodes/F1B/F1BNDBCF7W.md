---
tag: F1BNDBCF7W
kind: example
name: The two-element chain is a frame of Grz
msc: ["03B45"]
topics: [3E7M66WW6Q]
audience: research
instance_of: [2Q8E4GQF3B]
uses: [2Q8E4GQF3B, NGHWZ9Y7ZV, 0QV2JS9RJ3, 0GJZW9JFZQ]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Let $W = \set{a, b}$ with $R = \set{(a, a), (a, b), (b, b)}$, the [[partial order|0QV2JS9RJ3]] $a \leq b$.
We show that the axiom $\square(\square(p \to \square p) \to p) \to p$ of [[Grzegorczyk logic|2Q8E4GQF3B]] is valid on this frame.
It suffices to show: if $w \not\models p$, then some $v$ with $w R v$ has $v \models \square(p \to \square p)$ and $v \not\models p$, since then $w \not\models \square(\square(p \to \square p) \to p)$.

1. Case $w = b$ and $b \not\models p$. The only successor of $b$ is $b$, and $p \to \square p$ is true at $b$ since $p$ is false there. So $v = b$ works.
2. Case $w = a$, $a \not\models p$ and $b \not\models p$. Since $a R b$, step 1 gives $v = b$.
3. Case $w = a$, $a \not\models p$ and $b \models p$. At $b$, $\square p$ is true, so $p \to \square p$ is true. At $a$, $p$ is false, so $p \to \square p$ is true. So $a \models \square(p \to \square p)$, and $v = a$ works, since $a R a$.
4. Cases 1 to 3 cover every valuation and every world where $p$ is false. Where $p$ is true, the axiom holds, since its conclusion is true.

## Remarks

The argument works for every finite partial order $(W, \leq)$.
Let $w \not\models p$, and choose $v \geq w$ with $v \not\models p$ that is maximal among such worlds.
Let $u \geq v$ with $u \neq v$.
Then $u \models p$ by maximality.
Every $t \geq u$ has $t \geq v$ by [[transitivity|0GJZW9JFZQ]], and $t \neq v$ by antisymmetry, so $t \models p$; hence $u \models \square p$.
So $p \to \square p$ holds at every $u \geq v$, also at $v$ where $p$ is false, and $v$ is the world required above.
Finiteness is used to choose $v$; on $(\N, \leq)$ the axiom fails, as shown in the non-examples of [[Grzegorczyk logic|2Q8E4GQF3B]].

## Explanations

### L1 human

Two points, one below the other, each seeing itself, form a picture for Grzegorczyk logic.
We check the axiom by looking for the highest point where $p$ is false.
Above that point $p$ is true and stays true, which is what the axiom needs.

### L2 human

The typical use of this example is as a pattern: to check $\mathrm{Grz}$ on a finite order, go to a highest world where $p$ fails.
A trap: in case 3 the required world is $a$ itself, which uses reflexivity.
On the irreflexive chain $a R b$ with $p$ false at $a$ and true at $b$, the only successor $b$ of $a$ satisfies $p$, so $a \models \square(\square(p \to \square p) \to p)$ and the axiom fails at $a$.
