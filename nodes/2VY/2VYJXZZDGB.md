---
tag: 2VYJXZZDGB
kind: statement
role: theorem
name: Parsons's theorem
msc: ["03F30", "03F25", "03D20"]
topics: [8XY7JYZKFW]
audience: research
uses: [5NVA2JRHPV, TNZ995J8AP, N238J43XNE, N470JF7ZJX, 97QF3KHSBY, 7RFM1XPJQV, P1RW6JWX73, 88FJKEX4SH, S0GAFZK93F]
about: [TNZ995J8AP, MESZ87G9ET]
proofs: [41QRRZ2MFA]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: The big five subsystems of second-order arithmetic
  - url: https://en.wikipedia.org/wiki/Herbrand%27s_theorem
    locator: Generalizations of Herbrand's theorem
history:
  first_stated: "Charles Parsons, 1970"
  notes: "Parsons, Mints and Takeuti proved the theorem independently; Sieg later gave a proof by Herbrand analysis."
---

## Statement

Parsons's theorem says that $\Sigma_1$ induction adds no new $\forall \exists$ theorems to primitive recursive arithmetic, and that every such theorem has a primitive recursive witness.

Let $\mathsf{PRA}$ be [[primitive recursive arithmetic|330YAP9Y4Q]] as a classical first-order theory.
It has a function symbol for each [[primitive recursive function|5NVA2JRHPV]], the defining equations of these functions, and induction for quantifier-free formulas.
Let $\mathrm{I}\Sigma_1$ be the theory in the same language whose axioms are those of $\mathsf{PRA}$ and the induction scheme for $\Sigma_1$ formulas $\exists z \, \chi$ with $\chi$ quantifier-free.

**Theorem (Parsons).**
Let $\varphi(x, y)$ be a quantifier-free formula, where $x$ is a tuple of variables.
If $\mathrm{I}\Sigma_1 \vdash \forall x \, \exists y \, \varphi(x, y)$, then there is a primitive recursive function symbol $f$ such that $\mathsf{PRA} \vdash \varphi(x, f(x))$.

In particular, $\mathrm{I}\Sigma_1$ is [[conservative|N238J43XNE]] over $\mathsf{PRA}$ for $\Pi^0_2$ sentences, and the provably total functions of $\mathrm{I}\Sigma_1$ are exactly the primitive recursive functions.

## Remarks

### A first use: the integer square root

We apply the theorem to the integer square root.
$\mathrm{I}\Sigma_1$ proves the sentence
$$\forall x \, \exists y \, \bigl(y \cdot y \le x < (y + 1) \cdot (y + 1)\bigr)$$
by $\Sigma_1$ induction on $x$: the root of $0$ is $0$, and the root of $x + 1$ is the root $y$ of $x$ or $y + 1$.
The theorem then gives a primitive recursive $f$ with $\mathsf{PRA} \vdash f(x)^2 \le x < (f(x) + 1)^2$.
The [[Herbrand analysis|MESZ87G9ET]] of this proof turns the induction into the recursion
$$f(0) = 0, \qquad f(x + 1) = \begin{cases} f(x) + 1 & \text{if } (f(x) + 1)^2 \le x + 1, \\ f(x) & \text{otherwise.} \end{cases}$$
Check: $f(3) = 1$, and $(1 + 1)^2 = 4 \le 4$ gives $f(4) = 2$.

### Why each hypothesis is needed

Induction must be restricted to $\Sigma_1$ formulas.
The theory $\mathrm{I}\Sigma_2$ proves that the [[Ackermann function|N470JF7ZJX]] is total, and this function is [[not primitive recursive|97QF3KHSBY]].
So the theorem fails for $\mathrm{I}\Sigma_2$, as the [[failure of Herbrand analysis in IΣ2|88FJKEX4SH]] shows in detail.

The conclusion must be $\Pi^0_2$.
The sentence $\forall x \, \exists y \, \forall z \, (T(x, x, y) \vee \neg T(x, x, z))$, with Kleene's $T$ predicate, is provable in pure classical logic.
Yet [[no computable function gives its $y$|7RFM1XPJQV]], since such a function would decide the halting problem.

The matrix $\varphi$ is quantifier-free so that $\varphi(x, f(x))$ is a formula of $\mathsf{PRA}$.
A matrix $\exists z \, \psi$ with $\psi$ quantifier-free reduces to this case, because we can pair $y$ and $z$ into one variable.

### What it gives you

