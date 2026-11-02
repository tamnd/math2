---
tag: ENYXKW76AA
kind: concept
name: Ruelle zeta function
msc: ["37C30", "11M41"]
sources:
  - url: https://en.wikipedia.org/wiki/Ruelle_zeta_function
same_as:
  wikidata: Q7377817
  wikipedia: Ruelle zeta function
---

## Summary

The Ruelle zeta function of a map is a weighted count of its [[periodic points|T75CZ5H47N]].
Each fixed point of $f^n$ is counted with the product of a weight function along its orbit.
With the weight $1$ it is the [[Artin–Mazur zeta function|2A5Z21CE4P]].
It is a basic tool of the thermodynamic formalism, where its poles and zeros are related to the eigenvalues of [[transfer operators|CNZV00JQRC]].
Ruelle also defined a version for flows, with a product over closed orbits.
For geodesic flows of hyperbolic surfaces, this version is close to the Selberg zeta function.

## Explanations

### L1 human

Instead of just counting periodic points, one can give each periodic orbit a weight, for example a probability or a stretching factor.
The Ruelle zeta function packs these weighted counts for all periods into one function.
Its singularities then tell how fast the weighted counts grow, which in turn gives the pressure and the rate of mixing of the system.
