---
tag: CMS45G38XT
kind: statement
role: theorem
name: Weinberg–Witten theorem
msc: [81T05, 81R20]
uses: [QWK3BYVJ9W, XHPDM5T2JG]
about: [W031YNVRE3]
sources:
  - url: https://en.wikipedia.org/wiki/Weinberg%E2%80%93Witten_theorem
same_as:
  wikidata: Q7980241
  wikipedia: Weinberg–Witten theorem
---

## Statement

Consider a relativistic quantum field theory in four spacetime dimensions with massless one-particle states of helicity $h$.

1. Assume the theory has a conserved current $J^\mu$ that is a Lorentz-covariant four-vector operator, whose charge $Q = \int J^0 \, d^3x$ is nonzero on these massless states.
   Then $\abs{h} \le \tfrac12$.
2. Assume the theory has a conserved stress-energy tensor $T^{\mu\nu}$ that is a Lorentz-covariant tensor operator, whose four-momentum $P^\mu = \int T^{0\mu} \, d^3x$ is the momentum of these states.
   Then $\abs{h} \le 1$.

## Remarks

In both parts one also assumes that the matrix elements $\langle p', h \rvert J^\mu(0) \lvert p, h \rangle$ (or those of $T^{\mu\nu}$) tend to their forward values as $p' \to p$.
The proof compares two facts about these matrix elements for lightlike $p$ and $p'$.
The forward limit is fixed by the charge (or the momentum) and is nonzero.
Work in the frame where $\mathbf{p}' = -\mathbf{p}$.
A rotation by $\theta$ about the axis of $\mathbf{p}$ fixes both momenta and multiplies the matrix element by a phase $e^{\pm 2ih\theta}$.
A vector or a tensor can only produce phases with $\abs{2h} \le 1$ or $\abs{2h} \le 2$, so the matrix element vanishes for larger $\abs{h}$, which contradicts the limit.

Examples: the photon has $\abs{h} = 1$ and carries no charge, so part 1 does not forbid it.
The graviton has $\abs{h} = 2$, so by part 2 a theory with a graviton has no Lorentz-covariant conserved stress-energy tensor.
In general relativity the gravitational energy is indeed not given by a covariant tensor, which is consistent with the theorem.

## Explanations

### L1 human

The theorem forbids certain massless particles from being composite in a naive way.
A massless particle of spin above one half cannot carry a charge of a covariant conserved current.
A massless particle of spin above one cannot be described by a theory with a covariant conserved energy-momentum tensor.

### L2 human

The theorem is a tool for ruling out ideas, such as an emergent graviton in a theory with an ordinary Lorentz-covariant stress tensor.
Its loopholes are known.
Gauge theories have currents that are not gauge invariant.
In theories where spacetime itself emerges, as in [[AdS/CFT|92T9TPF13Y]], the graviton does not live in the same spacetime as the stress tensor.
It also shows that gluons, which have helicity $\pm 1$ and color charge, cannot have a gauge-invariant Lorentz-covariant conserved color current.
