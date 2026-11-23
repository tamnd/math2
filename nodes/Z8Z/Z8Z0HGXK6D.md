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

Let the sorts be $F$ for scalars and $V$ for vectors.
The two-sorted signature has three groups of symbols.

1. Field symbols: $+_F, \cdot_F \colon F \times F \to F$, $-_F \colon F \to F$, and the constants $0_F$ and $1_F$ of sort $F$.
2. Group symbols: $+_V \colon V \times V \to V$, $-_V \colon V \to V$, and the constant $0_V$ of sort $V$.
3. Scalar multiplication: $\ast \colon F \times V \to V$.

The theory $T_{\mathrm{VS}}$ has the [[field|04C5ZBG1WT]] axioms for sort $F$, the abelian group axioms for sort $V$, and four laws of scalar multiplication, each closed by $\forall$ over variables of the right sorts:
$$a \ast (u +_V v) = a \ast u +_V a \ast v, \quad (a +_F b) \ast v = a \ast v +_V b \ast v, \quad (a \cdot_F b) \ast v = a \ast (b \ast v), \quad 1_F \ast v = v.$$
We check that the models of $T_{\mathrm{VS}}$ are exactly the pairs $(K, W)$ of a field $K$ and a [[vector space|000AYPA9AJ]] $W$ over $K$.

A model $\mathcal{M}$ has a nonempty domain $M_F$ for scalars and $M_V$ for vectors, as in [[many-sorted logic|7TDHDN8P96]].
The field axioms make $(M_F, +_F, \cdot_F, -_F, 0_F, 1_F)$ a field $K$, and the group axioms make $(M_V, +_V, -_V, 0_V)$ an abelian group $W$.
The four laws are the vector space axioms for $W$ over $K$.
Conversely, a field $K$ and a vector space $W$ over $K$ give a model with $M_F = K$ and $M_V = W$.

The two-sorted language can also quantify over scalars.
The sentence
$$\exists u{:}V \, \exists v{:}V \, \forall a{:}F \, \forall b{:}F \, \big( a \ast u +_V b \ast v = 0_V \to (a = 0_F \land b = 0_F) \big)$$
says that $W$ has two linearly independent vectors, that is, $\dim W \ge 2$.
It is true in $(\mathbb{R}, \mathbb{R}^2)$ with $u = (1, 0)$ and $v = (0, 1)$, since $a(1, 0) + b(0, 1) = (a, b)$ is zero only for $a = b = 0$.
It is false in $(\mathbb{R}, \mathbb{R})$: for $u = 0$ take $a = 1$ and $b = 0$, and for $u \neq 0$ take $a = v$ and $b = -u$, so that $vu - uv = 0$ with $b \neq 0$.

So one two-sorted theory has all vector spaces over all fields as its models.

## Remarks

In one-sorted logic, a vector space over a fixed field $K$ is a structure with one unary function symbol $\lambda_c$ for each $c \in K$, read as $v \mapsto cv$.
That language depends on $K$, and it cannot quantify over scalars.
The two-sorted language can, as in the sentence for $\dim W \ge 2$, where $\forall a{:}F$ ranges over the field.
The same pattern describes modules over rings, with a sort for the ring and a sort for the module.

## Explanations

### L1 human

A vector space has two kinds of objects: numbers, called scalars, and arrows, called vectors.
In two-sorted logic the letters $a$ and $b$ stand for scalars, and $u$ and $v$ for vectors.
The axioms say how to add vectors and how to stretch a vector by a scalar.
For example, $2 \ast (1, 3) = (2, 6)$ in the plane $\mathbb{R}^2$.

### L2 human

We check the law $(a +_F b) \ast v = a \ast v +_V b \ast v$ in $(\mathbb{R}, \mathbb{R}^2)$ at $a = 2$, $b = 3$ and $v = (1, -1)$.
The left side is
$$(2 + 3) \ast (1, -1) = 5 \ast (1, -1) = (5, -5).$$
The right side is
$$2 \ast (1, -1) +_V 3 \ast (1, -1) = (2, -2) + (3, -3) = (5, -5).$$
Each term is well-sorted: $a +_F b$ has sort $F$, and $\ast$ takes it together with $v$ of sort $V$ to a vector.
The typical use of the two-sorted language is to state facts that quantify over both scalars and vectors, such as linear independence.
Watch out: the zero scalar $0_F$ and the zero vector $0_V$ are different constants of different sorts.
