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

Let PRA be primitive recursive arithmetic as a first-order classical theory: a function symbol for each [[primitive recursive function|5NVA2JRHPV]], its defining equations, and induction for quantifier-free formulas.
Let $\mathrm{I}\Sigma_1$ be the theory in the same language with the axioms of PRA and the induction scheme for $\Sigma_1$ formulas $\exists z\, \chi$, with $\chi$ quantifier-free.

**Theorem (Parsons).**
Let $\varphi(x, y)$ be a quantifier-free formula, where $x$ is a tuple of variables.
If $\mathrm{I}\Sigma_1 \vdash \forall x\, \exists y\, \varphi(x, y)$, then there is a primitive recursive function symbol $f$ such that $\mathsf{PRA} \vdash \varphi(x, f(x))$.

In particular, $\mathrm{I}\Sigma_1$ is [[conservative|N238J43XNE]] over PRA for $\Pi^0_2$ sentences, and the provably total functions of $\mathrm{I}\Sigma_1$ are exactly the primitive recursive functions.

## Remarks

### Why each hypothesis is needed

- Induction must be restricted to $\Sigma_1$ formulas. $\mathrm{I}\Sigma_2$ proves that the [[Ackermann function|N470JF7ZJX]] is total, and this function is [[not primitive recursive|97QF3KHSBY]]; see [[the failure of Herbrand analysis in IΣ2|88FJKEX4SH]].
- The conclusion must be $\Pi^0_2$. The sentence $\forall x\, \exists y\, \forall z\, (T(x, x, y) \vee \neg T(x, x, z))$ is provable in pure classical logic, but [[no computable function gives its $y$|7RFM1XPJQV]].
- The matrix $\varphi$ is quantifier-free so that the conclusion is a formula of PRA. A matrix $\exists z\, \psi$ with $\psi$ quantifier-free reduces to this case, by pairing $y$ and $z$ into one variable.

### Consequences

- The provably total functions of $\mathrm{I}\Sigma_1$ are exactly the primitive recursive functions. In the language of PA, $\mathrm{I}\Sigma_1$ proves the recursion equations of each primitive recursive function for a $\Sigma_1$ definition of its graph, and the theorem gives the converse.
- Weak König's lemma adds no $\Pi^0_2$ theorems: $\mathsf{WKL}_0$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0$, the first-order part of $\mathsf{RCA}_0$ is $\mathrm{I}\Sigma_1$, and the theorem then gives $\Pi^0_2$-conservativity over PRA.
- If finitist reasoning is identified with PRA, then every $\Pi^0_2$ theorem of $\mathrm{I}\Sigma_1$ has a finitist proof. This is a partial realization of [[Hilbert's program|P1RW6JWX73]].

### Converse

Every theorem of PRA is a theorem of $\mathrm{I}\Sigma_1$, since $\mathrm{I}\Sigma_1$ contains PRA.
So the two theories have the same $\Pi^0_2$ theorems.
Since every $\Pi^0_1$ sentence is $\Pi^0_2$, the theorem and Gödel's second incompleteness theorem for PRA show that $\mathrm{I}\Sigma_1$ does not prove the consistency of PRA.

### Generalizations

- In bounded arithmetic, the analogue for Buss's theory $S^1_2$ says that its $\Sigma^b_1$-definable functions are exactly the polynomial time computable functions.
- The collection scheme $\mathrm{B}\Sigma_2$ added to $\mathrm{I}\Sigma_1$ gives a theory that is $\Pi^0_3$-conservative over $\mathrm{I}\Sigma_1$.
- [[Conservation theorems|TNZ995J8AP]] of the same shape hold for other pairs of theories, and they are often proved by the same witnessing method.

## History

Parsons proved the theorem in 1970.
Mints and Takeuti found other proofs independently, and Sieg gave the proof by [[Herbrand analysis|MESZ87G9ET]] that is outlined in the proof node.
The theorem is a model case of a $\Pi^0_2$ [[conservation theorem|TNZ995J8AP]] proved by proof-theoretic means.

## Explanations

### L1 human

Primitive recursive functions are those computed by programs whose loops have a bound fixed before the loop starts.
The theorem says: if a proof with a weak form of induction shows that for every $x$ there is a $y$ with a decidable property, then such a $y$ is computed by a program of this kind.
For example, the usual proof that each $x$ has a prime above it uses only this weak induction, and [[the prime is found by a bounded loop up to $x! + 1$|S0GAFZK93F]].

### L2 human

We apply the theorem to the square root.

1. $\mathrm{I}\Sigma_1$ proves $\forall x\, \exists y\, (y \cdot y \le x < (y + 1) \cdot (y + 1))$ by $\Sigma_1$ induction on $x$.
2. The theorem gives a primitive recursive $f$ with $f(x) \cdot f(x) \le x < (f(x) + 1) \cdot (f(x) + 1)$, provably in PRA.
3. Here $f(x) = \lfloor \sqrt{x} \rfloor$, and the Herbrand analysis computes it by $f(0) = 0$ and $f(x + 1) = f(x) + 1$ if $(f(x) + 1)^2 \le x + 1$, else $f(x)$.

The typical use is to bound the computational strength of a proof: a $\Pi^0_2$ theorem of $\mathrm{I}\Sigma_1$ has a primitive recursive witness.
A trap is to apply the theorem to $\mathrm{I}\Sigma_2$ or to $\Pi^0_3$ sentences, where it fails.

### L3 human

The theorem identifies the $\Pi^0_2$ part of $\mathrm{I}\Sigma_1$ with PRA, which Tait proposed as the formal counterpart of finitism.
Its proofs illustrate three methods: functional interpretation, cut elimination with Herbrand analysis, and model theory.
In reverse mathematics it explains why $\mathsf{RCA}_0$ and $\mathsf{WKL}_0$ are finitistically reducible, and it is the first level of a hierarchy of results on the provably total functions of $\mathrm{I}\Sigma_n$.
