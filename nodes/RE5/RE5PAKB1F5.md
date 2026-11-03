---
tag: RE5PAKB1F5
kind: definition
name: Finite-state transducer
msc: [68Q45]
defines: SDJ23BAFF7
uses: [RABRP2KG81, 1P6EP01HZF, SFMYM96C1B]
sources:
  - url: https://en.wikipedia.org/wiki/Finite-state_transducer
---

## Definition

A *finite-state transducer* is a tuple $T = (Q, \Sigma, \Gamma, I, F, E)$ where:

1. $Q$ is a finite set of states;
2. $\Sigma$ and $\Gamma$ are [[alphabets|RABRP2KG81]], the input and output alphabets;
3. $I \subseteq Q$ is the set of initial states and $F \subseteq Q$ is the set of final states;
4. $E \subseteq Q \times (\Sigma \cup \set{\varepsilon}) \times (\Gamma \cup \set{\varepsilon}) \times Q$ is a finite set of transitions, where $\varepsilon$ is the empty [[string|1P6EP01HZF]].

A pair $(u, v) \in \Sigma^* \times \Gamma^*$ is *accepted* by $T$ when there is a path $(p_0, x_1, y_1, p_1), (p_1, x_2, y_2, p_2), \ldots, (p_{m-1}, x_m, y_m, p_m)$ of transitions in $E$ with $p_0 \in I$, $p_m \in F$, $u = x_1 \cdots x_m$ and $v = y_1 \cdots y_m$.
The relation of $T$ is the set of accepted pairs.

## Remarks

Example: with $\Sigma = \set{a}$, $\Gamma = \set{b}$, $Q = \set{0, 1}$, $I = F = \set{0}$ and $E = \set{(0, a, b, 1), (1, \varepsilon, b, 0)}$, the paths from $0$ to $0$ go around the loop $k$ times, so the relation is $\set{(a^k, b^{2k}) : k \ge 0}$.
Non-example: a device with one transition $(0, a, b^n, 0)$ for every $n \ge 0$ fails clause 4, since $E$ must be finite and its labels must be single symbols or $\varepsilon$.
The relation $\set{(a, b^n) : n \ge 0}$ is still the relation of a finite-state transducer, for example with $E = \set{(0, a, \varepsilon, 1), (1, \varepsilon, b, 1)}$, $I = \set{0}$ and $F = \set{1}$.
Forgetting the output labels gives an [[NFA|SFMYM96C1B]] with $\varepsilon$-moves for the input projection of the relation.
Some authors allow whole words as transition labels; this gives the same relations.
