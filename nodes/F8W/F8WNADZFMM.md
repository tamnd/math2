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

A map, an object or a representative is called canonical when its construction uses only the data that are given, and no arbitrary choice.
Typical arbitrary choices are a [[basis|0KCQ9Y3QKA]], a generator, a coordinate system, an ordering, or an element picked from a set.
A canonical form for an [[equivalence relation|0G8VEZ3WTK]] $\sim$ on a set $X$ is a rule $c \colon X \to X$ with two properties: $c(x) \sim x$ for each $x$, and $c(x) = c(y)$ whenever $x \sim y$.
In informal use, natural means the same as canonical.
In category theory, natural has an exact meaning: the maps form a [[natural transformation|KYCPCC57FT]].
The distinction matters because a canonical construction commutes with every isomorphism, so it can be used in later constructions without a check that the result does not depend on a choice.

## Motivation

Let $V$ be a vector space of finite dimension $n$ over a field $F$.
The [[dual space|07JBSZE0V4]] $V^*$ and the double dual $V^{**}$ also have dimension $n$.
So $V$, $V^*$ and $V^{**}$ are all isomorphic, because two vector spaces of the same finite dimension are isomorphic.
But the two isomorphisms are of a different nature.
Each isomorphism $V \to V^*$ starts from a choice, for example a basis of $V$, and a different basis gives a different isomorphism.
The [[evaluation map|0ZJM9D7NPS]] $V \to V^{**}$, $v \mapsto (f \mapsto f(v))$, uses no choice at all.
Mathematicians call the second isomorphism canonical, and they say that $V$ and $V^{**}$ are canonically isomorphic.
The word records a real difference: an identification that depends on a choice can give results that also depend on that choice.

The second use of the word comes from classification.
To decide whether two objects are equivalent, we bring each object to a standard representative of its class, and we compare the representatives.
The standard representative is the canonical form, or normal form, of the object.

## Notation

There is no standard symbol for "canonical".
Many authors write $V \cong W$ for any isomorphism, and they write "canonically isomorphic" in words when the isomorphism is canonical.
Some authors write $V = W$ for a canonical isomorphism; this is an [[abuse of notation|JV68YRB5YZ]].
Some authors put the abbreviation "can" over the arrow of a canonical map.
The words canonical, natural, standard, intrinsic and coordinate-free are used with nearly the same meaning.
The definite article signals the same idea: "the evaluation map" is canonical, while "an isomorphism $V \to V^*$" is not.
The terms canonical form and normal form are synonyms in most books, but some books reserve "canonical form" for a representative that is unique.
On this site, a canonical form is always unique in its class, and a page that uses a form that is unique only up to some choice says so.

## Remarks

### Examples

1. [[The evaluation map $V \to V^{**}$ is canonical|J3X26BSQEY]]. Its formula $v \mapsto (f \mapsto f(v))$ names only $v$ and $f$, and no basis.
2. The quotient map $G \to G/N$, $g \mapsto gN$, from a group to its [[quotient group|0KYX2N69J0]] is canonical. Its formula uses only $G$ and the [[normal subgroup|0CB0DX5BVV]] $N$.
3. [[The fraction in lowest terms is a canonical form for fractions|XSDTDMVKHX]]. Two fractions with nonzero denominators are equal exactly when their [[forms in lowest terms|0R64A2CVN4]] are the same pair of integers.
4. The [[reduced row echelon form|0WF5AQYTW6]] is a canonical form for row equivalence of matrices. Each matrix is row equivalent to exactly one matrix in reduced row echelon form.
5. For sets $A$, $B$ and $C$, the map $(A \times B) \times C \to A \times (B \times C)$, $((a, b), c) \mapsto (a, (b, c))$, is a canonical bijection. It only moves the brackets.
6. For a subset $A \subseteq X$, the inclusion map $A \to X$, $a \mapsto a$, is the canonical injection.

### Non-examples

1. [[An isomorphism from $\mathbb{R}^2$ to its dual given by a basis is not canonical|A3CP855PNV]]. Two bases give two different isomorphisms, so the condition "no arbitrary choice" fails.
2. Let $C_5$ be a cyclic group of order $5$. An isomorphism $C_5 \to \mathbb{Z}/5\mathbb{Z}$ needs a choice of generator $g$, and then sends $g^k$ to $k$. There are $4$ generators, so there are $4$ such isomorphisms, and no one of them is preferred.
3. A real vector space $V$ of dimension $n$ is isomorphic to $\mathbb{R}^n$, but each isomorphism $V \to \mathbb{R}^n$ is the map to [[coordinate vectors|04CYQHN6MC]] for a chosen basis. So the isomorphism fails the condition "no arbitrary choice".
4. The Jordan normal form of a complex square matrix is not a canonical form in the strict sense of this page. It is unique only up to the order of the Jordan blocks, so the condition $c(x) = c(y)$ for $x \sim y$ needs an extra rule that orders the blocks.

### Basic properties

