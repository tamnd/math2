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

Take the two-sorted language of [[vector spaces|Z8Z0HGXK6D]], with sorts $F$ and $V$.
The one-sorted language has the same function symbols without sorts, and two new unary relation symbols $P_F$ and $P_V$.
The relativization $\varphi^*$ of a two-sorted formula $\varphi$ leaves atomic formulas and connectives alone and changes each quantifier:
$$(\forall x{:}s \, \psi)^* = \forall x \, (P_s(x) \to \psi^*), \qquad (\exists x{:}s \, \psi)^* = \exists x \, (P_s(x) \land \psi^*).$$
Let $\mathrm{Ax}$ contain $\exists x \, P_F(x)$, $\exists x \, P_V(x)$, $P_F(0_F)$, $P_F(1_F)$, $P_V(0_V)$, and one closure axiom for each function symbol, such as
$$\forall a \, \forall v \, \big( (P_F(a) \land P_V(v)) \to P_V(a \ast v) \big).$$
We check that $\varphi$ and $\varphi^*$ say the same thing.

1. From one sort to two.
   A one-sorted model $\mathcal{N}$ of $\mathrm{Ax}$ gives a two-sorted [[structure|983GZBQYT4]] $\mathcal{N}^\circ$ with $M_F = P_F^{\mathcal{N}}$ and $M_V = P_V^{\mathcal{N}}$.
   These sets are nonempty, and the closure axioms make each function map them to the right sort.
2. From two sorts to one.
   A two-sorted structure $\mathcal{M}$ gives a one-sorted structure on the disjoint union $M_F \sqcup M_V$.
   Each function symbol keeps its old values on well-sorted arguments and takes any fixed element as its value elsewhere.
3. Same truth.
   By [[structural induction|12MQ2NJ29A]] on $\varphi$, for every assignment that gives each variable an element of its sort, $\mathcal{N}^\circ \models \varphi$ exactly when $\mathcal{N} \models \varphi^*$.
   The quantifier step holds because the guards $P_s(x) \to$ and $P_s(x) \land$ restrict $x$ to the domain of sort $s$.
4. A test sentence.
   Let $\delta$ be the sentence "$\dim \ge 2$" from the vector-space example, $\exists u{:}V \, \exists v{:}V \, \forall a{:}F \, \forall b{:}F \, \chi$ with $\chi$ quantifier-free.
   Its relativization is
   $$\exists u \, \Big( P_V(u) \land \exists v \, \Big( P_V(v) \land \forall a \, \big( P_F(a) \to \forall b \, (P_F(b) \to \chi) \big) \Big) \Big).$$
5. So $\delta^*$ is true in the one-sorted structure built from $(\mathbb{R}, \mathbb{R}^2)$, and false in the one built from $(\mathbb{R}, \mathbb{R})$, just as $\delta$ is.

So relativization turns each two-sorted sentence into a one-sorted sentence with the same meaning.

## Remarks

Steps 1 and 2 turn each model of one side into a model of the other with the same truth values.
So for every set $\Sigma$ of sentences, $\Sigma \models \varphi$ in [[many-sorted logic|7TDHDN8P96]] exactly when $\Sigma^* \cup \mathrm{Ax} \models \varphi^*$ in one-sorted logic.
That is how completeness and compactness pass from one-sorted to many-sorted logic.

The sorts in a one-sorted model of $\mathrm{Ax}$ may overlap, since nothing forbids an element in both $P_F$ and $P_V$.
Add $\forall x \, \neg (P_F(x) \land P_V(x))$ if you want them disjoint; the translation works either way.
If you drop $\exists x \, P_F(x)$ from $\mathrm{Ax}$, step 1 breaks, because $M_F$ may be empty.

## Explanations

### L1 human

You can always put all the objects into one big box.
Then you stick a label "scalar" or "vector" on each object.
"For all scalars $a$" becomes "for all $a$, if $a$ is a scalar, then".
"There is a vector $v$" becomes "there is a $v$ that is a vector and".

### L2 human

We relativize $\forall a{:}F \, \exists v{:}V \, (a \ast v = 0_V)$ from the outside in.
The outer quantifier gives $\forall a \, (P_F(a) \to \dots)$.
The inner quantifier gives $\exists v \, (P_V(v) \land a \ast v = 0_V)$.
Put together, the result is
$$\forall a \, \big( P_F(a) \to \exists v \, (P_V(v) \land a \ast v = 0_V) \big).$$
Check: it is true in every vector space, with $v = 0_V$, because $a \ast 0_V = 0_V$.
The typical use of relativization is to carry theorems about one-sorted logic over to many-sorted logic.
Watch out: the universal case uses $\to$ and the existential case uses $\land$.
Swap them, and $\exists v \, (P_V(v) \to a \ast v = 0_V)$ becomes true as soon as some element is not a vector.
