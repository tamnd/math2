---
tag: CGV3Z8SN55
kind: example
name: Congruence modulo 2 satisfies the equality axioms but is not equality
msc: ["03B10", "08A30"]
topics: [PSRDJXRW53]
audience: ug2
not_instance_of:
  - target: Q1494G7FBM
    note: interpreting the equality symbol on the integers as congruence modulo 2 satisfies every equality axiom, but in logic with equality the symbol must mean identity, so this is not a structure of that logic
uses: [Q1494G7FBM, 79ND6CD7ND, DCSXXT4SER, 0011MTQMR6, 0G8VEZ3WTK, 0B1261B5ED]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Equality and its axioms
  - book: isbn:9781482237726
    locator: Chapter 2
---

## Example

Let $\sigma = \{ +, \cdot, -, 0, 1 \}$ be the signature of [[rings|0B1261B5ED]], with a binary relation symbol $\approx$ that plays the role of $=$.
Let $\mathcal{M}$ have domain $\mathbb{Z}$, the usual ring operations, and $\approx$ read as
$$E = \{ (a, b) \in \mathbb{Z}^2 : a \equiv b \pmod 2 \}.$$
We check that $\mathcal{M}$ satisfies every equality axiom for $\approx$, and that $E$ is not identity.

1. Reflexivity: $a - a = 0$ is even, so $a \mathrel{E} a$ for every $a$.
2. Substitution for $+$: let $a \mathrel{E} b$ and $c \mathrel{E} d$.
   Then $(a + c) - (b + d) = (a - b) + (c - d)$ is a sum of two even numbers, so $(a + c) \mathrel{E} (b + d)$.
3. Substitution for $\cdot$: with the same hypotheses, $ac - bd = a(c - d) + d(a - b)$ is even.
4. Substitution for the unary $-$: $(-a) - (-b) = -(a - b)$ is even when $a - b$ is even.
5. The constants $0$ and $1$ have arity $0$ and need only reflexivity.
6. Substitution for $\approx$: let $a \mathrel{E} b$, $c \mathrel{E} d$ and $a \mathrel{E} c$.
   $E$ is an [[equivalence relation|0G8VEZ3WTK]], so $b \mathrel{E} a \mathrel{E} c \mathrel{E} d$ gives $b \mathrel{E} d$.
7. So $\mathcal{M}$ satisfies all the equality axioms, the same list as in [[the equality axioms for groups|79ND6CD7ND]] with one axiom for each ring symbol.
8. But $0 \mathrel{E} 2$ and $0 \neq 2$.
   So $E$ is not identity, and $\mathcal{M}$ is not a structure of [[first-order logic with equality|Q1494G7FBM]] with $\approx$ as its equality.

So the equality axioms do not force the symbol to mean identity.

## Remarks

### What the structure believes

In $\mathcal{M}$ the sentence $\forall x \, \forall y \, \forall z \, (x \approx y \lor x \approx z \lor y \approx z)$ is true, because of three integers two have the same parity.
So $\mathcal{M}$ "believes" that it has at most two elements, although $\mathbb{Z}$ is infinite.
The [[quotient|0011MTQMR6]] $\mathcal{M} / E$ is the ring $\mathbb{Z} / 2\mathbb{Z}$, where $\approx$ is true identity, and it makes the same sentences true as $\mathcal{M}$.

### Why the quotient agrees

The argument works for every relation $E$ that satisfies the equality axioms, that is, for every [[congruence|DCSXXT4SER]].

1. Let $\pi \colon \mathbb{Z} \to \mathbb{Z} / 2\mathbb{Z}$ be the quotient map, and let $s$ be an assignment in $\mathbb{Z}$.
2. For each term $t$, the value of $t$ in $\mathcal{M} / E$ under $\pi \circ s$ is $\pi$ of its value in $\mathcal{M}$ under $s$.
   This holds by induction on $t$, because $E$ respects $+$, $\cdot$ and $-$.
3. An atomic formula $t_1 \approx t_2$ holds in $\mathcal{M}$ under $s$ exactly when the two values are in $E$, that is, when their images under $\pi$ are equal.
4. The connectives commute with this correspondence.
5. For $\exists x \, \varphi$: $\pi$ is onto, so each witness in $\mathbb{Z} / 2\mathbb{Z}$ has the form $\pi(a)$, and $a$ is a witness in $\mathbb{Z}$; the converse is direct.
6. So each formula holds in $\mathcal{M}$ under $s$ exactly when it holds in $\mathcal{M} / E$ under $\pi \circ s$.

## Explanations

### L1 human

The rules for equals say two things: everything equals itself, and equals can replace equals.
The relation "has the same parity" on the integers obeys all these rules.
But $0$ and $2$ have the same parity and are different numbers.
So the rules alone do not make a relation into true equality.

### L2 human

We check one instance of the substitution axiom for $\cdot$ with numbers.
Take $a = 3$, $b = 7$, $c = 4$ and $d = 10$, so $a \mathrel{E} b$ and $c \mathrel{E} d$.
Then
$$ac = 12, \qquad bd = 70, \qquad bd - ac = 58,$$
and $58$ is even, so $ac \mathrel{E} bd$, as step 3 predicts.
In $\mathbb{Z} / 2\mathbb{Z}$ the same instance reads $\bar{1} \cdot \bar{0} = \bar{0} = \bar{1} \cdot \bar{0}$.
The typical use of this construction is in the proof of the completeness theorem with equality: the Henkin model is first built with a congruence in place of $=$, and then divided by it.
Watch out: "satisfies the axioms of equality" and "is equality" differ, and the difference disappears only after the quotient.
