---
tag: E1TQVD7TVM
kind: proof
name: Proof of the number of injections
msc: [05A05]
proves: 0X0N833FF8
uses: [05099E1NMJ, 0PVG1CRAJN, 0N5M924N3P, 0D2MXBV21T, 0SNQEF7Z53, 03QC59M99B, 0EE2V3CHFK, 0GV2573FP4]
methods: [0ASJVEFA9J]
sources:
  - url: https://proofwiki.org/wiki/Cardinality_of_Set_of_Injections
---

## Proof

Fix $B$ with $|B| = n$. For a set $A$, let $I(A)$ be the set of [[injective|0PVG1CRAJN]] functions from $A$ to $B$. We argue by induction on $k = |A|$ that $I(A)$ is finite with $(n)_k$ elements.

1. Let $k = 0$. Then $A = \varnothing$, and the empty function is the only function from $A$ to $B$. It is injective. So $|I(A)| = 1 = (n)_0$.
2. Suppose the claim holds for all sets with $k$ elements. Let $|A| = k + 1$, with a [[bijection|0SNQEF7Z53]] $f : \set{1, \dots, k+1} \to A$.
3. Put $a = f(k+1)$ and $A' = A \setminus \set{a}$. The restriction of $f$ to $\set{1, \dots, k}$ is a bijection onto $A'$, so $|A'| = k$.
4. By the induction hypothesis, $I(A')$ has $N = (n)_k$ elements. Here $(n)_k$ is the [[falling factorial|0N5M924N3P]].
5. For $\varphi \in I(A)$, the [[restriction|0D2MXBV21T]] $\varphi|_{A'}$ is injective, so it lies in $I(A')$. For $\psi \in I(A')$, let $E_\psi$ be the set of $\varphi \in I(A)$ with $\varphi|_{A'} = \psi$.
6. Each $\varphi \in I(A)$ lies in exactly one set $E_\psi$, namely for $\psi = \varphi|_{A'}$. So the sets $E_\psi$ are pairwise disjoint, and their union is $I(A)$.
7. Fix $\psi \in I(A')$ and let $C = \psi(A')$. The map $\psi$ is a bijection from $A'$ onto $C$. Composing a numbering of $A'$ with $\psi$ numbers $C$, so $|C| = k$, as in the [[bijection principle|0GV2573FP4]].
8. By the [[complement principle|03QC59M99B]], $B \setminus C$ is finite with $n - k$ elements. In particular $k \le n$.
9. For $\varphi \in E_\psi$, we have $\varphi(a) \notin C$. Otherwise $\varphi(a) = \psi(x) = \varphi(x)$ for some $x \in A'$, against injectivity, since $x \ne a$.
10. Conversely, for $b \in B \setminus C$, extend $\psi$ by $a \mapsto b$. The result is injective, because $\psi$ is injective and $b$ is not a value of $\psi$.
11. So $\varphi \mapsto \varphi(a)$ is a bijection from $E_\psi$ to $B \setminus C$, with the extension of step 10 as inverse. Composing a numbering of $B \setminus C$ with this inverse shows $|E_\psi| = n - k$.
12. If $N = 0$, then $I(A')$ is empty, so by step 6 the set $I(A)$ is empty. Also $(n)_{k+1} = (n)_k (n - k) = 0$.
13. If $N \ge 1$, the [[rule of sum|0EE2V3CHFK]] applied to the $N$ sets $E_\psi$ gives $|I(A)| = N (n - k) = (n)_k (n - k)$.
14. By the definition of the falling factorial, $(n)_k (n - k) = (n)_{k+1}$. So $|I(A)| = (n)_{k+1}$, and the induction is complete.

## Idea

Build an injection one point at a time.
The new point may go to any element of $B$ that is not already used, and exactly $k$ are used.
So each step multiplies the count by the number of unused values, which gives the falling factorial.
