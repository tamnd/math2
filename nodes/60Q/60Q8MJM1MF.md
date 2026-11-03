---
tag: 60Q8MJM1MF
kind: concept
name: Clebsch–Gordan coefficients
msc: [81R05, 17B10, "22E70"]
sources:
  - url: https://en.wikipedia.org/wiki/Clebsch%E2%80%93Gordan_coefficients
same_as:
  wikidata: Q898619
  wikipedia: Clebsch–Gordan coefficients
---

## Summary

Take two irreducible representations of $SU(2)$, or of $\mathfrak{su}(2)$.
The Clebsch–Gordan coefficients are the entries of the change of basis that splits their tensor product into irreducible pieces.
They express a state of total angular momentum $J$ through products of states of the two parts.
They are central in quantum mechanics, where they describe the coupling of two angular momenta.
The decomposition behind them is the rule $V_{j_1} \otimes V_{j_2} \cong V_{\abs{j_1 - j_2}} \oplus \dots \oplus V_{j_1 + j_2}$ for the [[representations of sl2|8WBY6R28CR]], here labelled by spin, so that $V_j$ has dimension $2j + 1$.

## Explanations

### L1 human

Two spinning particles have spins $j_1$ and $j_2$, and the pair together has a total spin $J$.
The possible values of $J$ go from $\abs{j_1 - j_2}$ to $j_1 + j_2$ in steps of one.
A state with a definite total spin is a combination of states with definite spins of the two particles.
The Clebsch–Gordan coefficients are the weights of that combination.
For two spins $1/2$, the state of total spin $0$ is $(\uparrow\downarrow - \downarrow\uparrow)/\sqrt{2}$.