1. A canonical form decides equivalence. Let $c$ be a canonical form for $\sim$. If $c(x) = c(y)$, then $x \sim c(x) = c(y) \sim y$, so $x \sim y$ by symmetry and transitivity. If $x \sim y$, then $c(x) = c(y)$ by definition. So $x \sim y$ holds exactly when $c(x) = c(y)$.
2. A canonical form is idempotent: $c(c(x)) = c(x)$. The reason: $c(x) \sim x$, so the second property gives $c(c(x)) = c(x)$.
3. The evaluation map commutes with isomorphisms. Let $\varphi \colon V \to W$ be an isomorphism. For $f \in W^*$ put $\varphi^*(f) = f \circ \varphi$, and for $\xi \in V^{**}$ put $\varphi^{**}(\xi) = \xi \circ \varphi^*$. For $v \in V$ and $f \in W^*$ we get $\varphi^{**}(\operatorname{ev}_V(v))(f) = \operatorname{ev}_V(v)(f \circ \varphi) = f(\varphi(v)) = \operatorname{ev}_W(\varphi(v))(f)$. So $\varphi^{**} \circ \operatorname{ev}_V = \operatorname{ev}_W \circ \varphi$.
4. A map defined by a basis can change with the basis. For $V = \mathbb{R}$, the basis $\{1\}$ gives the map $1 \mapsto (x \mapsto x)$, and the basis $\{2\}$ gives the map $1 \mapsto (x \mapsto x/4)$. The computation is in non-example 1 and its page.
5. A canonical map need not be the only map of its kind. A product $A \times B$ has two canonical projections, to $A$ and to $B$, and both are canonical.

### History

The word canonical comes from the Latin canon, a rule or a standard.
Samuel Eilenberg and Saunders Mac Lane made the word "natural" exact in their paper "General theory of natural equivalences" of 1945.
The formal notion is on the page [[natural transformation|KYCPCC57FT]].

### Common errors

1. A student treats "isomorphic" as "canonically isomorphic". The student identifies $V$ with $V^*$ by a basis, and then claims a result that changes when the basis changes.
2. A student thinks that canonical means unique. A canonical map is free of choices, but there can be several canonical maps, as for the two projections of a product.
3. A student uses a normal form without its convention. The fraction $-6/-4$ and the fraction $3/2$ are equal, but they have the same lowest terms form only with the rule that the denominator is positive.

## Explanations

### L1 human

A canonical choice is a choice that everybody makes in the same way, because the problem itself tells us what to do.
For a fraction, the canonical way to write it is in lowest terms: $6/8$ becomes $3/4$, and every person who simplifies it gets $3/4$.
A non-canonical choice needs a decision that the problem does not make for us.
For example, to give each point of a flat plane two numbers, we must first choose where to put the axes.
Two people can choose differently and get different numbers for the same point.
Mathematicians prefer canonical constructions, because the result then depends only on the problem and not on the person.

### L2 human

We decide whether the fractions $21/35$ and $-12/-20$ are equal by their canonical forms.

1. The rule: divide the numerator and the denominator by their greatest common divisor, and make the denominator positive.
2. For $21/35$: $\gcd(21, 35) = 7$, and $21/7 = 3$, $35/7 = 5$. The canonical form is $3/5$.
3. For $-12/-20$: $\gcd(12, 20) = 4$, and we divide by $-4$ to make the denominator positive. This gives $3/5$.
4. The canonical forms are equal, so the two fractions are equal, by basic property 1.

The typical use of a canonical form is a test of equivalence, as here.
The typical use of a canonical map is a statement that holds for all objects at once, as in basic property 3.
A trap: an isomorphism that is written without a visible choice may still hide one.
For example, the map $\mathbb{R}^2 \to (\mathbb{R}^2)^*$ that sends $x$ to $y \mapsto x_1 y_1 + x_2 y_2$ uses the standard inner product, and on an abstract vector space there is no standard inner product.

### L3 human

In category theory, a family of maps $\eta_V \colon F(V) \to G(V)$, one for each object $V$, is natural when $G(\varphi) \circ \eta_V = \eta_W \circ F(\varphi)$ for each morphism $\varphi \colon V \to W$.
Basic property 3 says that the evaluation maps form a natural transformation from the identity functor to the double dual functor on vector spaces.
No natural isomorphism $V \to V^*$ exists, because the dual is a contravariant functor.
We can make the dual covariant on isomorphisms, by sending $\varphi$ to $(\varphi^*)^{-1}$.
Even then, on one-dimensional rational vector spaces, naturality for the scaling $\varphi = 2$ gives $\tfrac{1}{2}\eta_V(v) = \eta_V(2v) = 2\eta_V(v)$, so $\eta_V = 0$.
Objects defined by a universal property, such as a [[quotient group|0KYX2N69J0]] or a product, are canonical in a weaker sense: they are unique up to a unique isomorphism, and the canonical maps are part of the data.
Canonical forms appear in many areas: normal forms of terms in rewriting systems, the Smith normal form of integer matrices, the reduced Gröbner basis of a polynomial ideal, and canonical labellings of graphs.
In each case, a canonical form turns a question about equivalence classes into a question about equality, and an algorithm that computes the form decides the equivalence.
The exact notion of naturality belongs to category theory; the other jargon words of the area are on the page [[mathematical jargon|4M1FGQ0HNZ]].
