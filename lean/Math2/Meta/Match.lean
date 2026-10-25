module

public import Mathlib.GroupTheory.Coset.Card
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

end Math2.Match

end
