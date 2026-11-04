---
tag: AXAH8H9YHP
kind: proof
name: Proof of the number of subsets of a finite set by indicator functions
msc: [05A05]
proves: 0C5RDJE73X
uses: [0BC7KX51Z8, 0VSB0XF4G7, 08QQH9F7G0, 0GV2573FP4, 01VG2A0BHW]
sources:
  - url: https://proofwiki.org/wiki/Cardinality_of_Power_Set_of_Finite_Set
---

## Proof

We build a bijection from the [[power set|0BC7KX51Z8]] to a set of functions.

1. Let $F = \set{0, 1}^X$ be the set of all functions from $X$ to $\set{0, 1}$.
2. Define $\Phi : \mathcal{P}(X) \to F$ by $\Phi(S) = 1_S$, the [[indicator function|0VSB0XF4G7]] of $S$. So $1_S(x) = 1$ for $x \in S$ and $1_S(x) = 0$ for $x \in X \setminus S$.
3. Define $\Psi : F \to \mathcal{P}(X)$ by $\Psi(\varphi) = \set{x \in X : \varphi(x) = 1}$.
4. For $S \subseteq X$, the set $\Psi(\Phi(S))$ is the set of $x$ with $1_S(x) = 1$. This is $S$.
5. For $\varphi \in F$, let $T = \Psi(\varphi)$. Then $1_T(x) = 1 = \varphi(x)$ for $x \in T$.
6. For $x \notin T$ we have $\varphi(x) \ne 1$. Since $\varphi$ takes values in $\set{0, 1}$, this gives $\varphi(x) = 0 = 1_T(x)$. So $\Phi(\Psi(\varphi)) = \varphi$.
7. Thus $\Phi$ has a two-sided inverse, so it is a bijection by the [[inverse criterion|01VG2A0BHW]].
8. By the [[number of functions between finite sets|08QQH9F7G0]], $F$ is finite and $|F| = 2^n$.
9. A numbering of $F$ composed with $\Psi$ numbers $\mathcal{P}(X)$. So $\mathcal{P}(X)$ is finite, and the [[bijection principle|0GV2573FP4]] gives $|\mathcal{P}(X)| = |F| = 2^n$.

## Idea

A subset is determined by answering "in or out?" for each element.
The answers form a function from $X$ to $\set{0, 1}$, and every such function arises from exactly one subset.
So subsets are counted by functions, and there are $2^n$ of those.
