---
tag: S8FKECAJEA
kind: example
name: A polynomial calculus refutation for two pigeons and one hole
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
instance_of: [ZERBQSTZB5]
uses: [ZERBQSTZB5, RJ571F7FF0]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
---

## Example

The [[pigeonhole formula|RJ571F7FF0]] $\mathrm{PHP}^2_1$ has two pigeons, one hole and the variables $x_1 = x_{11}$ and $x_2 = x_{21}$.
Its clauses are $x_1$, $x_2$ and $\neg x_1 \vee \neg x_2$.
With $1$ read as true, as in the [[algebraic proof systems|ZERBQSTZB5]], the translations are the pigeon axioms $1 - x_1$ and $1 - x_2$ and the hole axiom $x_1 x_2$.

The following sequence is a polynomial calculus refutation over an arbitrary field $\mathbb{F}$.

1. $1 - x_2$, an axiom.
2. $x_1 - x_1 x_2$, the multiplication of line 1 by the variable $x_1$.
3. $x_1 x_2$, an axiom.
4. $x_1$, the linear combination of lines 2 and 3 with coefficients $1$ and $1$.
5. $1 - x_1$, an axiom.
6. $1$, the linear combination of lines 4 and 5 with coefficients $1$ and $1$.

We check the two sums.
In line 4, $(x_1 - x_1 x_2) + x_1 x_2 = x_1$.
In line 6, $x_1 + (1 - x_1) = 1$.

The measures are these.

- The degree is $2$, the degree of lines 2 and 3.
- The length is $6$ lines.
- The size is $2 + 2 + 1 + 1 + 2 + 1 = 9$ monomials.

## Remarks

The degree $2$ is the least possible.
A refutation of degree $1$ cannot use the axiom $x_1 x_2$ or a Boolean axiom, since these have degree $2$.
The other axioms $1 - x_1$ and $1 - x_2$ have the common zero $x_1 = x_2 = 1$, so by soundness they have no refutation.
This agrees with Razborov's bound for $\mathrm{PHP}^m_n$, which for $n = 1$ gives degree at least $1/2 + 1$, so at least $2$.

The same steps give the Nullstellensatz refutation $x_1 (1 - x_2) + x_1 x_2 + (1 - x_1) = 1$ of degree $2$.
They follow the resolution refutation that resolves $\neg x_1 \vee \neg x_2$ with $x_2$ to get $\neg x_1$, and then $\neg x_1$ with $x_1$.
Line 4 is the translation $x_1$ of the clause $\neg x_1$.

## Explanations

### L1 human

Two pigeons must each sit in the one hole, and they may not share it.
With $1$ for true, the rules become the polynomials $1 - x_1$, $1 - x_2$ and $x_1 x_2$, which are all $0$ when the rules hold.
Multiplying the second rule by $x_1$ and adding the third rule gives $x_1$, which says "pigeon $1$ is not in the hole".
Adding the first rule then gives $1$, so the rules cannot all hold.

### L2 human

A polynomial calculus refutation keeps every line as a polynomial that vanishes at each common $0$-$1$ zero of the axioms.

1. Multiply by a variable to make two lines share a monomial, here $x_1 x_2$.
2. Add the lines to cancel the shared monomial.
3. Repeat until the constant $1$ appears.

A trap is to multiply by a polynomial in one step: the rule allows only a variable, and a product by a longer polynomial needs several steps and a linear combination.
