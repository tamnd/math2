---
tag: J36EHBHF6J
kind: statement
role: theorem
name: Frege's theorem and Hume's principle
aliases: [hume-principle, freges-theorem]
msc: ["03B16", "03F35", "03A05"]
topics: [MDHDYV8QZW]
audience: grad
about: [G6X7SZSNC5, 0QFT7Z76N5]
uses: [G6X7SZSNC5, ~205409ab, 0B0KR7FH2Q, VT2Q5BZEGH, 0QFT7Z76N5, 0HESMMSYEG, 5PGSQYB5Y1]
proofs: [~fdd3d34d]
sources:
  - wikipedia: en:314743@r1350988939
    locator: Hume's principle
    note: adopted
    mention: wikipedia://en/314743
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/Hume%27s_principle
    locator: Origins
  - url: https://en.wikipedia.org/wiki/Frege%27s_theorem
    locator: Overview
same_as:
  wikidata: Q1553014
  wikipedia: Hume's principle
inventory: [XCJH1RYZQY]
---

## Statement

Work in [[second-order logic|G6X7SZSNC5]] with the full [[comprehension schema|~205409ab]].
Add one operator $\#$ that turns each unary relation variable $F$ into an individual term $\#F$, read "the number of $F$".
For unary relation variables $F$ and $G$, let $F \approx G$ abbreviate

$$\exists R \, \big[ \forall x \, (F(x) \to \exists! y \, (G(y) \land R(x, y))) \land \forall y \, (G(y) \to \exists! x \, (F(x) \land R(x, y))) \big].$$

So $F \approx G$ says that the $F$-objects and the $G$-objects are [[equinumerous|0B0KR7FH2Q]].
Hume's principle (HP) is the axiom

$$\forall F \, \forall G \, \big( \#F = \#G \leftrightarrow F \approx G \big).$$

Frege arithmetic (FA) is second-order logic with HP as its only non-logical axiom.
Write $\#[x : \varphi]$ for $\#F$, where comprehension gives $F$ with $\forall x \, (F(x) \leftrightarrow \varphi)$.
Define the following, where $P^*$ is the [[ancestral|VT2Q5BZEGH]] of $P$:

- $0 := \#[x : x \neq x]$;
- $P(m, n) :\leftrightarrow \exists F \, \exists y \, \big( F(y) \land n = \#F \land m = \#[x : F(x) \land x \neq y] \big)$;
- $P^*(a, b) :\leftrightarrow \forall X \, \big[ \big( \forall x \, (P(a, x) \to X(x)) \land \forall x \, \forall y \, (X(x) \land P(x, y) \to X(y)) \big) \to X(b) \big]$;
- $P^{*=}(a, b) :\leftrightarrow P^*(a, b) \lor a = b$, and $N(n) :\leftrightarrow P^{*=}(0, n)$.

Frege's theorem: FA proves the following six sentences.

1. $N(0)$.
2. $\forall m \, \neg P(m, 0)$.
3. $\forall m \, \forall n \, \forall n' \, (P(m, n) \land P(m, n') \to n = n')$.
4. $\forall m \, \forall m' \, \forall n \, (P(m, n) \land P(m', n) \to m = m')$.
5. $\forall n \, \big( N(n) \to \exists m \, (P(n, m) \land N(m)) \big)$.
6. $\forall X \, \big[ \big( X(0) \land \forall x \, \forall y \, (N(x) \land X(x) \land P(x, y) \to X(y)) \big) \to \forall x \, (N(x) \to X(x)) \big]$.

So $N$, $0$ and $P$ satisfy the axioms of second-order [[Peano arithmetic|0QFT7Z76N5]] for zero and successor.

## Remarks

### Why each hypothesis is needed

- Full comprehension is needed. The definitions of $N$ and $P^*$ quantify over all concepts, and the proof applies them to concepts defined with $N$ and $P^*$ themselves.
- HP is needed. Without it, $\#$ is an arbitrary operator; if $\#F$ is the same object for all $F$, then $P(0, 0)$ holds and sentence 2 fails.
- The logic must be second-order. HP compares concepts by a quantifier over relations, and the ancestral needs a quantifier over concepts.

### Consequences

