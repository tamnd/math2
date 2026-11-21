---
tag: P6CAAK802G
kind: example
name: Closure in dense linear orders
msc: ["03C07", "06A05"]
topics: [Z772KEC9BY]
audience: grad
instance_of: [DKAGC639W9]
uses: [DKAGC639W9, 2W4S2H4VYA, 7FDDXV3JK7]
sources:
  - url: https://en.wikipedia.org/wiki/Strongly_minimal_theory
    locator: lead section
  - book: isbn:9780387987606
---

## Example

Let $\mathcal{M} = (M, <)$ be a [[dense linear order|2W4S2H4VYA]] without endpoints and let $A \subseteq M$.
We show that $\operatorname{acl}(A) = \operatorname{dcl}(A) = A$.

1. Each $a \in A$ is the only solution of $x = a$, so $A \subseteq \operatorname{dcl}(A) \subseteq \operatorname{acl}(A)$.
2. Let $b \notin A$ and let $\varphi(x)$ be an $L_A$-formula that holds at $b$, with parameters in a finite set $A_0 \subseteq A$.
3. By [[quantifier elimination|7FDDXV3JK7]], $\varphi$ is a Boolean combination of formulas $x < a$, $x = a$ and $a < x$ with $a \in A_0$.
4. Let $I$ be the open interval between the largest element of $A_0$ below $b$ and the smallest element of $A_0$ above $b$, with $-\infty$ or $+\infty$ when there is none.
5. All points of $I$ satisfy the same atomic formulas over $A_0$ as $b$, so $\varphi$ holds on all of $I$.
6. The interval $I$ contains $b$, so it is nonempty, and it is infinite by density and the lack of endpoints.
7. So every formula over $A$ that holds at $b$ has infinitely many solutions, and $b \notin \operatorname{acl}(A)$.

## Remarks

This shows that dense linear orders have a trivial closure: parameters tie down only themselves.
The exchange property holds in a trivial way here, but the theory is not strongly minimal: the formula $a < x$ defines an infinite set with an infinite complement.
In the ordered field $\R$ the situation is different: $\operatorname{dcl}(\emptyset)$ contains all real algebraic numbers, since each one is a root of a polynomial with a known position among the roots.

## Explanations

### L1 human

In the rationals with their order, a number that is not among the given numbers sits in a gap between two of them.
Every property that the order can express holds for all numbers in that gap.
So no property singles the number out, or even puts it into a finite list.

### L2 human

We check that $1/2 \notin \operatorname{acl}(\set{0, 1})$ in $(\Q, <)$.

1. The element $1/2$ lies in the interval $(0, 1)$, between the parameters.
2. Every formula over $\set{0, 1}$ that holds at $1/2$ holds at every point of $(0, 1)$, by step 5 of the example.
3. The interval $(0, 1)$ contains infinitely many rationals.

The typical use is to see that the closure depends on the structure: the same set $\Q$ with addition has $\operatorname{dcl}(\set{1}) = \Q$.
The trap is to forget the unbounded intervals: an element above all of $A_0$ is also not algebraic.
