---
records:
    - id: KEXCR4T6ZN
      kind: course
      title: Probabilistic Methods in PDE
      creators:
        - name: Anindya Goswami
          role: instructor
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IISER Pune
              ids:
                nptel: "111106134"
      scope:
        value: in
        rule: S6
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111106134"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
    - id: KEXVYV0SNS
      kind: preprint
      title: Expander Graph Propagation
      creators:
        - name: Andreea Deac
          role: author
        - name: Marc Lackenby
          role: author
        - name: Petar Veličković
          role: author
      date: "2022-10-06"
      subjects:
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: cs.AI
        - system: arxiv
          code: math.CO
        - system: arxiv
          code: stat.ML
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2022-10-06"
          ids:
            arxiv: "2210.02997"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2210.02997"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
    - id: KEXWVTK74D
      kind: monograph
      title: Front Tracking for Hyperbolic Conservation Laws
      creators:
        - name: Helge Holden
          role: author
        - name: Nils H. Risebro
          role: author
      date: "2002"
      expressions:
        - key: e1
          kind: edition
          date: "2002"
          ids:
            doi:
                - 10.1007/978-3-642-23911-3
                - 10.1007/978-3-642-56139-9
                - 10.1007/978-3-662-47507-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2011"
              ids:
                isbn:
                    - "9783642239106"
                    - "9783642239113"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2002"
              ids:
                isbn:
                    - "9783540432890"
                    - "9783642561399"
            - key: m3
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2015"
              ids:
                isbn:
                    - "9783662475065"
                    - "9783662475072"
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-23911-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-56139-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-47507-2
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
