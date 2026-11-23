---
tag: RVTJNF5HMF
kind: example
name: Löb's formula is not first-order definable
msc: ["03B45", "03C95"]
topics: [SPQVNPZDTB]
audience: grad
not_instance_of:
  - target: 3RYBWYPJVD
    note: Löb's formula defines a class of frames that no first-order sentence defines, so it has no first-order correspondent
uses: [3RYBWYPJVD, QQ6PZFGGB3, 1NR3HAWG9D, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Example

On the natural numbers with $<$, make $p$ false everywhere.
Every number has a larger number, so $\square p$ is false everywhere, and $\square p \to p$ is true everywhere.
So $\square(\square p \to p)$ is true at $0$, while $\square p$ is false at $0$.
Löb's formula $\square(\square p \to p) \to \square p$ fails, and the culprit is the endless ascending chain.

Let $\mathrm{L}$ be Löb's formula.
We show that no first-order sentence $\alpha$ in the language with one binary symbol $R$ satisfies $\mathfrak{F} \models \mathrm{L} \iff \mathfrak{F} \models \alpha$ for every frame $\mathfrak{F}$.
So $\mathrm{L}$ has no first-order [[correspondent|3RYBWYPJVD]].

1. Claim A: every finite strict linear order $(\{0, \ldots, k\}, <)$ validates $\mathrm{L}$.
   It is transitive and, being finite, has no infinite ascending chain, so part 3 of [[Löb's axiom in provability logic|QQ6PZFGGB3]] applies.
2. Claim B: if a frame has an infinite chain $c_0 R c_1 R c_2 R \cdots$, it does not validate $\mathrm{L}$.
   The worlds $c_i$ need not be distinct.
   Put $V(p) = W \setminus \{c_i : i \in \mathbb{N}\}$.
3. Each $c_i$ sees $c_{i+1}$, where $p$ is false, so $\square p$ is false at every $c_i$.
   In particular $c_0 \not\models \square p$.
4. Let $c_0 R u$.
   If $u$ is no $c_i$, then $u \models p$, so $u \models \square p \to p$.
   If $u = c_j$, then $u \not\models \square p$ by step 3, so again $u \models \square p \to p$.
5. So $c_0 \models \square(\square p \to p)$ and $c_0 \not\models \square p$, and $\mathrm{L}$ fails at $c_0$.
   This proves Claim B.

### The compactness argument

6. Now assume that $\alpha$ corresponds to $\mathrm{L}$.
   Add constants $c_0, c_1, \ldots$, and let $\Gamma = \{\alpha\} \cup \{R(c_i, c_{i+1}) : i \in \mathbb{N}\}$.
7. A finite subset of $\Gamma$ mentions only $c_0, \ldots, c_k$ for some $k$.
   The structure $(\{0, \ldots, k\}, <)$ with $c_i$ read as $i$ satisfies it, since it satisfies $\alpha$ by Claim A.
8. By the [[compactness theorem|1NR3HAWG9D]], $\Gamma$ has a model $\mathfrak{F}$.
   Then $\mathfrak{F} \models \alpha$, so $\mathfrak{F} \models \mathrm{L}$.
9. But $\mathfrak{F}$ contains the chain $c_0 R c_1 R \cdots$, so $\mathfrak{F} \not\models \mathrm{L}$ by Claim B.
   This is a contradiction.

## Remarks

The example shows that frame validity of a modal formula can be a second-order condition.
The obstacle is converse well-foundedness, which first-order logic cannot express, by compactness.
The same argument works for every modal formula that holds on all finite strict linear orders and fails on every frame with an infinite chain.

Restricting to transitive frames does not help.
The frames in step 7 are transitive, so the class of transitive frames that validate $\mathrm{L}$ is not first-order either.

Failure of first-order definability does not prevent completeness.
The formula $\mathrm{L}$ axiomatizes the provability logic $\mathsf{GL}$ over $\mathsf{K}$, and $\mathsf{GL}$ is complete for finite transitive irreflexive frames.

## Explanations

### L1 human

Löb's formula holds in a picture of points and arrows exactly when the arrows compose and there is no endless walk along them.
"There is no endless walk" cannot be written with "for all points" and "there is a point".
The reason is that any such sentence true in all short finite chains is also true in some picture with an endless chain.

### L2 human

Here is Claim B on a frame that compactness might produce.
Take a single reflexive point $c$, so the chain is $c R c R c \cdots$ with all $c_i = c$.
The valuation of step 2 makes $p$ false at $c$.
Then $c \not\models \square p$, so $c \models \square p \to p$, and $c \models \square(\square p \to p)$.
But $c \not\models \square p$, so $\mathrm{L}$ fails at $c$.
The typical use of this compactness argument is to prove that a modal formula has no first-order correspondent.
Watch out: compactness gives some frame with an infinite chain, not the frame $(\mathbb{N}, <)$, so Claim B must hold for every frame with an infinite chain.
