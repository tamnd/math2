---
tag: SG43F9BZFR
kind: example
name: The path graph on three vertices as a model of the theory of graphs
msc: ["03C07", "05C99"]
topics: [NJDME6F845]
audience: ug2
instance_of: [MVCH6N9SNW]
uses: [CWQV9PTCB3, 1WTCZB4DVB, 983GZBQYT4, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_(mathematical_logic)
    locator: Examples
  - book: isbn:9780122384523
    locator: Section 2.2
---

## Example

Let $L = \{E\}$ with one binary relation symbol $E$, and let $T_{\mathrm{gr}}$ be the theory of simple [[graphs|00C0BR7D7H]], with the two axioms
$$\gamma_1 = \forall x \, \neg E(x, x), \qquad \gamma_2 = \forall x \, \forall y \, (E(x, y) \to E(y, x)).$$
Let $\mathcal{P}$ be the path graph on three vertices: the domain is $\{1, 2, 3\}$, and $E^{\mathcal{P}} = \{ (1, 2), (2, 1), (2, 3), (3, 2) \}$.
We check that $\mathcal{P}$ is a [[model|CWQV9PTCB3]] of $T_{\mathrm{gr}}$.

1. For $\gamma_1$, the clause for $\forall$ of [[satisfaction|1WTCZB4DVB]] asks us to check $\neg E(x, x)$ under $x \mapsto a$ for $a = 1, 2, 3$.
2. The pairs $(1, 1)$, $(2, 2)$ and $(3, 3)$ are not in $E^{\mathcal{P}}$, so $E(x, x)$ fails for each $a$, and $\neg E(x, x)$ holds.
   So $\mathcal{P} \models \gamma_1$.
3. For $\gamma_2$, we check $E(x, y) \to E(y, x)$ under each of the nine assignments $x \mapsto a$, $y \mapsto b$.
4. For the five pairs $(a, b)$ outside $E^{\mathcal{P}}$, the hypothesis fails, so the implication holds by the clause for $\to$.
5. For the four pairs inside $E^{\mathcal{P}}$, the reversed pair is also inside: $(1, 2)$ and $(2, 1)$ swap, and $(2, 3)$ and $(3, 2)$ swap.
   So the conclusion holds, and $\mathcal{P} \models \gamma_2$.
6. Both axioms are true, so $\mathcal{P} \models T_{\mathrm{gr}}$.

## Remarks

The general method is the one used here: check each axiom of the theory, quantifier by quantifier, in the given structure.
The models of $T_{\mathrm{gr}}$ are exactly the simple graphs, with $E$ read as adjacency.
The theory has many other models, such as the cycle on four vertices and the graph with no edges on any nonempty set.

Small changes break the model.
The structure on $\{1, 2, 3\}$ with $E = \{ (1, 2) \}$ is not a model, because $\gamma_2$ fails under $x \mapsto 1$, $y \mapsto 2$.
The directed $3$-cycle, with $E = \{ (1, 2), (2, 3), (3, 1) \}$, satisfies $\gamma_1$ but not $\gamma_2$.

## Explanations

### L1 human

Three dots in a row, with a line from the first to the middle and from the middle to the last, form a graph.
The rules of a graph say that no dot is joined to itself, and that if one dot is joined to another, then the other is joined back.
Both rules hold in the picture, so the picture is a model of the rules.

### L2 human

We check $\gamma_2$ on the assignment $x \mapsto 3$, $y \mapsto 2$, one of the four where the hypothesis holds.
The hypothesis and the conclusion become
$$E(x, y) \mapsto (3, 2) \in E^{\mathcal{P}}, \qquad E(y, x) \mapsto (2, 3) \in E^{\mathcal{P}},$$
so both hold, and the implication holds under this assignment.

The typical use is to show that a structure belongs to a class of structures given by axioms.
Watch out: listing each edge once, as $\{ (1, 2), (2, 3) \}$, gives a directed graph, and that structure fails $\gamma_2$.
