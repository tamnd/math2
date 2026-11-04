---
tag: D3C15GJE8D
kind: statement
role: proposition
name: Formula complexity
sources:
  - wikipedia: en:72252525@r1359919666
    locator: S2S (mathematics), section Formula complexity
    note: adopted
    mention: wikipedia://en/72252525#GEJX
    sections: [Statement]
inventory: [Q9YV09J3RE]
---

## Statement

A set of binary strings is definable in S2S if and only if it is regular (i.e. forms a regular language). In S1S, a (unary) predicate on sets is (parameter-free) definable if and only if it is an ω-regular language. For S2S, for formulas that use their free variables only on strings not containing a 1, the expressiveness is the same as for S1S.

For every S2S formula φ(*S*<sub>1</sub>,...,*S*<sub>*k*</sub>), (with *k* free variables) and finite tree of binary strings *T*, φ(*S*<sub>1</sub>∩T,...,*S*<sub>*k*</sub>∩T) can be computed in time linear in |*T*| (see Courcelle's theorem), but as noted above, the overhead can be iterated exponential in the formula size (more precisely, the time is $O(|T|k)+2_{O(|\phi|)}^2$).

For S1S, every formula is equivalent to a Δ<sup>1</sup><sub>1</sub> formula, and to a boolean combination of Π<sup>0</sup><sub>2</sub> arithmetic formulas. Moreover, every S1S formula is equivalent to acceptance by a corresponding ω-automaton of the parameters of the formula. The automaton can be a deterministic parity automaton: A parity automaton has an integer priority for each state, and accepts if and only if the highest priority seen infinitely often is odd (alternatively, even).

For S2S, using tree automata (below), every formula is equivalent to a Δ<sup>1</sup><sub>2</sub> formula. Moreover, every S2S formula is equivalent to a formula with just four quantifiers, ∃*S*∀*T*∃*s*∀*t* ... (assuming that our formalization has both the prefix relation and the successor functions). For S1S, three quantifiers (∃*S*∀*s*∃*t*) suffice, and for WS2S and WS1S, two quantifiers (∃*S*∀*t*) suffice; the prefix relation is not needed here for WS2S and WS1S.

However, with free second-order variables, not every S2S formula can be expressed in second-order arithmetic through just Π<sup>1</sup><sub>1</sub> [[transfinite recursion|0ZHQMQ2C1N]] (see reverse mathematics). RCA<sub>0</sub> + (schema) {τ: τ is a true S2S sentence} is equivalent to (schema) {τ: τ is a Π<sup>1</sup><sub>3</sub> sentence provable in Π<sup>1</sup><sub>2</sub>-CA<sub>0</sub> }. Over a base theory, the schemas are equivalent to (schema over *k*) ∀*S*⊆ω ∃α<sub>1</sub>\<...\<α<sub>*k*</sub> *L*<sub>α<sub>1</sub></sub>(*S*) ≺<sub>Σ<sub>1</sub></sub> ... ≺<sub>Σ<sub>1</sub></sub> *L*<sub>α<sub>*k*</sub></sub>(S) where *L* is the constructible universe (see also large countable ordinal). Due to limited induction, Π<sup>1</sup><sub>2</sub>-CA<sub>0</sub> does not prove that all true (under the standard decision procedure) Π<sup>1</sup><sub>3</sub> S2S statements are actually true even though each such sentence is provable Π<sup>1</sup><sub>2</sub>-CA<sub>0</sub>.

Moreover, given sets of binary strings *S* and *T*, the following are equivalent: (1) *T* is S2S definable from some set of binary strings polynomial time computable from *S*. (2) *T* can be computed from the set of winning positions for some game whose payoff is a finite boolean combination of Π<sup>0</sup><sub>2</sub>(*S*) sets. (3) *T* can be defined from *S* in arithmetic μ-calculus (arithmetic formulas + least fixed-point logic) (4) *T* is in the least β-model (i.e. an ω-model whose set-theoretic counterpart is transitive) containing *S* and satisfying all Π<sup>1</sup><sub>3</sub> consequences of in Π<sup>1</sup><sub>2</sub>-CA<sub>0</sub>.

Proof sketch:
