---
tag: 7XKWHMNGQH
kind: example
name: The Herbrand universe of one constant and one unary function symbol
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
instance_of: [NFW38QJ3A7]
uses: [JKP0XNXRPB, 0MWKJ44V5A, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
---

## Example

Let $L = \{ 0, s \}$, with a constant symbol $0$ and a unary function symbol $s$.
For $n \in \mathbb{N}$, write $s^n(0)$ for the term $s(s(\cdots s(0) \cdots))$ with $n$ copies of $s$, so $s^0(0) = 0$ and $s^3(0) = s(s(s(0)))$.
We show that the [[Herbrand universe|JKP0XNXRPB]] is
$$H(L) = \{ s^n(0) : n \in \mathbb{N} \},$$
and that $n \mapsto s^n(0)$ is a bijection from $\mathbb{N}$ to $H(L)$.

1. Each $s^n(0)$ is a closed term, because it comes from the constant $0$ by $n$ applications of $s$.
   So each $s^n(0)$ lies in $H(L)$.
2. Conversely, every closed term has the form $s^n(0)$, by [[structural induction|12MQ2NJ29A]].
   The only constant is $0 = s^0(0)$.
   The only function symbol is $s$, and if $t = s^n(0)$, then $s(t) = s^{n+1}(0)$.
3. The terms $s^m(0)$ and $s^n(0)$ with $m \neq n$ are different strings, because they contain different numbers of the symbol $s$.
   So the map $n \mapsto s^n(0)$ is injective.
4. Steps 1 and 2 show that the map is onto $H(L)$, and step 3 shows that it is injective, so it is a bijection.

The levels of the definition are easy to read off:
$$H_0 = \{ 0 \}, \qquad H_1 = \{ 0, s(0) \}, \qquad H_2 = \{ 0, s(0), s^2(0) \}.$$
In general the term $s^n(0)$ first appears at level $n$.

## Remarks

The example shows that $H(L)$ is a copy of the [[natural numbers|0MWKJ44V5A]], with $s$ in the role of the successor and $0$ in the role of zero.
It is the simplest infinite Herbrand universe, and the examples of Herbrand structures use it again and again.

The evaluation map depends on the structure.
In the structure $(\mathbb{N}, 0, n \mapsto n + 1)$ it sends $s^n(0)$ to $n$, and it is the inverse of the bijection above.
In the structure $(\mathbb{Z} / 3\mathbb{Z}, 0, n \mapsto n + 1)$ it sends $s^n(0)$ to $n \bmod 3$.
That map is onto but not injective, so the terms $s^3(0)$ and $0$ are different elements of $H(L)$ with the same value.

If we add a unary relation symbol $P$, the Herbrand base is $\{ P(s^n(0)) : n \in \mathbb{N} \}$.
So a set of ground atoms is the same thing as a subset of $\mathbb{N}$.

## Explanations

### L1 human

With a starting name $0$ and a "next" symbol $s$, the names are $0$, $s(0)$, $s(s(0))$, and so on.
There is exactly one name for each natural number: count the copies of $s$.
The name $s(s(s(0)))$ is three symbols $s$ in front of $0$.

### L2 human

The typical use is to read a set of ground atoms as a set of numbers.
For $L = \{ 0, s, P \}$, the set of atoms $\{ P(0), P(s^2(0)), P(s^4(0)), \ldots \}$ corresponds to the even numbers.
Under this match, the universal sentence $\forall x \, (P(x) \to P(s(s(x))))$ says that the set is closed under adding $2$.
Watch out: $s^3(0)$ is not the number $3$.
It is a string of symbols, and a structure may give it the value $3$, or $0$ in $\mathbb{Z} / 3\mathbb{Z}$, or something else.
