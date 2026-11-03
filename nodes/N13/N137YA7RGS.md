---
tag: N137YA7RGS
kind: statement
role: theorem
name: Harish-Chandra Plancherel theorem
msc: ["22E46", "43A85", "22E30"]
uses: [XJS07AJ50Y, VY0HXD3GC4, 95Q8WZMN0W, DH3PYQJXH0, QESEAKKABM, 2HM21Z7XN9, 9AB7HYGPEK, CWDF4KGHS3, 0V33BNKZ9S]
about: [QESEAKKABM, 2HM21Z7XN9]
sources:
  - url: https://en.wikipedia.org/wiki/Plancherel_theorem_for_spherical_functions
---

## Statement

Let $G$ be a connected [[semisimple Lie group|XJS07AJ50Y]] with finite centre, with a fixed [[Haar measure|VY0HXD3GC4]].
Let $\mu$ be its [[Plancherel measure|QESEAKKABM]] on the [[unitary dual|95Q8WZMN0W]] $\widehat{G}$.

1. The support of $\mu$ is the set of [[tempered|2HM21Z7XN9]] irreducible unitary representations of $G$.
2. The measure $\mu$ is given explicitly as follows. Let $P = M_P A_P N_P$ run over representatives of the association classes of cuspidal parabolic subgroups of $G$. Let $\mathfrak a_P^*$ be the real dual of the Lie algebra of $A_P$. Let $\sigma$ be a [[discrete series|9AB7HYGPEK]] representation of $M_P$ and let $\nu \in \mathfrak a_P^*$. Let $\pi_{P, \sigma, \nu}$ be the unitarily induced [[principal series representation|CWDF4KGHS3]] $\mathrm{Ind}_P^G(\sigma \otimes e^{i \nu} \otimes 1)$, with distribution character $\Theta_{P, \sigma, \nu}$. Then there are explicit nonnegative functions $p_P(\sigma, \nu)$ such that for every [[smooth function|0V33BNKZ9S]] $f$ with compact support on $G$,
$$f(e) = \sum_{P} \sum_{\sigma} \int_{\mathfrak a_P^*} \Theta_{P, \sigma, \nu}(f) \, p_P(\sigma, \nu) \, d\nu.$$

For $P = G$ the group $A_P$ is trivial and the inner integral is a single term.
That part of the formula is $\sum_\sigma d_\sigma \Theta_\sigma(f)$ over the discrete series $\sigma$ of $G$, where $d_\sigma$ is the formal degree.

## Remarks

The existence and uniqueness of $\mu$ come from the abstract [[Plancherel theorem for groups|DH3PYQJXH0]], since Harish-Chandra proved that $G$ is a type I group.
Harish-Chandra's work determines $\mu$ completely: the discrete series of $G$ appear as atoms with mass $d_\sigma$, and each series $\pi_{P, \sigma, \nu}$ contributes a measure in $\nu$ with density $p_P(\sigma, \nu)$.
The proof uses [[Harish-Chandra's Schwartz space|JCDV4FZ86G]], the classification of the discrete series by their characters, and the asymptotics of Eisenstein integrals governed by the [[Harish-Chandra c-function|4X2N0BN3M0]].
The group $G$ has discrete series if and only if $G$ and a maximal compact subgroup $K$ have equal rank; otherwise the term for $P = G$ is absent.

Example: for $G = \mathrm{SL}(2, \R)$ there are two cuspidal parabolic classes, $G$ itself and the minimal parabolic subgroup.
Up to normalizing constants, the discrete series of lowest $K$-type $n \ge 2$ have formal degree proportional to $n - 1$.
Induce the even and odd principal series from the characters $\mathrm{diag}(a, a^{-1}) \mapsto \abs{a}^{i \nu}$ and $\mathrm{diag}(a, a^{-1}) \mapsto \sgn(a) \abs{a}^{i \nu}$.
Then they carry densities proportional to $\nu \tanh(\pi \nu / 2)$ and $\nu \coth(\pi \nu / 2)$.

## Explanations

### L1 human

The Plancherel theorem breaks the space $L^2(G)$ of a group into irreducible pieces and says how much of each piece is used.
For semisimple Lie groups, Harish-Chandra found all the pieces and all the weights.
Only the tempered representations occur, and they come in families, one family for each kind of parabolic subgroup, plus isolated pieces called the discrete series.

### L2 human

The theorem is the nonabelian analogue of Fourier inversion $f(0) = \int \hat f(\xi) \, d\xi$ on $\R^n$: the value $f(e)$ is recovered from the characters of $f$.
Its restriction to bi-$K$-invariant functions is the [[Plancherel theorem for spherical functions|PHYHP9TW29]], where only the spherical principal series appear and the density is $\abs{c(\lambda)}^{-2}$.
The densities $p_P(\sigma, \nu)$ are built from Harish-Chandra's $\mu$-functions, which generalize $\abs{c}^{-2}$.
The result is a cornerstone of the trace formula and of the Langlands program for real groups.
