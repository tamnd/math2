---
tag: HGKPSMZPZN
kind: proof
name: Proof that normal operators have equal norms for T and its adjoint
msc: ["15A04", "47B15"]
topics: [3YM9EK6VMB]
audience: ug1
proves: EMW3QTE3H9
uses: [0VGSYBWHV2, 0ST8QF9T3T, 0ENZN5G4CV, 0MB8HQW495, TPP76FP659, WAYMK9GR5S]
methods: [0NTF6DMVAP, TFQ1845T84]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_operator
    locator: Properties
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Proof

We write the difference of the two squared norms as the quadratic form of a self-adjoint operator, and then we use the fact that such an operator is $0$ when its quadratic form is $0$.

1. Let $v \in V$. By the [[definition of the adjoint|0ST8QF9T3T]], $\norm{Tv}^2 = \ip{Tv}{Tv} = \ip{T^* T v}{v}$.
2. By [[the algebraic properties of the adjoint|TPP76FP659]], $(T^*)^* = T$. So the definition applied to $T^*$ gives $\norm{T^* v}^2 = \ip{T^* v}{T^* v} = \ip{T T^* v}{v}$.
3. Subtract step 2 from step 1, and set $S = T^* T - T T^*$. This gives
$$\norm{Tv}^2 - \norm{T^* v}^2 = \ip{S v}{v}.$$
4. Part 1, first direction. If $T$ is [[normal|0ENZN5G4CV]], then $S = 0$, so step 3 gives $\norm{Tv}^2 = \norm{T^* v}^2$. Both norms are nonnegative, so $\norm{Tv} = \norm{T^* v}$.
5. Part 1, second direction. The algebraic properties give $(T^* T)^* = T^* T^{**} = T^* T$ and $(T T^*)^* = T^{**} T^* = T T^*$. So $S$ is [[self-adjoint|0MB8HQW495]].
6. If $\norm{Tv} = \norm{T^* v}$ for all $v$, then step 3 gives $\ip{Sv}{v} = 0$ for all $v$.
7. By part 3 of [[the quadratic form statement|WAYMK9GR5S]], a self-adjoint operator with zero quadratic form is $0$. So $S = 0$, and $T$ is normal.
8. Part 2. Let $T$ be normal. By the positivity of the [[inner product|0VGSYBWHV2]], $Tv = 0$ exactly when $\norm{Tv} = 0$. By part 1, this holds exactly when $\norm{T^* v} = 0$, that is, when $T^* v = 0$.
9. Part 3. By the algebraic properties, $(T - \lambda I)^* = T^* - \overline{\lambda} I$.
10. Expand both products:
$$(T - \lambda I)^* (T - \lambda I) = T^* T - \lambda T^* - \overline{\lambda} T + \abs{\lambda}^2 I,$$
$$(T - \lambda I)(T - \lambda I)^* = T T^* - \overline{\lambda} T - \lambda T^* + \abs{\lambda}^2 I.$$
11. Since $T^* T = T T^*$, the two right sides of step 10 are equal. So $T - \lambda I$ is normal.
12. Apply part 2 to the normal operator $T - \lambda I$, whose adjoint is $T^* - \overline{\lambda} I$ by step 9. So $(T - \lambda I) v = 0$ exactly when $(T^* - \overline{\lambda} I) v = 0$, which is part 3.

## Idea

The identity $\norm{Tv}^2 - \norm{T^* v}^2 = \ip{(T^* T - T T^*) v}{v}$ turns a condition on norms into a condition on a quadratic form.
The operator $T^* T - T T^*$ is self-adjoint, and a self-adjoint operator is $0$ exactly when its quadratic form is $0$.
Parts 2 and 3 then come from looking at the vectors of norm $0$, first for $T$ and then for $T - \lambda I$.

## Variants

Over $\mathbb{C}$, step 7 can use part 1 of the quadratic form statement instead, since over $\mathbb{C}$ every operator with zero quadratic form is $0$, self-adjoint or not.
Over $\mathbb{R}$ the self-adjointness of $S$ from step 5 cannot be skipped: the quarter turn of $\mathbb{R}^2$ has zero quadratic form without being $0$.
