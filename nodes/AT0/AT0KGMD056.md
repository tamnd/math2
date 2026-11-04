---
tag: AT0KGMD056
kind: proof
name: Proof of the Schröder–Bernstein theorem
msc: ["03E10"]
proves: 0A9V6RKQG6
uses: [0PVG1CRAJN, 0SNQEF7Z53, 0XKH881BZ7, 0Q3F20XB0A, 0DSHAVH45F, 05GK32H72H]
sources:
  - url: https://arxiv.org/abs/1409.1755
---

## Proof

We build the bijection piece by piece: it follows $f$ on one part of $A$ and $g^{-1}$ on the rest.

1. Let $f \colon A \to B$ and $g \colon B \to A$ be [[injective functions|0PVG1CRAJN]].
2. By [[definition by recursion|0DSHAVH45F]], define subsets $C_n \subseteq A$ by $C_0 = A \setminus g(B)$ and $C_{n+1} = g(f(C_n))$. Here $g(f(C_n))$ is the [[image|0Q3F20XB0A]] of $C_n$ under $g \circ f$.
3. Let $C = \bigcup_{n \in \N} C_n$ be their [[union|05GK32H72H]].
4. Let $x \in A \setminus C$. Then $x \notin C_0$, so $x \in g(B)$. Since $g$ is injective, exactly one $y \in B$ has $g(y) = x$. Write $g^{-1}(x) = y$.
5. Define $h \colon A \to B$ by $h(x) = f(x)$ if $x \in C$, and $h(x) = g^{-1}(x)$ if $x \notin C$.
6. We show that $h$ is injective. Let $x, x' \in A$ with $h(x) = h(x')$.
7. If $x, x' \in C$, then $f(x) = f(x')$, so $x = x'$ because $f$ is injective.
8. If $x, x' \notin C$, then $g^{-1}(x) = g^{-1}(x')$. Applying $g$ gives $x = x'$.
9. Suppose $x \in C$ and $x' \notin C$. Then $f(x) = g^{-1}(x')$, so $x' = g(f(x))$.
10. In step 9, $x \in C_n$ for some $n$, so $x' \in g(f(C_n)) = C_{n+1} \subseteq C$. This contradicts $x' \notin C$. The case $x \notin C$, $x' \in C$ is the same with the roles exchanged.
11. So $h$ is injective. We show that $h$ is [[surjective|0XKH881BZ7]]. Let $y \in B$ and put $x = g(y)$.
12. If $x \notin C$, then $g^{-1}(x) = y$ by step 4, so $h(x) = y$.
13. If $x \in C$, then $x \in C_n$ for some $n$. Since $x \in g(B)$, $x \notin C_0$, so $n \ge 1$.
14. So $x \in C_n = g(f(C_{n-1}))$, and $x = g(f(z))$ for some $z \in C_{n-1} \subseteq C$.
15. Then $g(y) = g(f(z))$, so $y = f(z)$ because $g$ is injective. Since $z \in C$, $h(z) = f(z) = y$.
16. Thus $h$ is injective and surjective, so $h \colon A \to B$ is a [[bijective function|0SNQEF7Z53]].

## Idea

The points of $A$ outside $g(B)$ have no preimage under $g$, so they must be sent by $f$. Following them under $g \circ f$ gives the set $C$ where we use $f$. Everywhere else, $g$ can be undone, and the two pieces fit together without overlap or gaps.
