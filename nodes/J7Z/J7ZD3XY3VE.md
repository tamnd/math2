---
tag: J7ZD3XY3VE
kind: statement
role: proposition
name: The Artin conjecture
aliases: [artin-conjecture-l-functions]
sources:
  - wikipedia: en:2774171@r1373389734
    locator: Artin L-function, section Conjectures > The Artin conjecture
    note: adopted
    mention: wikipedia://en/2774171#1Z7W
    sections: [Statement]
inventory: [NNCMVT65WS]
---

## Statement

The *Artin conjecture* also called *Artin holomorphy conjecture* states that $L(s,\rho,L/K)$ for a non-trivial, irreducible representation $\rho$ is [[entire function|0419794R0T]]..

Assumption that representation is non-trivial is necessary, because for trivial representation we get Dedekind zeta function with one simple pole at $s=1$. Assumption that representation is irreducible allows to simplify statement excluding representation induced from trivial representation. However this statement is natural generalization of theorem that Hecke L-functions are entire for non-trivial, primitive Hecke character.

Main problem with holomorphy of analytic continuation arises from fact that meromorphic continuation is constructed as product of Hecke L-functions in integer powers: zeros of functions used with negative powers produce poles that must be cancelled by zeros of functions used with positive powers. Direct proof of Artin conjecture from this construction would require very detailed knowledge about location and multiplicities of nontrivial zeros of Hecke L-functions, problem that is generally very hard for L-functions.

Further improvement of Brauer's theorem to use only positive integers coefficient is not possible in general case: groups where all characters can be induced from one-dimensional characters using possitive integer coefficients are called monomial groups, and (Taketa 1930) proved that all monomial group are [[solvable groups|0FXJ7YFMMX]]. Moreover, this is only necessary condition: the SL(2,3) is solvable group that has complex character of 2-dimensional representation that cannot be expressed this way.

Artin conjecture was solved in very specific cases:

- for one-dimensional representations conjecture follows from holomorphy of Hecke L-functions. More generally Artin, showed that the conjecture is true for all representations induced from 1-dimensional representations.
- in case of two-dimensional representations, they can be classified by the nature of the image subgroup: it may be cyclic, dihedral, tetrahedral, octahedral, or icosahedral.
  - For odd and irreducible, two-dimensional representations follows from the proof of Serre's modularity conjecture, regardless of image subgroup.
  - For the cyclic or dihedral case follows easily from Erich Hecke's work.
  - (Langlands 1980) used the base change lifting to prove the tetrahedral case.
  - (Tunnell 1981) extended Langlands work to cover the octahedral case.
  - The general icosahedral case is open and is active area of research.

Artin conjecture combined with factorization of Dedekind zeta function for Galois extensions implies Dedekind conjecture, that for any finite extension $L/K$ of number fields the quotient:

$$\frac{\zeta_L(s)}{\zeta_K(s)}$$

is entire function.
