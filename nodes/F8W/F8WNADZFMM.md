---
tag: F8WNADZFMM
kind: concept
name: Canonical and natural
aliases: [canonical, canonical-map, canonical-form, natural-map]
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug2
uses: [0EPAT51DXQ, 0G8VEZ3WTK, 07JBSZE0V4, 0KCQ9Y3QKA]
sources:
  - url: https://en.wikipedia.org/wiki/Canonical_map
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Canonical_form
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Natural_transformation
    locator: Unnatural isomorphism
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Descriptive informalities
---

## Summary

When a book says "the canonical map $V \to V^{**}$", the word *canonical* is a promise: nobody had to choose anything to build the map.
The map sends a vector $v$ to the rule "evaluate at $v$", and that rule makes sense in every vector space, with no basis and no coordinates.

A map, an object or a representative is *canonical* when its construction uses only the data that are given, and no arbitrary choice.
Typical arbitrary choices are a [[basis|0KCQ9Y3QKA]], a generator, a coordinate system, an ordering, or an element picked from a set.
A *canonical form* for an [[equivalence relation|0G8VEZ3WTK]] $\sim$ on a set $X$ is a rule $c \colon X \to X$ with two properties:
$$c(x) \sim x \text{ for every } x \in X, \qquad x \sim y \implies c(x) = c(y).$$
In informal use, *natural* means the same as canonical.
In category theory, *natural* has an exact meaning: the maps form a [[natural transformation|KYCPCC57FT]].

## Motivation

Let $V$ be a vector space of finite dimension $n$ over a field $F$.
The [[dual space|07JBSZE0V4]] $V^*$ and the double dual $V^{**}$ also have dimension $n$, so all three spaces are isomorphic.
But the isomorphisms are of two different kinds.
Every isomorphism $V \to V^*$ starts from a choice, for example a basis of $V$, and another basis gives another isomorphism.
The [[evaluation map|0ZJM9D7NPS]] $V \to V^{**}$, $v \mapsto (f \mapsto f(v))$, uses no choice at all.
So $V$ and $V^{**}$ are *canonically isomorphic*, and $V$ and $V^*$ are only isomorphic.
The difference is practical: a result proved through a chosen identification may change when the choice changes, and a result proved through a canonical one cannot.

The finite dimension matters.
In every vector space the evaluation map is linear and injective, so it is still canonical.
When $V$ has infinite dimension, it is not surjective, so $V \to V^{**}$ is a canonical injection but not an isomorphism.

The second use of the word comes from classification.
To decide whether two objects are equivalent, we bring each one to a standard representative of its class and compare the representatives.
The standard representative is the canonical form, or normal form, of the object.

## Notation

There is no symbol for "canonical".
Most authors write $V \cong W$ for any isomorphism and say "canonically isomorphic" in words.
Some write $V = W$ for a canonical isomorphism, which is an [[abuse of notation|JV68YRB5YZ]], and some put "can" over the arrow.
The words canonical, natural, standard, intrinsic and coordinate-free are used with nearly the same meaning.
The article is a signal too: "the evaluation map" is canonical, while "an isomorphism $V \to V^*$" is not.

The phrase "canonical form" has two readings in books.
In the strict reading, the form is unique in its class, as for a fraction in lowest terms.
In the loose reading, it is a normal form that is unique only up to some choice, as for the Jordan form, which is unique up to the order of its blocks.
To tell which one an author uses, look for the uniqueness statement next to the definition.
On this site a canonical form is unique in its class, and a page that uses a looser form says so.

## Remarks

### A map that needs no choice

Take $V = \mathbb{R}^2$ and $v = (1, 2)$.
The evaluation map turns $v$ into the rule $\operatorname{ev}(v) \colon f \mapsto f(v)$ on functionals.
For the functional $f(x, y) = 3x - y$ we get
$$\operatorname{ev}(v)(f) = f(1, 2) = 3 \cdot 1 - 2 = 1.$$
No basis appeared in this computation.
[[The evaluation map is canonical|J3X26BSQEY]] also describes $\operatorname{ev}$ with two different bases and shows that both give the same map, which is the test for a canonical map.

