---
records:
    - id: QJ6393QTBW
      kind: monograph
      title: Les Ondelettes en 1989
      creators:
        - name: Pierre Gilles Lemarié
          role: editor
      date: "1990"
      expressions:
        - key: e1
          kind: edition
          date: "1990"
          ids:
            doi: 10.1007/bfb0083510
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1990"
              ids:
                isbn:
                    - "9783540529323"
                    - "9783540471790"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0083510
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: QJ66EM4754
      kind: preprint
      title: 'TORQUE: Optimizing What (not) to Quantize Before and After Rotation'
      creators:
        - name: Ran Ben Basat
          role: author
        - name: Michael Mitzenmacher
          role: author
        - name: Shay Vargaftik
          role: author
      date: "2026-09-28"
      subjects:
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: cs.AI
        - system: arxiv
          code: cs.IT
        - system: arxiv
          code: cs.NI
        - system: arxiv
          code: math.IT
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-28"
          ids:
            arxiv: "2609.36032"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.36032"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: QJ6AEW93RB
      kind: preprint
      title: Continuous phase transitions in the $k$-creation process without stirring in $d=1$
      creators:
        - name: Rick Durrett
          role: author
      date: "2026-09-28"
      subjects:
        - system: arxiv
          code: math.PR
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-28"
          ids:
            arxiv: "2609.35320"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.35320"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
