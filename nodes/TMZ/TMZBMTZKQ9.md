---
tag: TMZBMTZKQ9
kind: definition
name: Algebraic and definable closure
msc: ["03C07", "03C45"]
topics: [Z772KEC9BY]
audience: grad
defines: DKAGC639W9
uses: [983GZBQYT4, HYJ10AF6RT, 9V71Q3SD1G]
sources:
  - url: https://en.wikipedia.org/wiki/Strongly_minimal_theory
    locator: lead section
  - book: isbn:9780387987606
---

## Definition

Let $\mathcal{M}$ be an $L$-[[structure|983GZBQYT4]] with domain $M$, and let $A \subseteq M$.
For an $L_A$-[[formula|HYJ10AF6RT]] $\varphi(x)$ write $\varphi(\mathcal{M}) = \set{b \in M : \mathcal{M} \models \varphi(b)}$.

1. An element $b \in M$ is *algebraic over $A$* if $b \in \varphi(\mathcal{M})$ for some $L_A$-formula $\varphi$ with $\varphi(\mathcal{M})$ finite.
2. An element $b \in M$ is *definable over $A$* if $\varphi(\mathcal{M}) = \set{b}$ for some $L_A$-formula $\varphi$.
3. The *algebraic closure* of $A$ is $\operatorname{acl}(A) = \set{b \in M : b \text{ is algebraic over } A}$.
4. The *definable closure* of $A$ is $\operatorname{dcl}(A) = \set{b \in M : b \text{ is definable over } A}$.
5. A complete [[type|9V71Q3SD1G]] $p(x)$ over $A$ is *algebraic* if it contains a formula $\varphi$ with $\varphi(\mathcal{M})$ finite.

## Notation

The closures are $\operatorname{acl}(A)$ and $\operatorname{dcl}(A)$, or $\operatorname{acl}^{\mathcal{M}}(A)$ and $\operatorname{dcl}^{\mathcal{M}}(A)$.
For a tuple $\bar{b}$, one writes $\bar{b} \in \operatorname{acl}(A)$ when each coordinate is in $\operatorname{acl}(A)$.

## Remarks

The main page of the idea, with examples, is [[algebraic and definable closure|DKAGC639W9]].
We prove that $\operatorname{acl}$ is idempotent; the same proof with "exactly one" in place of "at most $k$" works for $\operatorname{dcl}$.

1. Let $b \in \operatorname{acl}(\operatorname{acl}(A))$. Some formula $\varphi(x, \bar{a})$ with $\bar{a} = (a_1, \dots, a_n)$ in $\operatorname{acl}(A)$ holds at $b$ and has exactly $k$ solutions.
2. For each $i$, some $L_A$-formula $\psi_i(y)$ holds at $a_i$ and has $m_i$ solutions.
3. Let $\chi(x)$ be $\exists \bar{y} \, \bigl(\bigwedge_i \psi_i(y_i) \wedge \varphi(x, \bar{y}) \wedge \exists^{\le k} z \, \varphi(z, \bar{y})\bigr)$, an $L_A$-formula. Here $\exists^{\le k}$ is the first-order quantifier "at most $k$".
4. The tuple $\bar{y} = \bar{a}$ shows that $\chi(b)$ holds.
5. A solution of $\chi$ is among the at most $k$ solutions of $\varphi(x, \bar{c})$ for one of the at most $m_1 \cdots m_n$ tuples $\bar{c}$ allowed by the $\psi_i$.
6. So $\chi$ has at most $k \, m_1 \cdots m_n$ solutions, and $b \in \operatorname{acl}(A)$.

Example: in the field $\C$, the number $i$ is in $\operatorname{acl}(\emptyset)$, as a solution of $x \cdot x + 1 = 0$.

Non-example: in the field $\C$, the number $i$ is not in $\operatorname{dcl}(\emptyset)$, since complex conjugation is an automorphism that moves it.

## Explanations

### L1 human

The algebraic closure of a set collects the elements that belong to some finite set described with the help of the set.
The definable closure collects the elements that are described exactly.

### L2 human

To show $b \notin \operatorname{dcl}(A)$, find an automorphism of $\mathcal{M}$ that fixes $A$ pointwise and moves $b$.

1. If $\varphi(\mathcal{M}) = \set{b}$ and $\sigma$ fixes $A$, then $\sigma(b)$ also satisfies $\varphi$.
2. So $\sigma(b) = b$, and an automorphism that moves $b$ shows that no such $\varphi$ exists.

The trap is that the converse test needs a rich model: in a small model, an element can be fixed by every automorphism without being definable.
