---
tag: BD4PEHWBRX
kind: example
name: Divisibility, evenness and primality as formulas of arithmetic
msc: ["03F30", "03B10"]
topics: [QHCRN4JVG0, AY09KYSW81]
audience: ug2
instance_of: [CY1TXHF6KQ]
illustrates: [D8SD54M5PN]
uses: [329ZG1Z0G5, 1DQ1M6ZWS4, 0PG2H7WKGG, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
    locator: Examples
  - book: isbn:9780521857840
---

## Example

We work in the [[language of arithmetic|D8SD54M5PN]] $L_A$ and its standard model $\mathfrak{N}$.
We define three relations by formulas, and we check that each formula defines the intended relation, so each relation is a [[definable set|CY1TXHF6KQ]] of $\mathfrak{N}$.

The formulas are:
$$\mathrm{Div}(x, y) := \exists z \le y\; (z \cdot x = y),$$
$$\mathrm{Even}(x) := \exists y \le x\; (y + y = x),$$
$$\mathrm{Prime}(x) := \overline{1} < x \land \forall y \le x\; \forall z \le x\; \bigl(y \cdot z = x \to (y = \overline{1} \lor z = \overline{1})\bigr).$$

1. $\mathrm{Div}$ defines [[divisibility|0PG2H7WKGG]]. If $m \mid n$ with $n \ge 1$, then $n = k m$ with $k \ge 1$ and $m \ge 1$, so $k \le n$, and $z = k$ is a witness. If $n = 0$, then $z = 0$ is a witness, and indeed every $m$ divides $0$. Conversely, a witness $z$ gives $n = z m$, so $m \mid n$.
2. The bound $z \le y$ in step 1 loses no witness, by the argument of step 1. So the bounded formula and the unbounded formula $\exists z\,(z \cdot x = y)$ define the same relation in $\mathfrak{N}$.
3. $\mathrm{Even}$ defines the even numbers. If $n = 2k$, then $k \le n$ and $k + k = n$. Conversely, a witness $y$ gives $n = 2y$.
4. $\mathrm{Prime}$ defines the [[prime numbers|01826KMG2H]]. A number $n$ is prime when $n > 1$ and its only factorizations $n = a b$ have $a = 1$ or $b = 1$.
5. In such a factorization of $n \ge 1$, both $a \ge 1$ and $b \ge 1$, so $a \le n$ and $b \le n$. So the bounds $y \le x$ and $z \le x$ do not exclude any factorization.

We check the formulas on small numbers.

6. $\mathrm{Div}(\overline{6}, \overline{18})$ is true, with the witness $z = 3$: $3 \le 18$ and $3 \cdot 6 = 18$.
7. $\mathrm{Div}(\overline{4}, \overline{18})$ is false: the products $z \cdot 4$ for $z = 0, 1, \ldots, 18$ are the multiples of $4$, and $18$ is not a multiple of $4$.
8. $\mathrm{Even}(\overline{14})$ is true, with the witness $y = 7$.
9. $\mathrm{Prime}(\overline{7})$ is true: $1 < 7$, and the only pairs $(y, z)$ with $y, z \le 7$ and $y z = 7$ are $(1, 7)$ and $(7, 1)$.
10. $\mathrm{Prime}(\overline{1})$ is false, because the first conjunct $1 < 1$ is false.

## Remarks

The example shows that $L_A$ has no symbol for "divides" or "prime", but expresses both with $+$, $\cdot$, $<$ and quantifiers.
All three formulas use only bounded quantifiers, so they are $\Delta_0$ formulas in the sense of [[this page|GE43CSZTS9]].
In $\mathfrak{N}$ a $\Delta_0$ formula can be checked by a finite search, so these three relations are decidable.
If we drop the bounds, then $\mathrm{Div}$ and $\mathrm{Even}$ become $\Sigma_1$ formulas with the same meaning in $\mathfrak{N}$, but we lose the information that the search is finite.
If we drop the conjunct $\overline{1} < x$ in $\mathrm{Prime}$, then the formula also holds at $x = 1$; at $x = 0$ it still fails, because $y = z = 0$ gives $0 \cdot 0 = 0$ with neither factor equal to $1$.

## Explanations

### L1 human

The language of arithmetic has no word for "prime", so we spell it out.
"$x$ is prime" becomes "$x$ is larger than $1$, and whenever two numbers up to $x$ multiply to $x$, one of them is $1$".
For $x = 7$ this holds, since $7 = 1 \cdot 7$ is the only way.
For $x = 6$ it fails, since $6 = 2 \cdot 3$.

### L2 human

We check $\mathrm{Div}(\overline{0}, \overline{5})$ and $\mathrm{Div}(\overline{5}, \overline{0})$.

1. $\mathrm{Div}(\overline{0}, \overline{5})$ asks for $z \le 5$ with $z \cdot 0 = 5$.
2. Every $z$ gives $z \cdot 0 = 0 \ne 5$, so the formula is false: $0$ does not divide $5$.
3. $\mathrm{Div}(\overline{5}, \overline{0})$ asks for $z \le 0$ with $z \cdot 5 = 0$.
4. The witness $z = 0$ works, so the formula is true: $5$ divides $0$.

The typical use of such formulas is to state number theory in $L_A$, for example the infinitude of primes in [[this example|HTTAH8PY38]].
A trap is the order of the factors: in a weak theory without commutativity, $z \cdot x = y$ and $x \cdot z = y$ are different formulas, and a definition must fix one of them.
