---
tag: 7TJPSD6H5P
kind: example
name: The reduced power of the reals modulo the Fréchet filter
msc: ["03C20"]
topics: [HZG1YP26AB]
audience: grad
instance_of: [F4WRD396PB]
not_instance_of:
  - target: AX9Q86GB8M
    note: "the Fréchet filter is not an ultrafilter, and the quotient ring is not a field"
uses: [F4WRD396PB, QN98V7NMCD, J64Y3JC0RE, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Reduced_product
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ultraproduct
    locator: Definition
---

## Example

Let $F$ be the [[Fréchet filter|QN98V7NMCD]] on $\N$: the subsets of $\N$ with finite complement.
Let $R = \R^{\N} / F$ be the [[reduced power|F4WRD396PB]] of the ring $(\R, +, \cdot, 0, 1)$.
So two real sequences are equal in $R$ when they agree from some index on.
We check that $R$ is a commutative ring, that it is not a [[field|04C5ZBG1WT]], and that $F$ is not an [[ultrafilter|J64Y3JC0RE]].

1. The axioms of commutative rings are equations, so they are Horn sentences, and they hold in $R$ because reduced products preserve Horn sentences.
2. Let $a = (1, 0, 1, 0, \dots)$ and $b = (0, 1, 0, 1, \dots)$. The set $\set{i : a(i) = 0}$ is the set of odd numbers, which is not cofinite. So $[a] \neq 0$, and in the same way $[b] \neq 0$.
3. The product $a \cdot b$ is the zero sequence, so $[a] \cdot [b] = 0$. A field has no zero divisors, so $R$ is not a field.
4. Neither the set of even numbers nor its complement, the set of odd numbers, is cofinite. So $F$ contains neither, and $F$ is not an ultrafilter.

## Remarks

The example shows why ultraproducts use ultrafilters.
The field axiom $\forall x \, (x = 0 \lor \exists y \, (x \cdot y = 1))$ holds in every factor, but it is not a Horn sentence, and it fails in $R$.
If $F$ is replaced by a nonprincipal ultrafilter $\mathcal{U} \supseteq F$, then $\mathcal{U}$ contains the evens or the odds, so one of $[a]$ and $[b]$ becomes $0$.
The quotient $\R^{\N} / \mathcal{U}$ is then a field, the field of [[hyperreal numbers|421QMTFG9T]].
The ring $R$ is the ring of "germs at infinity" of real sequences.

## Explanations

### L1 human

We treat two infinite lists of real numbers as equal when they agree after some point.
The lists $1, 0, 1, 0, \dots$ and $0, 1, 0, 1, \dots$ are both not equal to the zero list.
Their product, taken entry by entry, is the zero list.
In a field this cannot happen, so this structure is not a field.

### L2 human

We check that $[c]$ is invertible in $R$ when $c(i) \neq 0$ for all large $i$.

1. Let $c(i) \neq 0$ for $i \ge N$.
2. Define $d(i) = 1 / c(i)$ for $i \ge N$ and $d(i) = 0$ for $i < N$.
3. Then $c(i) d(i) = 1$ for $i \ge N$, a cofinite set, so $[c] \cdot [d] = 1$ in $R$.

So the non-invertible nonzero elements are the classes of sequences that are $0$ infinitely often and nonzero infinitely often.
The trap is to think that "nonzero in $R$" means "eventually nonzero"; it means "not eventually zero".
