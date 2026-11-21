---
tag: G3GGANFA7C
kind: example
name: Real closed fields are model complete in the ring signature
aliases: [real-closed-fields-model-complete-ring-signature]
msc: ["03C10", "12D15"]
topics: [1A9JSC5YG8]
audience: grad
instance_of: [YR6HCMABTE]
uses: [ERVV6RWNNX, FSJ9NGRRPA, DDY3Q3PJ6W, 0P3VCBDEE2, C9494XYEMN, 8WZF9SBP39]
sources:
  - url: https://en.wikipedia.org/wiki/Model_complete_theory
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Example

Let $L_{\mathrm{ring}} = \set{+, -, \cdot, 0, 1}$.
A field $K$ is [[real closed|DDY3Q3PJ6W]] when $-1$ is not a sum of squares in $K$, every element or its negative is a square, and every polynomial of odd degree over $K$ has a root in $K$.
Let $T$ be the $L_{\mathrm{ring}}$-theory of real closed fields.
We show that $T$ is [[model complete|ERVV6RWNNX]].

1. In a real closed field $K$, the relation "$y - x$ is a square" is a field ordering, and it is the only one. So $K$ is an [[ordered field|0P3VCBDEE2]] in a unique way.
2. Let $K \subseteq F$ be real closed fields, and let $a, b \in K$ with $a \le b$ in $K$. Then $b - a = c^2$ for some $c \in K$.
3. The same equation holds in $F$, so $a \le b$ in $F$. So the inclusion $K \subseteq F$ preserves the order, and it is an inclusion of ordered fields.
4. By [[Tarski's theorem|FSJ9NGRRPA]], each formula of the ordered signature is equivalent in real closed ordered fields to a quantifier-free formula $\psi$.
5. [[Embeddings preserve quantifier-free formulas|C9494XYEMN]], so $\psi$ has the same truth value at a tuple of $K$ in $K$ and in $F$.
6. So $K$ is an [[elementary substructure|8WZF9SBP39]] of $F$ in the ordered signature. In particular, $K \preceq F$ for all $L_{\mathrm{ring}}$-formulas, which are formulas of the ordered signature.

So every inclusion between models of $T$ is elementary, and $T$ is model complete.

## Remarks

The example shows a model complete theory without [[quantifier elimination|7FDDXV3JK7]].
In $L_{\mathrm{ring}}$, the formula $\exists y \, (x = y \cdot y)$ has no quantifier-free equivalent; see [[this non-example|367Y9XDMXG]].
The order is defined by the existential formula $\exists z \, (y - x = z^2)$.
Its negation $x > y$ is defined by the existential formula $\exists z \, (z \ne 0 \wedge x - y = z^2)$.
So each quantifier-free formula of the ordered signature becomes an existential $L_{\mathrm{ring}}$-formula, as [[Robinson's test|QHEADWYQ64]] predicts.

When a parameter changes, the result changes in this way.

- For the theory of all ordered fields, model completeness fails: $\Q \subseteq \R$ is an inclusion of ordered fields, and $\exists y \, (y \cdot y = 1 + 1)$ is false in $\Q$ and true in $\R$.
- For fields with more than one ordering, such as $\Q(\sqrt 2)$, step 1 fails, and a ring embedding need not preserve a chosen order.

## Explanations

### L1 human

The real numbers and the real algebraic numbers are both real closed fields.
In such a field, a number is positive or zero exactly when it is a square.
So a field inside another one knows the order of the larger field: $2$ is positive because $2 = (\sqrt 2)^2$ in both.
Because of this, the smaller field gives the same answer as the larger one to every question in the language of plus and times.

### L2 human

We check one instance of step 3.

1. Let $K$ be the real algebraic numbers and $F = \R$.
2. In $K$, the number $3 - \sqrt 2$ is positive, since $3 - \sqrt 2 = c^2$ with $c = \sqrt{3 - \sqrt 2}$, which is algebraic.
3. In $\R$ the same $c$ works, so $3 - \sqrt 2$ is positive in $\R$ too.
4. So a question such as "$\exists y \, (y^2 = 3 - \sqrt 2)$" has the same answer in $K$ and in $\R$.

The typical use of the example is to show that model completeness is weaker than quantifier elimination.
A trap is to apply the argument to ordered fields that are not real closed, where the order is not the set of squares.
