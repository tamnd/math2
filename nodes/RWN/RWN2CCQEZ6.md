---
tag: RWN2CCQEZ6
kind: proof
name: Proof of the class equation
msc: ["20E45"]
proves: 08BPSC6YTE
uses: [0P8CY9V437, 0Q88KQD17A, 0ZC7FYE0NZ, 0S7Y9Q990Q, 0VK5V9P8G3]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Conjugacy class equation
---

## Proof

We split $G$ into conjugacy classes and sort the classes by size.

1. The [[conjugacy classes|0Q88KQD17A]] are the orbits of the [[action by conjugation|0P8CY9V437]]. Since [[orbits partition|0ZC7FYE0NZ]] the set, the classes are pairwise disjoint and cover $G$.
2. Let $a \in G$. Then $a = e a e^{-1} \in \operatorname{Cl}(a)$. So $\operatorname{Cl}(a) = \set{a}$ if and only if $g a g^{-1} = a$ for all $g \in G$.
3. As $g a g^{-1} = a$ is equivalent to $g a = a g$, step 2 says $\operatorname{Cl}(a) = \set{a}$ if and only if $a$ lies in the [[centre|0S7Y9Q990Q]] $Z(G)$.
4. By step 3, the classes with one element are the sets $\set{z}$ with $z \in Z(G)$. Together they contain exactly $\abs{Z(G)}$ elements.
5. The classes with more than one element are $\operatorname{Cl}(a_1), \dots, \operatorname{Cl}(a_k)$, by the choice of $a_1, \dots, a_k$. Since $G$ is finite, step 1 gives $\abs{G} = \abs{Z(G)} + \sum_{i=1}^{k} \abs{\operatorname{Cl}(a_i)}$.
6. By the [[class size formula|0VK5V9P8G3]], $\abs{\operatorname{Cl}(a_i)} = [G : C_G(a_i)]$. So $\abs{G} = \abs{Z(G)} + \sum_{i=1}^{k} [G : C_G(a_i)]$.

## Idea

The conjugacy classes cut the group into disjoint pieces. The pieces with one element are exactly the central elements, and each other piece has the size of the index of a centraliser. Adding up the sizes gives the equation.
