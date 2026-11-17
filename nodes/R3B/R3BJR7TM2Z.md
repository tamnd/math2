---
tag: R3BJR7TM2Z
kind: example
name: The Cantor normal form notation for epsilon nought
msc: ["03F15", "03E10"]
topics: [XTTKZTYDSD]
audience: grad
instance_of: [7MBX59Y7N9]
uses: [3CNSYYX2HF, 6GD30FGYDZ, DXKWBFWCE0, KT50SMH3EC, QQQRJA90EP]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_notation
    locator: Cantor
  - url: https://en.wikipedia.org/wiki/Ordinal_arithmetic
    locator: Cantor normal form
---

## Example

Let $T$ be the set of terms defined by two rules.

- $0$ is a term.
- If $a_1, \ldots, a_k$ are terms with $k \ge 1$ and $a_1 \succeq a_2 \succeq \cdots \succeq a_k$, then $\omega^{a_1} + \cdots + \omega^{a_k}$ is a term.

The order $\prec$ on terms is defined by recursion on the length of terms.

- $0 \prec b$ for every term $b \ne 0$.
- For $a = \omega^{a_1} + \cdots + \omega^{a_k}$ and $b = \omega^{b_1} + \cdots + \omega^{b_m}$, let $a \prec b$ if $(a_1, \ldots, a_k)$ is a proper initial segment of $(b_1, \ldots, b_m)$. Also let $a \prec b$ if $a_i \prec b_i$ at the first index $i$ where the lists differ.

Code each term by a natural number in a standard way, for example by its string of symbols.
We check that $(T, \prec)$ is an [[ordinal notation system|3CNSYYX2HF]] for [[epsilon nought|KT50SMH3EC]].

1. The set $T$ and the relation $\prec$ are primitive recursive. Each rule refers only to shorter terms, so a test of membership or of order is a recursion on the length of the codes. This gives [[primitive recursive relations|QQQRJA90EP]].
2. Define $v(0) = 0$ and $v(\omega^{a_1} + \cdots + \omega^{a_k}) = \omega^{v(a_1)} + \cdots + \omega^{v(a_k)}$. By induction on the length of terms, $v(a) < \varepsilon_0$, because the ordinals below $\varepsilon_0$ are closed under $+$ and $\alpha \mapsto \omega^\alpha$.
3. The term $\omega^{a_1} + \cdots + \omega^{a_k}$ with equal neighbouring exponents grouped is a [[Cantor normal form|6GD30FGYDZ]] with coefficients. So the [[comparison of Cantor normal forms|DXKWBFWCE0]] gives: $a \prec b$ if and only if $v(a) < v(b)$. The two lexicographic rules agree, because a run of $c$ equal exponents compares like the pair $(\beta, c)$.
4. By step 3, $v$ is injective and preserves the order. So $\prec$ is a strict total order on $T$, and it is well-founded, since a descending sequence of terms would give a descending sequence of ordinals.
5. Every ordinal $\alpha < \varepsilon_0$ is $v(a)$ for some term $a$: write $\alpha$ in Cantor normal form, and write each exponent, which is smaller than $\alpha$, in the same way. So $v$ is onto $\varepsilon_0$, and $\abs{\prec} = \varepsilon_0$.

A sample comparison: $a = \omega^{\omega^0} + \omega^0$ names $\omega + 1$, and $b = \omega^{\omega^0 + \omega^0}$ names $\omega^2$.
The first exponents are $\omega^0$ and $\omega^0 + \omega^0$; the list $(0)$ is a proper initial segment of $(0, 0)$, so $\omega^0 \prec \omega^0 + \omega^0$.
So $a \prec b$, and indeed $\omega + 1 < \omega^2$.

## Remarks

This is the standard notation system for $\varepsilon_0$, the one in Gentzen's consistency proof and in the statement that the proof-theoretic ordinal of PA is $\varepsilon_0$.
Step 4 uses the ordinals of set theory to prove well-foundedness.
Inside PA, the well-foundedness of an initial segment below a fixed term is provable, but the well-foundedness of all of $T$ is not; see [[transfinite induction in arithmetic|ZE54ABPMJ0]].
If one adds a symbol for $\varepsilon_0$ and closes again under the rules, one gets a system for $\varepsilon_1$, and so on.

## Explanations

### L1 human

Every ordinal below $\varepsilon_0$ can be written using only $0$, plus signs and powers of $\omega$.
For example, $\omega^{\omega^0} + \omega^0$ is a long way of writing $\omega + 1$.
To compare two such expressions, compare the exponents of the first terms, then of the second terms, and so on.
A computer can do this, and it always gives the right answer.

### L2 human

We compare $a = \omega^{\omega^{\omega^0}} + \omega^0$ with $b = \omega^{\omega^0 + \omega^0} + \omega^{\omega^0}$.

1. The values are $v(a) = \omega^\omega + 1$ and $v(b) = \omega^2 + \omega$.
2. The first exponents are $\omega^{\omega^0}$ and $\omega^0 + \omega^0$.
3. To compare them, compare their first exponents $\omega^0$ and $0$. Since $0 \prec \omega^0$, the exponent of $a$ is larger.
4. So $b \prec a$, and indeed $\omega^2 + \omega < \omega^\omega + 1$.

The typical use is in a proof of termination: a process that lowers a term of $T$ at each step must stop.
The trap: a string such as $\omega^0 + \omega^{\omega^0}$ is not a term of $T$, because its exponents increase.
Its value $1 + \omega$ equals $\omega$, which has the term $\omega^{\omega^0}$.
