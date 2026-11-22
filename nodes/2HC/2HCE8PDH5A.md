---
tag: 2HCE8PDH5A
kind: proof
name: Proof that the inverse of a bijective linear map is linear
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: E08G7CVKPK
methods: [0NTF6DMVAP, DD2P85Y8E9]
uses: [0XSJ25Z9M4, 0W766JAPSN, 0RJF668P1T, 0PVG1CRAJN]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Linear endomorphisms and isomorphisms
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Proof

We apply $T$ to both sides of each linearity condition for $T^{-1}$ and then use that $T$ is injective.
Let $S = T^{-1}$, so that $T(S(w)) = w$ for each $w \in W$, by the [[definition of the inverse|0W766JAPSN]].

1. Let $w_1, w_2 \in W$; additivity of $T$ gives $T(S(w_1) + S(w_2)) = T(S(w_1)) + T(S(w_2)) = w_1 + w_2$.
2. Also $T(S(w_1 + w_2)) = w_1 + w_2$.
3. So $T$ sends $S(w_1) + S(w_2)$ and $S(w_1 + w_2)$ to the same vector.
4. The map $T$ is [[injective|0PVG1CRAJN]], so $S(w_1 + w_2) = S(w_1) + S(w_2)$.
5. Let $a \in F$ and $w \in W$; homogeneity of $T$ gives $T(a\,S(w)) = a\,T(S(w)) = aw$.
6. Also $T(S(aw)) = aw$, and $T$ is injective, so $S(aw) = a\,S(w)$.
7. Steps 4 and 6 show that $S$ is a [[linear map|0RJF668P1T]], and it is bijective with inverse $T$.

## Idea

Apply $T$ to both candidate values.
Linearity of $T$ shows that both give the same vector, and injectivity of $T$ shows that the candidates are equal.

## Variants

Both checks fit in one step: $T(a\,S(w_1) + S(w_2)) = a w_1 + w_2 = T(S(a w_1 + w_2))$, and injectivity gives $S(a w_1 + w_2) = a\,S(w_1) + S(w_2)$.
In finite dimension with bases, the matrix of $T$ is invertible and the matrix of $T^{-1}$ is the inverse matrix.
This proves linearity by a formula, but it needs a choice of bases and works only in finite dimension.
