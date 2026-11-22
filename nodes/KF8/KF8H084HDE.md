---
tag: KF8H084HDE
kind: example
name: Rational numbers defined by abstraction
msc: ["00A35"]
topics: [BP0WAF23HB]
audience: ug1
instance_of: [B60DBNF77S]
uses: [B60DBNF77S, 0G8VEZ3WTK, 0W95W33CMP, 0011MTQMR6, 0NCJ5WXN6Z, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_number
    locator: Formal construction
  - url: https://en.wikipedia.org/wiki/Equivalence_class
    locator: Examples
---

## Example

Let $P = \{ (a, b) : a, b \in \mathbb{Z}, \ b \neq 0 \}$ be the set of pairs of [[integers|0C4JS9RF5M]] with a nonzero second entry.
Define a relation on $P$ by
$$(a, b) \sim (c, d) \iff ad = bc.$$
A [[rational number|0NCJ5WXN6Z]] is an [[equivalence class|0W95W33CMP]] of this relation, $\mathbb{Q} := P/{\sim}$ is the [[quotient set|0011MTQMR6]], and we write $\tfrac{a}{b}$ for the class of $(a, b)$.
This is a definition by abstraction, one of the [[kinds of definitions|B60DBNF77S]].
Its first obligation is to show that $\sim$ is an [[equivalence relation|0G8VEZ3WTK]].

1. Reflexive.
   For $(a, b) \in P$ we have $ab = ba$, so $(a, b) \sim (a, b)$.
2. Symmetric.
   If $ad = bc$, then $cb = da$, so $(c, d) \sim (a, b)$.
3. Transitive.
   Suppose $(a, b) \sim (c, d)$ and $(c, d) \sim (e, f)$, so that $ad = bc$ and $cf = de$.
4. Multiply the first equation by $f$ and use the second:
   $$adf = bcf = b(cf) = bde.$$
   So $d(af - be) = 0$.
5. The integer $d$ is not $0$, because $(c, d) \in P$.
   A product of two integers is $0$ only when a factor is $0$, so $af - be = 0$.
6. So $af = be$, and $(a, b) \sim (e, f)$.

Now the definition decides equalities by a calculation with integers.
We have $\tfrac{1}{2} = \tfrac{2}{4}$ because $1 \cdot 4 = 2 \cdot 2$, and $\tfrac{1}{2} = \tfrac{-3}{-6}$ because $1 \cdot (-6) = 2 \cdot (-3)$.
But $\tfrac{1}{2} \neq \tfrac{2}{3}$, because $1 \cdot 3 = 3$ and $2 \cdot 2 = 4$.

## Remarks

Before the definition, $(1, 2)$ and $(2, 4)$ are different pairs.
After it, they name the same element of $\mathbb{Q}$, so the definition turns "equal fractions" into equal objects.

Step 5 uses that $\mathbb{Z}$ has no zero divisors.
The same construction works for every integral domain and gives its [[field of fractions|0F2PTGX1A2]].
The condition $b \neq 0$ is needed too.
If we allow $b = 0$, transitivity fails:
$$(1, 1) \sim (0, 0) \text{ and } (0, 0) \sim (2, 1), \quad \text{but} \quad 1 \cdot 1 \neq 1 \cdot 2.$$

Addition is defined by $\tfrac{a}{b} + \tfrac{c}{d} := \tfrac{ad + bc}{bd}$.
That formula uses representatives, so it must be shown [[well defined|HNGZEBKVY2]], and the rule that [[adds numerators and denominators|C3Z6VNAXSG]] fails the same test.
The [[construction of the integers|0NS58JP68E]] from pairs of natural numbers follows the same pattern.

## Explanations

### L1 human

The fractions one half, two quarters and three sixths look different, but they name the same amount.
A definition by abstraction makes this exact.
It says that two fractions name the same number when their cross products are equal.
For one half and two quarters, $1 \times 4$ and $2 \times 2$ are both $4$, so they are the same number.
A rational number is then the whole family of fractions that name it.

### L2 human

We use the definition to show that $\tfrac{a}{b} = \tfrac{ka}{kb}$ for every nonzero integer $k$.
First, the pair $(ka, kb)$ is in $P$, because $kb \neq 0$ when $k \neq 0$ and $b \neq 0$.
By the definition of $\sim$ we must check $a \cdot (kb) = b \cdot (ka)$, and both sides equal $kab$ by the commutative and associative laws.
So $(a, b) \sim (ka, kb)$, and the two classes are equal.
The proof shows the usual use of the definition: an equality of rational numbers becomes an equality of integers that we can check.
Watch out: a rational number is the class, not the pair.
The rule $\tfrac{a}{b} \mapsto a$ is not a function on $\mathbb{Q}$, because $\tfrac{1}{2} = \tfrac{2}{4}$ but $1 \neq 2$.
