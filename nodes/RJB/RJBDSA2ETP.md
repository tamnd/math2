---
tag: RJBDSA2ETP
kind: statement
role: theorem
name: Beth definability theorem
msc: [03C40]
uses: [92SWXST1ZM, MVCH6N9SNW, 983GZBQYT4, HYJ10AF6RT, E2CBFNAVZY]
about: [92SWXST1ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Beth_definability_theorem
same_as:
  wikidata: Q4897670
  wikipedia: Beth definability theorem
---

## Statement

Let $L$ be a signature, let $P$ be an $n$-ary relation symbol not in $L$, and let $T$ be a [[theory|92SWXST1ZM]] in the signature $L \cup \set{P}$.
Suppose that $P$ is implicitly defined by $T$.
That is, any two [[models|MVCH6N9SNW]] of $T$ with the same domain and the same interpretation of each symbol of $L$ interpret $P$ alike.
Then $P$ is explicitly defined by $T$.
That is, there is an $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n)$ with
$$T \models \forall x_1 \cdots \forall x_n \, \big(P(x_1, \dots, x_n) \leftrightarrow \varphi(x_1, \dots, x_n)\big).$$

## Remarks

The converse is immediate: an explicit definition fixes $P$ in each [[structure|983GZBQYT4]] for $L$.
The standard proof uses the [[Craig interpolation theorem|E2CBFNAVZY]].
Take a copy $P'$ of $P$ and the copy $T'$ of $T$; implicit definability says $T \cup T' \models P(\bar x) \to P'(\bar x)$.
By compactness, finitely many sentences suffice, and an interpolant between the $P$-side and the $P'$-side is the required formula $\varphi$.

Example: let $L = \set{+, \cdot, 0, 1}$ and let $T$ be the theory of real closed ordered fields, with the order symbol $\le$ in the role of $P$.
In each model of $T$, the nonnegative elements are exactly the squares, so $\le$ is implicitly defined.
An explicit definition is $x \le y \leftrightarrow \exists z \, (y = x + z \cdot z)$.

## Explanations

### L1 human

Suppose some axioms pin down a new notion uniquely, once the old notions are fixed.
Beth's theorem says that the new notion can then be written as a formula in the old notions.
In first-order logic, a unique description always gives an explicit definition.

### L2 human

The theorem was proved by Evert Willem Beth in 1953.
It follows from Craig interpolation, and both results fail for many logics beyond first-order logic.
In abstract model theory, logics with the Beth property are studied as those in which implicit definitions can always be made explicit.
