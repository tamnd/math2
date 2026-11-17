---
tag: HHZMPDMADJ
kind: example
name: The relativization of a two-sorted sentence
msc: ["03C07", "03B10"]
topics: [PSRDJXRW53]
audience: grad
instance_of: [7TDHDN8P96]
uses: [7TDHDN8P96, Z8Z0HGXK6D, 983GZBQYT4, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Many-sorted_logic
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: "Chapter: Beyond First-order Logic"
---

## Example

Take the two-sorted language of [[vector spaces|Z8Z0HGXK6D]] with sorts $F$ and $V$.
The one-sorted language has the same function symbols without sorts, and two new unary relation symbols $P_F$ and $P_V$.
For a two-sorted formula $\varphi$, its relativization $\varphi^*$ replaces $\forall x{:}s \, \psi$ by $\forall x \, (P_s(x) \to \psi^*)$ and $\exists x{:}s \, \psi$ by $\exists x \, (P_s(x) \land \psi^*)$.
Let $\mathrm{Ax}$ contain $\exists x \, P_F(x)$, $\exists x \, P_V(x)$, $P_F(0_F)$, $P_V(0_V)$, and, for each function symbol, a closure axiom such as $\forall a \, \forall v \, ((P_F(a) \land P_V(v)) \to P_V(a \ast v))$.
We check that $\varphi$ and $\varphi^*$ have the same models, up to this translation.

1. A one-sorted model $\mathcal{N}$ of $\mathrm{Ax}$ gives a two-sorted structure $\mathcal{N}^\circ$ with $M_F = P_F^{\mathcal{N}}$ and $M_V = P_V^{\mathcal{N}}$. These sets are nonempty, and the closure axioms make each function map them to the right sort.
2. Conversely, a two-sorted structure $\mathcal{M}$ gives a one-sorted structure on the disjoint union $M_F \sqcup M_V$. Each function symbol gets its old values on well-sorted arguments and any fixed element as value elsewhere.
3. By [[structural induction|12MQ2NJ29A]] on $\varphi$: for every assignment of elements of the right sorts, $\mathcal{N}^\circ \models \varphi$ exactly when $\mathcal{N} \models \varphi^*$. The quantifier step holds because $P_s(x) \to {}$ and $P_s(x) \land {}$ restrict $x$ to the domain of sort $s$.
4. Apply this to the sentence $\delta$ "$\dim \ge 2$" of the vector-space example. Its relativization is $\exists u \, (P_V(u) \land \exists v \, (P_V(v) \land \forall a \, (P_F(a) \to \forall b \, (P_F(b) \to \chi))))$, where $\chi$ is the unchanged quantifier-free part.
5. So $\delta^*$ holds in the one-sorted structure built from $(\mathbb{R}, \mathbb{R}^2)$, and it fails in the one built from $(\mathbb{R}, \mathbb{R})$.

So relativization turns each two-sorted sentence into a one-sorted sentence with the same meaning.

## Remarks

The translation gives, for every set $\Sigma$ of sentences, $\Sigma \models \varphi$ exactly when $\Sigma^* \cup \mathrm{Ax} \models \varphi^*$.
Steps 1 and 2 give the two directions, since each model of one side gives a model of the other with the same truth values.
So the completeness and compactness theorems pass from one-sorted to many-sorted logic.
The sorts in the one-sorted model need not be disjoint, unless one adds axioms such as $\forall x \, \neg (P_F(x) \land P_V(x))$.

## Explanations

### L1 human

One can always merge the sorts into one domain.
Then one adds a label "is a scalar" or "is a vector" to each object.
"For all scalars $a$" becomes "for all $a$, if $a$ is a scalar, then".
"There is a vector $v$" becomes "there is a $v$ that is a vector and".

### L2 human

We relativize $\forall a{:}F \, \exists v{:}V \, (a \ast v = 0_V)$.

1. The outer quantifier gives $\forall a \, (P_F(a) \to \dots)$.
2. The inner quantifier gives $\exists v \, (P_V(v) \land a \ast v = 0_V)$.
3. The result is $\forall a \, (P_F(a) \to \exists v \, (P_V(v) \land a \ast v = 0_V))$.
4. It is true in every vector space, with $v = 0_V$.

The typical use of relativization is to transfer theorems from one-sorted to many-sorted logic.
A trap: the universal case uses $\to$ and the existential case uses $\land$; swapping them changes the meaning.
