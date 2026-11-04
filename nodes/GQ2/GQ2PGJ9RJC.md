---
tag: GQ2PGJ9RJC
kind: proof
name: Proof that the size of a conjugacy class is the index of the centraliser
msc: ["20E45"]
proves: 0VK5V9P8G3
uses: [0P8CY9V437, 0Q88KQD17A, 0Q0Z1BEXTF, 00F2JFA41J, 0RGGF8ZS6D, 0E2HSCKZ6C, 0S19CWFZM2]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Conjugacy class equation
---

## Proof

We apply the orbit-stabiliser theorem to the [[action by conjugation|0P8CY9V437]], $g \cdot x = g x g^{-1}$.

1. The [[orbit|00F2JFA41J]] of $a$ under conjugation is $\set{g a g^{-1} : g \in G}$. By the [[definition of a conjugacy class|0Q88KQD17A]], this is $\operatorname{Cl}(a)$.
2. The [[stabiliser|0RGGF8ZS6D]] of $a$ is $\set{g \in G : g a g^{-1} = a}$. Multiplying on the right by $g$, or by $g^{-1}$, shows $g a g^{-1} = a$ if and only if $g a = a g$.
3. So the stabiliser of $a$ is $\set{g \in G : ga = ag}$, which is the [[centraliser|0Q0Z1BEXTF]] $C_G(a)$.
4. By the [[orbit-stabiliser theorem|0E2HSCKZ6C]] and steps 1 and 3, $\abs{\operatorname{Cl}(a)} = [G : C_G(a)]$.
5. If $G$ is finite, the [[orbit size formula|0S19CWFZM2]] shows that the size of each orbit divides $\abs{G}$. By step 1, $\abs{\operatorname{Cl}(a)}$ divides $\abs{G}$.

## Idea

Conjugation is an action, its orbits are the conjugacy classes, and the elements that fix $a$ are those that commute with $a$. The orbit-stabiliser theorem then turns the class size into the index of the centraliser.
