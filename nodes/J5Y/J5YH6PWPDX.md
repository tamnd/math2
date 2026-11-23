---
tag: J5YH6PWPDX
kind: example
name: Every full structure is a Henkin model
msc: ["03B16", "03C85"]
topics: [MDHDYV8QZW]
audience: grad
instance_of: [KWEJFK5943]
uses: [KWEJFK5943, G6X7SZSNC5, 5GS6DRJ5SY, 00E0YZCERH]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Semantics
  - book: isbn:9780122384523
    locator: Chapter 4
---

## Example

If every subset of the domain is allowed as a value of a set variable, then every set that a formula defines is allowed too.
This is the reason why the full semantics is a special case of the Henkin semantics.
Let $\mathcal{M}$ be an $L$-structure with domain $M$, and let $\mathfrak{F} = (\mathcal{M}, (\mathcal{P}(M^n))_{n \ge 1})$ be the full structure over $\mathcal{M}$.
We show that $\mathfrak{F}$ is a [[Henkin model|KWEJFK5943]].

1. Each $\mathcal{P}(M^n)$ is a set of $n$-ary relations on $M$, so $\mathfrak{F}$ is a general structure.
2. Satisfaction in $\mathfrak{F}$ is satisfaction in the full semantics of [[second-order logic|G6X7SZSNC5]].
   The reason is that in both cases the $n$-ary relation variables range over all of $\mathcal{P}(M^n)$.
3. Take an instance $\forall \bar{y} \, \forall \bar{Y} \, \exists X \, \forall \bar{x} \, (X(\bar{x}) \leftrightarrow \varphi)$ of the [[comprehension schema|5GS6DRJ5SY]].
   Here $\bar{x} = (x_1, \ldots, x_n)$, and $X$ is not free in $\varphi$.
4. Fix values $\bar{b}$ for $\bar{y}$ and $\bar{B}$ for $\bar{Y}$, and let $A = \set{\bar{a} \in M^n : \mathfrak{F} \models \varphi[\bar{a}, \bar{b}, \bar{B}]}$.
5. The set $A$ is a subset of $M^n$, so $A \in \mathcal{P}(M^n)$, and $A$ is an allowed value of $X$.
6. With $X = A$, the formula $X(\bar{x}) \leftrightarrow \varphi$ holds for every $\bar{x}$, by the definition of $A$.
   Here we use that $X$ is not free in $\varphi$, so the value of $X$ does not change the truth of $\varphi$.
7. The values in step 4 were arbitrary, so the instance is true in $\mathfrak{F}$.
   This holds for every instance, so $\mathfrak{F}$ is a Henkin model.

## Remarks

### What follows

The full semantics is a special case of the Henkin semantics.
So every sentence that is true in all Henkin models is valid in the full semantics.

### The converse on finite domains

On a finite domain the converse holds: every Henkin model is full.
Let $A = \set{\bar{a}_1, \ldots, \bar{a}_k} \subseteq M^n$ with $\bar{a}_i = (a_{i1}, \ldots, a_{in})$ and $k \ge 1$.
Comprehension for the following formula, with the parameters $y_{ij}$ set to $a_{ij}$, gives $A \in D_n$:
$$\bigvee_{i = 1}^{k} \bigwedge_{j = 1}^{n} x_j = y_{ij}.$$
The formula $x_1 \neq x_1$ gives $\emptyset \in D_n$.
So $D_n = \mathcal{P}(M^n)$ when $M$ is finite.
On an infinite domain the converse fails, as the [[non-standard Henkin model of arithmetic|8C0K8ZBW48]] shows.

## Explanations

### L1 human

A full structure allows every set as a value of a set variable.
A Henkin model must allow at least the sets that the language can describe.
Every set that the language describes is a set, so a full structure allows it.
So a full structure always passes the test for a Henkin model.

### L2 human

We check one comprehension instance in the full structure on $M = \set{1, 2, 3, 4}$ with the usual order $<$.

1. The formula is $\varphi(x, y) := y < x$, and the instance is $\forall y \, \exists X \, \forall x \, (X(x) \leftrightarrow y < x)$.
2. For $y = 2$, the set $A = \set{x : 2 < x} = \set{3, 4}$ is a subset of $M$, so it is in $\mathcal{P}(M)$.
3. With $X = \set{3, 4}$, the two sides of the biconditional agree for each $x$.
4. The cases $y = 1, 3, 4$ give the sets $\set{2, 3, 4}$, $\set{4}$ and $\emptyset$ in the same way.

Check: for $x = 3$ and $x = 4$ both sides are true, and for $x = 1$ and $x = 2$ both sides are false.

The typical use of this example is the inclusion "Henkin-valid implies valid in the full semantics".
The trap is to forget the condition that $X$ is not free in $\varphi$.
For $\varphi = \neg X(x)$, step 6 fails, and the instance would say that some set equals its own complement.
