---
tag: 8DQKEDXM8S
kind: example
name: Finite fields fail the joint embedding property
aliases: [finite-fields-fail-joint-embedding]
msc: ["03C15", "12E20"]
topics: [ZS8X8KS54R]
audience: grad
not_instance_of:
  - target: 59FQ5Q2B8R
    note: a field containing copies of both F_2 and F_3 would have characteristic 2 and 3 at once
uses: [59FQ5Q2B8R, KA80AZB1CX, 08RTDHX1SK, 08YERZDM9X, SCRB74SWQN, XSCSX39GEZ]
sources:
  - book: isbn:9780521587136
---

## Example

Work in the signature of rings $\set{+, -, \cdot, 0, 1}$, and let $\mathcal{F}$ be the class of [[finite fields|08RTDHX1SK]].
We show that $\mathcal{F}$ fails the [[joint embedding property|59FQ5Q2B8R]].

1. Take $\mathbb{F}_2$ and $\mathbb{F}_3$ in $\mathcal{F}$.
2. Suppose both [[embed|SCRB74SWQN]] into a field $K$; an embedding sends $1$ to $1$ and preserves $+$.
3. In $\mathbb{F}_2$ we have $1 + 1 = 0$, so $1 + 1 = 0$ in $K$.
4. In $\mathbb{F}_3$ we have $1 + 1 + 1 = 0$, so $1 + 1 + 1 = 0$ in $K$.
5. Subtracting gives $1 = 0$ in $K$, which is impossible in a field.

## Remarks

Within one characteristic $p$, the class of finite fields of characteristic $p$ has JEP: $\mathbb{F}_{p^m}$ and $\mathbb{F}_{p^n}$ embed into $\mathbb{F}_{p^{mn}}$, by the theory of [[subfields of a finite field|08YERZDM9X]].
That class also has the [[amalgamation property|XSCSX39GEZ]], and its Fraïssé limit is the algebraic closure of $\mathbb{F}_p$.
So $\mathcal{F}$ splits into one Fraïssé class per prime.
The example shows that AP inside each part does not give JEP for the union.

## Explanations

### L1 human

In $\mathbb{F}_2$, two equals zero, and in $\mathbb{F}_3$, three equals zero.
A field containing both would have one equal to zero, which no field allows.
So these two fields never sit together inside one field.

### L2 human

We check JEP in characteristic $2$ for $\mathbb{F}_4$ and $\mathbb{F}_8$.

1. $\mathbb{F}_{2^m}$ is a subfield of $\mathbb{F}_{2^n}$ exactly when $m$ divides $n$.
2. Both $2$ and $3$ divide $6$, so $\mathbb{F}_4$ and $\mathbb{F}_8$ embed into $\mathbb{F}_{64}$.

The typical use is to see that JEP is independent of AP.
A trap is to look only at the multiplicative groups; $\mathbb{F}_2^\times$ and $\mathbb{F}_3^\times$ do embed into a common finite cyclic group.
