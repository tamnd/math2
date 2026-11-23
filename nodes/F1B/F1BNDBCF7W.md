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

A chain of two points, each seeing itself, validates the axiom of [[Grzegorczyk logic|2Q8E4GQF3B]].
Let $W = \{a, b\}$ with $R = \{(a, a), (a, b), (b, b)\}$, the [[partial order|0QV2JS9RJ3]] $a \leq b$.
We show that the axiom below is valid on this frame:

$$\square(\square(p \to \square p) \to p) \to p.$$

At a world where $p$ is true, the axiom holds because its conclusion is true.
So let $w \not\models p$.
It suffices to find some $v$ with $w R v$, $v \models \square(p \to \square p)$ and $v \not\models p$.
Then $v \not\models \square(p \to \square p) \to p$, so $w \not\models \square(\square(p \to \square p) \to p)$, and the axiom holds at $w$.

1. Case $w = b$ and $b \not\models p$.
   The only successor of $b$ is $b$, and $p \to \square p$ is true at $b$ because $p$ is false there.
   So $v = b$ works.
2. Case $w = a$, with $a \not\models p$ and $b \not\models p$.
   Since $a R b$, step 1 gives $v = b$.
3. Case $w = a$, with $a \not\models p$ and $b \models p$.
   At $b$, $\square p$ is true, so $p \to \square p$ is true.
   At $a$, $p$ is false, so $p \to \square p$ is true.
   So $a \models \square(p \to \square p)$, and $v = a$ works, because $a R a$.
4. Cases 1 to 3 cover every valuation and every world where $p$ is false.

## Remarks

The same argument works for every finite partial order $(W, \leq)$.
Let $w \not\models p$, and choose $v \geq w$ with $v \not\models p$ that is maximal among such worlds.
Take any $u \geq v$ with $u \neq v$, so $u \models p$ by maximality.
Every $t \geq u$ has $t \geq v$ by [[transitivity|0GJZW9JFZQ]], and $t \neq v$ by antisymmetry, so $t \models p$.
Hence $u \models \square p$, so $p \to \square p$ holds at every $u \geq v$, and also at $v$, where $p$ is false.
So $v$ is the world we need.

Finiteness is used only to choose a maximal $v$.
On $(\mathbb{N}, \leq)$ no such choice exists, and the axiom fails, as the remarks on [[Grzegorczyk logic|2Q8E4GQF3B]] show.
Reflexivity is used in case 3, where the world we need is $a$ itself.
On the irreflexive chain where $a R b$ is the only arrow, take $p$ false at $a$ and true at $b$.
The only successor $b$ of $a$ satisfies $p$, so $a \models \square(\square(p \to \square p) \to p)$, and the axiom fails at $a$.

## Explanations

### L1 human

Two points, one below the other, with each point seeing itself, form a picture for Grzegorczyk logic.
We check the axiom by looking for the highest point where $p$ is false.
Above that point $p$ is true and stays true, which is what the axiom needs.

### L2 human

The example is a pattern for checking $\mathrm{Grz}$ on any finite order.
Go to a highest world $v$ where $p$ fails.
Every world strictly above $v$ makes $p$ true, and so do all the worlds above it, so $p \to \square p$ holds everywhere above $v$.
At $v$ itself, $p \to \square p$ holds because $p$ is false.
So $v$ makes the hypothesis $\square(p \to \square p) \to p$ false, and the axiom survives.
Watch out for reflexivity: in case 3 the witness is the starting world $a$.

### L3 human

The search for a highest world where $p$ fails is the reflexive form of the argument for Löb's axiom on finite strict orders.
There one looks for a last world where $p$ fails, and well-foundedness of the converse relation makes the search end.
The frame condition for $\mathrm{Grz}$ is a partial order with no infinite strictly ascending chain, and the chain $a \leq b$ is its smallest case with two worlds.