Many everyday maps pass the same test.
The quotient map $G \to G/N$, $g \mapsto gN$, onto a [[quotient group|0KYX2N69J0]] uses only $G$ and the [[normal subgroup|0CB0DX5BVV]] $N$.
The inclusion $A \to X$ of a subset, $a \mapsto a$, uses only $A$ and $X$.
The bijection $(A \times B) \times C \to A \times (B \times C)$, $((a, b), c) \mapsto (a, (b, c))$, only moves brackets.

### A map that needs a choice

On $V = \mathbb{R}^2$, send each basis vector to the matching vector of the [[dual basis|0ZD2CF6ZS0]].
With the standard basis, $(1, 0)$ goes to the functional $(u, v) \mapsto u$.
With the basis $(1, 0), (1, 1)$, the same vector $(1, 0)$ goes to $(u, v) \mapsto u - v$.
At the point $(0, 1)$ these functionals give $0$ and $-1$, so the two rules differ.
[[An isomorphism to the dual given by a basis is not canonical|A3CP855PNV]] works this out in full.

The same happens with groups.
An isomorphism from a cyclic group $C_5$ to $\mathbb{Z}/5\mathbb{Z}$ must pick a generator $g$ and send $g^k$ to $k$.
There are $4$ generators, so there are $4$ such isomorphisms, and no one of them is preferred.
In the same way, an isomorphism $V \to \mathbb{R}^n$ is the map to [[coordinate vectors|04CYQHN6MC]] for a chosen basis.

### Canonical forms decide equivalence

Is $21/35$ equal to $-12/-20$?
Bring each fraction to lowest terms with a positive denominator:
$$\frac{21}{35} = \frac{21/7}{35/7} = \frac{3}{5}, \qquad \frac{-12}{-20} = \frac{-12/(-4)}{-20/(-4)} = \frac{3}{5}.$$
The forms agree, so the fractions are equal.
Check: $21 \cdot (-20) = -420 = 35 \cdot (-12)$.
[[The fraction in lowest terms|XSDTDMVKHX]] proves that this rule is a canonical form.

The method works for every canonical form $c$.
If $c(x) = c(y)$, then $x \sim c(x) = c(y) \sim y$, so $x \sim y$ by symmetry and transitivity.
If $x \sim y$, then $c(x) = c(y)$ by the definition.
So $x \sim y$ holds exactly when $c(x) = c(y)$.
A canonical form is also idempotent, $c(c(x)) = c(x)$, because $c(x) \sim x$.
The [[reduced row echelon form|0WF5AQYTW6]] is a canonical form for row equivalence of matrices.

### Two readings of "natural"

Informally, "natural" is a synonym of "canonical".
Formally, a family of maps $\eta_V$, one for each object $V$, is natural when it commutes with every morphism.
For the evaluation maps and an isomorphism $\varphi \colon V \to W$, this is the identity
$$\varphi^{**} \circ \operatorname{ev}_V = \operatorname{ev}_W \circ \varphi,$$
where $\varphi^*(f) = f \circ \varphi$ and $\varphi^{**}(\xi) = \xi \circ \varphi^*$.
Check it on $v \in V$ and $f \in W^*$: both sides give $f(\varphi(v))$.
To tell which reading an author uses, look for functors and a commuting square; without them, the word is informal.
The [[naturality of the evaluation map|R19758JQWE]] gives the formal version.

### Watch out

The first trap is to read "isomorphic" as "canonically isomorphic".
A student identifies $V$ with $V^*$ by a basis and then states a result that changes when the basis changes.
The cure is to name the basis or the inner product, and keep it fixed.

