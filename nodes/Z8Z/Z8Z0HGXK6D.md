---
tag: Z8Z0HGXK6D
kind: example
name: Vector spaces as two-sorted structures
msc: ["03C07", "15A03"]
topics: [PSRDJXRW53]
audience: grad
instance_of: [7TDHDN8P96]
uses: [7TDHDN8P96, 000AYPA9AJ, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Many-sorted_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: lead section
---

## Example

Let the sorts be $F$ (scalars) and $V$ (vectors).
The two-sorted signature has:

- $+_F, \cdot_F \colon F \times F \to F$, $-_F \colon F \to F$, and constants $0_F, 1_F$ of sort $F$;
- $+_V \colon V \times V \to V$, $-_V \colon V \to V$, and a constant $0_V$ of sort $V$;
- scalar multiplication $\ast \colon F \times V \to V$.

The theory $T_{\mathrm{VS}}$ has the [[field|04C5ZBG1WT]] axioms for sort $F$, the abelian group axioms for sort $V$, and the four laws of scalar multiplication.
We check that the models of $T_{\mathrm{VS}}$ are exactly the pairs $(K, W)$ of a field and a [[vector space|000AYPA9AJ]] over it.

1. A model $\mathcal{M}$ has a nonempty domain $M_F$ for scalars and $M_V$ for vectors, as in [[many-sorted logic|7TDHDN8P96]].
2. The field axioms on sort $F$ make $(M_F, +_F, \cdot_F, -_F, 0_F, 1_F)$ a field $K$.
3. The group axioms on sort $V$ make $(M_V, +_V, -_V, 0_V)$ an abelian group $W$.
4. The laws $a \ast (u +_V v) = a \ast u +_V a \ast v$, $(a +_F b) \ast v = a \ast v +_V b \ast v$, $(a \cdot_F b) \ast v = a \ast (b \ast v)$ and $1_F \ast v = v$, each closed by $\forall$ over the right sorts, make $W$ a vector space over $K$.
5. Conversely, each field $K$ and vector space $W$ over $K$ give a model with $M_F = K$ and $M_V = W$.
6. The sentence $\exists u{:}V \, \exists v{:}V \, \forall a{:}F \, \forall b{:}F \, (a \ast u +_V b \ast v = 0_V \to (a = 0_F \land b = 0_F))$ says that $\dim W \ge 2$. It holds in $(\mathbb{R}, \mathbb{R}^2)$ with $u = (1, 0)$ and $v = (0, 1)$, and fails in $(\mathbb{R}, \mathbb{R})$.

So one two-sorted theory has all vector spaces over all fields as its models.

## Remarks

In one-sorted logic, a vector space over a fixed field $K$ is a structure with one unary function symbol $\lambda_a$ for each $a \in K$, read as $v \mapsto a v$.
That language depends on $K$, and it cannot quantify over scalars.
The two-sorted language can, as in step 6, where $\forall a{:}F$ ranges over the field.
The same pattern gives modules over rings, and representations of groups.

## Explanations

### L1 human

A vector space has two kinds of objects: numbers, called scalars, and vectors.
In two-sorted logic, the letters $a, b$ stand for scalars and $u, v$ for vectors.
The axioms say how to add vectors and how to multiply a vector by a scalar.
For example, $2 \ast (1, 3) = (2, 6)$ in the plane $\mathbb{R}^2$.

### L2 human

We check the law $(a +_F b) \ast v = a \ast v +_V b \ast v$ in $(\mathbb{R}, \mathbb{R}^2)$ at $a = 2$, $b = 3$ and $v = (1, -1)$.

1. The left side is $5 \ast (1, -1) = (5, -5)$.
2. The right side is $(2, -2) + (3, -3) = (5, -5)$.
3. Each term is well-sorted: $a +_F b$ has sort $F$, and $\ast$ takes it with $v$ of sort $V$ to a vector.

The typical use of the two-sorted language is to state facts that quantify over both scalars and vectors, such as linear independence.
A trap: the zero scalar $0_F$ and the zero vector $0_V$ are different constants of different sorts.
