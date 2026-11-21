---
tag: RJBDSA2ETP
kind: statement
role: theorem
name: Beth definability theorem
aliases: [beth-definability-theorem, beth-theorem, implicit-definability-implies-explicit]
msc: ["03C40"]
topics: [JYJHB4YBAH]
audience: grad
about: [92SWXST1ZM]
uses: [92SWXST1ZM, MVCH6N9SNW, 983GZBQYT4, HYJ10AF6RT, WDVVEYD6AT, EY20BF96SJ, E2CBFNAVZY]
history:
  first_stated: "1953"
  notes: "Beth published the theorem in 1953; Craig later derived it from his interpolation theorem."
sources:
  - url: https://en.wikipedia.org/wiki/Beth_definability_theorem
    locator: Statement
  - book: isbn:9780521587136
same_as:
  wikidata: Q4897670
  wikipedia: Beth definability theorem
---

## Statement

Let $L$ be a [[signature|WDVVEYD6AT]], let $P$ be an $n$-ary relation symbol not in $L$, and let $T$ be a [[theory|92SWXST1ZM]] in the signature $L \cup \set{P}$.

- $P$ is *implicitly defined* by $T$ if any two [[models|MVCH6N9SNW]] of $T$ with the same domain and the same interpretation of each symbol of $L$ interpret $P$ alike.
- $P$ is *explicitly defined* by $T$ if there is an $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n)$ with
$$T \models \forall x_1 \cdots \forall x_n \, \big(P(x_1, \dots, x_n) \leftrightarrow \varphi(x_1, \dots, x_n)\big).$$

1. $P$ is implicitly defined by $T$ if and only if $P$ is explicitly defined by $T$.
2. (Padoa's method.) If there are models $(\mathcal{M}, P_1)$ and $(\mathcal{M}, P_2)$ of $T$ with the same [[reduct|EY20BF96SJ]] $\mathcal{M}$ to $L$ and $P_1 \ne P_2$, then no $L$-formula explicitly defines $P$ in $T$.

Part 2 is the direction "explicit implies implicit" of part 1, read in contrapositive form.

## Remarks

### Why each hypothesis is needed

- All models of $T$, not one model. In $(\mathbb{N}, <)$ the set $E$ of even numbers is fixed by every automorphism, since the identity is the only one, but $E$ is not definable from $<$. Indeed $\mathrm{Th}(\mathbb{N}, <, E)$ does not implicitly define $E$: it has nonstandard models in which shifting a copy of $\mathbb{Z}$ by one place moves $E$.
- Arbitrary models, not finite ones. On finite linear orders $1 < \cdots < m$, the axioms "$P$ holds of the least element, and $P$ alternates along successors" implicitly define $P = \set{1, 3, 5, \ldots}$. An explicit definition $\varphi$ would let $\exists x \, (\varphi(x) \wedge \forall y \, (y \le x))$ say that $m$ is odd, which [[no sentence can|N3AC6Y96RZ]].

### Consequences

- In the theory of real closed ordered fields, the order is implicitly defined from $+$, $\cdot$, $0$ and $1$, since the nonnegative elements are the squares. An explicit definition is $x \le y \leftrightarrow \exists z \, (y = x + z \cdot z)$.
- In $\mathrm{Th}(\mathbb{Q}, +, 0, <)$ the order is not definable from $+$ and $0$. The map $x \mapsto -x$ is an isomorphism from $(\mathbb{Q}, +, 0, <)$ onto $(\mathbb{Q}, +, 0, >)$, so both are models with the same reduct, and Padoa's method applies.
- If $P$ is implicitly defined by $T$, every $(L \cup \set{P})$-formula is $T$-equivalent to an $L$-formula, obtained by substituting $\varphi$ for $P$. So implicitly defined symbols add no new definable sets to the models of $T$.

### Converse

The converse of part 1 is the direction "explicit implies implicit", which is immediate: in each [[structure|983GZBQYT4]] for $L$, the formula $\varphi$ fixes the interpretation of $P$.

### Generalizations

- The same holds for several new relation symbols at once, and for new function and constant symbols, by treating their graphs as relations.
- A relation can be implicitly defined "up to finitely many choices"; [[Svenonius's theorem|JNXY3WRYFY]] and the [[Chang-Makkai theorem|MFR9Z5PPH4]] describe what remains of definability then.
- The [[proof|A91RG9GJFE]] from [[Craig interpolation|E2CBFNAVZY]] shows that, in first-order logic, interpolation implies definability.

## History

Evert Willem Beth published the theorem in 1953.
Craig gave a second proof by deriving it from his interpolation theorem, and this is the proof given [[here|A91RG9GJFE]].
The easy direction, used to show non-definability, is named after Alessandro Padoa, of Peano's school.

## Explanations

### L1 human

Suppose some rules pin down a new notion completely, once the old notions are fixed.
Beth's theorem says that you can then write the new notion as a formula in the old notions.
In first-order logic, a unique description always comes with an explicit definition.

### L2 human

We use Padoa's method to show that $<$ is not definable from $+$ and $0$ on $\mathbb{Q}$.

1. Let $T = \mathrm{Th}(\mathbb{Q}, +, 0, <)$ and $\sigma(x) = -x$.
2. $\sigma$ preserves $+$ and $0$, and it reverses the order: $a < b$ if and only if $\sigma(a) > \sigma(b)$.
3. So $\sigma$ is an isomorphism from $(\mathbb{Q}, +, 0, <)$ onto $(\mathbb{Q}, +, 0, >)$, and the second structure is also a model of $T$.
4. The two models have the same reduct $(\mathbb{Q}, +, 0)$, and $0 < 1$ holds in the first but not in the second.

By part 2, no formula in $+$ and $0$ defines $<$ in $T$.
A trap is to look for one structure with two orders that are not isomorphic; Padoa's method needs two models of the same theory $T$ with the same reduct.

### L3 human

Beth's theorem says that first-order logic has no hidden definitions: whatever a theory determines, it also expresses.
Its failure on finite structures is one of the classical gaps between finite and infinite model theory, together with the failure of the [[Łoś-Tarski theorem|9RN0KYXNT1]].
Its semantic refinements, [[Svenonius's theorem|JNXY3WRYFY]] and the [[Chang-Makkai theorem|MFR9Z5PPH4]], replace the comparison of two models by automorphisms or by counting expansions.
