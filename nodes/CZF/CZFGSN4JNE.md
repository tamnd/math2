---
tag: CZFGSN4JNE
kind: definition
name: Ultrahomogeneous structure
msc: ["03C15"]
topics: [ZS8X8KS54R]
audience: grad
defines: H8VM37SSAX
uses: [983GZBQYT4, 676H7EGTKJ, PZMGQMDN25, DSQ17TNW1C, 5FKW715RGJ, SCRB74SWQN]
sources:
  - url: https://en.wikipedia.org/wiki/Fraïssé_limit
    locator: Fraïssé's theorem
  - book: isbn:9780521587136
---

## Definition

Let $M$ be an $L$-[[structure|983GZBQYT4]].
$M$ is *ultrahomogeneous* if for all finitely generated [[substructures|676H7EGTKJ]] $A, B \subseteq M$ and every [[isomorphism|PZMGQMDN25]] $p \colon A \to B$, there is an [[automorphism|DSQ17TNW1C]] $\sigma$ of $M$ with $\sigma \restriction A = p$.

$M$ is *weakly homogeneous* if for all finitely generated $A \subseteq B$ in the [[age|5FKW715RGJ]] of $M$ and every [[embedding|SCRB74SWQN]] $f \colon A \to M$, there is an embedding $g \colon B \to M$ with $g \restriction A = f$.

## Notation

Many authors write "homogeneous" for "ultrahomogeneous".
Weak homogeneity is also called the extension property.
In a relational signature "finitely generated" means "finite".

## Remarks

Every ultrahomogeneous structure is weakly homogeneous.
For countable $M$ the converse holds, by a back-and-forth argument.

Example: $(\Q, <)$ is ultrahomogeneous; see [[this example|86YZAQ1WWC]].

Non-example: $(\Z, <)$ is not, since the isomorphism $\set{0, 1} \to \set{0, 2}$ does not extend; see [[this non-example|5JVJ0HJV34]].

## Explanations

### L1 human

Every matching between two finite pieces that look alike comes from a symmetry of the whole structure.

### L2 human

We check weak homogeneity of $(\Q, <)$ for one step.

1. Let $A = \set{1 < 3}$, $B = \set{1 < 2 < 3}$, and $f(1) = 0$, $f(3) = 10$.
2. Put $g(2) = 5$, a rational between $0$ and $10$.
3. Then $g$ extends $f$ and is an embedding of $B$.

A trap is to confuse ultrahomogeneity with transitivity on single points.
