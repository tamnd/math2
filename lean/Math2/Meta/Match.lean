module

public import Mathlib.GroupTheory.Coset.Card
public import Mathlib.GroupTheory.IndexNormal
public import Mathlib.GroupTheory.OrderOfElement
public import Mathlib.GroupTheory.QuotientGroup.Basic
public import Mathlib.GroupTheory.SpecificGroups.Cyclic.Subgroup
public import Math2.Meta.Attr

/-!
# Adapters

An adapter derives the exact statement of a node from a Mathlib declaration that has a different form (spec 07.3). The binding in the front matter has `match: stronger` or `match: variant`, and its `adapter` field names the adapter. The adapter has the attribute `@[m2 "TAG"]`.

The fidelity review covers the adapter together with the binding. Thus keep each adapter small, and state it in the words of the node.
-/

public section

namespace Math2.Match

/-- m2://3C53TD: Lagrange's theorem in the form of the node, for a finite group. Mathlib states it for each group, with `Nat.card`. -/
@[m2 "3C53TD"]
theorem lagrange {G : Type*} [Group G] [Finite G] (H : Subgroup G) : Nat.card H ∣ Nat.card G :=
  Subgroup.card_subgroup_dvd_card H

/-- m2://0D9NDGE9KP: uniqueness of inverses in a group. Mathlib states it for each division monoid. -/
@[m2 "0D9NDGE9KP"]
theorem inv_unique {G : Type*} [Group G] {a b : G} (h : a * b = 1) : b = a⁻¹ :=
  eq_inv_of_mul_eq_one_right h


/-- m2://04RG02S6BA: a cyclic group is abelian. Mathlib gives an instance of `IsMulCommutative`. -/
@[m2 "04RG02S6BA"]
theorem cyclic_comm {G : Type*} [Group G] [IsCyclic G] (a b : G) : a * b = b * a :=
  isMulCommutative_iff.mp IsCyclic.isMulCommutative a b

/-- m2://08V7JHS3QZ: the order of an element divides the order of a finite group. Mathlib states it for each group, with `Nat.card`. -/
@[m2 "08V7JHS3QZ"]
theorem orderOf_dvd {G : Type*} [Group G] [Finite G] (g : G) : orderOf g ∣ Nat.card G :=
  orderOf_dvd_natCard g

/-- m2://05MM4EK4SA: a group of prime order is cyclic, and each element other than the identity generates it. Mathlib states the two parts in separate declarations. -/
@[m2 "05MM4EK4SA"]
theorem prime_card {G : Type*} [Group G] {p : ℕ} [Fact p.Prime] (h : Nat.card G = p) :
    IsCyclic G ∧ ∀ g : G, g ≠ 1 → Subgroup.zpowers g = ⊤ :=
  ⟨isCyclic_of_prime_card h, fun _ hg => zpowers_eq_top_of_prime_card h hg⟩

/-- m2://0C9ZKYSPYR: the kernel of a homomorphism of groups is normal. Mathlib states it for each codomain with a multiplication and a unit. -/
@[m2 "0C9ZKYSPYR"]
theorem ker_normal {G H : Type*} [Group G] [Group H] (φ : G →* H) : φ.ker.Normal :=
  MonoidHom.normal_ker φ

/-- m2://0N2P0XRTDF: a homomorphism of groups is injective if and only if its kernel is trivial. Mathlib states the other direction of the equivalence, for each codomain with a multiplication and a unit. -/
@[m2 "0N2P0XRTDF"]
theorem injective_iff_ker {G H : Type*} [Group G] [Group H] (φ : G →* H) :
    Function.Injective φ ↔ φ.ker = ⊥ :=
  (MonoidHom.ker_eq_bot_iff φ).symm

/-- m2://0CXXJNG5B6: the first isomorphism theorem, with the map of the node. Mathlib gives the isomorphism; this theorem shows that it sends the coset of `g` to `φ g`. -/
@[m2 "0CXXJNG5B6"]
theorem first_iso {G H : Type*} [Group G] [Group H] (φ : G →* H) (g : G) :
    (QuotientGroup.quotientKerEquivRange φ (g : G ⧸ φ.ker) : H) = φ g :=
  rfl

end Math2.Match

end
