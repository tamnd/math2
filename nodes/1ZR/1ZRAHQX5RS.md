---
tag: 1ZRAHQX5RS
kind: proof
name: Proof that the automorphism group of a finite extension has order at most the degree
msc: [12F10]
proves: 0QM98DNWVW
uses: [0NRYPM9Y27, 0XVR72M51M, 0GGE0Z0JQ1, 0DFYTNZ6AM, 0GK1WB9R98, 0N5QW9K7MH, 0ZN39QDTP9, 0KJVQV3E0F, 0A7KJ68XHT]
sources:
  - url: https://www.jmilne.org/math/CourseNotes/FT.pdf
---

## Proof

We first prove a lemma by induction on the degree. All fields are commutative, and homomorphisms are [[ring homomorphisms|0GGE0Z0JQ1]] that send $1$ to $1$.

Lemma. Let $E/F$ be a [[finite extension|0NRYPM9Y27]], let $M$ be a field and let $\rho \colon F \to M$ be a homomorphism. Then at most $[E : F]$ homomorphisms $\tau \colon E \to M$ satisfy $\tau(c) = \rho(c)$ for all $c \in F$.

1. Let $d = [E : F]$. If $d = 1$, then $E = F$, and the only such $\tau$ is $\rho$.
2. Let $d > 1$, and assume the lemma for all finite extensions of degree less than $d$. Choose $a \in E$ with $a \notin F$.
3. The extension $E/F$ is finite, so $a$ is [[algebraic|0DFYTNZ6AM]] over $F$. Let $g = \sum_k g_k x^k$ be its [[minimal polynomial|0GK1WB9R98]], of degree $r$. Then $[F(a) : F] = r$ by the [[degree of a simple extension|0N5QW9K7MH]].
4. Since $a \notin F$, we have $F(a) \neq F$, so $r \ge 2$. By the [[tower law|0A7KJ68XHT]], $[E : F(a)] = d/r < d$.
5. Let $g^\rho = \sum_k \rho(g_k) x^k \in M[x]$. It has degree $r$, because $\rho(1) = 1$ and a homomorphism of fields is injective.
6. Let $\tau$ extend $\rho$. Applying $\tau$ to $g(a) = 0$ gives $g^\rho(\tau(a)) = 0$. So $\tau(a)$ is one of the [[at most $r$ roots|0KJVQV3E0F]] of $g^\rho$ in $M$.
7. By the [[structure of simple extensions|0ZN39QDTP9]], every element of $F(a)$ is $h(a)$ for some $h \in F[x]$. Then $\tau(h(a)) = h^\rho(\tau(a))$.
8. So the restriction of $\tau$ to $F(a)$ is determined by $\tau(a)$. Hence there are at most $r$ possible restrictions $\sigma \colon F(a) \to M$.
9. For each such $\sigma$, the induction hypothesis for $E/F(a)$ and $\sigma$ gives at most $[E : F(a)]$ homomorphisms $\tau$ that extend $\sigma$.
10. Every $\tau$ extending $\rho$ extends its own restriction $\sigma$. So there are at most $r \cdot [E : F(a)] = [E : F]$ such $\tau$, by the tower law. This proves the lemma.

Now let $L/K$ be a finite extension.

11. Every element $\sigma$ of [[$\operatorname{Aut}(L/K)$|0XVR72M51M]] is a homomorphism $L \to L$ with $\sigma(c) = c$ for $c \in K$.
12. Apply the lemma with $E = L$, $F = K$, $M = L$ and $\rho$ the inclusion $K \to L$. It gives at most $[L : K]$ such homomorphisms.
13. So $\operatorname{Aut}(L/K)$ is finite, and $\abs{\operatorname{Aut}(L/K)} \le [L : K]$.

## Idea

An automorphism fixing $K$ must send each generator to a root of its minimal polynomial, and such a polynomial has few roots. Adjoining one element at a time, the number of choices at each stage is at most the degree of that stage. The tower law multiplies these bounds into $[L : K]$.
