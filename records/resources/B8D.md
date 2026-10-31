---
records:
    - id: B8D26BYA7T
      kind: preprint
      title: Proof of the Kahn Saks Conjecture
      creators:
        - name: Max Aires
          role: author
      date: "2026-09-25"
      subjects:
        - system: arxiv
          code: math.CO
        - system: arxiv
          code: cs.DM
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-25"
          ids:
            arxiv: "2609.30895"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.30895"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
    - id: B8DXQ8K1J7
      kind: monograph
      title: Harmonic Maps Between Surfaces (with a Special Chapter on Conformal Mappings)
      creators:
        - name: Jürgen Jost
          role: author
      date: "1984"
      expressions:
        - key: e1
          kind: edition
          date: "1984"
          ids:
            doi: 10.1007/bfb0100160
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1984"
              ids:
                isbn:
                    - "9783540133391"
                    - "9783540388685"
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
          native_id: 10.1007/bfb0100160
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