The provably total functions of $\mathrm{I}\Sigma_1$ are exactly the primitive recursive functions.
In the language of PA, one direction holds because $\mathrm{I}\Sigma_1$ proves, by $\Sigma_1$ induction, that a $\Sigma_1$ definition of the graph of each primitive recursive function defines a total function.
The theorem gives the other direction.

Weak König's lemma adds no $\Pi^0_2$ theorems.
[[WKL0 is Π¹₁-conservative over RCA0|8G2GVRXWG5]] by Harrington's theorem, and the first-order part of $\mathsf{RCA}_0$ is $\mathrm{I}\Sigma_1$.
Combined with Parsons's theorem this gives the result of Friedman that [[WKL0 is Π⁰₂-conservative over PRA|V609D9SZ05]].
Watch out: $\mathsf{WKL}_0$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0$, not over $\mathsf{PRA}$, whose language has no set variables.

If we identify finitist reasoning with $\mathsf{PRA}$, then every $\Pi^0_2$ theorem of $\mathrm{I}\Sigma_1$ has a finitist proof.
This is a partial realization of [[Hilbert's program|P1RW6JWX73]].

### The converse

The converse is immediate: $\mathrm{I}\Sigma_1$ contains $\mathsf{PRA}$, so every theorem of $\mathsf{PRA}$ is a theorem of $\mathrm{I}\Sigma_1$.
So the two theories have exactly the same $\Pi^0_2$ theorems.
Every $\Pi^0_1$ sentence is also $\Pi^0_2$, so by Gödel's second incompleteness theorem for $\mathsf{PRA}$, the theory $\mathrm{I}\Sigma_1$ does not prove the consistency of $\mathsf{PRA}$.

### Generalizations

The collection scheme $\mathrm{B}\Sigma_2$ added to $\mathrm{I}\Sigma_1$ gives a theory that is $\Pi^0_3$-conservative over $\mathrm{I}\Sigma_1$.
In bounded arithmetic the analogue is Buss's theorem: the $\Sigma^b_1$-definable functions of $S^1_2$ are exactly the polynomial time computable functions.
Other [[conservation theorems|TNZ995J8AP]] of the same shape are often proved by the same witnessing method.

## History

Parsons proved the theorem in 1970.
Mints and Takeuti found other proofs independently.
Sieg gave the proof by [[Herbrand analysis|MESZ87G9ET]] in 1985, and the [[proof outline|41QRRZ2MFA]] follows it.

## Explanations

### L1 human

Primitive recursive functions are those computed by programs whose loops have a bound fixed before the loop starts.
The theorem says this: if a proof with a weak form of induction shows that for every $x$ there is a $y$ with a decidable property, then a program of this kind finds such a $y$.
For example, the usual proof that each $n$ has a prime above it uses only this weak induction.
And indeed [[the prime is found by a bounded search up to $n! + 1$|S0GAFZK93F]].

### L2 human

We use the theorem to show that a fast function is not provably total in $\mathrm{I}\Sigma_1$.
The Ackermann function $A$ is computable, so its graph $A(x, y) = z$ has a $\Sigma_1$ definition $\exists w \, \chi(x, y, z, w)$ with $\chi$ quantifier-free.
Suppose that $\mathrm{I}\Sigma_1$ proves $\forall x \, \forall y \, \exists v \, \chi(x, y, (v)_0, (v)_1)$, where $(v)_0$ and $(v)_1$ unpack a pair.
Then the theorem gives a primitive recursive $f$ with $\chi(x, y, (f(x, y))_0, (f(x, y))_1)$.
So $A(x, y) = (f(x, y))_0$ would be primitive recursive, which is false.

The typical use is exactly this: to bound the strength of a theory by the growth of its provably total functions.
Watch out: the theorem says nothing about $\mathrm{I}\Sigma_2$ or about $\Pi^0_3$ sentences, where it fails.

### L3 human

The theorem identifies the $\Pi^0_2$ part of $\mathrm{I}\Sigma_1$ with $\mathsf{PRA}$, which Tait proposed as the formal counterpart of finitism.
Its proofs show three methods side by side: functional interpretation, cut elimination with Herbrand analysis, and model theory.
In reverse mathematics it explains why $\mathsf{RCA}_0$ and $\mathsf{WKL}_0$ are finitistically reducible.
It is also the first level of a hierarchy: the provably total functions of $\mathrm{I}\Sigma_n$ grow with $n$, and their union over all $n$ is the class of provably total functions of PA, the $\varepsilon_0$-recursive functions.