- Addition and multiplication are definable from $0$ and $P$ in second-order logic, by the recursion theorem. So all of second-order Peano arithmetic is interpretable in FA.
- HP has a model. Its domain is $\N$, with $\#F = |F| + 1$ for finite $F$ and $\#F = 0$ for infinite $F$.
- To check this model, note that two finite sets are equinumerous exactly when their sizes agree, and any two infinite subsets of $\N$ are equinumerous.
- Coextensive concepts have the same number: the identity relation is a bijection, so HP gives $\#F = \#G$.

### Converse

The Peano axioms do not imply HP, since their language has no operator $\#$.
A weak converse holds: the model above can be described inside second-order arithmetic, so second-order arithmetic interprets FA.
FA also speaks about numbers outside $N$.
For example, removing $0$ from $N$ leaves a concept equinumerous with $N$, via $P$, so $P(\#N, \#N)$ holds.
Lemma C of the [[proof|~fdd3d34d]] then shows that $\#N$ is not in $N$.

### Generalizations

Frege's own system replaced HP by Basic Law V, $\varepsilon F = \varepsilon G \leftrightarrow \forall x \, (F(x) \leftrightarrow G(x))$, where $\varepsilon F$ is the extension of $F$.
Basic Law V implies HP once numbers are defined as extensions, but it is inconsistent by [[Russell's paradox|0HESMMSYEG]].
Take $R := [x : \exists F \, (x = \varepsilon F \land \neg F(x))]$ and $r := \varepsilon R$; then $R(r) \leftrightarrow \neg R(r)$.
Frege's theorem shows that the derivation of arithmetic needs only HP, which is consistent.
Neo-logicism takes HP as an analytic definition of number, and so revives a form of [[logicism|5PGSQYB5Y1]].
Similar abstraction principles, of the form $\alpha(F) = \alpha(G) \leftrightarrow E(F, G)$ for an equivalence relation $E$, are studied in the same program.

## History

HP appears in Frege's "Die Grundlagen der Arithmetik" of 1884, which quotes Hume's "A Treatise of Human Nature" of 1739-1740.
Frege's "Grundgesetze der Arithmetik" (volume 1 in 1893, volume 2 in 1903) derived arithmetic from Basic Law V.
Russell reported his paradox to Frege in 1902, while volume 2 was in preparation.
Parsons observed in 1965 that HP alone suffices for the derivation.
Wright carried out the derivation from HP in the early 1980s.
Heck showed in 1993 that Frege's own derivation uses Basic Law V essentially only to prove HP.
The name "Hume's principle" is due to Boolos.

## Explanations

### L1 human

Two bags hold the same number of marbles exactly when the marbles can be paired off, one from each bag, with none left over.
This is Hume's principle; it defines "same number" without counting.
Frege showed that this one rule, with pure logic, gives all of arithmetic.
Zero is the number of things that are not equal to themselves, since there are no such things.
One is the number of the things equal to zero, since there is exactly one such thing.
Then two is the number of the things equal to zero or one, and so on forever.

### L2 human

We check that $1 := \#[x : x = 0]$ satisfies $P(0, 1)$, the first step of the successor.

1. Let $F := [x : x = 0]$ and $y := 0$. Then $F(y)$ holds, since $0 = 0$.
2. By definition, $\#F = 1$.
3. The concept $[x : F(x) \land x \neq 0]$ is $[x : x = 0 \land x \neq 0]$, and nothing falls under it.
4. Two empty concepts are equinumerous: any $R$ works, since both conditions in $\approx$ are vacuous.
5. So HP gives $\#[x : x = 0 \land x \neq 0] = \#[x : x \neq x] = 0$.
6. Steps 1, 2 and 5 are the three clauses of $P(0, 1)$, with this $F$ and $y$.

In the same way, $2 := \#[x : x = 0 \lor x = 1]$ satisfies $P(1, 2)$; this uses $0 \neq 1$, which follows from sentence 2 and $P(0, 1)$.
The typical use of HP is this pattern: compute a number by finding a bijection, never by counting.
The trap is to read $P(m, n)$ as "$n = m + 1$" before it is proved that $P$ is a function on $N$; that is sentence 3.

### L3 human

Frege's theorem shows that second-order logic plus one abstraction principle interprets second-order arithmetic.
It also shows that FA and second-order arithmetic are equiconsistent, since each interprets the other.
The philosophical debate is whether HP is a logical or analytic truth; the logical content is the derivation itself.
The proof is a model for impredicative reasoning: $N$ is defined by a quantifier over all concepts, including $N$ itself.