The second trap is to think that canonical means unique.
A product $A \times B$ has two canonical projections, one to $A$ and one to $B$.
Canonical means free of choices, not the only map of its kind.

The third trap is a choice that hides in the formula.
The map $x \mapsto (y \mapsto x_1 y_1 + x_2 y_2)$ from $\mathbb{R}^2$ to its dual looks free of choices, but it uses the dot product.
On an abstract vector space there is no standard inner product, so the map has no meaning there.

### History

The word *canonical* comes from the Latin *canon*, a rule or a standard.
Samuel Eilenberg and Saunders Mac Lane made the word "natural" exact in their paper "General theory of natural equivalences" of 1945.
The double dual of a vector space was one of their first examples.

### Try it

First, a real vector space $V$ has a basis $b_1, b_2$, and $s(v)$ is the sum of the coordinates of $v$ in that basis.
Is $s$ canonical?
No: in the basis $2b_1, b_2$ the vector $b_1$ has coordinates $(\tfrac{1}{2}, 0)$, so the rule gives $\tfrac{1}{2}$ in place of $1$.

Second, show that $35/-49$ and $-15/21$ are equal by their canonical forms.
Both become $-5/7$: divide the first by $-7$ and the second by $3$.

## Explanations

### L1 human

A canonical choice is one that everybody makes in the same way, because the problem itself says what to do.
Simplify $6/8$ and you get $3/4$, and every person who simplifies it gets $3/4$.
A non-canonical choice needs a decision that the problem does not make.
To give each point of a flat plane two numbers, you must first decide where to put the axes.
Two people can decide differently and get different numbers for the same point.
Mathematicians prefer canonical constructions, because then the result depends only on the problem and not on the person.

### L2 human

Here is a typical question: can we identify $\mathbb{R}^2$ with its dual space without making a choice?
Try the basis rule first.
With the standard basis $e_1, e_2$, the vector $(x, y)$ goes to $(u, v) \mapsto xu + yv$.
With the basis $b_1 = (1, 0)$, $b_2 = (1, 1)$, the dual basis is $b_1^*(u, v) = u - v$ and $b_2^*(u, v) = v$.
Since $(x, y) = (x - y) b_1 + y b_2$, the vector $(x, y)$ goes to
$$(x - y)(u - v) + yv = (x - y)u + (2y - x)v.$$
For $(x, y) = (1, 0)$ the two rules give $u$ and $u - v$, which are different functionals.
So the identification depends on the basis.

Now try the double dual.
The evaluation map sends $(1, 0)$ to the rule $f \mapsto f(1, 0)$, and this rule was written without a basis.
The two spaces $V^*$ and $V^{**}$ have the same dimension as $V$, but only one of them is identified with $V$ for free.
This is why a careful text writes "$V^{**} = V$" in finite dimension and never "$V^* = V$" without naming an inner product.

### L3 human

In category theory, the evaluation maps form a natural transformation from the identity functor to the double dual functor on vector spaces, and in finite dimension a natural isomorphism.
No natural isomorphism $V \to V^*$ exists.
The dual is contravariant, so the question needs a covariant version, for example on isomorphisms with $\varphi \mapsto (\varphi^*)^{-1}$.
Even then, on one-dimensional rational vector spaces, naturality for the scaling $\varphi = 2$ gives $\tfrac{1}{2} \eta_V(v) = \eta_V(2v) = 2 \eta_V(v)$, so $\eta_V = 0$.

Objects defined by a universal property, such as a quotient or a product, are canonical in a weaker sense: they are unique up to a unique isomorphism, and the canonical maps are part of the data.
Canonical forms appear across mathematics: the Smith normal form of integer matrices, the reduced Gröbner basis of a polynomial ideal, normal forms of terms in rewriting systems, and canonical labelings of graphs.
In each case a canonical form turns a question about classes into a question about equality, and an algorithm that computes the form decides the equivalence.
The other informal words of mathematics are in [[mathematical jargon|4M1FGQ0HNZ]].
