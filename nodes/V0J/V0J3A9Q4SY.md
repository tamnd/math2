---
tag: V0J3A9Q4SY
kind: example
name: The smallest filtration of a transitive model need not be transitive
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [6ZZSHAKG5F]
uses: [6ZZSHAKG5F, T99DK51S0W, NGHWZ9Y7ZV, 0GJZW9JFZQ]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Take the [[Kripke model|NGHWZ9Y7ZV]] with
$$W = \set{a, b, b', c}, \quad R = \set{(a, b), (b', c)}, \quad V(p) = \set{b, b'}, \quad V(q) = \set{c},$$
and $\Sigma = \set{p, q, \square q}$.
We compare the smallest [[filtration|6ZZSHAKG5F]] with the transitive filtration.

1. $R$ is [[transitive|0GJZW9JFZQ]], since $b$ and $c$ have no successors, so no chain $x R y R z$ exists.
2. $\square q$ is false at $a$, since the successor $b$ lacks $q$.
3. $\square q$ is true at $b$ and at $c$, which have no successors, and at $b'$, since the successor $c$ has $q$.
4. The values of $(p, q, \square q)$ are $(0, 0, 0)$ at $a$, $(1, 0, 1)$ at $b$ and $b'$, and $(0, 1, 1)$ at $c$.
5. So the classes are $A = \set{a}$, $B = \set{b, b'}$ and $C = \set{c}$.
6. The smallest filtration takes the images of the arrows: $R^s = \set{(A, B), (B, C)}$.
7. $R^s$ is not transitive: $A R^s B$ and $B R^s C$ hold, and $A R^s C$ fails.
8. The transitive filtration has $[w] R^t [v]$ when, for every $\square\varphi \in \Sigma$, $w \models \square\varphi$ implies $v \models \square\varphi$ and $v \models \varphi$.
9. $A$ makes $\square q$ false, so $A$ sees every class: $A R^t A$, $A R^t B$, $A R^t C$.
10. $B$ makes $\square q$ true, so $B R^t [v]$ needs $q$ and $\square q$ at $v$. Only $C$ qualifies, so $B R^t C$.
11. $C$ makes $\square q$ true, so in the same way $C R^t C$ is the only arrow from $C$.
12. So $R^t = \set{(A, A), (A, B), (A, C), (B, C), (C, C)}$.
13. $R^t$ is transitive: the chains are $A, A, x$ and $A, B, C$ and $A, C, C$ and $B, C, C$ and $C, C, C$, and each end pair is in $R^t$.
14. $R^t$ contains $R^s$, and step 8 gives the condition of a filtration, so $R^t$ is a filtration.
15. Filtration lemma for $\square q$: at $A$, the successor $A$ lacks $q$, so $\square q$ is false. At $B$ and $C$, the only successor $C$ has $q$, so $\square q$ is true. This matches steps 2 and 3.

## Remarks

The example shows why logics of transitive frames, such as $\mathsf{K4}$ and $\mathsf{S4}$, need the transitive filtration.
The smallest filtration merges $b$ and $b'$, and the merge creates the path $A, B, C$ without a shortcut.
The transitive filtration is transitive for every transitive model, and it satisfies the [[filtration theorem|T99DK51S0W]].
Its proof of the condition $w R v \Rightarrow [w] R^t [v]$ uses the transitivity of $R$: from $\square\varphi$ at $w$ we get $\square\varphi$ at $v$.
If we give $b$ the successor $c$ as well, then $a R c$ is needed for transitivity, and the smallest filtration contains $(A, C)$.

## Explanations

### L1 human

Two people, $b$ and $b'$, look the same to us, so we merge them into one person $B$.
Person $a$ points to $b$, and $b'$ points to $c$.
After the merge, $A$ points to $B$, and $B$ points to $C$.
But nobody pointed from $a$ to $c$, so the merged picture has a two-step path without a direct step.
The fix is to add the missing arrows in a careful way.

### L2 human

1. Take the formula $\square q \to \square\square q$, an instance of axiom $\mathrm{4}$, at $A$.
2. In the model with $R^s$, $\square q$ is false at $A$, so the instance holds at $A$.
3. At $B$, $\square q$ is true, and $\square\square q$ needs $\square q$ at $C$, which is true. So the instance holds at $B$.
4. On the frame $(\set{A, B, C}, R^s)$ with $q$ true only at $B$, $\square q$ is true at $A$ and false at $B$. So $\mathrm{4}$ fails at $A$, and this frame is not a frame of $\mathsf{K4}$.

The typical use of the transitive filtration is the proof of the finite model property of $\mathsf{K4}$ and $\mathsf{S4}$.
A trap: the smallest filtration of a model of a logic need not be a frame of the logic.
So the finite model property needs the right filtration.
