---
tag: FSJ9NGRRPA
kind: statement
role: theorem
name: Quantifier elimination for real closed fields
aliases: [tarski-quantifier-elimination-real-closed-fields, rcf-quantifier-elimination, tarskis-theorem-real-closed-fields]
msc: ["03C10", "12L12", "12D15"]
topics: [1A9JSC5YG8]
audience: grad
uses: [0P3VCBDEE2, RE5TFTDP4D, 92SWXST1ZM, HYJ10AF6RT]
about: [7FDDXV3JK7]
sources:
  - url: https://en.wikipedia.org/wiki/Real_closed_field
  - url: https://en.wikipedia.org/wiki/Quantifier_elimination
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 3
---

## Statement

Let $\mathcal{L} = \set{+, -, \cdot, 0, 1, <}$ be the language of ordered rings.
Let $\mathrm{RCF}$ be the $\mathcal{L}$-[[theory|92SWXST1ZM]] of [[real closed fields|DDY3Q3PJ6W]] with their unique field ordering.
Its axioms are those of an [[ordered field|0P3VCBDEE2]], together with two more.
One axiom says that every positive element has a square root.
One scheme says that every polynomial of odd degree has a root.
Then $\mathrm{RCF}$ admits [[quantifier elimination|RE5TFTDP4D]]: for every $\mathcal{L}$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n)$ there is a quantifier-free $\mathcal{L}$-formula $\psi(x_1, \dots, x_n)$ such that
$$\mathrm{RCF} \vdash \forall x_1 \cdots \forall x_n \, \bigl(\varphi(x_1, \dots, x_n) \leftrightarrow \psi(x_1, \dots, x_n)\bigr).$$

A proof is [[the proof by the embedding test|A9B90X77TX]].

## Remarks

### Why each hypothesis is needed

- The symbol $<$. In the language of rings, the set $\set{x \in \R : \exists y \, (x = y^2)} = [0, \infty)$ is definable, but every quantifier-free definable subset of $\R$ in that language is finite or cofinite; see [[this example|367Y9XDMXG]].
- Real closedness. In the ordered field $\Q$, the set of squares is defined by $\exists y \, (x = y \cdot y)$. Every interval of positive length among the positive rationals contains squares and non-squares, so this set is not a finite union of points and convex sets. A quantifier-free set in one variable is such a union, since each integer polynomial has finitely many real roots.
- The odd-degree scheme. The ordered fields in which every positive element is a square do not form a complete theory: $\exists y \, (y^3 = 2)$ holds in $\R$ but fails in the field of real constructible numbers. A theory of ordered fields with quantifier elimination is complete, since quantifier-free sentences compare integers.

### Consequences

- $\mathrm{RCF}$ is [[complete|655K8Y7VS8]], so every real closed field satisfies the same first-order sentences as $\R$; and $\mathrm{RCF}$ is decidable.
- $\mathrm{RCF}$ is model complete; for example [[the real algebraic numbers form an elementary substructure of the real field|D5MSQ48C9Y]].
- $\mathrm{RCF}$ is the [[model completion of the theory of ordered fields|PA9E15Q1AY]].
- The projection of a semialgebraic set is semialgebraic, which is the [[Tarski-Seidenberg theorem|3W5JGDZAN0]].
- Every definable subset of a real closed field is a finite union of points and open intervals, so $\mathrm{RCF}$ is [[o-minimal|DTWHAW1N0V]].

### Converse

The theorem characterizes the real closed fields among ordered fields in a weak sense.
An ordered field is real closed if and only if every polynomial over it has the intermediate value property, and every o-minimal ordered field is real closed.

### Generalizations

- Macintyre proved quantifier elimination for the field $\Q_p$ of $p$-adic numbers, in the language of rings with predicates for the $n$-th powers.
- In the ring signature, $\mathrm{RCF}$ keeps model completeness but loses quantifier elimination; see [[this example|G3GGANFA7C]].

## History

Tarski proved the theorem and gave a decision method for elementary algebra and geometry; it was published in 1948.

## Explanations

### L1 human

A statement about real numbers that uses "there exists" and "for all", together with addition, multiplication and order, can be rewritten without "there exists" and "for all".
What remains is a combination of polynomial equations and inequalities in the free variables.
For example, "the quadratic $x^2 + bx + c$ has a real root" is the same as "$b^2 - 4c \ge 0$".
So every such question about the real numbers can, in principle, be decided by a computation.

### L2 human

We eliminate the quantifier in $\varphi(b, c) = \exists x \, (x^2 + b x + c = 0)$.

1. Complete the square: $x^2 + b x + c = (x + \frac b 2)^2 - \frac{b^2 - 4c}{4}$.
2. So $\varphi(b, c)$ holds if and only if $\frac{b^2 - 4c}{4}$ is a square.
3. In a real closed field, an element is a square if and only if it is $\ge 0$, by the square root axiom.
4. So $\varphi(b, c) \leftrightarrow b^2 - 4c > 0 \lor b^2 - 4c = 0$, modulo $\mathrm{RCF}$.

The typical use is to turn a question about all real closed fields into a sign condition on polynomials in the parameters.
A trap is to drop the order: in the ring language, "$a$ is a square" has no quantifier-free equivalent.

### L3 human

Quantifier elimination is the model-theoretic core of real algebraic geometry.
It shows that the sets definable in $\R$ with $+$, $\cdot$ and $<$ are exactly the semialgebraic sets, and that projections and images under polynomial maps stay in this class.
The completeness of $\mathrm{RCF}$ transfers results from $\R$ to every real closed field, and gives a short proof of Artin's solution of [[Hilbert's seventeenth problem|J45F4F13VB]].
The algorithmic forms of the theorem, such as [[cylindrical algebraic decomposition|GE8FCGKPTR]], make the decision method practical in small dimensions.
The analogous result for [[algebraically closed fields|2NBBJADY5N]] uses only the language of rings.
