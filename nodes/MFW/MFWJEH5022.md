---
tag: MFWJEH5022
kind: example
name: Division does not interpret a function symbol on the real numbers
msc: ["03C07"]
topics: [NJDME6F845]
audience: ug2
not_instance_of:
  - target: 983GZBQYT4
    note: the interpretation of a function symbol must be a total function, and 1 / 0 has no value
uses: [983GZBQYT4, 0EPAT51DXQ, 08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_(mathematical_logic)
    locator: Definition
---

## Example

Let $L = \{f\}$ be the signature with one binary function symbol $f$.
Let the domain be the set $\mathbb{R}$ of [[real numbers|08J2M1JYAG]], and try to interpret $f$ as division, $f^{\mathcal{M}}(a, b) = a / b$.
We show that this does not give an $L$-[[structure|983GZBQYT4]].

1. A structure needs a [[function|0EPAT51DXQ]] $f^{\mathcal{M}} \colon \mathbb{R}^2 \to \mathbb{R}$, so $f^{\mathcal{M}}(a, b)$ must have a value for every pair $(a, b) \in \mathbb{R}^2$.
2. Take the pair $(1, 0)$.
   A value $q = 1 / 0$ would satisfy $q \cdot 0 = 1$, but $q \cdot 0 = 0$ for every real number $q$.
3. So $1 / 0$ has no value, and division is not a function from $\mathbb{R}^2$ to $\mathbb{R}$.

The totality condition fails at the pair $(1, 0)$, so $(\mathbb{R}, /)$ is not an $L$-structure.

## Remarks

A function symbol must be interpreted by an operation that is defined on the whole of $M^n$.
There are three standard repairs, and each one changes a different part of the setup.

The first repair makes the domain smaller.
On $\mathbb{R} \setminus \{0\}$, the quotient of two nonzero numbers is defined and nonzero, so $(\mathbb{R} \setminus \{0\}, /)$ is an $L$-structure.

The second repair uses a relation symbol instead of a function symbol.
Let $D$ be a ternary relation symbol, and let
$$D^{\mathcal{M}} = \{ (a, b, q) \in \mathbb{R}^3 : b \neq 0 \text{ and } q \cdot b = a \}.$$
Every subset of $\mathbb{R}^3$ is allowed, so $(\mathbb{R}, D^{\mathcal{M}})$ is a structure for $\{D\}$.

The third repair gives $a / 0$ some fixed value.
Mathlib sets $a / 0 = 0$ for every $a$, which makes division total on $\mathbb{R}$.
The price is that the law $b \cdot (a / b) = a$ now needs the hypothesis $b \neq 0$, since $0 \cdot (1 / 0) = 0 \neq 1$.

## Explanations

### L1 human

In a structure, each operation symbol must give an answer for every input.
Division of real numbers fails this test, because we cannot divide $1$ by $0$.
So "the real numbers with division" is not a structure in the strict sense.
If we remove $0$ from the set, every division has an answer, and we get a structure.

### L2 human

We check the first repair on the domain $N = \mathbb{R} \setminus \{0\}$.
Let $a, b \in N$.
Then $b \neq 0$, so $a / b$ is a real number.
If $a / b = 0$, then $a = (a / b) \cdot b = 0$, which contradicts $a \neq 0$, so $a / b \in N$.
Thus $/ \colon N^2 \to N$ is a function.

The typical use of the example is to explain why fields are usually given in the signature $\{+, \cdot, -, 0, 1\}$ with no symbol for division.
Watch out: division is total on $\mathbb{R} \times (\mathbb{R} \setminus \{0\})$, but that set is not of the form $M^2$, so it does not give a structure.
