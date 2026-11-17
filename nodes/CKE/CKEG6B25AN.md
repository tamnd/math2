---
tag: CKEG6B25AN
kind: example
name: Second-order Peano arithmetic is categorical
msc: ["03B16", "03C85"]
topics: [MDHDYV8QZW]
audience: grad
instance_of: [G6X7SZSNC5]
uses: [G6X7SZSNC5, 0QFT7Z76N5, 1JJCGNX240, YWTERZZME5, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: Historical second-order formulation
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Expressive power
  - book: isbn:9780122384523
    locator: Chapter 4
---

## Example

Let $L = \set{0, S}$, with a constant $0$ and a unary function symbol $S$.
Second-order Peano arithmetic $\mathrm{PA}^2$ is the conjunction of three sentences of [[second-order logic|G6X7SZSNC5]]:

$$\text{(P1)} \ \forall x \, S(x) \neq 0, \qquad \text{(P2)} \ \forall x \forall y \, (S(x) = S(y) \to x = y),$$

$$\text{(P3)} \ \forall X \, \big( (X(0) \land \forall x \, (X(x) \to X(S(x)))) \to \forall x \, X(x) \big).$$

We show that in the full semantics, every model $\mathcal{M} = (M, 0^{\mathcal{M}}, S^{\mathcal{M}})$ of $\mathrm{PA}^2$ is [[isomorphic|YWTERZZME5]] to $\mathcal{N} = (\mathbb{N}, 0, n \mapsto n + 1)$.
So $\mathrm{PA}^2$ is a [[categorical theory|1JJCGNX240]].
In the steps, induction on $n$ means [[mathematical induction|0ASJVEFA9J]] in the metatheory, in $\mathbb{N}$.

1. Call a relation $R \subseteq \mathbb{N} \times M$ closed when $(0, 0^{\mathcal{M}}) \in R$, and $(n, a) \in R$ implies $(n + 1, S^{\mathcal{M}}(a)) \in R$. The set $\mathbb{N} \times M$ is closed, so closed relations exist.
2. Let $h$ be the intersection of all closed relations. Each closed relation contains $(0, 0^{\mathcal{M}})$, so $h$ does. If $(n, a) \in h$, then $(n + 1, S^{\mathcal{M}}(a))$ lies in each closed relation, so it lies in $h$. Thus $h$ is the least closed relation.
3. Every $n$ has some $a$ with $(n, a) \in h$. The set of such $n$ contains $0$ by step 2 and is closed under $n \mapsto n + 1$ by step 2, so it is $\mathbb{N}$ by induction.
4. The element $0^{\mathcal{M}}$ is the only $a$ with $(0, a) \in h$. Suppose $(0, a) \in h$ with $a \neq 0^{\mathcal{M}}$, and let $h' = h \setminus \set{(0, a)}$. Then $(0, 0^{\mathcal{M}}) \in h'$.
5. The relation $h'$ is closed: if $(n, b) \in h'$, then $(n + 1, S^{\mathcal{M}}(b)) \in h$, and this pair is not $(0, a)$ because $n + 1 \neq 0$. So $h \subseteq h'$ by step 2, which contradicts $(0, a) \in h \setminus h'$.
6. Assume that $a$ is the only element with $(n, a) \in h$. Suppose $(n + 1, c) \in h$ with $c \neq S^{\mathcal{M}}(a)$, and let $h' = h \setminus \set{(n + 1, c)}$. Then $(0, 0^{\mathcal{M}}) \in h'$, since $n + 1 \neq 0$.
7. The relation $h'$ is closed. Let $(m, b) \in h'$. If $(m + 1, S^{\mathcal{M}}(b)) = (n + 1, c)$, then $m = n$, so $b = a$ by the assumption of step 6, and $c = S^{\mathcal{M}}(a)$, a contradiction. So $(m + 1, S^{\mathcal{M}}(b)) \in h'$.
8. As in step 5, step 7 gives $h \subseteq h'$, a contradiction. By steps 4 to 7 and induction, $h$ is the graph of a function $f \colon \mathbb{N} \to M$.
9. Since $h$ is closed, $f(0) = 0^{\mathcal{M}}$ and $f(n + 1) = S^{\mathcal{M}}(f(n))$ for every $n$.
10. The function $f$ is onto. Let $B = \set{f(n) : n \in \mathbb{N}} \subseteq M$. By step 9, $0^{\mathcal{M}} \in B$, and $S^{\mathcal{M}}(f(n)) = f(n + 1) \in B$.
11. In the full semantics, the variable $X$ of (P3) ranges over all subsets of $M$, so we may take $X = B$. Then (P3) in $\mathcal{M}$ gives $B = M$.
12. The function $f$ is one-to-one. We show by induction on $n$: for all $m$, if $f(m) = f(n)$, then $m = n$.
13. Case $n = 0$. If $m \neq 0$, then $m = k + 1$, and $f(m) = S^{\mathcal{M}}(f(k)) \neq 0^{\mathcal{M}} = f(0)$ by (P1).
14. Case $n + 1$. Let $f(m) = f(n + 1) = S^{\mathcal{M}}(f(n))$. By (P1), $f(m) \neq 0^{\mathcal{M}}$, so $m \neq 0$ and $m = k + 1$. Then $S^{\mathcal{M}}(f(k)) = S^{\mathcal{M}}(f(n))$, so $f(k) = f(n)$ by (P2), so $k = n$ by the induction hypothesis, and $m = n + 1$.
15. By steps 9, 11 and 14, $f$ is a bijection that maps $0$ to $0^{\mathcal{M}}$ and commutes with the successor. So $f$ is an isomorphism from $\mathcal{N}$ onto $\mathcal{M}$.

## Remarks

The full semantics is used in one place only, in step 11.
In a Henkin model the set $B$ need not belong to the family over which $X$ ranges, and indeed [[a Henkin model of $\mathrm{PA}^2$ can be non-standard|8C0K8ZBW48]].
The first-order induction schema has the same weakness, because it applies only to sets that a formula defines; see [[the first-order induction schema|KCZ2EVJVS2]].

When the signature also has $+$ and $\cdot$ with the recursion equations $x + 0 = x$, $x + S(y) = S(x + y)$, $x \cdot 0 = 0$ and $x \cdot S(y) = x \cdot y + x$, the same $f$ preserves $+$ and $\cdot$.
Induction on $y$ shows $f(x + y) = f(x) +^{\mathcal{M}} f(y)$, and then $f(x \cdot y) = f(x) \cdot^{\mathcal{M}} f(y)$.
So the full theory of arithmetic in second-order logic is categorical as well.

The same pattern works for the real numbers.
The axioms of an ordered field with the second-order least upper bound axiom have only one model up to isomorphism, by the [[uniqueness of the complete ordered field|0G8G1TH5WK]].
A first-order theory with an infinite model is never categorical, by the [[Löwenheim-Skolem theorem|484M0TZ1S7]].

## Explanations

### L1 human

The three rules say: $0$ is not the next number after any number, different numbers have different next numbers, and induction holds.
Any system of objects that obeys these rules is a copy of $0, 1, 2, 3, \ldots$ with new names.
We match $0$ with the first object, $1$ with its next object, $2$ with the next one after that, and so on.
Induction over all sets of objects shows that this matching reaches every object.
The first two rules show that the matching never uses an object twice.

### L2 human

We see what goes wrong without (P3).
Let $M = \mathbb{N} \cup \set{a_k : k \in \mathbb{Z}}$, a copy of $\mathbb{N}$ followed by a copy of $\mathbb{Z}$, with $S(n) = n + 1$ and $S(a_k) = a_{k+1}$.

1. (P1) holds: $S(n) = n + 1 \neq 0$, and $S(a_k) = a_{k+1} \neq 0$.
2. (P2) holds: $S$ is one-to-one on each copy, and the two copies do not meet.
3. The function $f$ of step 9 is $f(n) = n$, so its image is $B = \mathbb{N}$.
4. The set $B$ contains $0$ and is closed under $S$, but $B \neq M$. So (P3) fails for $X = B$, and step 11 is exactly the step that fails.

The typical use of this example is to show that the second-order axioms fix the natural numbers, which no first-order theory can do.
The trap is to read the result as a result about provability: categoricity does not give a proof system that derives every true sentence of arithmetic.

### L3 human

The construction of $h$ as the least closed relation is the set-theoretic recursion theorem, which Dedekind proved in 1888 for the same purpose.
The argument shows more: any two models of $\mathrm{PA}^2$ are isomorphic by a unique isomorphism, because step 9 forces the value of $f$ at each $n$.
Categoricity of a single sentence implies that the theory decides every sentence semantically.
Combined with Gödel's incompleteness theorem, this shows that the full semantics has no complete effective proof system, as on the page on [[second-order logic|G6X7SZSNC5]].
